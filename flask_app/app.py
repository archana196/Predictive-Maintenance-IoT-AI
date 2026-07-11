# =============================================================
# app.py — AI-Powered Predictive Maintenance System
# Flask Application Entry Point
# =============================================================

import os
import sqlite3
from datetime import datetime
from functools import wraps

import joblib
import pandas as pd
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from utils.history_logger import log_prediction

# ---------------------------------------------------------------------------
# App & Path Configuration
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "predictive_maintenance_secret_2024"

# Absolute base directory (flask_app/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute path to data/ directory (one level up from flask_app/)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

# Database path
DATABASE = os.path.join(BASE_DIR, "database", "users.db")

# History CSV path
HISTORY_CSV = os.path.join(DATA_DIR, "prediction_history.csv")

# ---------------------------------------------------------------------------
# Load ML Model & Encoders at Startup
# ---------------------------------------------------------------------------

try:
    model = joblib.load(os.path.join(BASE_DIR, "model", "model.pkl"))
    encoders = joblib.load(os.path.join(BASE_DIR, "model", "encoders.pkl"))
except FileNotFoundError as exc:
    raise RuntimeError(
        "Model files not found. Ensure model/model.pkl and model/encoders.pkl exist."
    ) from exc

# ---------------------------------------------------------------------------
# Database Helpers
# ---------------------------------------------------------------------------

os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)


def get_db():
    """Open a SQLite connection with Row factory."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """Create the users table if it does not already exist."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            email    TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Initialise on startup
initialize_database()

# ---------------------------------------------------------------------------
# Auth Decorator
# ---------------------------------------------------------------------------


def login_required(f):
    """Redirect to /login if the user is not authenticated."""

    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated


# ---------------------------------------------------------------------------
# Risk Level Helper
# ---------------------------------------------------------------------------


def compute_risk_level(probability, prediction):
    """
    Derive a human-readable risk level from model confidence and prediction.

    Rules:
        Healthy prediction → Low risk always.
        Failure + confidence < 70%  → Medium
        Failure + confidence >= 70% → High
    """
    if prediction == "Healthy":
        return "Low"
    if probability < 70:
        return "Medium"
    return "High"


# ---------------------------------------------------------------------------
# Routes — Authentication
# ---------------------------------------------------------------------------


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """User registration page."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("All fields are required.", "danger")
            return render_template("signup.html")

        hashed_password = generate_password_hash(password)

        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, hashed_password),
            )
            conn.commit()
            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("An account with that email already exists.", "danger")
        finally:
            conn.close()

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """User login page."""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]
            flash(f"Welcome back, {user['name']}! 👋", "success")
            return redirect(url_for("home"))

        flash("Invalid email or password. Please try again.", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Clear session and redirect to login."""
    session.clear()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("login"))


# ---------------------------------------------------------------------------
# Routes — Dashboard
# ---------------------------------------------------------------------------


@app.route("/")
@login_required
def home():
    """Main prediction form dashboard."""
    return render_template("index.html", user=session["user_name"])


# ---------------------------------------------------------------------------
# Routes — Prediction
# ---------------------------------------------------------------------------


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    """
    Accept form data, encode categorical features, run the LightGBM model,
    log the result to CSV, and render the results page.
    """
    try:
        # --- Raw categorical inputs ---
        raw_type = request.form["Type"]
        raw_shift = request.form["Shift"]
        raw_day_type = request.form["Day_Type"]

        # --- Encode categoricals ---
        enc_type = encoders["Type"].transform([raw_type])[0]
        enc_shift = encoders["Shift"].transform([raw_shift])[0]
        enc_day_type = encoders["Day_Type"].transform([raw_day_type])[0]

        # --- Build feature DataFrame ---
        features = pd.DataFrame(
            [
                {
                    "Type": enc_type,
                    "Air_temperature_K": float(request.form["Air_temperature_K"]),
                    "Process_temperature_K": float(
                        request.form["Process_temperature_K"]
                    ),
                    "Rotational_speed_rpm": float(
                        request.form["Rotational_speed_rpm"]
                    ),
                    "Torque_Nm": float(request.form["Torque_Nm"]),
                    "Tool_wear_min": float(request.form["Tool_wear_min"]),
                    "Ambient_Temperature": float(
                        request.form["Ambient_Temperature"]
                    ),
                    "Load_Density": float(request.form["Load_Density"]),
                    "Humidity": float(request.form["Humidity"]),
                    "Shift": enc_shift,
                    "Day_Type": enc_day_type,
                }
            ]
        )

        # --- Predict ---
        prediction_raw = model.predict(features)[0]
        probability_arr = model.predict_proba(features)[0]
        confidence = round(float(max(probability_arr)) * 100, 2)

        status = "Healthy" if prediction_raw == 0 else "Failure"
        risk_level = compute_risk_level(confidence, status)

        # Capture prediction timestamp
        prediction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --- Log to CSV ---
        log_prediction(
            machine_type=raw_type,
            prediction=status,
            probability=confidence,
            risk_level=risk_level,
            user_email=session.get("user_email", "unknown"),
        )

        return render_template(
            "results.html",
            status=status,
            confidence=confidence,
            risk_level=risk_level,
            prediction_time=prediction_time,
            machine_type=raw_type,
        )

    except KeyError as e:
        flash(f"Missing input field: {e}. Please fill in all fields.", "danger")
        return redirect(url_for("home"))
    except ValueError as e:
        flash(f"Invalid input value: {e}. Please enter valid numbers.", "danger")
        return redirect(url_for("home"))
    except Exception as e:
        flash(f"Prediction error: {e}", "danger")
        return redirect(url_for("home"))


# ---------------------------------------------------------------------------
# Routes — History
# ---------------------------------------------------------------------------


@app.route("/history")
@login_required
def history():
    """
    Display the current user's prediction history.

    - Filters the shared CSV to show ONLY rows belonging to the
      logged-in user (matched by email stored in session).
    - Shows the last 5 of the user's own predictions, most recent first.
    - Defensively repairs the CSV header if it was ever missing.
    """
    from utils.history_logger import _ensure_csv_exists, COLUMNS as CSV_COLUMNS

    records     = []
    total_count = 0
    user_email  = session.get("user_email", "")
    expected_cols = CSV_COLUMNS

    try:
        if os.path.isfile(HISTORY_CSV):
            # Repair missing/empty header before reading
            _ensure_csv_exists()

            df = pd.read_csv(HISTORY_CSV)

            # Fix-up if header row is missing (legacy data)
            if not all(col in df.columns for col in expected_cols):
                df = pd.read_csv(HISTORY_CSV, header=None, names=expected_cols)

            # ── PERSONALISATION ──────────────────────────────────────────
            # Keep only rows that belong to the current user
            user_df = df[df["User Email"].astype(str).str.lower() == user_email.lower()]
            # ─────────────────────────────────────────────────────────────

            total_count = len(user_df)

            # Last 5 of this user's predictions, most recent first
            last_five = user_df.tail(5).iloc[::-1]
            records   = last_five.to_dict(orient="records")
        else:
            flash("No prediction history file found.", "info")
    except Exception as e:
        flash(f"Could not load history: {e}", "danger")

    return render_template(
        "history.html",
        tables=records,
        total_count=total_count,
    )


@app.route("/download_history")
@login_required
def download_history():
    """
    Let the logged-in user download ONLY their own prediction records.

    - Reads the shared CSV, filters to current user's rows, writes to an
      in-memory buffer, and streams it as a CSV download.
    - The shared CSV on disk is never modified.
    """
    import io
    from utils.history_logger import _ensure_csv_exists, COLUMNS as CSV_COLUMNS

    user_email    = session.get("user_email", "")
    expected_cols = CSV_COLUMNS

    if not os.path.isfile(HISTORY_CSV):
        flash("No history file found to download.", "warning")
        return redirect(url_for("history"))

    try:
        _ensure_csv_exists()
        df = pd.read_csv(HISTORY_CSV)

        # Fix-up missing header (legacy data)
        if not all(col in df.columns for col in expected_cols):
            df = pd.read_csv(HISTORY_CSV, header=None, names=expected_cols)

        # ── PERSONALISATION ──────────────────────────────────────────────
        # Keep only the current user's rows
        user_df = df[df["User Email"].astype(str).str.lower() == user_email.lower()]
        # ─────────────────────────────────────────────────────────────────

        if user_df.empty:
            flash("You have no predictions to download yet.", "info")
            return redirect(url_for("history"))

        # Write filtered data to an in-memory CSV buffer
        buffer = io.StringIO()
        user_df.to_csv(buffer, index=False)
        buffer.seek(0)

        # Convert to bytes for send_file
        bytes_buffer = io.BytesIO(buffer.getvalue().encode("utf-8"))
        bytes_buffer.seek(0)

        # Build a safe filename from the user's email
        safe_name = user_email.replace("@", "_").replace(".", "_")
        download_name = f"history_{safe_name}.csv"

        return send_file(
            bytes_buffer,
            mimetype="text/csv",
            as_attachment=True,
            download_name=download_name,
        )

    except Exception as e:
        flash(f"Could not prepare download: {e}", "danger")
        return redirect(url_for("history"))


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
# =============================================================
# utils/history_logger.py
# Prediction History Logger for Predictive Maintenance System
# =============================================================

import os
import csv
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# Resolve the absolute path to the data/ directory, which lives two levels
# above this file: flask_app/utils/ → flask_app/ → project root → data/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
HISTORY_CSV = os.path.join(DATA_DIR, "prediction_history.csv")

# CSV column headers (order must stay fixed — matches the template)
COLUMNS = [
    "Timestamp",
    "Machine Type",
    "Prediction",
    "Probability",
    "Risk Level",
    "User Email",
]


def _ensure_csv_exists():
    """
    Guarantee that prediction_history.csv exists AND has a valid header row.

    Handles three cases:
      1. File does not exist        → create with header
      2. File exists but is empty   → write header (was the original bug)
      3. File exists but has no     → prepend header by rewriting the file
         recognised header row
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    file_missing = not os.path.isfile(HISTORY_CSV)
    file_empty   = file_missing or os.path.getsize(HISTORY_CSV) == 0

    if file_missing or file_empty:
        # Create or overwrite with just the header
        with open(HISTORY_CSV, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
        return

    # File exists and is non-empty — check whether the first line is our header
    with open(HISTORY_CSV, mode="r", encoding="utf-8") as f:
        first_line = f.readline().strip()

    expected_header = ",".join(COLUMNS)
    if first_line != expected_header:
        # Header is missing or corrupted — read existing raw data rows and
        # rewrite the file with a proper header prepended.
        with open(HISTORY_CSV, mode="r", encoding="utf-8") as f:
            existing_rows = f.readlines()

        with open(HISTORY_CSV, mode="w", newline="", encoding="utf-8") as f:
            f.write(expected_header + "\n")
            for row in existing_rows:
                f.write(row)


def log_prediction(machine_type, prediction, probability, risk_level, user_email):
    """
    Append a single prediction record to prediction_history.csv.

    Parameters
    ----------
    machine_type : str
        Original (decoded) machine type label, e.g. "L", "M", or "H".
    prediction   : str
        Human-readable result: "Healthy" or "Failure".
    probability  : float
        Confidence percentage (0-100), already rounded to 2 decimal places.
    risk_level   : str
        Computed risk level: "Low", "Medium", or "High".
    user_email   : str
        E-mail of the currently logged-in user.
    """
    # Always verify the CSV is healthy before writing
    _ensure_csv_exists()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = {
        "Timestamp":    timestamp,
        "Machine Type": machine_type,
        "Prediction":   prediction,
        "Probability":  probability,
        "Risk Level":   risk_level,
        "User Email":   user_email,
    }

    with open(HISTORY_CSV, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writerow(row)

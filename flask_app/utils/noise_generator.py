import pandas as pd
import numpy as np

def add_gaussian_noise(df, sensor_cols, noise_level=0.05):
    df_noisy = df.copy()
    for col in sensor_cols:
        std = df[col].std()
        noise = np.random.normal(0, noise_level * std, size=len(df))
        df_noisy[col] = df[col] + noise
    return df_noisy

def generate_noisy_datasets(df, sensor_cols, save_path="../data/"):
    noise_levels = [0.05, 0.10, 0.20]
    for level in noise_levels:
        df_noisy = add_gaussian_noise(df, sensor_cols, noise_level=level)
        filename = f"{save_path}noisy_{int(level*100)}pct.csv"
        df_noisy.to_csv(filename, index=False)
        print(f"Saved: {filename}")
    return True
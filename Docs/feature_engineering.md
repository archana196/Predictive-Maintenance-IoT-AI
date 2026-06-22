# Feature Engineering Documentation

## Overview

To improve predictive maintenance modeling, rolling statistical features were generated from the original AI4I 2020 dataset. These features capture short-term trends and variations in machine sensor readings.

## Source Features

Rolling statistics were created for the following numerical variables:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

## Rolling Window Sizes

Two window sizes were used:

- 5 observations
- 10 observations

## Generated Feature Types

### Rolling Mean

Measures the average value within a rolling window.

Examples:
- Air Temperature [K]_rollmean_5
- Torque [Nm]_rollmean_10

### Rolling Standard Deviation

Measures variability within a rolling window.

Examples:
- Process Temperature [K]_rollstd_5
- Tool Wear [min]_rollstd_10

### Rolling Variance

Measures the spread of values within a rolling window.

Examples:
- Rotational Speed [rpm]_rollvar_5
- Torque [Nm]_rollvar_10

### Rolling Minimum

Captures the minimum value within a rolling window.

Examples:
- Air Temperature [K]_rollmin_5
- Tool Wear [min]_rollmin_10

### Rolling Maximum

Captures the maximum value within a rolling window.

Examples:
- Process Temperature [K]_rollmax_5
- Rotational Speed [rpm]_rollmax_10

## Feature Summary

| Statistic | Window Size | Purpose |
|------------|------------|------------|
| Mean | 5, 10 | Captures local trends |
| Standard Deviation | 5, 10 | Measures variability |
| Variance | 5, 10 | Measures data dispersion |
| Minimum | 5, 10 | Captures local lows |
| Maximum | 5, 10 | Captures local highs |

## Total Features Created

- Original Dataset Columns: 14
- Engineered Features Added: 50
- Total Columns in Enhanced Dataset: 64

## Output Dataset

The engineered features were saved in:

`data/week1_features.csv`

## Purpose

These rolling statistical features help machine learning models identify patterns, trends, and anomalies that may indicate impending machine failures, thereby improving predictive maintenance performance.

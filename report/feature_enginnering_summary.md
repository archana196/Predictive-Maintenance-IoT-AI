# Feature Engineering Summary
## Project: Predictive Maintenance IoT-AI
### Author: Abhay Soni

## Rolling Mean
Calculates average of sensor values over a window.
Smooths out noise in sensor data.
Formula: mean of last N values

## Rolling Standard Deviation
Measures variability/spread in sensor readings.
High std = unstable sensor behavior = possible failure.

## Rolling Variance
Square of standard deviation.
Highlights sudden changes in sensor signals.

## Window Sizes Used
- Window 5: Short-term signal changes
- Window 10: Long-term signal trends

## Features Created
- 5 sensors × 3 features × 2 windows = 30 features

## Output
Saved to: data/week1_features.csv
# Model Configuration
- Algorithm: LightGBM Classifier
- Estimators: 100
- Learning Rate: 0.1
- Class Weight: Balanced

# Features Used
Rolling mean, std, variance features (window 5 and 10)

# Train/Test Split
- Train: 80%
- Test: 20%
- Stratified split to maintain class balance

# Output
Model saved to: data/lightgbm_model.pkl
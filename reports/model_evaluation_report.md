# Model Evaluation Report

## Objective

Evaluate the performance of the baseline LightGBM classifier for predictive maintenance.

## Model

* Algorithm: LightGBM Classifier
* Random State: 42

## Evaluation Metrics

| Metric    |   Value |
| --------- | ------: |
| Accuracy  |  99.90% |
| Precision | 100.00% |
| Recall    |  97.06% |
| F1-Score  |  98.51% |
| ROC-AUC   |  98.53% |

## Observations

* The baseline LightGBM model achieved excellent predictive performance.
* The model correctly identified nearly all machine failures.
* Precision of 100% indicates there were no false positive predictions on the test set.
* Recall of 97.06% shows that most machine failures were detected successfully.
* The high ROC-AUC score demonstrates strong class separation capability.

## Conclusion

The baseline LightGBM model provides a strong benchmark for the predictive maintenance system. The next stage will focus on improving robustness through Stratified 5-Fold Cross Validation and SMOTE to better handle the imbalanced dataset.

# Module 2 — Analytics and Predictive Modeling

## Project Overview

This module performs exploratory data analysis and predictive modeling using
the Titanic dataset.

The dataset was loaded in `01_eda.ipynb`, cleaned, and saved as `titanic.csv`.

Final cleaned dataset:

- Rows: 889
- Columns: 14

The modeling notebook `02_modeling.ipynb` uses the cleaned `titanic.csv`
as its input dataset.

## Files

- `01_eda.ipynb` — Exploratory Data Analysis
- `02_modeling.ipynb` — Predictive Modeling
- `titanic.csv` — Final cleaned dataset
- `best_titanic_pipeline.joblib` — Saved complete modeling pipeline

## Classification Modeling

Three classification models were developed:

1. Logistic Regression
2. Decision Tree
3. Random Forest

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

## Class Imbalance

The following approaches were compared:

- Baseline
- Class Weight Balanced
- SMOTE

SMOTE was applied only to the training data.

## Hyperparameter Tuning

Random Forest hyperparameters were tuned using GridSearchCV with 5-fold
cross-validation.

Out-of-bag scoring was also used for Random Forest.

## Regression

A Linear Regression model was developed to predict Fare.

The regression model was evaluated using:

- MAE
- RMSE
- R²
- Adjusted R²

A residual plot was used to assess heteroscedasticity.

## Final Model

The final classification model was selected based on the classification
evaluation metrics.

The complete preprocessing and modeling pipeline was saved as:

`best_titanic_pipeline.joblib`

The saved pipeline was reloaded and tested using raw input data.

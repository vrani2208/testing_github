# Module 2 — Analytics and Predictive Modeling

## Project Overview

This module performs exploratory data analysis and predictive modeling using
the Titanic dataset.

The dataset was loaded in `01_eda.ipynb`, cleaned, and saved as `titanic.csv`.

### Final Cleaned Dataset

- Rows: 889
- Columns: 14

The modeling notebook `02_modeling.ipynb` uses the cleaned `titanic.csv` as
its input dataset.

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

SMOTE was applied only to the training data to avoid data leakage.

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

## EDA Interpretations

### Missing Values

The cleaned Titanic dataset contains 889 rows and 14 columns. Missing values
were handled during the data-cleaning stage before modeling.

### Age and Fare Distributions

The Age and Fare distributions were examined using histograms and box plots.
The Fare distribution is positively skewed, with a longer right tail caused
by relatively high fare values.

The mean, median, and mode of Fare were calculated and reported in the EDA
notebook to describe its central tendency.

### Outlier Analysis

The IQR method was used to identify potential outliers in Age and Fare.
Fare contained more noticeable extreme values because of its right-skewed
distribution.

### Survival by Sex

Survival rates were compared across passenger sex. The analysis showed a
clear difference in survival outcomes between male and female passengers.

### Survival by Passenger Class

Survival rates were also compared across passenger classes. Passenger class
showed a meaningful relationship with survival outcomes.

### Survival by Sex and Passenger Class

A combined analysis of sex and passenger class showed that survival patterns
varied across both variables. This indicates that both passenger sex and
class provide useful predictive information for the classification task.

### Correlation Analysis

A 6×6 correlation matrix was created using the selected numerical variables,
excluding `adult_male` and `alone`.

The strongest correlations identified in the EDA were interpreted in the
notebook and were considered when understanding relationships between the
variables.

### Multivariate Analysis

Multiple multivariate visualizations were created to examine relationships
between passenger characteristics and survival. These included combinations
of sex, passenger class, age, fare, and survival.

### Standardization

Age and Fare were standardized using StandardScaler. After standardization,
both variables had a mean approximately equal to 0 and a standard deviation
approximately equal to 1.

## Model Comparison

### Classification Models

| Model | Accuracy | Precision | Recall | F1 | AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8090 | 0.7833 | 0.6912 | 0.7344 | 0.8610 |
| Decision Tree | 0.7640 | 0.7600 | 0.5588 | 0.6441 | 0.8374 |
| Random Forest | 0.8090 | 0.7656 | 0.7206 | 0.7424 | 0.8196 |

### Regression Model

| Model | MAE | RMSE | R² | Adjusted R² |
|---|---:|---:|---:|---:|
| Linear Regression | 21.1386 | 41.7465 | 0.3468 | 0.3118 |

Classification and regression metrics are presented as separate groups because
they evaluate different types of predictive tasks and are not directly
comparable.

## Class Imbalance Analysis

Three approaches were compared for handling class imbalance:

| Strategy | Precision | Recall | F1 |
|---|---:|---:|---:|
| Baseline | 0.7833 | 0.6912 | 0.7344 |
| Class Weight Balanced | 0.7183 | 0.7500 | 0.7338 |
| SMOTE | 0.7353 | 0.7353 | 0.7353 |

The comparison shows how different imbalance-handling strategies affect
precision, recall, and F1 score. SMOTE was applied only to the training data
to avoid data leakage.

## Final Model

The final classification model selected for this project was Logistic
Regression. The selection was based on the classification evaluation metrics
documented in the model comparison and final recommendation sections.

## Final Recommendation

Based on the classification results, Logistic Regression was selected as the
final classifier. It achieved an accuracy of 0.8090, precision of 0.7833,
recall of 0.6912, F1 score of 0.7344, and ROC-AUC of 0.8610.

Random Forest achieved the same accuracy of 0.8090 and had a higher recall of
0.7206 and F1 score of 0.7424. However, Logistic Regression achieved higher
precision and ROC-AUC.

Therefore, Logistic Regression was selected as the final classification model
based on the evaluation criteria used in this project.

The complete preprocessing and modeling pipeline was saved as
`best_titanic_pipeline.joblib`.

The saved pipeline was successfully reloaded and tested using raw input data.

## Regression Conclusion

The Linear Regression model achieved:

- MAE: 21.1386
- RMSE: 41.7465
- R²: 0.3468
- Adjusted R²: 0.3118

The residual plot showed that the residual variance was not constant across
the range of predicted Fare values. This provides visual evidence of
heteroscedasticity in the regression model.

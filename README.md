# Student Stress Monitoring

**Paper Title:** Protecting Student Mental Health with a Context-Aware Machine Learning Framework for Stress Monitoring

This repository contains the implementation, preprocessing, and ML pipelines used to analyze and predict student stress levels using publicly available survey datasets.

## 📁 Datasets Used

### Dataset 01: [Student Stress Factors: A Comprehensive Analysis](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data)

- **File:** stressLevelDataset.csv
- **Rows:** 1100
- **Columns:** 21
- **Missing Values:** No
- **Duplicates:** None
- **Target:** stress_level (3 classes)

This dataset includes psychological, physiological, academic, social, and environmental stress factors reported by students in a nationwide survey.

---

### Dataset 02: [Stress and Well-being Data of College Students](https://www.kaggle.com/datasets/ashutoshsingh22102/stress-and-well-being-data-of-college-students)

- **File:** Stress Dataset.csv
- **Rows:** 843
- **Columns:** 26
- **Missing Values:** No
- **Duplicates:** 27
- **Target:** Type of stress (eustress or distress)

Collected via Google Forms, this dataset captures emotional, academic, and health-related stress indicators from college students aged 18–21.

---

## ✅ Results

### Dataset 01: Student Stress Factors

| ML Model                          | Configuration       | Accuracy | F1 Score | Recall  | Precision |
| --------------------------------- | ------------------- | -------- | -------- | ------- | --------- |
| Voting Classifier (hard)          | Mixed Preprocessing | 93.091%  | 93.099%  | 93.086% | 93.126%   |
| Voting Classifier (weighted_hard) | Mixed Preprocessing | 93.091%  | 93.091%  | 93.086% | 93.099%   |
| Random Forest                     | SelectKBest         | 92.364%  | 92.365%  | 92.356% | 92.378%   |
| Voting Classifier (soft)          | Mixed Preprocessing | 92.364%  | 92.356%  | 92.356% | 92.356%   |
| Voting Classifier (weighted_soft) | Mixed Preprocessing | 92.364%  | 92.365%  | 92.356% | 92.378%   |
| AdaBoost                          | SelectKBest         | 92.000%  | 92.005%  | 92.083% | 92.121%   |
| XGBoost                           | SelectKBest         | 91.636%  | 91.636%  | 91.776% | 92.014%   |
| Gradient Boosting                 | SelectKBest         | 91.273%  | 91.279%  | 91.404% | 91.498%   |
| Stacking Classifier               | Mixed Preprocessing | 91.273%  | 91.252%  | 91.220% | 91.317%   |
| Support Vector Machine            | PCA                 | 90.546%  | 90.557%  | 90.551% | 90.567%   |
| Bagging                           | SelectKBest         | 89.455%  | 89.493%  | 89.508% | 89.716%   |

---

### Dataset 02: Stress and Well-being Data

| ML Model                          | Configuration       | Accuracy | F1 Score | Recall  | Precision |
| --------------------------------- | ------------------- | -------- | -------- | ------- | --------- |
| Stacking Classifier               | Mixed Preprocessing | 99.530%  | 97.950%  | 99.830% | 96.300%   |
| Support Vector Machine            | PCA                 | 99.052%  | 96.494%  | 93.939% | 99.656%   |
| Voting Classifier (weighted_hard) | Mixed Preprocessing | 99.052%  | 96.494%  | 93.939% | 99.656%   |
| Voting Classifier (weighted_soft) | Mixed Preprocessing | 99.052%  | 96.494%  | 93.939% | 99.656%   |
| Voting Classifier (soft)          | Mixed Preprocessing | 97.630%  | 89.942%  | 83.712% | 99.154%   |
| Voting Classifier (hard)          | Mixed Preprocessing | 97.156%  | 87.318%  | 79.546% | 98.990%   |
| AdaBoost                          | Original Data       | 96.683%  | 85.866%  | 79.372% | 94.818%   |
| XGBoost                           | SelectKBest         | 96.209%  | 82.058%  | 73.485% | 98.667%   |
| Gradient Boosting                 | Normalized Data     | 95.735%  | 79.044%  | 69.318% | 98.508%   |
| Random Forest                     | SelectKBest         | 94.787%  | 72.332%  | 63.258% | 98.194%   |
| Bagging                           | SelectKBest         | 94.313%  | 68.831%  | 59.091% | 98.039%   |

---

# -*- coding: utf-8 -*-
"""mental_health_ (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18hLlDiLhRXf7EnubKi0nLLarb6YyExsD
"""

# === Import Libraries ===
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, KFold
from sklearn.feature_selection import SelectKBest, f_classif, RFECV
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = '/content/mental_health_wearable_data.csv'
data2 = pd.read_csv(file_path)

data2.head()

print("Shape:", data2.shape)

print("Columns:", list(data2.columns))

print("Duplicated rows:", data2.duplicated().sum())

data2.info()

print(data2.count())

data2 = data2.drop(data2.columns[0], axis=1)

# Correlation heatmap
plt.figure(figsize=(15, 15))
numeric_data = data2.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Expand structured columns
eeg_expanded = data2['EEG_Frequency_Bands'].apply(ast.literal_eval).apply(pd.Series)
eeg_expanded.columns = [f'EEG_Band_{i+1}' for i in eeg_expanded.columns]

preprocessed_expanded = data2['Preprocessed_Features'].apply(ast.literal_eval).apply(pd.Series)
preprocessed_expanded.columns = ['Feature_1', 'Feature_2']

#Encode categorical variables
categorical_cols = ['Cognitive_State', 'Emotional_State', 'Gender', 'Session_Type', 'Environmental_Context']
encoded_df = data2[categorical_cols].apply(LabelEncoder().fit_transform)

# Select numerical columns
numerical_features = data2[['GSR_Values', 'Age', 'Duration (minutes)']]

# Combine all features
X = pd.concat([eeg_expanded, preprocessed_expanded, numerical_features, encoded_df], axis=1)
y = data2['Target']

imputer = SimpleImputer(strategy='mean')
scaler = StandardScaler()

X_imputed = imputer.fit_transform(X)
X_scaled = scaler.fit_transform(X_imputed)

# Feature selection/reduction
skb = SelectKBest(score_func=f_classif, k=10)
X_kbest = skb.fit_transform(X_scaled, y)

rf = RandomForestClassifier(random_state=42)
rfecv = RFECV(estimator=rf, step=1, cv=5, scoring='accuracy')
X_rfecv = rfecv.fit_transform(X_scaled, y)

pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_scaled)

# All feature sets
feature_sets = {
    'No_Selection': X_scaled,
    'SelectKBest': X_kbest,
    'RFECV': X_rfecv,
    'PCA': X_pca
}

# Train-test split options
splits = {
    '70-30': 0.3,
    '75-25': 0.25,
    '80-20': 0.2
}

# Models
models = {
    'SVM': SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42),
    'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42)
}

results = []

for split_name, test_size in splits.items():
    for fs_name, X_fs in feature_sets.items():
        X_train, X_test, y_train, y_test = train_test_split(X_fs, y, test_size=test_size, random_state=42)

        for model_name, model in models.items():
            clf = model
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)

            print(f"Split: {split_name} | Feature Set: {fs_name} | Model: {model_name}")
            print("Accuracy:", acc)
            print("Confusion Matrix:\n", cm)
            print("Classification Report:\n", classification_report(y_test, y_pred))
            print("-" * 60)

            results.append({
                'Split': split_name,
                'Feature_Set': fs_name,
                'Model': model_name,
                'Accuracy': acc,
                'Precision': report['macro avg']['precision'],
                'Recall': report['macro avg']['recall'],
                'F1-Score': report['macro avg']['f1-score']
            })

# Save as DataFrame
results_df = pd.DataFrame(results)

# Pivot Table Summary
pivot_df = results_df.pivot_table(index=['Feature_Set', 'Model'], columns='Split', values='Accuracy')
print("\nSummary of Accuracy Results:\n")
print(pivot_df)

# Barplot of results
sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
sns.barplot(data=results_df, x='Feature_Set', y='Accuracy', hue='Model')
plt.title('Model Accuracy by Feature Selection Method')
plt.ylim(0, 1)
plt.show()

# K-Fold Evaluation
print("\n\n===== K-FOLD CROSS VALIDATION RESULTS =====")
kf_results = []

kf = KFold(n_splits=5, shuffle=True, random_state=42)

for fs_name, X_fs in feature_sets.items():
    for model_name, model in models.items():
        clf = model
        scores = cross_val_score(clf, X_fs, y, cv=kf)
        y_pred = cross_val_predict(clf, X_fs, y, cv=kf)
        report = classification_report(y, y_pred, output_dict=True)

        kf_results.append({
            'Feature_Set': fs_name,
            'Model': model_name,
            'Accuracy': np.mean(scores),
            'Precision': report['macro avg']['precision'],
            'Recall': report['macro avg']['recall'],
            'F1-Score': report['macro avg']['f1-score']
        })

# Show K-Fold results
kf_results_df = pd.DataFrame(kf_results)
print(kf_results_df)
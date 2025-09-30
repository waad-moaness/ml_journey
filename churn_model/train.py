
import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

from sklearn.metrics import mutual_info_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Customer-Churn.csv")


df.columns = df.columns.str.lower().str.replace(' ', '_')


categorical = list(df.dtypes[df.dtypes == "object"].index)

numerical = list(df.dtypes[~(df.dtypes == "object")].index)

for c  in categorical:
    df[c] = df[c].str.lower().str.replace(' ', '_')


categorical_col = [
 'gender',
 'partner',
 'dependents',
 'phoneservice',
 'multiplelines',
 'internetservice',
 'onlinesecurity',
 'onlinebackup',
 'deviceprotection',
 'techsupport',
 'streamingtv',
 'streamingmovies',
 'contract',
 'paperlessbilling',
 'paymentmethod',
'seniorcitizen']

numerical_col = ['tenure', 'monthlycharges', 'totalcharges']


df[numerical_col] = df[numerical_col].apply(pd.to_numeric, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)


X_full = df[categorical_col+numerical_col]
y_full = df.churn

dv= DictVectorizer(sparse=False)
X_full_dict = X_full[categorical_col+numerical_col].to_dict(orient= 'records')
X_full = dv.fit_transform(X_full_dict)

scaler = StandardScaler()
X_full_scaled = scaler.fit_transform(X_full)


lr= LogisticRegression()

lr.fit(X_full_scaled,y_full)
y_predict = lr.predict(X_full_scaled)
y_pred_proba = lr.predict_proba(X_full_scaled)[:, 1] 
roc_accuracy_full= roc_auc_score(y_full,y_pred_proba)


with open("CustomerChurn.pkl", 'wb') as fout:
    pickle.dump((lr,dv,scaler),fout)


print(roc_accuracy_full)




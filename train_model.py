import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from joblib import dump

df = pd.read_csv("Scada_Data.csv")
X = df[['ProcTemp', 'EnvTemp']]
y = df['EnergyCon']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

dump(model, 'energy_predictor.joblib')

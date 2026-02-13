from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# โหลด dataset
data = pd.read_csv("bmi_dataset.csv")

X = data[['Height_cm', 'Weight_kg']]
y = data['BMI']

# แบ่ง train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# สร้างโมเดล
model = LinearRegression()
model.fit(X_train, y_train)

# ทำนาย
y_pred = model.predict(X_test)

# คำนวณค่า MSE และ R2
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2:", r2)

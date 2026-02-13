import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# โหลดข้อมูล
data = pd.read_csv("bmi_dataset.csv")

# features และ target
X = data[["Age", "Height_cm", "Weight_kg"]]
y = data["BMI"]

# แบ่ง train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# สร้างโมเดล
model = LinearRegression()
model.fit(X_train, y_train)

# บันทึกโมเดล
joblib.dump(model, "bmi_model.pkl")

print("Model trained and saved as bmi_model.pkl")

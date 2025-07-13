import joblib
import numpy as np
from sklearn.datasets import load_iris
from models.mlmodels import IrisFeatures

# Define predict method
def predict_class(features: IrisFeatures):
    model = joblib.load("mlutil/iris_rf_model.pkl")
    target_names = load_iris().target_names
    sample = np.array([[features.sepal_length, features.sepal_width,
                        features.petal_length, features.petal_width]])
    prediction = model.predict(sample)
    print(f"Predicted Class: {target_names[prediction[0]]}")
    return target_names[prediction[0]]

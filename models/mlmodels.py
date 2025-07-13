from pydantic import BaseModel

class IrisFeatures(BaseModel):
    sepal_length: float = 6.2
    sepal_width: float = 3.4
    petal_length: float = 5.4
    petal_width: float = 2.3
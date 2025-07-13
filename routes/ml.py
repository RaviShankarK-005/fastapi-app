from fastapi import APIRouter, Depends
from models.mlmodels import IrisFeatures
from mlutil.predict import predict_class
import authutil.auth as authimpl

router = APIRouter(
    prefix="",
    dependencies=[Depends(authimpl.get_current_user)],  # 🔒 applies to all routes
    tags=["mlutil"]
)

# Endpoint
@router.post("/predict")
def predict_endpoint(features: IrisFeatures):
    predicted = predict_class(features)
    return {"predicted_class": predicted}
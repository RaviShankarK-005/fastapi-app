from fastapi import FastAPI
from routes import user,ml,jwt

app=FastAPI()
app.include_router(user.router)
app.include_router(ml.router)
app.include_router(jwt.router)

# Endpoint
@app.post("/")
def home():
    return {"body":"homee!"}
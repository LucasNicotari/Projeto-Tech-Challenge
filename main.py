from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Vitibrasil API",
    description="Consulta aos dados da vitivinicultura brasileira",
    version="1.0"
)

app.include_router(router)

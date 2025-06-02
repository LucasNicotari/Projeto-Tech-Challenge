from fastapi import APIRouter, Query
from app.services import ler_csv, ler_csv_filtrado

router = APIRouter()

@router.get("/producao")
def producao(ano: int = Query(None, description="Filtra os dados por ano")):
    return ler_csv_filtrado("dados/Producao.csv", ano)

@router.get("/processamento")
def processamento():
    return ler_csv("dados/Processamento.csv")

@router.get("/comercializacao")
def comercializacao():
    return ler_csv("dados/Comercializacao.csv")

@router.get("/importacao")
def importacao():
    return ler_csv("dados/Importacao.csv")

@router.get("/exportacao")
def exportacao():
    return ler_csv("dados/Exportacao.csv")

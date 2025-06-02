import pandas as pd

def ler_csv(caminho: str, encoding="utf-8", sep=","):
    df = pd.read_csv(caminho, encoding=encoding, sep=sep)
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")

def ler_csv_filtrado(caminho: str, ano: int = None, encoding="utf-8", sep=","):
    df = pd.read_csv(caminho, encoding=encoding, sep=sep)
    df = df.where(pd.notnull(df), None)

    if ano:
        ano_str = str(ano)
        if ano_str in df.columns:
            if "produto" in df.columns:
                df = df[["produto", ano_str]]
            else:
                df = df[[ano_str]]
        else:
            return {"erro": f"Ano {ano} não encontrado no arquivo."}

    return df.to_dict(orient="records")

from fastapi import FastAPI, Query
from services import get_token, get_equipamentos

app = FastAPI()

# Endpoint com query param
@app.get("/equipamentos")
def equipamentos(status: str = Query(default="Y", regex="^(Y|N)$")):
    try:
        token = get_token()
        dados = get_equipamentos(token, status)
        return dados
    except Exception as e:
        return {"erro": str(e)}

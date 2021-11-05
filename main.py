import uvicorn
from fastapi import FastAPI
from router import contato
from database import criar_bd
from mangum import Mangum

app = FastAPI()

criar_bd()

app.include_router(contato)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

handler = Mangum(app=app)

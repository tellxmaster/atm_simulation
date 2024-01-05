# app/main.py

from fastapi import FastAPI
import uvicorn
from app.controllers import account_controller, transaction_controller
from database import engine, init_db  # Importa la función init_db
from fastapi.middleware.cors import CORSMiddleware

# Inicializar la base de datos
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(account_controller.router)
app.include_router(transaction_controller.router)

# Opcional: Si quieres iniciar el servidor directamente desde aquí
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

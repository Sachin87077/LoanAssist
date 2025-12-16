from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(title="LoanAssist Backend")

app.include_router(chat_router)

@app.get("/")
def health():
    return {"status": "ok"}

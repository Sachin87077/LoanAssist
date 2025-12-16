from fastapi import APIRouter
from pydantic import BaseModel
from master_agent.orchestrator import MasterAgent

router = APIRouter()
agent = MasterAgent()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    reply = agent.handle_message(req.message)
    return {"reply": reply}

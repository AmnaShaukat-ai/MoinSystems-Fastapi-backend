from fastapi import APIRouter
from models.chat_models import ChatRequest, ChatResponse
from services.rag_service import chatbot

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    answer = chatbot(request.query)

    return ChatResponse(
        answer=answer,
        sources=[]
    )

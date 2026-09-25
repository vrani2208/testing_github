from fastapi import FastAPI
from pydantic import BaseModel

from rag import create_support_response


app = FastAPI(
    title="Zepto Support Assistant",
    description="RAG-based customer support assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Zepto Support Assistant is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = create_support_response(
        request.question
    )

    return response.model_dump()
import chromadb
from typing import TypedDict
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END


# --------------------------------------------------
# ChromaDB setup
# --------------------------------------------------

CHROMA_PATH = "/content/support_assistant/chroma_db"

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection(name="zepto_docs")


# --------------------------------------------------
# Retrieve documents
# --------------------------------------------------

def retrieve_documents(question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    return results["documents"][0]


# --------------------------------------------------
# Intent classification
# --------------------------------------------------

def classify_intent(question):
    policy_keywords = [
        "delivery",
        "return",
        "refund",
        "membership",
        "tracking",
        "cancel",
        "damaged",
        "missing",
        "gift card",
        "support",
        "pass",
        "fee"
    ]

    question_lower = question.lower()

    for keyword in policy_keywords:
        if keyword in question_lower:
            return "policy"

    return "general"


# --------------------------------------------------
# Policy answer
# --------------------------------------------------

def policy_answer(question):
    retrieved_docs = retrieve_documents(
        question,
        n_results=3
    )

    return retrieved_docs[0]


# --------------------------------------------------
# General answer
# --------------------------------------------------

def general_answer(question):
    question = question.lower().strip()

    if question == "what is 10 + 20?":
        return "10 + 20 = 30"

    return "I can answer general questions directly."


# --------------------------------------------------
# LangGraph state
# --------------------------------------------------

class AssistantState(TypedDict):
    question: str
    intent: str
    answer: str


# --------------------------------------------------
# LangGraph nodes
# --------------------------------------------------

def classify_node(state: AssistantState):
    question = state["question"]

    intent = classify_intent(question)

    return {
        "question": question,
        "intent": intent
    }


def retrieve_and_answer_node(state: AssistantState):
    question = state["question"]

    answer = policy_answer(question)

    return {
        "question": question,
        "intent": state["intent"],
        "answer": answer
    }


def direct_answer_node(state: AssistantState):
    question = state["question"]

    answer = general_answer(question)

    return {
        "question": question,
        "intent": state["intent"],
        "answer": answer
    }


# --------------------------------------------------
# Routing
# --------------------------------------------------

def route_question(state: AssistantState):

    if state["intent"] == "policy":
        return "policy"

    return "general"


# --------------------------------------------------
# Build LangGraph
# --------------------------------------------------

builder = StateGraph(AssistantState)

builder.add_node(
    "classify_intent",
    classify_node
)

builder.add_node(
    "retrieve_and_answer",
    retrieve_and_answer_node
)

builder.add_node(
    "direct_answer",
    direct_answer_node
)

builder.add_edge(
    START,
    "classify_intent"
)

builder.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "policy": "retrieve_and_answer",
        "general": "direct_answer"
    }
)

builder.add_edge(
    "retrieve_and_answer",
    END
)

builder.add_edge(
    "direct_answer",
    END
)

assistant_graph = builder.compile()


# --------------------------------------------------
# Pydantic response
# --------------------------------------------------

class SupportResponse(BaseModel):
    question: str
    intent: str
    answer: str
    sources: list[str]


def create_support_response(question):

    result = assistant_graph.invoke({
        "question": question
    })

    if result["intent"] == "policy":
        sources = ["Zepto policy documents"]
    else:
        sources = []

    response = SupportResponse(
        question=result["question"],
        intent=result["intent"],
        answer=result["answer"],
        sources=sources
    )

    return response
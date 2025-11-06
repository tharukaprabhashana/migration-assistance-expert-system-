import logging
import os
from typing import Any, Dict, List, Tuple

from fastapi import FastAPI
from pydantic import BaseModel

from chat_agent import PersonSlots, extract_and_plan, chat_turn, format_results_natural
from engine import MigrationEngine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("expert-chat")

app = FastAPI(title="Migration Expert System API", version="0.1.0")


class ExtractRequest(BaseModel):
    text: str
    state: Dict[str, Any] | None = None


class ExtractResponse(BaseModel):
    slots: Dict[str, Any]
    questions: List[str]


class RunRequest(BaseModel):
    person: Dict[str, Any]


class RunResponse(BaseModel):
    results: Dict[str, Any]

class ChatTurnRequest(BaseModel):
    text: str
    state: Dict[str, Any] | None = None
    history: list[dict] = []

class ChatTurnResponse(BaseModel):
    assistant: str
    state: Dict[str, Any]
    ready: bool

@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/extract_and_plan", response_model=ExtractResponse)
async def api_extract_and_plan(req: ExtractRequest) -> ExtractResponse:
    logger.info("/extract_and_plan called: text=%s", req.text)
    state_slots = PersonSlots(**(req.state or {}))
    merged, questions = extract_and_plan(req.text, state_slots)
    logger.info(
        "extracted: preferred_country=%s marital_status=%s missing=%d",
        merged.preferred_country,
        merged.marital_status,
        len(questions),
    )
    return ExtractResponse(slots=merged.dict(), questions=list(questions))


@app.post("/run_engine", response_model=RunResponse)
async def api_run_engine(req: RunRequest) -> RunResponse:
    logger.info("/run_engine called")
    engine = MigrationEngine()
    # Normalize spouse defaults when not married
    person = dict(req.person)
    if (person.get("marital_status") or "").lower() != "married":
        person["has_spouse"] = False
        person["spouse_is_working"] = False
    results = engine.run_for_person(person)
    logger.info(
        "engine done: elig=%d points=%d alts=%d",
        len(results.get("eligibility") or []),
        len(results.get("points") or []),
        len(results.get("alternative_suggestions") or []),
    )
    return RunResponse(results=results)


class FormatRequest(BaseModel):
    results: Dict[str, Any]
    state: Dict[str, Any] | None = None
    show_alternatives: bool = True


class FormatResponse(BaseModel):
    message: str


@app.post("/format_results", response_model=FormatResponse)
async def api_format_results(req: FormatRequest) -> FormatResponse:
    logger.info("/format_results called")
    try:
        state = PersonSlots(**(req.state or {}))
        msg = format_results_natural(req.results, state, show_alternatives=req.show_alternatives)
        return FormatResponse(message=msg)
    except Exception as e:
        logger.exception("format_results failed")
        raise e


@app.post("/chat_turn", response_model=ChatTurnResponse)
async def api_chat_turn(req: ChatTurnRequest) -> ChatTurnResponse:
    logger.info("/chat_turn called: text=%s", req.text)
    state_slots = PersonSlots(**(req.state or {}))
    assistant, new_state, ready = chat_turn(req.text, state_slots, req.history or [])
    logger.info("chat_turn ready=%s preferred=%s", ready, new_state.preferred_country)
    return ChatTurnResponse(assistant=assistant, state=new_state.dict(), ready=ready)

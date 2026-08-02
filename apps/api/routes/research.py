"""Research API routes - MVP skeleton."""

from datetime import datetime


def get_research(research_id: str):
    return {
        "research_id": research_id,
        "status": "draft",
        "updated_at": datetime.utcnow().isoformat(),
    }


def create_research(payload: dict):
    return {
        "research_id": payload.get("research_id"),
        "status": "created",
    }

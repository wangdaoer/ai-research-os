from __future__ import annotations

import os
from contextlib import asynccontextmanager
from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import JSON, Date, Float, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./research.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)


class Base(DeclarativeBase):
    pass


class ResearchRecord(Base):
    __tablename__ = "research_records"
    research_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    company: Mapped[str] = mapped_column(String(80))
    research_date: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(24))
    confidence: Mapped[float] = mapped_column(Float)
    thesis: Mapped[str] = mapped_column(String(500))
    decision: Mapped[dict] = mapped_column(JSON)
    agents: Mapped[list] = mapped_column(JSON)
    risks: Mapped[list] = mapped_column(JSON)


SEED = [
    {
        "research_id": "CN-300458-20260802-001",
        "ticker": "300458",
        "company": "全志科技",
        "research_date": date(2026, 8, 2),
        "status": "WATCH",
        "confidence": 0.58,
        "thesis": "端侧 AI 与 AIoT 需求能否穿透到收入、利润和现金流。",
        "decision": {"action": "WATCH", "position": "0%-3%", "reason": "等待商业化与盈利验证"},
        "agents": [
            {"name": "Fundamental", "score": 82, "conclusion": "经营改善仍需财报验证"},
            {"name": "Industry", "score": 78, "conclusion": "端侧 AI 方向积极，兑现速度不确定"},
            {"name": "Valuation", "score": 70, "conclusion": "估值可能领先盈利"},
            {"name": "Bear", "score": 91, "conclusion": "AI 叙事强于收入是主要风险"},
        ],
        "risks": ["AI 商业化慢于预期", "毛利率承压", "估值提前反映增长"],
    },
    {
        "research_id": "CN-300750-20260802-001",
        "ticker": "300750",
        "company": "宁德时代",
        "research_date": date(2026, 8, 2),
        "status": "TRACKING",
        "confidence": 0.72,
        "thesis": "全球竞争优势与储能增长能否提供高于当前定价的增量价值。",
        "decision": {"action": "WATCH", "position": "0%-5%", "reason": "价格与赔率仍需验证"},
        "agents": [
            {"name": "Fundamental", "score": 90, "conclusion": "规模与现金创造能力较强"},
            {"name": "Industry", "score": 86, "conclusion": "动力电池与储能长期需求稳健"},
            {"name": "Valuation", "score": 74, "conclusion": "好公司仍需匹配好价格"},
            {"name": "Bear", "score": 84, "conclusion": "价格战与海外风险需持续跟踪"},
        ],
        "risks": ["行业价格竞争", "海外政策与本地化", "估值压缩"],
    },
]


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        for item in SEED:
            if session.get(ResearchRecord, item["research_id"]) is None:
                session.add(ResearchRecord(**item))
        session.commit()
    yield


app = FastAPI(title="AI Research OS API", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchCreate(BaseModel):
    ticker: str = Field(pattern=r"^\d{6}$")
    company: str
    thesis: str


def serialize(row: ResearchRecord) -> dict:
    return {
        "research_id": row.research_id,
        "ticker": row.ticker,
        "company": row.company,
        "research_date": row.research_date.isoformat(),
        "status": row.status,
        "confidence": row.confidence,
        "thesis": row.thesis,
        "decision": row.decision,
        "agents": row.agents,
        "risks": row.risks,
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/research")
def list_research() -> list[dict]:
    with Session(engine) as session:
        rows = session.scalars(select(ResearchRecord).order_by(ResearchRecord.ticker)).all()
        return [serialize(row) for row in rows]


@app.get("/research/{ticker}")
def get_research(ticker: str) -> dict:
    with Session(engine) as session:
        row = session.scalar(select(ResearchRecord).where(ResearchRecord.ticker == ticker))
        if row is None:
            raise HTTPException(status_code=404, detail="research not found")
        return serialize(row)


@app.post("/research", status_code=201)
def create_research(payload: ResearchCreate) -> dict:
    research_id = f"CN-{payload.ticker}-{date.today():%Y%m%d}-001"
    row = ResearchRecord(
        research_id=research_id,
        ticker=payload.ticker,
        company=payload.company,
        research_date=date.today(),
        status="RESEARCHING",
        confidence=0.0,
        thesis=payload.thesis,
        decision={"action": "PENDING", "position": "0%", "reason": "等待 Agent 分析"},
        agents=[],
        risks=[],
    )
    with Session(engine) as session:
        if session.get(ResearchRecord, research_id):
            raise HTTPException(status_code=409, detail="research already exists")
        session.add(row)
        session.commit()
    return serialize(row)

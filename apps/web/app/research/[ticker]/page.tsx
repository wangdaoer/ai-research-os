import { notFound } from "next/navigation";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

type Agent = { name: string; score: number; conclusion: string };
type Research = {
  ticker: string;
  company: string;
  status: string;
  confidence: number;
  thesis: string;
  decision: { action: string; position: string; reason: string };
  agents: Agent[];
  risks: string[];
};

async function getResearch(ticker: string): Promise<Research | null> {
  const response = await fetch(`${API_URL}/research/${ticker}`, { cache: "no-store" });
  if (response.status === 404) return null;
  if (!response.ok) throw new Error("无法读取研究数据");
  return response.json();
}

export default async function ResearchPage({ params }: { params: Promise<{ ticker: string }> }) {
  const { ticker } = await params;
  const record = await getResearch(ticker);
  if (!record) notFound();

  return (
    <>
      <section className="hero compact">
        <p className="eyebrow">RESEARCH ROOM · {record.ticker}</p>
        <h1>{record.company}</h1>
        <p>{record.thesis}</p>
      </section>

      <section className="metrics">
        <article><span>状态</span><strong>{record.status}</strong></article>
        <article><span>置信度</span><strong>{Math.round(record.confidence * 100)}%</strong></article>
        <article><span>建议仓位</span><strong>{record.decision.position}</strong></article>
      </section>

      <div className="sectionTitle"><h2>Agent Team</h2><span>Independent analysis</span></div>
      <section className="grid agents">
        {record.agents.map(agent => (
          <article className="card" key={agent.name}>
            <div className="cardHead"><span>{agent.name}</span><b>{agent.score}</b></div>
            <p>{agent.conclusion}</p>
          </article>
        ))}
      </section>

      <section className="decision">
        <div><span>Investment Committee</span><h2>{record.decision.action}</h2><p>{record.decision.reason}</p></div>
        <div><span>主要风险</span><ul>{record.risks.map(risk => <li key={risk}>{risk}</li>)}</ul></div>
      </section>
    </>
  );
}

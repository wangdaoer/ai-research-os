import Link from "next/link";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

type Research = {
  research_id: string;
  ticker: string;
  company: string;
  status: string;
  confidence: number;
  thesis: string;
  decision: { action: string; position: string; reason: string };
  risks: string[];
};

async function getResearch(): Promise<Research[]> {
  const response = await fetch(`${API_URL}/research`, { cache: "no-store" });
  if (!response.ok) throw new Error("无法读取研究数据");
  return response.json();
}

export default async function DashboardPage() {
  const records = await getResearch();
  return (
    <>
      <section className="hero">
        <p className="eyebrow">PERSONAL INVESTMENT COMMAND CENTER</p>
        <h1>把研究、决策与复盘放进同一个系统。</h1>
        <p>当前 Alpha 版本已接通 Next.js、FastAPI 与 PostgreSQL，并加载两个真实研究案例。</p>
      </section>

      <section className="metrics">
        <article><span>研究案例</span><strong>{records.length}</strong></article>
        <article><span>待跟踪</span><strong>{records.filter(x => x.status !== "ARCHIVED").length}</strong></article>
        <article><span>系统风险</span><strong>中等</strong></article>
      </section>

      <section>
        <div className="sectionTitle"><h2>研究池</h2><span>Research Memory</span></div>
        <div className="grid">
          {records.map(record => (
            <Link className="card" href={`/research/${record.ticker}`} key={record.research_id}>
              <div className="cardHead"><span>{record.ticker}</span><b>{record.status}</b></div>
              <h3>{record.company}</h3>
              <p>{record.thesis}</p>
              <div className="confidence"><span>置信度</span><strong>{Math.round(record.confidence * 100)}%</strong></div>
              <small>{record.decision.action} · {record.decision.position}</small>
            </Link>
          ))}
        </div>
      </section>

      <section className="insight">
        <span>RULE-0002</span>
        <h2>产业趋势不会自动转化为投资收益。</h2>
        <p>必须经过需求、订单、收入、利润和现金流的完整验证链。</p>
      </section>
    </>
  );
}

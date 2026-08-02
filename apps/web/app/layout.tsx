import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "AI Research OS",
  description: "Personal AI investment research operating system",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body>
        <header className="topbar">
          <Link href="/" className="brand">AI Research OS</Link>
          <nav>
            <Link href="/">Dashboard</Link>
            <Link href="/research/300458">300458</Link>
            <Link href="/research/300750">300750</Link>
          </nav>
        </header>
        <main className="shell">{children}</main>
      </body>
    </html>
  );
}

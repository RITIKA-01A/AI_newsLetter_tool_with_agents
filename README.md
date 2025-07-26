# 🧠 Agentic Newsletter Generator using CrewAI, LangChain, and Groq

This project creates an intelligent newsletter generation workflow using [CrewAI](https://docs.crewai.com/), [LangChain](https://www.langchain.com/), and [Groq's ultra-fast LLMs](https://console.groq.com/). It simulates a multi-agent collaboration between a researcher, writer, and proofreader to deliver structured, insightful, and source-backed articles on emerging tech topics.

---

## 🚀 Features

- **LLM-powered Agents**: Simulates realistic agent roles using Groq's `llama3-8b-8192` model.
- **Google Search Tool Integration**: Agents leverage real-time information using `SerperDevTool` for informed research and validation.
- **Multi-stage Workflow**:
  - 📡 **Research Agent** gathers insights and identifies key trends.
  - ✍️ **Writer Agent** converts insights into an engaging article.
  - 🧐 **Proofreader Agent** polishes, verifies facts, and appends citations and further reading links.
- **Markdown Output**: Final article is saved as a `newsletter.md` file, ready for publishing or review.

---

## 🛠️ Tech Stack

- 🧠 **CrewAI** – Agent orchestration framework
- 🧩 **LangChain** – LLM wrappers and tooling
- ⚡ **Groq** – Ultra-fast LLM inference (LLaMA3-8B)
- 🌐 **SerperDevTool** – Real-time web search via Serper API
- 🐍 Python 3.10+
- 🔐 `python-dotenv` – For managing API keys securely

---

## 📦 Installation

```bash
git clone https://github.com/RITIKA-01A/AI_newsLetter_tool_with_agents.git
cd AI_newsLetter_tool_with_agents
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## 🧪 How to Run
```
python crew.py
```

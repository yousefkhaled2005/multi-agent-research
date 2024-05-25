# Multi-Agent Autonomous Research & Technical Report Generation System

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph-brightgreen.svg)](https://github.com/langchain-ai/langgraph)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced autonomous multi-agent system designed for automated deep research, academic paper synthesis, and technical report writing in both **Arabic** and **English**. Orchestrated via **LangGraph** with cyclic feedback loops, episodic memory, citation grounding, and strict fact-verification.

---

## 🧠 Multi-Agent Orchestration Architecture

```
                    +-----------------------------+
                    |        User Prompt          |
                    | (e.g. "Arabic LLM Alignment")|
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    |       Research Planner      |
                    | (Deconstructs query into    |
                    |  sub-topics & search plans) |
                    +--------------+--------------+
                                   |
                    +--------------v--------------+
                    |       Parallel Searchers    |
                    |  +------------------------+ |
                    |  | ArXiv Academic Papers  | |
                    |  | Web Intelligence       | |
                    |  +------------------------+ |
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    |      Source Synthesizer     |
                    |  (Cross-document clustering |
                    |   & initial draft creation) |
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    |     Fact-Checking Agent     | <----+
                    |  (Claims vs Sources audit)  |      |
                    +--------------+--------------+      | Needs revision
                                   |                     |
                            [Fact Check Passed?] --------+
                                   |
                                 Yes
                                   v
                    +-----------------------------+
                    |     Bilingual Publisher     |
                    | (Formats Markdown/PDF with  |
                    |  Arabic/English Typography) |
                    +-----------------------------+
```

---

## 🌟 Key Capabilities

- **Stateful LangGraph Workflow**: True multi-agent cyclic graph supporting iterative refinement, dynamic search escalation, and human-in-the-loop checkpoints.
- **Academic & Web Grounding**: Integrated ArXiv API and SerpAPI retrieval with automated abstract parsing and PDF metadata extraction.
- **Fact-Checking & Anti-Hallucination**: Dedicated auditor agent cross-references generated claims against raw retrieved passages before report compilation.
- **Bilingual Synthesis (Arabic & English)**: Native support for Arabic academic and technical summaries with correct directional typography and terminology.
- **Episodic Memory Integration**: Remembers previous research threads and prevents duplicate document queries.
- **Production API & Streaming**: FastAPI endpoints with asynchronous task queues, SSE progress events, and Docker containerization.

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/yousefkhaled2005/multi-agent-research.git
cd multi-agent-research

python -m venv venv
# Linux / macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
cp .env.example .env
# Edit .env with your LLM provider and search keys:
# OPENAI_API_KEY=...
# ANTHROPIC_API_KEY=...
# SERPAPI_API_KEY=...
```

### 3. Run the Research Engine via CLI

```bash
python -m src.cli --topic "Recent advances in Arabic LLM fine-tuning and DPO alignment" --lang ar
```

### 4. Run the API Server

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

Interactive documentation is available at `http://localhost:8000/docs`.

---

## 📊 Sample Output Report Excerpt

> ### التقرير التقني: التطورات الحديثة في مواءمة النماذج اللغوية العربية الكبيرة
> 
> **الموجز التنفيذي:**  
> شهدت أبحاث مواءمة النماذج اللغوية (LLM Alignment) باللغة العربية تطوراً متسارعاً خلال عامي 2023–2024، مع التحول من أساليب RLHF التقليدية إلى Direct Preference Optimization (DPO) و QLoRA...  
> 
> **المراجع الأكاديمية المدققة:**  
> 1. *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* (Rafailov et al., ArXiv:2305.18290)
> 2. *AraBERTv2: Contextualized Representations for Arabic* (Antoun et al.)

---

## 🧪 Testing

```bash
pytest tests/ -v
```

---

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Yousef Khaled**  
Senior AI Systems Architect  
- GitHub: [@yousefkhaled2005](https://github.com/yousefkhaled2005)

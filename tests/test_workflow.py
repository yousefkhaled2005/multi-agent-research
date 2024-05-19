from src.graph import ResearchOrchestrator


def test_research_workflow_arabic():
    orchestrator = ResearchOrchestrator()
    state = orchestrator.run(topic="نمذجة اللغة العربية بواسطة المحولات", language="ar")
    assert state["status"] == "completed"
    assert len(state["raw_sources"]) > 0
    assert state["final_report"] is not None
    assert "الموجز التنفيذي" in state["final_report"]


def test_research_workflow_english():
    orchestrator = ResearchOrchestrator()
    state = orchestrator.run(topic="State of LLM Evaluation", language="en")
    assert state["status"] == "completed"
    assert "Executive Summary" in state["final_report"]

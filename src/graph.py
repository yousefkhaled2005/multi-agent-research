"""
LangGraph orchestration pipeline assembling the multi-agent workflow.
"""
from src.state import ResearchState
from src.agents.planner import ResearchPlannerAgent
from src.agents.searcher import LiteratureSearcherAgent
from src.agents.synthesizer import ReportSynthesizerAgent
from src.agents.fact_checker import FactCheckerAgent
from src.agents.publisher import ReportPublisherAgent


class ResearchOrchestrator:
    """Stateful coordinator for research lifecycle."""

    def __init__(self):
        self.planner = ResearchPlannerAgent()
        self.searcher = LiteratureSearcherAgent()
        self.synthesizer = ReportSynthesizerAgent()
        self.fact_checker = FactCheckerAgent()
        self.publisher = ReportPublisherAgent()

    def run(self, topic: str, language: str = "ar") -> ResearchState:
        # Initialize state
        state: ResearchState = {
            "topic": topic,
            "language": language,
            "sub_queries": [],
            "raw_sources": [],
            "draft_sections": {},
            "fact_check_notes": [],
            "revision_count": 0,
            "final_report": None,
            "status": "initialized"
        }

        # Step 1: Planning
        state = self.planner.plan(state)

        # Step 2: Information Retrieval
        state = self.searcher.search(state)

        # Step 3: Synthesis
        state = self.synthesizer.synthesize(state)

        # Step 4: Verification Loop
        state = self.fact_checker.verify(state)

        # Step 5: Publishing
        state = self.publisher.publish(state)

        return state

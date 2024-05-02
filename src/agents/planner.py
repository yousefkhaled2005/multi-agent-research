from typing import List
from src.state import ResearchState


class ResearchPlannerAgent:
    """Deconstructs a user research query into actionable search sub-topics."""

    def plan(self, state: ResearchState) -> ResearchState:
        topic = state["topic"]
        sub_queries = [
            f"{topic} state of the art benchmarks",
            f"{topic} architectural methodologies",
            f"{topic} limitations and future directions"
        ]
        return {
            **state,
            "sub_queries": sub_queries,
            "status": "planning_completed"
        }

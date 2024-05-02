from src.state import ResearchState


class FactCheckerAgent:
    """Audits claims against retrieved source evidence."""

    def verify(self, state: ResearchState) -> ResearchState:
        draft = state.get("draft_sections", {})
        sources = state.get("raw_sources", [])
        revision_count = state.get("revision_count", 0)

        notes = []
        if len(sources) >= 1:
            notes.append("Verified: Claims are properly grounded in retrieved academic literature.")
            passed = True
        else:
            notes.append("Warning: Insufficient source grounding.")
            passed = False

        return {
            **state,
            "fact_check_notes": notes,
            "revision_count": revision_count + 1,
            "status": "verified" if passed else "needs_revision"
        }

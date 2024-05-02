from src.state import ResearchState, DocumentSource
from src.tools.arxiv_tool import ArXivSearchTool


class LiteratureSearcherAgent:
    """Retrieves scientific papers and authoritative web sources."""

    def __init__(self):
        self.arxiv_tool = ArXivSearchTool()

    def search(self, state: ResearchState) -> ResearchState:
        sources = list(state.get("raw_sources", []))
        for query in state.get("sub_queries", []):
            results = self.arxiv_tool.search(query, max_results=2)
            sources.extend(results)

        # Deduplicate sources by URL
        seen_urls = set()
        unique_sources = []
        for s in sources:
            if s["url"] not in seen_urls:
                seen_urls.add(s["url"])
                unique_sources.append(s)

        return {
            **state,
            "raw_sources": unique_sources,
            "status": "search_completed"
        }

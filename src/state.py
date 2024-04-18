from typing import TypedDict, List, Dict, Any, Optional


class DocumentSource(TypedDict):
    title: str
    url: str
    snippet: str
    source_type: str  # 'arxiv' | 'web'


class ResearchState(TypedDict):
    topic: str
    language: str
    sub_queries: List[str]
    raw_sources: List[DocumentSource]
    draft_sections: Dict[str, str]
    fact_check_notes: List[str]
    revision_count: int
    final_report: Optional[str]
    status: str

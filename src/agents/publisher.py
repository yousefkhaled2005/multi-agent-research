from src.state import ResearchState


class ReportPublisherAgent:
    """Formats and compiles final Markdown report with bilingual typography."""

    def publish(self, state: ResearchState) -> ResearchState:
        topic = state["topic"]
        draft = state.get("draft_sections", {})
        sources = state.get("raw_sources", [])
        lang = state.get("language", "ar")

        title = f"# التقرير البحثي: {topic}" if lang == "ar" else f"# Research Report: {topic}"
        summary_h = "## 1. الموجز التنفيذي" if lang == "ar" else "## 1. Executive Summary"
        findings_h = "## 2. أبرز النتائج والتحليلات" if lang == "ar" else "## 2. Key Findings"
        refs_h = "## 3. المراجع الأكاديمية المدققة" if lang == "ar" else "## 3. Grounded References"

        ref_lines = []
        for idx, src in enumerate(sources, 1):
            ref_lines.append(f"{idx}. [{src['title']}]({src['url']}) - *{src['snippet']}*")

        final_md = f"""{title}

{summary_h}
{draft.get('executive_summary', '')}

{findings_h}
{draft.get('key_findings', '')}

{draft.get('methodology_comparison', '')}

{refs_h}
""" + "\n".join(ref_lines)

        return {
            **state,
            "final_report": final_md,
            "status": "completed"
        }

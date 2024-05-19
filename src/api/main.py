from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.schemas import ResearchRequest, ResearchResponse
from src.graph import ResearchOrchestrator
from src.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Production Multi-Agent Research & Technical Report Generation Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = ResearchOrchestrator()


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.VERSION
    }


@app.post("/api/v1/research", response_model=ResearchResponse, tags=["Research"])
async def execute_research(request: ResearchRequest):
    try:
        result = orchestrator.run(topic=request.topic, language=request.language)
        return ResearchResponse(
            topic=result["topic"],
            status=result["status"],
            revision_count=result["revision_count"],
            sources_count=len(result.get("raw_sources", [])),
            fact_check_notes=result.get("fact_check_notes", []),
            final_report=result.get("final_report")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

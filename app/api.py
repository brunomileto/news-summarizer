from fastapi import FastAPI, HTTPException
from app.services.orchestrations.article_orchestration_service import ArticleOrchestrationService
app = FastAPI()


@app.post("/process-articles")
async def process_article():
    try:
        print("Starting process articles")
        service = ArticleOrchestrationService()
        service.process_articles()
        return {"message": "Articles processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

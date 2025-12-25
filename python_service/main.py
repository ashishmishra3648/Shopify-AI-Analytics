from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from agent import ShopifyAgent
import uvicorn
import os
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title="Shopify AI Analytics Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    shop_domain: str
    access_token: str

class QueryResponse(BaseModel):
    answer: str
    shopify_ql: Optional[str] = None
    data: Optional[dict] = None
    confidence: str

@app.get("/")
def health_check():
    return {"status": "ok", "service": "Shopify AI Analytics"}

@app.post("/analyze", response_model=QueryResponse)
async def analyze_query(request: QueryRequest):
    """
    Analyzes a natural language query, converts it to ShopifyQL, 
    fetches data from Shopify, and returns a human-readable answer.
    """
    try:
        agent = ShopifyAgent(
            shop_domain=request.shop_domain,
            access_token=request.access_token
        )
        
        result = await agent.process_question(request.query)
        
        return QueryResponse(
            answer=result["answer"],
            shopify_ql=result.get("shopify_ql"),
            data=result.get("data"),
            confidence=result.get("confidence", "medium")
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

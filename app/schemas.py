from pydantic import BaseModel
from typing import List, Optional

class JobDesc(BaseModel):
    id: str
    title: Optional[str] = None
    description: str

class MatchRequest(BaseModel):
    resume_text: str
    job_descriptions: List[JobDesc]
    top_n: int = 5

class JobMatch(BaseModel):
    id: str
    title: Optional[str]
    score: float
    matched_keywords: List[str]
    missing_keywords: List[str]

class MatchResponse(BaseModel):
    matches: List[JobMatch]

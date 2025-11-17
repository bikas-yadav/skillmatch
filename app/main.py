from fastapi import FastAPI
from app.schemas import MatchRequest, MatchResponse
from app.matcher import get_top_matches

app = FastAPI(title="SkillMatch API", version="0.1")

@app.get("/")
def root():
    return {"message": "SkillMatch API — resume to job matcher"}

@app.post("/match", response_model=MatchResponse)
def match(req: MatchRequest):
    jobs = [j.dict() for j in req.job_descriptions]
    matches = get_top_matches(req.resume_text, jobs, top_n=req.top_n)
    return {"matches": matches}

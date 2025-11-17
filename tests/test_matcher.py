from app.matcher import get_top_matches

def test_simple_match():
    resume = "python fastapi docker sql rest api"
    jobs = [
        {"id": "j1", "title": "Backend dev", "description": "python fastapi sql docker rest api"},
        {"id": "j2", "title": "Data engineer", "description": "spark hadoop scala java"}
    ]
    results = get_top_matches(resume, jobs, top_n=2)
    assert results[0]['id'] == 'j1'
    assert results[0]['score'] > results[1]['score']

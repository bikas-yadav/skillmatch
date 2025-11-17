from typing import List
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def simple_clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_top_matches(resume: str, jobs: List[dict], top_n: int = 5) -> List[dict]:
    texts = [simple_clean(resume)] + [simple_clean(j['description']) for j in jobs]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(texts)
    resume_vec = tfidf[0]
    job_vecs = tfidf[1:]
    scores = cosine_similarity(resume_vec, job_vecs).flatten()

    feature_names = np.array(vectorizer.get_feature_names_out())
    results = []
    resume_tokens = set(simple_clean(resume).split())
    for i, job in enumerate(jobs):
        score = float(scores[i])
        job_vec = job_vecs[i].toarray().flatten()
        if job_vec.sum() == 0:
            top_terms = []
        else:
            top_idx = job_vec.argsort()[-20:][::-1]
            top_terms = list(feature_names[top_idx])
        matched = [t for t in top_terms if t in resume_tokens]
        missing = [t for t in top_terms if t not in resume_tokens]
        results.append({
            'id': job.get('id'),
            'title': job.get('title'),
            'score': round(score, 4),
            'matched_keywords': matched[:10],
            'missing_keywords': missing[:10]
        })
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:top_n]

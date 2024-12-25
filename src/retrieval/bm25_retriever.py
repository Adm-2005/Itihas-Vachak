from rank_bm25 import BM25Okapi
from typing import List

class BM25Retriever:
    def __init__(self, corpus: List[str]) -> List[str]:
        self.corpus = [doc.split() for doc in corpus] 
        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        query_tokens = query.split()
        
        scores = self.bm25.get_scores(query_tokens)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

        return [self.corpus[idx] for idx in top_indices]

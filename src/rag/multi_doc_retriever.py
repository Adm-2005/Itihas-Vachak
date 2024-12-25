import sqlite3
from src.retrieval.hybrid_retriever import HybridRetriever

class MultiDocRetriever:
    def __init__(self, db_path:str, top_k:int = 5):
        self.db_path = db_path
        self.top_k = top_k
        self.retriever = HybridRetriever(db = self.db_path)

    def search(self, query:str):
        results = self.retriever.search(query, top_k = self.top_k)
        return results
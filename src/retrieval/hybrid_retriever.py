import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.indexing.hierarchical_tree import HierarchicalTree
from src.indexing.embeddings_indexer import EmbeddingsIndexer

class HybridRetriever:
    def __init__(self, index_path: str = 'data/index.faiss', db: str = 'data/db.sqlite', pdf_path: str = None, model_name: str = 'all-MiniLM-L6-v2'):
        self.indexer = EmbeddingsIndexer(model_name = model_name)
        self.hierarchy = HierarchicalTree()

        if os.path.exists(index_path):
            self.indexer.load_index(index_path = index_path, db = db)
        else:
            self.indexer.create_index()

        if pdf_path:
            self.hierarchy.build_tree_from_pdf(pdf_path)

    def retrieve(self, query: str, top_k: int = 5):
        semantic_results = self.indexer.search(query, top_k = top_k)
        
        extended_results = []
        for result in semantic_results:
            context = self.get_hierarchy_context(result)
            extended_results.append({
                "text": result,
                "hierarchy": context
            })
        
        return extended_results

    def get_hierarchy_context(self, text):
        for chapter, data in self.hierarchy.tree.items():
            if text == data['title']:
                return {"chapter": chapter, "section": None, "subsection": None}
            
            if 'sections' in data:
                for section, section_data in data['sections'].items():
                    if text == section_data['title']:
                        return {"chapter": chapter, "section": section, "subsection": None}
                    
                    if 'subsections' in section_data:
                        for subsection, subsection_title in section_data['subsections'].items():
                            if text == subsection_title:
                                return {"chapter": chapter, "section": section, "subsection": subsection}
        
        return {"chapter": None, "section": None, "subsection": None}

    def hybrid_score(self, query, text):
        query_embedding = self.indexer.model.encode([query])
        text_embedding = self.indexer.model.encode([text])
        
        semantic_score = cosine_similarity(query_embedding, text_embedding)[0][0]

        context = self.get_hierarchy_context(text)
        hierarchy_score = self.calculate_hierarchy_score(context)

        hybrid_score = 0.8 * semantic_score + 0.2 * hierarchy_score
        return hybrid_score

    def rank_results(self, query, results):
        scored_results = []
        for result in results:
            score = self.hybrid_score(query, result['text'])
            scored_results.append((result, score))
        
        scored_results.sort(key=lambda x: x[1], reverse=True)
        return [result for result, _ in scored_results]

    def search(self, query, top_k:int = 5):
        results = self.retrieve(query, top_k=top_k)
        ranked_results = self.rank_results(query, results)
        return ranked_results
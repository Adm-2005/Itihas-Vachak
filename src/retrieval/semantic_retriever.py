from src.indexing.embeddings_indexer import EmbeddingsIndexer
from src.indexing.hierarchical_tree import HierarchicalTree

class SemanticRetriever:
    def __init__(self, index_path:str = 'data/index.faiss', db:str = 'data/db.sqlite3', model_name:str = 'all-MiniLM-L6-v2'):
        self.indexer = EmbeddingsIndexer(model_name = model_name)
        self.indexer.load_index(index_path = index_path, db = db)
        self.hierarchy = HierarchicalTree()

    def load_hierarchy_from_pdf(self, pdf_path: str):
        self.hierarchy.build_tree_from_pdf(pdf_path)

    def retrieve(self, query: str, top_k: int = 5):
        results = self.indexer.search(query, top_k=top_k)
        extended_results = []

        for result in results:
            context = self.get_hierarchy_context(result)
            extended_results.append({
                "text": result,
                "hierarchy": context
            })

        return extended_results

    def get_hierarchy_context(self, text: str):
        for chapter, data in self.hierarchy.tree.items():
            if text in data['title']:
                return {"chapter": chapter, "section": None, "subsection": None}
            
            if 'sections' in data:
                for section, section_data in data['sections'].items():
                    if text in section_data['title']:
                        return {"chapter": chapter, "section": section, "subsection": None}
                    
                    if 'subsections' in section_data:
                        for subsection in section_data['subsections']:
                            if text == subsection:
                                return {"chapter": chapter, "section": section, "subsection": subsection}
                            
        return {"chapter": None, "section": None, "subsection": None}
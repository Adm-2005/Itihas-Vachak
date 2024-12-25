import pymupdf

class HierarchicalTree:
    def __init__(self):
        self.tree = {}

    def build_tree_from_pdf(self, pdf_path: str) -> dict:
        document = pymupdf.open(pdf_path)
        font_sizes = []

        for page in document:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block["lines"]:
                    for span in line["spans"]:
                        font_sizes.append(span["size"])
        
        unique_sizes = sorted(set(font_sizes), reverse=True)
        if len(unique_sizes) < 1:
            raise ValueError("No font sizes detected.")
        
        chapter_size = unique_sizes[0]
        section_size = unique_sizes[1] if len(unique_sizes) > 1 else None
        subsection_size = unique_sizes[2] if len(unique_sizes) > 2 else None

        current_chapter = None
        current_section = None

        for page in document:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        size = span["size"]

                        if size == chapter_size:
                            current_chapter = {'title': text, 'sections': {}}
                            self.tree[text] = current_chapter
                        elif section_size and size == section_size and current_chapter:
                            current_section = {'title': text, 'subsections': {}}
                            current_chapter['sections'][text] = current_section
                        elif subsection_size and size == subsection_size and current_section:
                            current_section['subsections'][text] = text

        return self.tree

    def print_tree(self):
        for chapter, data in self.tree.items():
            print(f"Chapter: {chapter}")

            if 'sections' in data and data['sections']:
                for section, section_data in data['sections'].items():
                    print(f"  Section: {section}")
                    
                    if 'subsections' in section_data and section_data['subsections']:
                        for subsection in section_data['subsections']:
                            print(f"    Subsection: {subsection}")
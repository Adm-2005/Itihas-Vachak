import os
from src.extraction.pdf_extractor import PdfExtractor
from src.extraction.text_cleaner import clean_text

def extract_and_clean():
    data_dir = 'data'

    pdf_files = [
        {
            'path': f'{data_dir}/raw/India Ancient Past By RS Sharma.pdf',
            'is_scanned': False
        },
        {
            'path': f'{data_dir}/raw/History of Medieval India By Satish Chandra.pdf',
            'is_scanned': True
        },
        {
            'path': f'{data_dir}/raw/History of Modern India By Bipin Chandra.pdf',
            'is_scanned': False
        }
    ]

    for file in pdf_files:
        extractor = PdfExtractor(pdf_path = file['path'], is_scanned = file['is_scanned'])
        extracted_text = extractor.extract_text()

        cleaned_text = clean_text(extracted_text)

        processed_text_path = f'{data_dir}/processed/{os.path.basename(file['path']).replace('.pdf', '.txt')}'

        with open(processed_text_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned_text))

        print(f'Text extracted and saved to {processed_text_path}')
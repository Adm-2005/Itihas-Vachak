import re
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s.,]", "", text)

    text = text.lower()

    sentences = nltk.sent_tokenize(text)

    return sentences
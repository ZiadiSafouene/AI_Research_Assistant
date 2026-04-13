from ai_research_assistant.src.ingestion.pdfloader import load_pdf
from ai_research_assistant.src.ingestion.text_cleaner import clean_text

def process_paper(file_path: str) -> str:
    raw_text = load_pdf(file_path)
    cleaned_text = clean_text(raw_text)
    return cleaned_text
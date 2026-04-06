import re

def clean_text(text: str) -> str:
    """
    Basic cleaning for research papers.
    """
    text = re.sub(r"\n+", "\n", text)

    text = re.split(r"References", text, flags=re.IGNORECASE)[0]
    
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    return text.strip()
from ai_research_assistant.src.ingestion.pipeline import process_paper
import os

PAPERS_DIR = "ai_research_assistant/data/raw_papers"
OUTPUT_DIR = "ai_research_assistant/data/processed_text"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(PAPERS_DIR):
    if file.endswith(".pdf"):
        path = os.path.join(PAPERS_DIR, file)
        text = process_paper(path)

        with open(os.path.join(OUTPUT_DIR, file.replace(".pdf", ".txt")), "w") as f:
            f.write(text)

print("Processing complete.")
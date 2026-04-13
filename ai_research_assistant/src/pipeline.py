from ai_research_assistant.src.ingestion.pipeline import process_paper
from ai_research_assistant.src.ingestion.chunker import chunk_text
from ai_research_assistant.src.summarization.summarizer import summarize_chunk
from ai_research_assistant.src.summarization.prompts import SUMMARY_PROMPT
from ai_research_assistant.src.summarization.aggregate import aggregate_summaries

def process_and_summarize(file_path: str):
    text = process_paper(file_path)
    chunks = chunk_text(text)

    summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk, SUMMARY_PROMPT)
        summaries.append(summary)

    final_summary = aggregate_summaries(summaries)

    return final_summary
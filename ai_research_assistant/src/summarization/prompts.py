SUMMARY_PROMPT = """
You are an AI research assistant.

Summarize the following research paper chunk into structured format:

- Problem: What problem is being solved?
- Method: What approach is used?
- Results: What are the key findings?
- Limitations: Any weaknesses?

Text:
{chunk}

Return concise answers.
"""
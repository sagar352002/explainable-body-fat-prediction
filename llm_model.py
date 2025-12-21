
# -----------------------------
# Imports
# -----------------------------
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from llm_output_template import body_fitness_prompt_template

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()


def generate_fitness_summary(llm_input: dict) -> list:
    """
    Takes llm_input dict and returns list of fitness insight bullet points
    """
    prompt = body_fitness_prompt_template(llm_input)

    llm = ChatOpenAI(
        model="openai/gpt-oss-20b:free",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0.6
    )

    response = llm.invoke(prompt)

    # Convert text → bullet list safely
    lines = [
        line.strip("•- ").strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return lines[:8]

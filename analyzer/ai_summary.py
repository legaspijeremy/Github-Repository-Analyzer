import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key
)


def generate_ai_summary(
    repo_name,
    description,
    readme,
    repo_metrics,
    documentation_score,
    documentation_metrics,
    code_quality,
    complexity_score,
    total_files,
    total_python_files,
):
    """
    Generate an AI-powered summary of a GitHub repository.
    """

    def format_metric_value(value):
        if isinstance(value, int) and not isinstance(value, bool):
            return f"{value:,}"

        return value

    # ----------------------------
    # Format Repository Metrics
    # ----------------------------

    repo_metrics_text = "\n".join(
        f"- {key.replace('_', ' ').title()}: {format_metric_value(value)}"
        for key, value in repo_metrics.items()
    )

    # ----------------------------
    # Format Documentation Metrics
    # ----------------------------

    documentation_metrics_text = "\n".join(
        f"- {key.replace('_', ' ').title()}: {format_metric_value(value)}"
        for key, value in documentation_metrics.items()
    )

    # ----------------------------
    # Format Code Quality Metrics
    # ----------------------------

    code_quality_text = "\n".join(
        f"- {key.replace('_', ' ').title()}: {format_metric_value(value)}"
        for key, value in code_quality.items()
    )

    # ----------------------------
    # Format Repository Scale Metrics
    # ----------------------------

    repository_scale_text = f"""
- Total Files: {total_files:,}
- Total Python Files: {total_python_files:,}
- Contributors: {repo_metrics["contributors"]:,}
- Complexity Score: {complexity_score}/100
"""

    # ----------------------------
    # Prompt
    # ----------------------------

    prompt = f"""
You are a Senior Software Engineer performing a professional GitHub repository review.

Analyze ONLY the repository information and metrics supplied below. Every statement
must be supported by the supplied information.

Repository Name:
{repo_name}

Description:
{description}

Repository Metrics:
{repo_metrics_text}

Documentation Score:
{documentation_score}/100

Documentation Metrics
---------------------
{documentation_metrics_text}

Code Quality Metrics:
{code_quality_text}

Repository Scale Metrics
------------------------
{repository_scale_text}

README (Partial):
{readme[:4000]}

Write the report using EXACTLY these Markdown headings and no other headings:

# Project Purpose

# Main Technologies

# Intended Users

# Key Features

# Documentation Assessment

# Code Quality Assessment

# Repository Scale

# Overall Repository Summary

Output Formatting Rules:
- Use Markdown headings exactly as listed.
- Use bullet lists instead of numbered lists where lists are helpful.
- Keep paragraphs short, with 2 to 4 sentences maximum.
- Keep the report concise and avoid unnecessary repetition.
- Use professional technical language suitable for an engineering report.
- Do not include introductory or concluding remarks outside the requested sections.

Section Guidance:
- Project Purpose: Explain what the repository does using only the name,
  description, README, and supplied metrics.
- Main Technologies: Identify only technologies explicitly present in the supplied
  information. If technologies are not clear, state that they are not clearly
  identifiable from the supplied information.
- Intended Users: Identify likely users only when supported by the supplied
  description or README. Do not speculate.
- Key Features: List only features explicitly supported by the README,
  description, or repository information.
- Documentation Assessment: Evaluate documentation using ONLY the Documentation
  Score, README Length, Headings, Code Blocks, Links, Images, Tables, and
  Sections Found. Explain how these metrics support the assessment. Do not
  comment on documentation that is unavailable.
- Code Quality Assessment: Evaluate code quality using ONLY Production Python
  Files, Total Lines of Code, Average Function Length, Average Class Size,
  Cyclomatic Complexity, and Maintainability Index. Explain what these metrics
  indicate. Do not describe values as good, bad, large, small, excellent, or poor
  unless the supplied metrics clearly justify that wording.
- Repository Scale: Summarize project scale using ONLY Total Files, Total Python
  Files, Contributors, and Complexity Score. Do not infer architecture.
- Overall Repository Summary: Provide a concise executive summary of 3 to 5
  sentences covering repository maturity, documentation, code quality, and
  project scale without introducing new information.

General Rules:
- Never hallucinate.
- Never invent technologies.
- Never invent frameworks.
- Never invent features.
- Never invent architecture or project goals.
- Never speculate.
- Never infer architecture.
- Never assume testing coverage.
- Never assume security practices.
- Never assume CI/CD pipelines.
- Never assume design patterns.
- Base every statement on the supplied repository information and metrics.
- If sufficient repository information is unavailable to answer a section,
  explicitly state: "Insufficient repository information to determine this."
  instead of making assumptions.
"""

    system_message = """
You are a Senior Software Engineer specializing in repository reviews,
documentation analysis, static code analysis, and software architecture.
You must only analyze the supplied information. Never speculate or
hallucinate. Produce professional engineering reports rather than
conversational responses.
"""

    # ----------------------------
    # Generate Summary
    # ----------------------------

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            max_completion_tokens=1200,
        )

        return response.choices[0].message.content

    except Exception as e:

        return (
            "Unable to generate AI Project Summary.\n\n"
            f"Reason: {str(e)}"
        )

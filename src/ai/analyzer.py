from src.ai.prompts import AI_ANALYSIS_PROMPT
import json

def build_ai_context(metrics):
    return {
        "dataset_summary": {
            "rows": metrics["overview"]["rows"],
            "columns": metrics["overview"]["columns"]
        },

        "data_quality": metrics["data_quality"],

        "key_patterns": {
            "categorical": metrics.get("categorical_analysis", {})
        }
    }

def build_prompt(metrics):
    structured_metrics = build_ai_context(metrics)

    return f"""
{AI_ANALYSIS_PROMPT}

METRICS:
{json.dumps(structured_metrics, indent=2, ensure_ascii=False)}
"""


def analyze_with_ai(metrics, llm_client):
    prompt = build_prompt(metrics)

    raw_output = llm_client.generate(prompt)

    structured_output = validate_ai_output(raw_output)

    return structured_output
    
def validate_ai_output(raw_output):
    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError:
        raise ValueError("AI output is not valid JSON")

    required_keys = [
        "dataset_overview",
        "data_quality_issues",
        "key_insights",
        "recommendations"
    ]

    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key: {key}")

    return data
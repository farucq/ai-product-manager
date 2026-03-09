from services.llm_service import ask_llm
from utils.helpers import log


def generate_features(issues):

    log("Generating product features")

    prompt = f"""
    Based on the following customer complaints generate product feature ideas.

    Complaints:
    {issues}

    Return a clear bullet list of features.
    """

    response = ask_llm(prompt)

    return response
from services.llm_service import ask_llm
from utils.helpers import log


def estimate_impact(features):

    log("Estimating feature impact")

    prompt = f"""
    Evaluate business impact of these features.

    {features}

    For each feature provide:

    Feature
    Impact Score (1-10)
    Expected User Adoption
    """

    result = ask_llm(prompt)

    return result
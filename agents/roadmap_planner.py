from services.llm_service import ask_llm
from utils.helpers import log


def create_roadmap(impact_analysis):

    log("Creating product roadmap")

    prompt = f"""
    Using the following impact analysis create a product roadmap.

    {impact_analysis}

    Divide roadmap into:

    Short Term
    Mid Term
    Long Term
    """

    roadmap = ask_llm(prompt)

    return roadmap
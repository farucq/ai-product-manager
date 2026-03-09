from services.sentiment_service import analyze_sentiment
from utils.helpers import load_feedback_data, clean_dataframe_reviews, log


def analyze_feedback(path):

    log("Loading feedback data")

    df = load_feedback_data(path)

    df = clean_dataframe_reviews(df)

    log("Running sentiment analysis")

    df["sentiment"] = df["review"].apply(analyze_sentiment)

    complaints = df[df["sentiment"] == "negative"]

    issues = complaints["review"].tolist()

    log(f"Found {len(issues)} negative feedback items")

    return issues, df
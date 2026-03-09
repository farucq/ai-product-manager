import pandas as pd
import re
from datetime import datetime


def load_feedback_data(file_path):

    df = pd.read_csv(file_path)

    if "review" not in df.columns:
        raise ValueError("CSV must contain a 'review' column")

    return df


def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def clean_dataframe_reviews(df):

    df["review"] = df["review"].apply(clean_text)

    return df


def format_feature_list(feature_text):

    features = []

    for line in feature_text.split("\n"):
        line = line.strip("-• ")
        if line:
            features.append(line)

    return features


def save_report(content, path="outputs/product_report.md"):

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(message):

    print(f"[{timestamp()}] {message}")
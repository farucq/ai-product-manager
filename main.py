from agents.feedback_analyzer import analyze_feedback
from agents.feature_planner import generate_features
from agents.impact_estimator import estimate_impact
from agents.roadmap_planner import create_roadmap
from utils.helpers import save_report, log


def run_pipeline(file_path):

    log("Starting AI Product Manager Pipeline")

    issues, df = analyze_feedback(file_path)

    features = generate_features(issues)

    impact = estimate_impact(features)

    roadmap = create_roadmap(impact)

    report = f"""
# AI Product Strategy Report

## Feature Suggestions

{features}

---

## Impact Analysis

{impact}

---

## Product Roadmap

{roadmap}

"""

    save_report(report)

    log("Product report generated")

    return report
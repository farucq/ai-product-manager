import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_pipeline

st.title("AI Autonomous Product Manager")

st.write("Upload a CSV file containing product feedback.")

uploaded_file = st.file_uploader(
    "Upload Feedback CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    if st.button("Run Product Analysis"):

        os.makedirs("data", exist_ok=True)

        temp_path = "data/uploaded_feedback.csv"

        df.to_csv(temp_path, index=False)

        report = run_pipeline(temp_path)

        st.markdown(report)
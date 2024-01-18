import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

    unique_qna_id = df["request_id"].unique().tolist()

    request_id = st.select_slider('Request ID', options=unique_qna_id)
    
    # select rows for each qna
    qna = df.loc[df["request_id"] == request_id]

    context = st.sidebar.text_area(label="context", value=qna["context"].iloc[0], height=1000)

    list_of_questions = qna["question"].unique().tolist()

    question = st.radio(label='Request ID', options=list_of_questions)
    ground_truth = qna[qna["question"] == question]["ground_truths"].item()
    box = st.text_area(label=question, value=ground_truth)
   


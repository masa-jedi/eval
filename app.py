import streamlit as st
import pandas as pd

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

    unique_qna_id = df["request_id"].unique().tolist()

    request_id = st.sidebar.select_slider('Request ID', options=unique_qna_id)
    
    # select rows for each qna
    qna = df.loc[df["request_id"] == request_id]



    topic = st.header(qna["question"].iloc[0])



    list_of_questions = qna["question"].unique().tolist()

    question = st.sidebar.radio(label='Request ID', options=list_of_questions)
    row = qna[qna["question"] == question]
    ground_truth = row["ground_truths"].item()
    answer = row["answer"].item()
    # similarity = row["answer_correctness"].item()

    col1, col2 = st.columns(2)
    col1.metric("correctness", row["answer_correctness"].item())
    col2.metric("similarity", row["answer_similarity"].item())
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Ground truth")
        st.text_area(label="ground_truth", value=ground_truth)

    with col2:
        st.header("local_model")
        st.text_area(label="answer", value=answer)
   

    contexts = st.text_area(label="contexts", value=qna["contexts"].iloc[0], height=1000)

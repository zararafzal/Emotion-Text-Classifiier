import streamlit as st
from transformers import pipeline

classifier = pipeline("text-classification", model="michellejieli/emotion_text_classifier")

def classify_text(text):
    result = classifier(text)[0]
    return result["label"]

st.text_input("Enter text here:", key="text")
if st.button("Classify"):
    result = classify_text(st.session_state.text)
    st.write(result)

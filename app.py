import streamlit as st
from transformers import pipeline

classifier = pipeline("text-classification", model="michellejieli/emotion_text_classifier")

def classify_text(text):
    result = classifier(text)[0]
    return result["label"]

text_input = st.text_input("Enter text here:")
if st.button("Classify"):
    result = classify_text(text_input)
    st.write(result)

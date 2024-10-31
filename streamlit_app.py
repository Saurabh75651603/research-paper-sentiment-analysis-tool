import streamlit as st
import fitz  # PyMuPDF for PDF handling
from docx import Document  # For DOCX handling
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Using VADER for sentiment analysis

st.title("Sentiment Analysis Tool")
st.write("Upload a file (text, PDF, or DOCX) for analysis.")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])


# Function to extract text from the uploaded file
def extract_text_from_file(file):
    if file.name.endswith(".txt"):
        # Read text file
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        # Read PDF file
        pdf_text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as pdf:
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                pdf_text += page.get_text()
        return pdf_text
    elif file.name.endswith(".docx"):
        # Read DOCX file
        doc = Document(file)
        doc_text = "\n".join([para.text for para in doc.paragraphs])
        return doc_text
    else:
        return "Unsupported file type."


# Function to perform sentiment analysis and categorize the sentiment
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']

    # Determine sentiment category based on compound score
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, compound_score, scores['pos'], scores['neu'], scores['neg']


# If a file is uploaded, process it
if uploaded_file:
    # Extract the content from the file
    content = extract_text_from_file(uploaded_file)

    # Run sentiment analysis on the extracted content
    sentiment, compound_score, positive_score, neutral_score, negative_score = analyze_sentiment(content)

    # Display the sentiment score only
    st.write("Sentiment Score:", f"{sentiment} (Compound Score: {compound_score:.2f})")

    # Display individual sentiment components
    st.write(f"Positive: {positive_score:.2f}, Neutral: {neutral_score:.2f}, Negative: {negative_score:.2f}")

    # Option to display additional details
    with st.expander("Show Summary and Extracted Content"):
        st.write("Extracted Content:")
        st.write(content)
        st.write("Summary:")
        st.write("This is a summary of the document.")  # Placeholder for summary
else:
    st.write("Please upload a text, PDF, or DOCX file.")

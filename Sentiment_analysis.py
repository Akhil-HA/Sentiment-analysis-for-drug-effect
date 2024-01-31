import PyPDF2
from nltk.sentiment import SentimentIntensityAnalyzer
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def extract_paragraphs_with_keywords(text, keywords):
    paragraphs = re.split(r'\n{2,}', text)  # Split text into paragraphs
    relevant_paragraphs = []

    for paragraph in paragraphs:
        if any(keyword in paragraph.lower() for keyword in keywords):
            relevant_paragraphs.append(paragraph)

    return relevant_paragraphs

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']
    return sentiment_score

def main():
    pdf_file_path = 'your_pdf_file.pdf'  # Replace with the actual path to your PDF file
    keywords = ['efficacy', 'sensitivity', 'resistance']

    try:
        pdf_text = read_pdf(pdf_file_path)
        relevant_paragraphs = extract_paragraphs_with_keywords(pdf_text, keywords)

        if not relevant_paragraphs:
            print("No relevant paragraphs found.")
            return

        overall_sentiment_score = 0
        for paragraph in relevant_paragraphs:
            sentiment_score = perform_sentiment_analysis(paragraph)
            overall_sentiment_score += sentiment_score

        overall_sentiment_score /= len(relevant_paragraphs)

        if overall_sentiment_score >= 0.05:
            print("Positive sentiment regarding drug efficacy.")
        elif overall_sentiment_score <= -0.05:
            print("Negative sentiment regarding drug efficacy.")
        else:
            print("Neutral sentiment regarding drug efficacy.")

    except Exception as e:
        print(f"Error reading or analyzing the PDF: {e}")

if __name__ == "__main__":
    main()

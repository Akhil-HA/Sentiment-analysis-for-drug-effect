# Sentiment-analysis-for-drug-effect

This is a program to parse through drug studies in the form of PDFs and perform sentiment analysis to confirm the efficacy of the drug.
It was developed using the NLTK and its VADER lexicon
Please keep the PDF to parse in the same folder as the script and modify the script to replace your_pdf_file.pdf with the name of the file to be parsed
This script reads the PDF file, extracts text from it, and then performs sentiment analysis using the NLTK Sentiment Intensity Analyzer. The sentiment score is then used to classify the sentiment as positive, negative, or neutral regarding drug efficacy.
This script first extracts paragraphs containing the specified keywords and then performs sentiment analysis on those relevant paragraphs. The sentiment score is averaged over all relevant paragraphs to determine the overall sentiment regarding drug efficacy. Adjust the keywords list to include any additional keywords you want to consider.

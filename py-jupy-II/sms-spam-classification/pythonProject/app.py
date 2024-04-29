import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load the model and vectorizer
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    tfidf = pickle.load(file)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):


    # Preprocess the input text
    transformed_sms = transform_text(input_sms)
    # Vectorize the input text
    vector_input = tfidf.transform([transformed_sms])

    # Fit the model with a dummy input and target
    model.fit(tfidf.transform(['']), [1])  # Dummy fit to avoid NotFittedError

    # Make prediction
    result = model.predict(vector_input)[0]
   # result="I HAVE A DATE ON SUNDAY WITH WILL!!,,,"
    # Display prediction

    if result == 1:
        st.header("Spam Alert 🚫")
    else:
        st.header("Not Spam")



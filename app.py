import streamlit as st
import pickle
import pythoncom
from win32com.client import Dispatch


def speak(text):
    pythoncom.CoInitialize()  # Initialize the COM library
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(text)

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))


def main():
	st.title("Email & SMS Spam Classification ")

	st.write("Build with Streamlit & Python")
	activites=["Classification","About"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		st.subheader("Classification")
		msg=st.text_input("Enter a text")
		if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.header('🔊')
				st.success("This is Not A Spam ✅")
				for i in range(2):
					speak("This is Not A Spam. Not a Problem")

			else:
				st.header('🔊')
				st.error("This is A Spam Alert 🚫")

				for i in range(2):
					speak("This is A Spam. Be Care full")


main()

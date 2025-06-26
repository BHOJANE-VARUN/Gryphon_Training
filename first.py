# def hello(str):
#     print(str)
# hello("hello world")
#
# a = hello
# a("hello from A")
#
# zeroToten = list(i for i in range(10))
# print(sum(i for i in range(10)))
# x = [i for i in range(10)]
# print(type(x))

# print(sum(i*i for i in range(10)))
#
# from functools import reduce
# x = reduce(lambda x, y: x if x > y else y, range(10))
# print(x)
#
# x = "Hello world Hello from computer"



import streamlit as st
import string

st.title("Word Count Dictionary Generator - By MrHafeez (for Demonstartion)")

st.write(
    """
    Paste or type your paragraph below.  
    Click **Get Word Counts** to see how many times each word appears!
    """
)

paragraph = st.text_area("Enter your paragraph here:")

if st.button("Get Word Counts"):
    if paragraph.strip():
        translator = str.maketrans('', '', string.punctuation)
        cleaned = paragraph.translate(translator).lower()
        words = cleaned.split()
        word_counts = {word: words.count(word) for word in set(words)}
        st.write(word_counts)
    else:
        st.warning("Please enter some text.")

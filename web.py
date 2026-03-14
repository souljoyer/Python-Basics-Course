import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my first app")
st.write("This app is is to increase your progress")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")


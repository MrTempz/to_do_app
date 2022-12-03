import streamlit as st
import functions

def web_add():
    todo = st.session_state['new_todo']
    todos = functions.get_todos()
    functions.add(todos, todo)

st.title('My to-do list')
st.subheader('This is my to-do app')
st.write('This app is to increase your productivity')

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter a to-do', on_change=web_add, key='new_todo')
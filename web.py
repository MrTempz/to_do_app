import streamlit as st
import todos

todo_list = todos.Todos()

def web_add():
    todo = st.session_state['new_todo']
    todo_list.add(todo)

st.title('My to-do list')
st.subheader('This is my to-do app')
st.write('This app is to increase your productivity')

for todo in todo_list.todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter a to-do', on_change=web_add, key='new_todo')
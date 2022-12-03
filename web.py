import streamlit as st
import todos

todo_list = todos.Todos()

def web_add():
    todo = st.session_state['new_todo']
    todo_list.add(todo)
    st.session_state['new_todo'] = ''

st.title('My to-do list')
st.subheader('This is my to-do app')
st.write('This app is to increase your productivity')

for todo in todo_list.todos:
    
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.complete_by_element(todo)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a new to-do', 
    placeholder='Enter a to-do', on_change=web_add, key='new_todo')

print(st.session_state)
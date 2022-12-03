import streamlit as st
import todos

todo_list = todos.Todos()

def web_add():
    todo = st.session_state['new_todo']
    todo_list.add(todo)
    st.session_state['new_todo'] = ''

def web_edit():
    new_todo = st.session_state['new_todo']
    for todo in todo_list.todos:
        if st.session_state[todo]:
            old_todo = todo
    todo_list.edit_by_element(old_todo, new_todo)
    st.session_state['new_todo'] = ''

def web_complete():
    todos_to_complete = []
    for todo in todo_list.todos:
        if st.session_state[todo]:
            todos_to_complete.append(todo)
    print(todos_to_complete)
    todo_list.bulk_complete(todos_to_complete)
    #st.session_state['new_todo'] = ''
    

def uncheck_all():
    for todo in todo_list.todos:
        st.session_state[todo] = False

st.title('My to-do list')
st.subheader('This is my to-do app')
st.write('This app is to increase your productivity')

checkbox_sum = 0
for todo in todo_list.todos:
    checkbox = st.checkbox(todo, key=todo)
    checkbox_sum += checkbox


st.text_input(label='Enter a to-do', 
    placeholder='Enter a to-do', key='new_todo')
if checkbox_sum == 0:
    st.button(label='Add', key='add', on_click=web_add)
elif checkbox_sum == 1:
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.button(label='Add', key='add', on_click=web_add)
    with col2:
        st.button(label='Edit', key='edit', on_click=web_edit)
    with col3:
        st.button(label='Complete', key='complete', 
            on_click=web_complete)
    with col4:
        st.button(label='Uncheck', key='uncheck', 
            on_click=uncheck_all)
else:
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.button(label='Add', key='add', on_click=web_add)
    with col2:
        st.button(label='Complete', key='complete', 
            on_click=web_complete)
    with col3:
        st.button(label='Uncheck', key='uncheck', 
            on_click=uncheck_all)

for item in st.session_state.keys():
    if st.session_state[item]:
        print(f'\t{item}:, {st.session_state[item]}')

#print(st.session_state)
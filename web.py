import streamlit
import TDfunctions as Foo
import ConstVariable as CON

todos_list = Foo.get_todos()


def add_todo():
    _ = streamlit.session_state['new_task'] + CON.N_
    todos_list.append(_)
    Foo.set_todos(list=todos_list)

streamlit.set_page_config(layout='wide')

streamlit.title('Todo App')
streamlit.subheader('Simple web app to write down a task list')

streamlit.write(
    'Made to increase <b><strong>productivity</strong></b> '
    'and decrease stress :)',
    unsafe_allow_html=True)

for number, todo in enumerate(todos_list):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(number)
        Foo.set_todos(list=todos_list)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

streamlit.text_input(label='Add task',
                     placeholder='Write here new todo...',
                     on_change=add_todo,
                     key='new_task')

# streamlit.session_state

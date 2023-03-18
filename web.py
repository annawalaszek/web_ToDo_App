import streamlit
import TDfunctions as Foo
import ConstVariable as CON

todos_list = Foo.get_todos()


def add_todo():
    _ = streamlit.session_state['new_task'] + CON.N_
    todos_list.append(_)
    Foo.set_todos(list=todos_list)


streamlit.title('Todo App')
streamlit.subheader('Simple web app to write down a task list')
streamlit.write(
    'Made to increase <b>productivity and decrease</b> stress :)')
streamlit.text_input(label='Add task',
                     placeholder='Write here new todo...',
                     on_change=add_todo,
                     key='new_task')
for number, todo in enumerate(todos_list):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(number)
        Foo.set_todos(list=todos_list)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

# streamlit.session_state

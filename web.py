import streamlit
import TDfunctions as Foo
import ConstVariable as CON

r"""
how to run streamlit
streamlit run D:\programowanie\udemy\The_Python_Mega_Course+Learn_in_50_days\To_Do_App\web.py [ARGUMENTS]
How to do requirements file
pip freeze > requirements.txt
"""

todos_list = Foo.get_todos()


def add_todo():
    _ = streamlit.session_state['new_task'] + CON.N_
    todos_list.append(_)
    Foo.set_todos(list=todos_list)


streamlit.title('Todo App')
streamlit.subheader('Simple web app to write down a task list')
streamlit.write('Made to increase productivity and decrease stress :)')

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

import streamlit as st
from functions import *


def add_todo(todo):
    if todo != "":
        st.session_state["todos"].append(todo)
        write_todos(st.session_state["todos"])
        # Clean new_todo input
        st.session_state.new_todo = ""


def del_todo(num):
    if f"checkbox_todo{num}" in st.session_state.keys():
        if st.session_state[f"checkbox_todo{num}"]:
            st.session_state["todos"].pop(num)
            write_todos(st.session_state["todos"])
            # Clean new_todo input
            st.session_state.new_todo = ""


if "todos" not in st.session_state:
    st.session_state["todos"] = read_todos()

st.header("ToDo App")
st.text("Simple application")

for i, t in enumerate(st.session_state["todos"]):
    # value=False: потому что иногда остается какой-то чекбокс включенным (почему-то)
    st.checkbox(label=t, key=f"checkbox_todo{i}", on_change=del_todo, args=(i, ), value=False)

input_new_todo = st.text_input(label="Enter todo here", value="", key="new_todo")
st.button(label="Add", on_click=add_todo, args=(input_new_todo,))




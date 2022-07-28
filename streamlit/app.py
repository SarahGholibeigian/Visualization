import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

dataframe = pd.DataFrame({"a":[1,2,3,4,5,6,7,8,9,0,2], "b":[12,32,43,54,75,96,27,18,49,20,32]})

# initialize the session_state so that it would not give us an error if we dont go
# to the setting first.
dict_key = {"first row":0, "last row":dataframe.shape[0], "column":"a"}

for i, j in dict_key.items():
    if i+"_" not in st.session_state:
        st.session_state[i+'_'] = j
        st.session_state[i] = j

# a = 2
# b = 7

# col = "a"
# print(dataframe.loc[2:7,[col]]) #print = st.write

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'],
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    # selected

if selected == "Settings":

    a = st.slider('choose the first row?', 0, dataframe.shape[0], st.session_state["first row_"], key="first row")
    b = st.number_input('Choose the last row',min_value=0, max_value=dataframe.shape[0], value=st.session_state["last row_"], step=1, key="last row")
    col = st.selectbox('select a column?', ('a', 'b'), key="column")
    st.session_state["first row_"] = a

if selected == "Home":

    st.expander("DataFrame", expanded=False)

    with st.expander("DataFrame"):
        a = st.session_state["first row_"]
        b = st.session_state["last row"]
        col = st.session_state.column

        # a = st.slider('choose the first row?', 0, dataframe.shape[0], 0)
        # b = st.number_input('Choose the last row',min_value=0, max_value=dataframe.shape[0], value=dataframe.shape[0], step=1,)
        # col = option = st.selectbox('select a column?', ('a', 'b'))

        if a>b:
            st.warning('First row should be smaller than last row!')
        else:
            st.write(dataframe.loc[a:b,[col]])

with st.sidebar:
    st.write(st.session_state) #
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
## in terminal: streamlit run app.py
## for option manu: pip install streamlit-option-menu




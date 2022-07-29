## in terminal: streamlit run app.py
## for option manu: pip install streamlit-option-menu

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

dataframe = pd.DataFrame({"a":[1,2,3,4,5,6,7,8,9,0,2], "b":[12,32,43,54,75,96,27,18,49,20,32]})

# Everytime we move between tabs (going from setting to home and come back) the widgets will run again and state_Session keys within the widget will be deleted and created again 


#1. if we define st.session_state outside of a widget, it works as an global variable, meaning it will not change if we ran the widget.
#2. any key we define in the widget, everytime move to another option in the menu, will run the widget again and create the key again and the value for the key will be default to 0. But for the global session_state, since it is not defined within the widget it will not change
#3. since the global session_state is defined first, when we ran the widget and it is used within the widget, it will give us an error. therefore we have to initialized it first so that it would not give us an error when we run the widget the first time.

# if 'test' not in st.session_state: #no need!! to initialized any key that is defined within a widget,it will be created when we run widget
#     st.session_state['test'] = 0

if 'global' not in st.session_state: #for the first time, since it is not in the widget to be created itself, we have to initialize it.
    st.session_state['global'] = 0
#     st.session_state['test'] = 0

dict_key = {"first row":0, "last row":dataframe.shape[0], "column":"a"}

for i, j in dict_key.items():
    if i+"_" not in st.session_state:
        st.session_state[i+'_'] = j
#         st.session_state[i] = j #no need, everytime we change the tab, will run the widget and will be created the key itself in state_session

# a = 2
# b = 7

# col = "a"
# print(dataframe.loc[2:7,[col]]) #print = st.write

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'],
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

if selected == "Settings":

    a = st.slider('choose the first row?', 0, dataframe.shape[0], st.session_state["first row_"], key="first row") #everytime widget 
    b = st.number_input('Choose the last row',min_value=0, max_value=dataframe.shape[0], value=st.session_state["last row_"], step=1, key="last row")
    col = st.selectbox('select a column?', ('a', 'b'), key="column")
    st.session_state["first row_"] = a

    st.header("My header")
    c = st.slider('why we need session_state?', 0, dataframe.shape[0], st.session_state["global"],  key = "test") #if we change between menu options, will back to default 0 if not use session_state
    st.session_state["global"] = c
    
if selected == "Home":
#     st.header("test_why")

    st.expander("DataFrame", expanded=False)

    with st.expander("DataFrame"):
        a = st.session_state["first row_"] #we have to define it again since it does nor know it. More like defining a and b in a function.
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





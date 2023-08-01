import streamlit as st
import json

st.header("Gherkin Tutorial")
st.write("Hello World")

if 'session_case' not in st.session_state:
    st.session_state["session_case"] = ""

### Sidebar Stuff ###
with st.sidebar:
    st.write("This is the sidebar")

    st.file_uploader(label="Upload AML File", key="AML_Upload_Button")
    st.download_button(label="Validation Report",
                       data=st.session_state["session_case"], file_name="test.json")
####################


case1, case2 = st.tabs(["Click this to see tab 1", "Tab 2"])

with case1:
    ### Column Stuff ###
    column1, column2 = st.columns([9, 3])
    with column1:
        with st.expander("Expand me"):
            button1 = st.button(label="Click me", key="button1",
                                type="primary", use_container_width=True)

    with column2:
        st.button(label="Click me", key="button2", type="secondary")
        st.number_input("Give a number")
        st.selectbox("Select an option", options=["Red", "Blue"])
        st.multiselect("Select an option", options=["Red", "Blue"])
        st.checkbox("Check box")
        ####################

with case2:
    with st.expander("Scenario"):
        scenario_input = st.text_input("Scenario description", key = "scenario_input")
    with st.expander("Given"):
        given_input= st.text_input("Given description", key = "given_input")
    with st.expander("When"):
        when_input = st.text_input("When description", key = "when_input")
    with st.expander("Then"):
        then_input = st.text_input("Then description", key = "then_input")

    case_save_button = st.button("Save Case", key = "case_save_button")

if button1:
    st.info("Successfully clicked on button")

if case_save_button:
    string_output = scenario_input + given_input + when_input + then_input
    list_output = [scenario_input, given_input, when_input, then_input]
    dict_output = {
        "scenario": scenario_input,
        "given": given_input,
        "When": when_input,
        "then": then_input,
    }

    st.session_state["session_case"] = json.dumps(dict_output)

    st.write(string_output)
    st.write(list_output)
    st.write(list_output[0])
    st.write(dict_output)
    st.write(dict_output["then"])
    st.write(st.session_state["session_case"])


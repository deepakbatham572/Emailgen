import streamlit as st
from utils import *


if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''

st.set_page_config("Email Generator" , 
                   page_icon=":e-mail:",
                   layout='centered')
                   

st.sidebar.title('😎🔑')
st.session_state['API_KEY'] =st.sidebar.text_input('Enter your HuggingFace API Key here' , type = 'password')


st.header("Lets Generate Emails 📧")

form_input = st.text_area("Enter your description here :" , height= 275)

col1 , col2 , col3 = st.columns([10, 10 ,5])
with col1:
    email_sender = st.text_input('Sender Name')

with col2:
    email_recipient = st.text_input("Reciever Name")

with col3: 
    email_style  =st.selectbox("Writing Style" ,
                               ('Formal', 'Informal' , 'Appreciating', 'Not Satisfied', 'Neutral' , 'Friendly' , 'Optimistic' , 'Curious' , 'Serious' , 'Other'),
                                index=0 )
    
    if email_style =='Other':
        custom_style  = st.text_input('Please specify your custom style')
    else:
        custom_style = email_style

submit  = st.button("Generate")

if submit:
    response = getLLMResponse(form_input, email_sender, email_recipient, email_style ,st.session_state['API_KEY'])
    formatted_response = response.replace('\n', '  \n')
    st.markdown(f"### Generated Email\n\n{formatted_response}")
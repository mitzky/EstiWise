import streamlit as st
import requests
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image
import base64

def get_img_as_base64(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded

background_image_path = "image/img.png"
image_path = "image/logo.png"
im = Image.open(image_path)
im2 = Image.open("image/logo.png")
background_image = Image.open(background_image_path)

tab1, tab2, tab3, = st.tabs(["About Us", "Contact", "Team Members"])

# Part 2: Tab 2 - About Us
with tab1:
    st.header("𝐀𝐛𝐨𝐮𝐭 𝐔𝐬")
    st.write("   The Main feature of a construction cost prediction system is it can accurately predict project costs based on various input parameters and historical data which are essential for project planning, budgeting, and decision-making in the real estate business. This program makes use of advanced algorithms and models to offer accurate and data-driven cost that it can estimate the cost of materials and land area based on the consumer's budget.  ")

   # Part 2 Tab 2 - Contact
with tab2:
    st.header("Contact") 
    st.write("Facebook: https://www.facebook.com/profile.php?id=61555403674164&mibextid=LQQJ4d\ ")
    st.write("Instagram: https://www.instagram.com/esti_wisee?igsh=MW5nbzNobXcyOW9ycg%3D%3D&utm_source=qr ")
    st.write("Gmail: estiwise@gmail.com")

# Part 2 Tab 2 - Team Members
with tab3:
    st.header("𝐓𝐞𝐚𝐦 𝐌𝐞𝐦𝐛𝐞𝐫𝐬")
    team_members = [

        {"name": "Bayarong, Bien Angelo", "info": "bayarong.348620@balayan.sti.edu.ph"},
        {"name": "Bocala, Kendrick", "info": " bocala.346568@balayan.sti.edu.ph "},
        {"name": "Eugenio, Juilie", "info": " eugenio.264253@balayan.sti.edu.ph "},
        {"name": "De Sagun, JayAnne Althea", "info": "desagun.346945@balayan.sti.edu.ph"},
        {"name": "Asuncion, Johnpaul", "info": " Tuazon.368030@balayan.sti.edu.ph "},
        {"name": "Caag, Ronnel", "info": "caag.373928@balayan.sti.edu.ph"},
        {"name": "Lingon, Yuan Albert", "info": ""},
    ]
    
    for member in team_members:
        expander = st.expander(member["name"])
        expander.write(member["info"])


st.markdown("""<style> .css-1544g2n.e1fqkh3o4 {margin-top: -70px;}</style>""", unsafe_allow_html=True)
st.markdown("""<style> .css-uf99v8.egzxvld5 {margin-top: -50px;}</style>""", unsafe_allow_html=True)

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{get_img_as_base64(background_image_path)}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
    }}
    </style>
    """

st.markdown(page_bg_img, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

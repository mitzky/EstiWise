import streamlit as st
import requests
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image
import base64



def calculate_construction_cost(area, num_floors, num_rooms, num_comfortrooms, ):
    cost_per_sqm = 6000

    total_area = area * num_floors
    total_cost = total_area * cost_per_sqm + num_rooms * 11000 + num_comfortrooms * 6000

    return total_cost
def calculate_total_cost2(permit_cost):
    total_cost2 = permit_cost
    return total_cost2

def total_expenses(total_cost2, total_cost):
    overall=total_cost2 + total_cost
    return overall

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
st.write("------------------------------------------------------------------")
area = st.number_input("Area (in square meters):", min_value=0.0)
num_floors = st.number_input("Number of floors:", min_value=1)
num_rooms = st.number_input("Number of rooms:", min_value=1, format="%d")
num_comfortrooms = st.number_input("Number of comfort rooms:", min_value=0, format="%d")
permit_cost = st.number_input("Building Permit Cost:", value=0.0, step=1000.0)

cement = area * 10 #Kg
steel = area * 4 #Kg
aggregate = area * 0.6 #Tons
paint = area * 0.5 #Liters
flooring = area * num_floors #Sq. Meters

summary = {"Cement (kg)": cement,
               "Steel (kg)": steel,
               "Aggregate (tons)": aggregate,
               "Paint (Liters)": paint,
               "Flooring (Square meters)": flooring
               }


    #Calculate construction cost based on inputs
total_cost = calculate_construction_cost(area, num_floors, num_rooms, num_comfortrooms)
total_cost2 = calculate_total_cost2(permit_cost)
overall = total_expenses(total_cost2, total_cost)
    #Display construction cost
st.header("Results:")
if st.button("Calculate"):
        st.write("Based on the inputs you provided, the estimated construction cost is:")
        st.title(f"PHP {overall:,.2f}")
        st.write("Hypothetically, you will be needing:")
        for key, value in summary.items():
            st.write(f"- {key}: {value}")
        st.write("Which costs:")
        st.title(f"PHP {total_cost:,.2f}")
        #Total
        if total_cost == 0:
            st.write("Hmm, it looks like you haven't entered any parameters yet.")
        elif total_cost < 100000:
            st.write("Wow, that's a great deal! Your construction cost estimate is very affordable.")
        elif total_cost < 200000:
            st.write("Your construction cost estimate is reasonable and fits within the average budget for most people.")
        elif total_cost < 500000:
            st.write("Your construction cost estimate is a bit high, but still within the range of what many people spend.")
        else:
            st.write(
                "Your construction cost estimate is very high. You must be rich!")
if st.button("Save"):
        content = f"Construction Cost Estimate:\nEstimated Cost: PHP {overall:,.2f}\n\nHypothetically, you will be needing:\n"
        for key, value in summary.items():
            content += f"- {key}: {value}\n"
        content += f"\nWhich costs: PHP {total_cost:,.2f}"
        #file download link
        st.download_button(label="Download Estimate", data=content, file_name="construction_estimate.txt", mime="text/plain")
 

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

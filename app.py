import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#to get url:  streamlit run app.py



# # the emojis page https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="tada", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# #---- ASSET LINK---
# # https://lottiefiles.com/search?q=coding&category=animations
lottie_coding = load_lottieurl("https://lottie.host/47b921eb-9aa7-4868-a2b6-c3a8db0d43cb/rUf0Yxu591.json")

# # ----- HEADER SECTION ---------
with st.container():
    st.subheader("Hi, it's Synaptic Sisters :wave:")
    st.title("EpiGenius: Detecting Skin Conditions with Machine Learning ")
    st.write("Framework: TensorFlow, Jupyter, Python ")  #make sure to edit this 

# # ---- WHAT I DOOO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is our mission?")
        st.write("##") 
        st.write(
            """ 
            DEEP DIVE INTO HEALTHCARE:


            The American Health Care System really thinks students are rich when we're broke college
            students. Healthcare costs are spiralling north and hopefully one day we can help 
            humans solve real medical problems. But our model cannot do this alone. Each time 
            you use SkinWise, I learn deeply (no pun intended) from it. 
            
            

            Check your skin health with our machine learning model below! 
            """
        )
        st.write("[Are Medical Advancements Only for the Rich?](https://opmed.doximity.com/articles/are-medical-advancements-only-for-the-rich)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

 #File Upload Section
st.write("---")
st.write("## 1. Camera, Action!")

# Add a file uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Save the uploaded image to a temporary location (e.g., 'temp_image.jpg')
    with open('temp_image.jpg', 'wb') as f:
        f.write(uploaded_image.read())

# Section 2: Reading your Image
st.write("## 2. Reading your Image")
st.markdown(
    """
    Using TensorFlow for Image Analysis

    We utilize TensorFlow as our machine learning model to analyze the uploaded image. TensorFlow is a powerful library for various machine learning tasks, including image analysis.
    """
    )



# Section 4: Results (Placeholder)
st.write("## 3. Results (Placeholder)")
result_placeholder = st.empty()  # Create an empty placeholder for the results

# Check if an image is uploaded
if uploaded_image is not None:
    # Display a loading spinner while processing the image
    with st.spinner("Analyzing the image..."):
        # Place your machine learning code here to analyze the uploaded image
        # Replace the following line with your actual analysis code
        import time
        time.sleep(5)  # Simulate processing for 5 seconds (Replace this with your analysis code)

        # Once the analysis is complete, update the results section
        result_placeholder.write("Results will be displayed here after image analysis.")
        result_placeholder.success("Analysis completed!")
        result_placeholder.write("Skin condition detected: Acne")
        result_placeholder.image("path_to_result_image.jpg", caption="Analysis Result")


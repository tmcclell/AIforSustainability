import streamlit as st
import requests
from PIL import Image

# Set the title and logo
st.set_page_config(page_title="AI for Sustainability", page_icon="assets/Planet Rainbows.png")
st.title("AI for Sustainability")

# Display the logo
logo = Image.open("assets/Planet Rainbows.png")
st.image(logo, width=100)

# File upload component
uploaded_file = st.file_uploader("Upload a PDF or Image file", type=["pdf", "png", "jpg", "jpeg"])

# Input box for user interaction
user_input = st.text_input("Enter additional input for the model")

# Button to trigger the backend request
if st.button("Analyze"):
    if uploaded_file is not None:
        with st.spinner("Processing..."):
            # Prepare the payload
            files = {"file": uploaded_file.getvalue()}
            data = {"user_input": user_input}

            # Send the request to the backend
            try:
                response = requests.post("http://127.0.0.1:8005/analyze", files=files, data=data)
                if response.status_code == 200:
                    st.success("Analysis complete!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please upload a file before analyzing.")
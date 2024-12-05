import streamlit as st
from PIL import Image
import io

# Set the page configuration
st.set_page_config(page_title="Image Prediction App", layout="wide")

st.markdown(
    """
    <style>
        /* Change the sidebar background to orange */
        [data-testid="stSidebar"] {
            background-color: #FFFFF;
        }

        /* Style sidebar text */
        [data-testid="stSidebar"] .css-1v3fvcr {
            color: #000000;
        }

        /* Style for headers */
        h1, h2 {
            color: #000000;
        }

        /* General body font style */
        .css-1v3fvcr, .css-qrbaxs, .css-16huue1 {
            font-family: Arial, sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background-image: url("https://th.bing.com/th?id=OIP.biGocqwyB42JnfNPbWN9xAHaD7&w=343&h=182&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Upload Image", "Use Camera","Results"])

# Home Section
if menu == "Home":
    st.title("Welcome to the SAR Image Colourization Web App")
    st.markdown(
        """
        <h3 style='color:blue;'>Your one-stop solution for image predictions!</h3>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    ### Features:
    <ul>
        <li style='color:blue;'>Upload an image or capture one using your camera.</li>
        <li style='color:blue;'>Get predictions using Deep Learning models.</li>
    </ul>
    """,
    unsafe_allow_html=True
)
    st.image("https://www.gim-international.com/cache/d/e/1/3/d/de13d4d43e847aab7eec6e159b3a676447335ac5.png", use_column_width=True)
    st.markdown("---")

# Upload Image Section
elif menu == "Upload Image":
    st.title("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image to upload", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Predict button
        if st.button("Predict"):
            # Placeholder for prediction logic
            st.success("Prediction: [Model's output goes here]")

# Camera Section
elif menu == "Use Camera":
    st.title("Capture Image Using Camera")
    
    # Camera input
    captured_image = st.camera_input("Take a picture")
    
    if captured_image is not None:
        # Display the captured image
        image = Image.open(captured_image)
        st.image(image, caption="Captured Image", use_column_width=True)
        
        # Predict button
        if st.button("Predict"):
            # Placeholder for prediction logic
            st.success("Prediction: [Model's output goes here]")

elif menu == "Results":
    st.success("Prediction: [Model's output goes here]")

# Footer
st.sidebar.markdown("---")
#st.sidebar.caption("Built by Amit Mane")

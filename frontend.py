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
            background-color: #FFA500;
        }

        /* Style sidebar text */
        [data-testid="stSidebar"] .css-1v3fvcr {
            color: white;
        }

        /* Style for headers */
        h1, h2 {
            color: #000080;
        }

        /* General body font style */
        .css-1v3fvcr, .css-qrbaxs, .css-16huue1 {
            font-family: Arial, sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background-image: url("https://th.bing.com/th/id/OIP.-8fTYvOql4-2HRbA2s291wHaEo?w=276&h=180&c=7&r=0&o=5&pid=1.7");
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
menu = st.sidebar.radio("Go to", ["Home", "Upload Image", "Use Camera"])

# Home Section
if menu == "Home":
    st.title("Welcome to the SAR Image Colourization Web App")
    st.subheader("Your one-stop solution for image predictions!")
    st.markdown("""
        ### Features:
        - Upload an image or capture one using your camera.
        - Get predictions using Deep Learning models.
    """)
    st.image("https://via.placeholder.com/800x400.png?text=Image+Prediction+App", use_column_width=True)
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

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built by Amit Mane")

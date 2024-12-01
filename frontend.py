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
            background-image: url("data:image/jpeg;base64,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");
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

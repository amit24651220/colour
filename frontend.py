import streamlit as st
from PIL import Image
import io

# Set the page configuration
st.set_page_config(page_title="Image Prediction App", layout="wide")

# Sidebar menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Upload Image", "Use Camera"])

# Home Section
if menu == "Home":
    st.title("Welcome to the Image Prediction Web App")
    st.subheader("Your one-stop solution for image predictions!")
    st.markdown("""
        ### Features:
        - Upload an image or capture one using your camera.
        - Get predictions using state-of-the-art AI models.
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

import streamlit as st
from PIL import Image
import io

# Set the page configuration
st.set_page_config(page_title="Image Prediction App", layout="wide")

st.markdown(
    """
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #f4f4f4, #e0e0e0);
            padding: 20px;
            border-right: 2px solid #d1d1d1;
        }

        /* Sidebar Text Styling */
        [data-testid="stSidebar"] * {
            color: #333333;
            font-family: 'Arial', sans-serif;
            font-size: 16px;
        }

        /* Header Styling */
        h1, h2, h3 {
            color: #222222;
            font-family: 'Poppins', sans-serif;
        }

        /* Body Font Styling */
        body, [data-testid="stAppViewContainer"] * {
            font-family: 'Roboto', sans-serif;
        }

        /* Background Image */
        [data-testid="stAppViewContainer"] {
            background: url("https://th.bing.com/th?id=OIP.biGocqwyB42JnfNPbWN9xAHaD7&w=343&h=182&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2") no-repeat center center fixed;
            background-size: cover;
        }

        /* Container Styling */
        .stApp {
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
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

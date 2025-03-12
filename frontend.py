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
            background: linear-gradient(135deg, #1e1e1e, #292929);
            padding: 20px;
            border-right: 3px solid #ff6600;
            box-shadow: 2px 0px 10px rgba(0, 0, 0, 0.2);
        }

        /* Sidebar Text Styling */
        [data-testid="stSidebar"] * {
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
        }

        /* Header Styling */
        h1, h2, h3 {
            color: #ff6600;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Body Font Styling */
        body, [data-testid="stAppViewContainer"] * {
            font-family: 'Roboto', sans-serif;
            color: #ffffff;
        }

        /* Background Image */
        [data-testid="stAppViewContainer"] {
            background: url("https://source.unsplash.com/1600x900/?technology,abstract") no-repeat center center fixed;
            background-size: cover;
        }

        /* Main App Container */
        .stApp {
            padding: 30px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }

        /* Custom Button */
        .stButton > button {
            background-color: #ff6600;
            color: #ffffff;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #ff4500;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)# Sidebar menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Upload Image", "Use Camera","Results"])

# Home Section
if menu == "Home":
    st.title("Welcome to the SAR Image Colourization Web App")
    st.markdown(
        """
        <h3 style='color:black;'>Your one-stop solution for image predictions!</h3>
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

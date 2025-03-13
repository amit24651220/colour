import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="SAR Image Colourization", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        /* General App Background */
        [data-testid="stAppViewContainer"] {
            background-color: #121212;
            color: #E0E0E0;
            font-family: 'Arial', sans-serif;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #1E1E1E;
            padding: 20px;
            border-right: 2px solid #FF6600;
        }
        
        /* Sidebar Titles and Text */
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
            font-size: 16px;
        }

        /* Header Styling */
        h1, h2, h3 {
            color: #FF6600 !important;
            text-align: center;
            font-weight: bold;
        }

        /* Custom Button */
        .stButton > button {
            background-color: #FF6600;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
        }

        .stButton > button:hover {
            background-color: #E65100;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Upload Image", "Use Camera", "Results"])

# Home Section
if menu == "Home":
    st.title("🚀 SAR Image Colourization App")
    st.write("### Transform grayscale SAR images into colorful, insightful visuals using AI.")
    
    st.markdown(
        """
        ### 🌟 Features:
        - 📂 Upload an image or capture one using your camera.
        - 🤖 AI-powered colorization for SAR images.
        - 📊 High-quality predictions with minimal effort.
        """
    )
    
    st.image("https://www.gim-international.com/cache/d/e/1/3/d/de13d4d43e847aab7eec6e159b3a676447335ac5.png", use_column_width=True)
    st.markdown("---")

# Upload Image Section
elif menu == "Upload Image":
    st.title("📤 Upload an Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="📷 Uploaded Image", use_column_width=True)
        if st.button("🔍 Predict"):
            st.success("✅ Prediction: [Model's output goes here]")

# Camera Section
elif menu == "Use Camera":
    st.title("📸 Capture an Image")
    captured_image = st.camera_input("Take a picture")

    if captured_image is not None:
        image = Image.open(captured_image)
        st.image(image, caption="📷 Captured Image", use_column_width=True)
        if st.button("🔍 Predict"):
            st.success("✅ Prediction: [Model's output goes here]")

# Results Section
elif menu == "Results":
    st.success("✅ Prediction: [Model's output goes here]")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("🚀 Built by Amit Mane")


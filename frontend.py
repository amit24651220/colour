import streamlit as st

# Set the page configuration
st.set_page_config(page_title="SAR Image Colourization", layout="centered")

# Frontend: Title and Subheading
st.title("Image Prediction Web App")
st.subheader("Upload an image to get predictions")

# File upload functionality
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Placeholder for prediction button and output
if uploaded_file is not None:
    # Display the uploaded image
   st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        # Backend placeholder (replace with your model's prediction code)
        st.write("Prediction: [Model's output goes here]")

# Footer or additional info
st.markdown("---")
st.caption("Build by Amit")

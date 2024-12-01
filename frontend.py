import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ['SAR Image Colourization'], 
                           icons=['house', 'book', 'clipboard-data', 'search'], 
                           menu_icon="cast", default_index=0)
    selected

# Main page
if selected == "SAR Image Colourization":
    st.header("SAR Image Colourization")
    #st.subheader("Test")
    test_images = []

    option = st.selectbox('Choose an input Image option:',
                          ('--select option--', 'Upload', 'Camera'))

    if option == "Upload":
        test_images = st.file_uploader("Choose Image(s):", accept_multiple_files=True)
        if st.button("Show Images"):
            st.image(test_images, width=4, use_column_width=True)

    elif option == "Camera":
        test_images = [st.camera_input("Capture an Image:")]
        if st.button("Show Images"):
            st.image(test_images, width=4, use_column_width=True)
# Set the page configuration
#st.set_page_config(page_title="SAR Image Colourization", layout="centered")

# Frontend: Title and Subheading
#st.title("Image Prediction Web App")
#st.subheader("Upload an image to get predictions")

# File upload functionality
#uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Placeholder for prediction button and output
#if uploaded_file is not None:
    # Display the uploaded image
   # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        # Backend placeholder (replace with your model's prediction code)
        st.write("Prediction: [Model's output goes here]")

# Footer or additional info
st.markdown("---")
st.caption("Built with Streamlit")

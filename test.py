import streamlit as st
import ollama

# Streamlit app setup
st.title("Image Description with Ollama")
st.write("Upload an image, and the model will describe it.")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Button to describe the image
    if st.button("Describe Image"):
        # Save the uploaded file to a temporary location
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.read())

        # Interact with Ollama model
        try:
            res = ollama.chat(
                model='llava',
                messages=[
                    {
                        'role': 'user',
                        'content': 'Describe this image',
                        'images': ['./temp_image.jpg']
                    }
                ]
            )

            # Display the model's response
            st.subheader("Model's Description:")
            st.write(res['message']['content'])

        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.write("Please upload an image to continue.")

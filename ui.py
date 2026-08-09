import streamlit as st
from ai import client
import base64

st.set_page_config(page_title="AI Assistant", layout="wide")
st.title("AI Assistant")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    file_uploader = st.file_uploader("Upload image", type=["jpg", "png"], key="file_uploader")

with col2:
    prompt = st.text_area("Enter your prompt", key="prompt")
    button = st.button("Submit", key="submit_button")
    if button and file_uploader is not None:
        st.image(file_uploader, caption="Uploaded Image", use_container_width=True)
    else:
        st.info("Upload an image to preview it here")

with col3:
    if button and file_uploader is not None:
        with st.spinner("Analyzing image..."):
            image_bytes = file_uploader.read()
            b64_image = base64.b64encode(image_bytes).decode("utf-8")
            image_data_url = f"data:image/png;base64,{b64_image}"
            response_text = client.generate_response_from_image(image_data_url, prompt)

        st.subheader("AI Response")
        st.markdown(response_text)
    else:
        st.info("AI response will be displayed here after you submit the prompt")
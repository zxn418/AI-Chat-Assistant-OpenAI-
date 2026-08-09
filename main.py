import streamlit as st
from ai import client
import base64

st.set_page_config(page_title="BFIM Care Developer Assitant AI", page_icon=":robot_face:", layout="wide")
st.title("BFIM Care Developer Assitant AI")



# #1. Initialize the Chat History
# if "messages" not in st.session_state:
#     st.session_state.messages = []
    
# #2. Display the session history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
# #3. Chat Input
# prompt = st.chat_input("Ask me anything about the code or how to fix the code.")
# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
        
#     #4. Call OpenAi
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = client.query(st.session_state.messages)
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             st.markdown(response)
#             st.rerun()

# image_prompt = st.text_input("Describe an image to generate:")
# if st.button("Generate Image") and image_prompt:
#     with st.spinner("Generating..."):
#         b64_data = client.generate_image(image_prompt)
#         image_bytes = base64.b64decode(b64_data)
#         st.image(image_bytes, caption=image_prompt)
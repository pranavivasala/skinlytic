import streamlit as st
import openai

# Load the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Function to call OpenAI API
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        api_key=openai_api_key,  # Use the secret key here
    )
    return response["choices"][0]["message"]["content"]

st.title("Let's get to know about your skin")

st.header("What's your skin type?")
skin_type = []
if st.checkbox("Dry"):
    skin_type.append("Dry")
if st.checkbox("Oily"):
    skin_type.append("Oily")
if st.checkbox("Normal"):
    skin_type.append("Normal")
if st.checkbox("Combination"):
    skin_type.append("Combination")

st.header("If Acne")
acne_type = []
if st.checkbox("Breakouts"):
    acne_type.append("Breakouts")
if st.checkbox("Pimples"):
    acne_type.append("Pimples")
if st.checkbox("Blemishes"):
    acne_type.append("Blemishes")
if st.checkbox("Non-acne"):
    acne_type.append("Non-acne")

if st.button("Submit"):
    user_input = f"Skin Type: {', '.join(skin_type)} | Acne: {', '.join(acne_type)}"
    st.write("Analyzing your skin condition...")
    
    # Call OpenAI API
    response = get_openai_response(f"Provide skincare advice for: {user_input}")
    
    st.subheader("AI Skin Analysis Result:")
    st.write(response)

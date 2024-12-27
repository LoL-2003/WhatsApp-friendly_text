import streamlit as st

def format_to_whatsapp(text):
    """
    Function to format text for WhatsApp-compatible formatting.
    """
    formatted_text = text
    
    # Replace bold (**text**) with WhatsApp-compatible bold (*text*)
    formatted_text = formatted_text.replace("**", "*")
    
    return formatted_text

# Streamlit app
st.title("WhatsApp Text Formatter")

# Input text from the user
input_text = st.text_area(
    "Enter the text to be formatted for WhatsApp:"
)

# Format the text
if st.button("Format Text"):
    if input_text.strip():
        formatted_output = format_to_whatsapp(input_text)
        st.text_area("Formatted Text for WhatsApp:", formatted_output, height=300)
    else:
        st.warning("Please enter some text to format!")

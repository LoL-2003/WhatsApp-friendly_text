import streamlit as st

def format_to_whatsapp(text):
    """
    Function to format text into WhatsApp-compatible formatting.
    """
    formatted_text = text
    
    # Replace bold (**text**) with WhatsApp-compatible bold (*text*)
    formatted_text = formatted_text.replace("**", "*")
    
    # Replace ### headers with bold and underline for emphasis
    formatted_text = formatted_text.replace("### ", "*_")
    formatted_text = formatted_text.replace("#### ", "*")

    return formatted_text

# Streamlit app
st.title("WhatsApp Text Formatter")

# Input text from the user
input_text = st.text_area(
    "Enter the text to be formatted for WhatsApp:",
    placeholder="Paste your formatted text here..."
)

# Format the text
if st.button("Format Text"):
    if input_text.strip():
        formatted_output = format_to_whatsapp(input_text)
        
        # Display the formatted output
        st.text_area("Formatted Text for WhatsApp:", formatted_output, height=300)
        
        # Escape backticks for safe embedding in JavaScript
        escaped_output = formatted_output.replace("`", "\\`").replace("\n", "\\n")
        
        # Add a copy-to-clipboard button
        st.markdown(
            f"""
            <button onclick="navigator.clipboard.writeText(`{escaped_output}`)" 
            style="padding:10px 15px; background-color:#4CAF50; color:white; border:none; cursor:pointer; border-radius:5px;">
            Copy to Clipboard
            </button>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter some text to format!")

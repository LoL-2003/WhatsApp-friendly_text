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
            <div style="position:relative;">
                <button onclick="navigator.clipboard.writeText(`{escaped_output}`); 
                alert('Text copied to clipboard!');" 
                style="padding:10px 20px; font-size:16px; 
                background-color:#4CAF50; color:white; border:none; cursor:pointer; 
                border-radius:5px; transition: background-color 0.3s;">
                Copy to Clipboard
                </button>
                <span id="copyMessage" style="display:none; font-size:12px; color:#4CAF50; margin-top:5px;">Copied!</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter some text to format!")

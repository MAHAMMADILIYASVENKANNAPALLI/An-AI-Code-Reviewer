import streamlit as st
import google.generativeai as genai

# Load API key from file
try:
    with open(r"C:\Users\Mahammad Iliyas\Downloads\key\AI Code Reviewer.txt", "r") as file:
        api_key = file.read().strip()
except Exception as e:
    st.error(f"Error loading API key: {e}")
    api_key = None

# Check if API key is loaded successfully
if api_key:
    # Configure the API key
    genai.configure(api_key=api_key)

    # Configure the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="""Analyze the submitted code and identify potential bugs, 
        errors, or areas of improvement. Generate a Bug Report and provide Fixed Code only."""
    )

    # Streamlit UI with a full-page sky-blue background
    st.markdown(
        """
        <style>
            /* Apply background color to the entire page */
            body {
                background-color: #87CEEB; /* Sky blue color */
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            .main {
                background-color: #87CEEB; /* Sky blue for main container */
                padding: 20px;
                border-radius: 10px;
            }
            .stTextInput, .stTextArea, .stButton > button {
                background-color: #ffffff; /* White input boxes */
                color: #333;
                border-radius: 10px;
                padding: 10px;
            }
            .stButton > button:hover {
                background-color: #1E90FF; /* Dodger Blue hover effect */
                color: white;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Title for the app
    st.title("🌟 An AI Code Reviewer 🚀")

    # Input area for user to submit code
    user_prompt = st.text_area("Enter Your Python Code here...")

    # Button to process the input code
    if st.button("Generate Review"):
        if user_prompt.strip():  # Ensure user entered code
            st.subheader("Code Review and Feedback")
            try:
                # Send user code to the model for analysis
                response = model.generate_content(user_prompt)
                # Display the generated response from the model
                st.write(response.text)
            except Exception as e:
                st.error(f"Error generating code review: {e}")
        else:
            st.warning("Please enter some Python code to review.")
else:
    st.error("API key not loaded. Please check the file path and contents.")

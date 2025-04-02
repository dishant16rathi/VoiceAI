import re
import streamlit as st
import requests

# Constants
API_BASE_URL = "https://fastapi-twilio.purplemushroom-d9ddba87.uksouth.azurecontainerapps.io"

# Page Configuration
st.set_page_config(
    page_title="QX AI Voice Assistant",
    page_icon="📞",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS: Override Streamlit's main container (.block-container) to mimic a card
st.markdown(
    """
    <style>
        /* Overall container styling with flex */
        .block-container {
            display: flex;
            flex-direction: column;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
            padding: 15px;
        }
        
        /* Reduced font sizes */
        .block-container h1 {
            font-size: 21px;
            padding: 0 0 20px 0; border-bottom: 1px solid #000; margin-bottom: 20px;
        }
        .block-container h2 {
            font-size: 15px;
            margin-bottom: 8px;
            padding:0;
        }
        .block-container h3 {
            font-size: 12px;
            margin-bottom: 6px;
        }
        .block-container p, .block-container li, .stTextInput > label, .stButton > button {
            font-size: 10px;
            margin-bottom: 6px;
        }
        
        /* Make buttons smaller */
        .stButton > button {
            padding: 2px 30px;
            display: inline-flex;
            align-items: center; height: 24px;
        }
        .stButton > button p{
            margin: 0; padding: 0; font-size: 12px; font-weight: 600;
        }
        /* Adjust input fields */
        .stTextInput > div > div > input {
            font-size: 0.9rem;
            padding: 0.25rem 0.5rem;
        }
        
        /* Adjust message boxes (success, error, warning) */
        .stAlert > div {
            padding: 0.5rem;
            font-size: 0.85rem;
        }
        
        /* Section containers with flex */
        .section-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 15px;
        }
        hr{
            margin: 10px 0;
        }
        .st-emotion-cache-16tyu1 hr{
            margin: 10px 0px 30px 0px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with Icon
st.title("📞 AI Voice Assistant - QX")

# Section: Server Status
st.header("🖥️ Server Status")
st.markdown("Check if the server is running and available.")

if st.button("🔍 Check Server Status", key="server-check", type="secondary", use_container_width=True):
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            st.success("✅ Server is up and running.")
        else:
            st.error("❌ Server is not reachable.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")


st.markdown("---")

# Section: Outgoing Calls
st.header("📞 Make an Outgoing Call")
st.markdown("Enter a phone number in **E.164 format** (e.g., `911234567890`) to initiate a call.")

# Input for phone number
phone_number = st.text_input("📱 Enter Phone Number", placeholder="911234567890")

# Phone number validation function
def is_valid_phone(number):
    """Validate phone number format: must start with 91 and have 10 digits after it."""
    return bool(re.fullmatch(r"91\d{10}", number))

# Call Now Button
if st.button("📤 Call Now", key="call-now", type="secondary", use_container_width=True):
    if phone_number:
        if is_valid_phone(phone_number):
            try:
                response = requests.post(f"{API_BASE_URL}/outgoing-call/?to_phone={phone_number}")
                if response.status_code == 200:
                    st.success("✅ Call initiated successfully!")
                else:
                    st.error(f"❌ Error: {response.json()}")
            except Exception as e:
                st.error(f"⚠️ Failed to initiate call: {e}")
        else:
            st.warning("⚠️ Invalid phone number! It must start with 91 and be followed by exactly 10 digits.")
    else:
        st.warning("⚠️ Please enter a valid phone number.")

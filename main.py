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
        .block-container {
            background-color: #ffffff;
            border-top: 2px solid #ddd;
            border-bottom: 2px solid #ddd;
            border-left: 1px solid #ddd;
            border-right: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            margin: auto;
            padding: 20px 20px 40px 20px;
        }
        .block-container h1, .block-container h2, .block-container h3, .block-container p {
            margin-bottom: 15px;
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

if st.button("🔍 Check Server Status", key="server-check"):
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
if st.button("📤 Call Now", key="call-now", type="secondary"):
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

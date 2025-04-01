import re
import streamlit as st
import requests

API_BASE_URL = "https://fastapi-twilio.purplemushroom-d9ddba87.uksouth.azurecontainerapps.io"  # noqa

st.title("AI Voice Assistant - QX")

# Section to check if the server is running
st.header("Server Status")
if st.button("Check Server Status"):
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            st.success("Server is up and running.")
        else:
            st.error("Server is not reachable.")
    except Exception as e:
        st.error(f"Error: {e}")

# Section to handle incoming calls
st.header("Incoming Calls")
st.write("Twilio will automatically hit the /incoming-call endpoint when a call comes at the Twilio number - +447883302421")    # noqa

# Section for outgoing calls
st.header("Make an Outgoing Call")
phone_number = st.text_input("Enter Phone Number (E.164 format, e.g., 911234567980)")   # noqa


def is_valid_phone(number):
    """Validate phone number format: must start with 91 and have 10 digits after it.""" # noqa
    return bool(re.fullmatch(r"91\d{10}", number))


if st.button("Call Now"):
    if phone_number:
        if is_valid_phone(phone_number):
            try:
                response = requests.post(f"{API_BASE_URL}/outgoing-call/?to_phone={phone_number}")  # noqa
                if response.status_code == 200:
                    st.success("Call initiated successfully!")
                else:
                    st.error(f"Error: {response.json()}")
            except Exception as e:
                st.error(f"Failed to initiate call: {e}")
        else:
            st.warning("Invalid phone number! It must start with 91 and be followed by exactly 10 digits.")     # noqa
    else:
        st.warning("Please enter a valid phone number.")

import streamlit as st
import requests
import base64

def extract_equation_from_image_google_api(image_file):
    api_key = st.secrets["GOOGLE_API_KEY"]
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"

    image_data = base64.b64encode(image_file.read()).decode()
    payload = {
        "requests": [
            {
                "image": {"content": image_data},
                "features": [{"type": "TEXT_DETECTION"}]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    try:
        text = result['responses'][0]['textAnnotations'][0]['description']
        return text.strip()
    except:
        return "No equation detected."

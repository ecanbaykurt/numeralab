import pytesseract
from PIL import Image

def extract_equation_from_image(uploaded_file):
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image, config='--psm 6')
    # Simple cleanup
    cleaned_eq = text.replace("\n", "").strip()
    # You can improve with Mathpix or LaTeX parser here
    return cleaned_eq or "Could not extract equation."

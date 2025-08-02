import os
from PIL import Image
import pytesseract

# Optional: Print working directory to debug paths
print("Current Working Directory:", os.getcwd())

# Set up Tesseract path if needed (only on Windows)
# If you've installed Tesseract manually, update this line
# For example: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Build the path to the image dynamically
image_path = os.path.join(os.path.dirname(__file__), "images", "prescription_image.jpeg")

# Optional: Check if the file exists before proceeding
if not os.path.exists(image_path):
    print(f"❌ Image file not found at: {image_path}")
    exit()

# Open the image
try:
    image = Image.open(image_path)
    print("✅ Image loaded successfully.")
except Exception as e:
    print(f"❌ Error opening image: {e}")
    exit()

# Perform OCR using pytesseract
try:
    extracted_text = pytesseract.image_to_string(image)
    print("📝 Extracted Text from Image:\n")
    print(extracted_text)
except Exception as e:
    print(f"❌ OCR processing failed: {e}")

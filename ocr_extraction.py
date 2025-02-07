




import cv2
import pytesseract
import easyocr
import json
import re
import numpy as np

# Set Tesseract Path (Only needed for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the uploaded image
image_path = r'C:\Users\Ramya\Downloads\intern\internnewassignmentproxy.png'

# Function: Preprocess Image for Better OCR Accuracy
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding for better clarity
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Denoise image to remove small artifacts
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    return denoised

# Function: Extract Text Using Tesseract OCR
def extract_text_tesseract(image_path):
    processed_img = preprocess_image(image_path)
    config = "--psm 6 --oem 3"  # Optimize OCR for structured text
    text = pytesseract.image_to_string(processed_img, config=config)
    return text

# Function: Extract Text Using EasyOCR (For Handwritten Text)
def extract_text_easyocr(image_path):
    reader = easyocr.Reader(['en'], gpu=False)  # Force CPU mode
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

# Function: Extract Key Data Using Regex
def extract_key_data(text):
    data = {}

    # # Extract Patient Name & DOB
    # name_match = re.search(r'Patient Name\s*[:\-]\s*([A-Za-z\s]+)', text)
    # dob_match = re.search(r'DOB\s*[:\-]\s*([\d/]+)', text)
    # Extract Patient Name & DOB
    name_match = re.search(r'Patient Name\s*[:\-]\s*([A-Za-z]+)', text)  # Ensures only the name is captured
    dob_match = re.search(r'DOB\s*[:\-]\s*([\d/]+)', text)  # Extracts DOB separately

    
    data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
    data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

    # Extract Injection & Exercise Therapy Status
    data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
    data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"

    # Extract Difficulty Ratings (Scale 0-5)
    ratings = {}
    rating_labels = [
        "Bending", "Putting on shoes", "Sleeping", "Standing", "Walking through a store",
        "Driving", "Preparing a meal", "Yard work", "Picking up items off the floor"
    ]
    for label in rating_labels:
        match = re.search(rf"{label}.*?(\d+)", text)
        ratings[label.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

    data["difficulty_ratings"] = ratings

    # Extract Patient Changes
    
    changes = {}
    changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+?)(?:\n|$)", text)
    changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+?)(?:\n|$)", text)
    changes["last_3_days"] = re.search(r"Describe any functional changes.*?:\s*([\w\s]+?)(?:\n|$)", text)

# Clean up extracted text
    for key in changes:
        changes[key] = changes[key].group(1).strip() if changes[key] else "Unknown"
    data["patient_changes"] = changes

    # Extract Pain Symptoms (Scale 0-10)
    symptoms = {}
    symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
    for label in symptom_labels:
        match = re.search(rf"{label}:\s*([\d]+)", text)
        symptoms[label.lower()] = int(match.group(1)) if match else 0

    data["pain_symptoms"] = symptoms

    # Extract Medical Assistant Data
    medical_data = {}
    medical_data["blood_pressure"] = re.search(r"Blood Pressure:\s*([\d/]+)", text)
    medical_data["hr"] = re.search(r"HR:\s*([\d]+)", text)
    medical_data["weight"] = re.search(r"Weight:\s*([\d]+)", text)
    medical_data["height"] = re.search(r"Height:\s*([\d'\" ]+)", text)
    medical_data["spo2"] = re.search(r"SpO2:\s*([\d]+)", text)
    medical_data["temperature"] = re.search(r"Temperature:\s*([\d.]+)", text)
    medical_data["blood_glucose"] = re.search(r"Blood Glucose:\s*([\d]+)", text)
    medical_data["respirations"] = re.search(r"Respirations:\s*([\d]+)", text)

    for key in medical_data:
        medical_data[key] = medical_data[key].group(1) if medical_data[key] else "Unknown"

    data["medical_assistant_data"] = medical_data

    return json.dumps(data, indent=4)

# Run OCR on Image
text_tesseract = extract_text_tesseract(image_path)  # Use Tesseract OCR
text_easyocr = extract_text_easyocr(image_path)  # Use EasyOCR for handwritten text

# Combine both extracted texts
final_text = text_tesseract + "\n" + text_easyocr

# Extract structured data
structured_data = extract_key_data(final_text)

# Print JSON Output
print(structured_data)

# # Save Output to JSON File
output_path = r'C:\Users\Ramya\Downloads\intern\output.json'
with open(output_path, "w") as json_file:
    json_file.write(structured_data)

print(f"✅ Extraction Complete! JSON saved at: {output_path}")

# import cv2
# import pytesseract
# import easyocr
# import json
# import re

# # Set path to Tesseract if needed (Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Ramya\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"

# # Preprocess image for better OCR accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
#     return thresh

# # Extract text using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img)
#     return text

# # Extract text using EasyOCR (for better handwritten recognition)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Extract key information using regex
# def extract_key_data(text):
#     data = {}
    
#     # Extract patient details
#     name_match = re.search(r'Name:\s*(.*)', text)
#     dob_match = re.search(r'DOB:\s*(\d{2}/\d{2}/\d{4})', text)
#     data["patient_name"] = name_match.group(1) if name_match else "Unknown"
#     data["dob"] = dob_match.group(1) if dob_match else "Unknown"

#     # Treatment details
#     data["injection"] = "Yes" if "Injection: Yes" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy: Yes" in text else "No"

#     # Difficulty Ratings (0-5)
#     data["difficulty_ratings"] = {
#         "bending": int(re.search(r'Bending:\s*(\d)', text).group(1)) if re.search(r'Bending:\s*(\d)', text) else 0,
#         "putting_on_shoes": int(re.search(r'Putting on Shoes:\s*(\d)', text).group(1)) if re.search(r'Putting on Shoes:\s*(\d)', text) else 0,
#         "sleeping": int(re.search(r'Sleeping:\s*(\d)', text).group(1)) if re.search(r'Sleeping:\s*(\d)', text) else 0
#     }

#     # Patient Changes
#     data["patient_changes"] = {
#         "since_last_treatment": re.search(r'Since Last Treatment:\s*(\w+)', text).group(1) if re.search(r'Since Last Treatment:\s*(\w+)', text) else "Unknown",
#         "since_start_of_treatment": re.search(r'Since Start of Treatment:\s*(\w+)', text).group(1) if re.search(r'Since Start of Treatment:\s*(\w+)', text) else "Unknown",
#         "last_3_days": re.search(r'Last 3 Days:\s*(\w+)', text).group(1) if re.search(r'Last 3 Days:\s*(\w+)', text) else "Unknown"
#     }

#     # Pain Symptoms (0-10)
#     data["pain_symptoms"] = {
#         "pain": int(re.search(r'Pain:\s*(\d+)', text).group(1)) if re.search(r'Pain:\s*(\d+)', text) else 0,
#         "numbness": int(re.search(r'Numbness:\s*(\d+)', text).group(1)) if re.search(r'Numbness:\s*(\d+)', text) else 0,
#     }

#     return json.dumps(data, indent=4)

# # Run OCR
# image_path = "sample_form.jpg"
# text = extract_text_tesseract(image_path)  # or extract_text_easyocr(image_path)
# structured_data = extract_key_data(text)
# print(structured_data)






# import cv2
# import pytesseract
# import easyocr
# import json
# import re
# import numpy as np
# import os

# # Set Tesseract Path (Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # ⏳ **Preprocess Image for Better OCR**
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Adaptive Thresholding (for better handwritten recognition)
#     adaptive_thresh = cv2.adaptiveThreshold(
#         gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
#     )

#     # Apply Morphological Transform to remove noise
#     kernel = np.ones((1, 1), np.uint8)
#     morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

#     return morph

# # 📌 **Extract Text with Tesseract**
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img, config="--psm 6")
#     return text

# # 📌 **Extract Text with EasyOCR (Better for Handwriting)**
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(["en"])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # 📌 **Extract Key Data Using Regex**
# def extract_key_data(text):
#     data = {}

#     # Patient Details
#     name_match = re.search(r"Patient Name\s*:\s*(.+)", text)
#     dob_match = re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1) if dob_match else "Unknown"

#     # Treatment Details
#     data["injection"] = "Yes" if re.search(r"Injection\s*:\s*Yes", text, re.IGNORECASE) else "No"
#     data["exercise_therapy"] = "Yes" if re.search(r"Exercise Therapy\s*:\s*Yes", text, re.IGNORECASE) else "No"

#     # Difficulty Ratings (0-5)
#     difficulty_tasks = [
#         "Bending", "Putting on shoes", "Sleeping", "Standing", 
#         "Walking through a store", "Driving", "Preparing a meal", "Yard work"
#     ]

#     data["difficulty_ratings"] = {}
#     for task in difficulty_tasks:
#         match = re.search(rf"{task}:\s*([0-5])", text)
#         data["difficulty_ratings"][task.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

#     # Patient Changes
#     data["patient_changes"] = {
#         "since_last_treatment": re.search(r"Patient Changes since last treatment:\s*(.+)", text, re.IGNORECASE).group(1).strip() if re.search(r"Patient Changes since last treatment:\s*(.+)", text, re.IGNORECASE) else "Unknown",
#         "since_start_of_treatment": re.search(r"Patient changes since the start of treatment:\s*(.+)", text, re.IGNORECASE).group(1).strip() if re.search(r"Patient changes since the start of treatment:\s*(.+)", text, re.IGNORECASE) else "Unknown",
#         "last_3_days": re.search(r"Describe any functional changes within the last three days \(good or bad\):\s*(.+)", text, re.IGNORECASE).group(1).strip() if re.search(r"Describe any functional changes within the last three days \(good or bad\):\s*(.+)", text, re.IGNORECASE) else "Unknown"
#     }

#     # Pain Symptoms (0-10)
#     pain_metrics = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     data["pain_symptoms"] = {}

#     for metric in pain_metrics:
#         match = re.search(rf"{metric}:\s*(\d+)", text)
#         data["pain_symptoms"][metric.lower()] = int(match.group(1)) if match else 0

#     return json.dumps(data, indent=4)

# # 📌 **Run OCR & Extract Data**
# image_path = r'C:\Users\Ramya\Downloads\intern\sample_form2.png'

# # Use both OCR engines
# tesseract_text = extract_text_tesseract(image_path)
# easyocr_text = extract_text_easyocr(image_path)

# # Combine results for better accuracy
# final_text = tesseract_text + "\n" + easyocr_text
# structured_data = extract_key_data(final_text)

# # ✅ Print Final Structured Data
# print(structured_data)






# # import cv2
# import pytesseract
# import easyocr
# import json
# import re
# import cv2

# # Set path to Tesseract if needed (Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Preprocess image for better OCR accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
#     return thresh

# # Extract text using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img)
#     return text

# # Extract text using EasyOCR (for better handwritten recognition)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Extract key information using regex
# def extract_key_data(text):
#     data = {}

#     # Extract patient details
#     name_match = re.search(r'Patient Name\s*:\s*([A-Za-z\s]+)', text)
#     dob_match = re.search(r'DOB\s*:\s*([\d/]+)', text)
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

#     # Extract injection & exercise therapy status
#     data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"

#     # Extract difficulty ratings (0-5)
#     ratings = {}
#     rating_labels = [
#         "Bending", "Putting on shoes", "Sleeping", "Standing", "Walking through a store",
#         "Driving", "Preparing a meal", "Yard work"
#     ]
#     for label in rating_labels:
#         match = re.search(rf"{label}:\s*([\d])", text)
#         ratings[label.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

#     data["difficulty_ratings"] = ratings

#     # Extract patient changes
#     changes = {}
#     changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text) else "Unknown"
#     changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text) else "Unknown"
#     changes["last_3_days"] = re.search(r"Describe any functional changes within the last three days.*?:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Describe any functional changes within the last three days.*?:\s*([\w\s]+)", text) else "Unknown"
    
#     data["patient_changes"] = changes

#     # Extract pain symptoms (0-10)
#     symptoms = {}
#     symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     for label in symptom_labels:
#         match = re.search(rf"{label}:\s*([\d]+)", text)
#         symptoms[label.lower()] = int(match.group(1)) if match else 0
    
#     data["pain_symptoms"] = symptoms

#     # Extract medical assistant data
#     medical_data = {}
#     medical_data["blood_pressure"] = re.search(r"Blood Pressure:\s*([\d/]+)", text).group(1) if re.search(r"Blood Pressure:\s*([\d/]+)", text) else "Unknown"
#     medical_data["hr"] = re.search(r"HR:\s*([\d]+)", text).group(1) if re.search(r"HR:\s*([\d]+)", text) else "Unknown"
#     medical_data["weight"] = re.search(r"Weight:\s*([\d]+)", text).group(1) if re.search(r"Weight:\s*([\d]+)", text) else "Unknown"
#     medical_data["height"] = re.search(r"Height:\s*([\d'\" ]+)", text).group(1).strip() if re.search(r"Height:\s*([\d'\" ]+)", text) else "Unknown"
#     medical_data["spo2"] = re.search(r"SpO2:\s*([\d]+)", text).group(1) if re.search(r"SpO2:\s*([\d]+)", text) else "Unknown"
#     medical_data["temperature"] = re.search(r"Temperature:\s*([\d.]+)", text).group(1) if re.search(r"Temperature:\s*([\d.]+)", text) else "Unknown"
#     medical_data["blood_glucose"] = re.search(r"Blood Glucose:\s*([\d]+)", text).group(1) if re.search(r"Blood Glucose:\s*([\d]+)", text) else "Unknown"
#     medical_data["respirations"] = re.search(r"Respirations:\s*([\d]+)", text).group(1) if re.search(r"Respirations:\s*([\d]+)", text) else "Unknown"

#     data["medical_assistant_data"] = medical_data

#     return json.dumps(data, indent=4)

# # Run OCR on Image
# image_path = r'C:\Users\Ramya\Downloads\intern\internassingment.png'  # Change to your actual image path
# text = extract_text_tesseract(image_path)  # Use Tesseract OCR
# # text = extract_text_easyocr(image_path)  # Uncomment to use EasyOCR

# # Extract structured data
# structured_data = extract_key_data(text)

# # Print JSON output
# print(structured_data)

# # Save to a JSON file
# with open("output.json", "w") as json_file:
#     json_file.write(structured_data)



# import cv2
# import pytesseract
# import easyocr
# import json
# import re

# # Set path to Tesseract if needed (Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Preprocess image for better OCR accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
#     return thresh

# # Extract text using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img)
#     return text

# # Extract text using EasyOCR (for better handwritten recognition)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Extract key information using regex
# def extract_key_data(text):
#     data = {}

#     # Extract patient details
#     name_match = re.search(r'Patient Name\s*:\s*([A-Za-z\s]+)', text)
#     dob_match = re.search(r'DOB\s*:\s*([\d/]+)', text)
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

#     # Extract injection & exercise therapy status
#     data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"

#     # Extract difficulty ratings (0-5)
#     ratings = {}
#     rating_labels = [
#         "Bending", "Putting on shoes", "Sleeping", "Standing", "Walking through a store",
#         "Driving", "Preparing a meal", "Yard work"
#     ]
#     for label in rating_labels:
#         match = re.search(rf"{label}:\s*([\d])", text)
#         ratings[label.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

#     data["difficulty_ratings"] = ratings

#     # Extract patient changes
#     changes = {}
#     changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text) else "Unknown"
#     changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text) else "Unknown"
#     changes["last_3_days"] = re.search(r"Describe any functional changes within the last three days.*?:\s*([\w\s]+)", text).group(1).strip() if re.search(r"Describe any functional changes within the last three days.*?:\s*([\w\s]+)", text) else "Unknown"
    
#     data["patient_changes"] = changes

#     # Extract pain symptoms (0-10)
#     symptoms = {}
#     symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     for label in symptom_labels:
#         match = re.search(rf"{label}:\s*([\d]+)", text)
#         symptoms[label.lower()] = int(match.group(1)) if match else 0
    
#     data["pain_symptoms"] = symptoms

#     # Extract medical assistant data
#     medical_data = {}
#     medical_data["blood_pressure"] = re.search(r"Blood Pressure:\s*([\d/]+)", text).group(1) if re.search(r"Blood Pressure:\s*([\d/]+)", text) else "Unknown"
#     medical_data["hr"] = re.search(r"HR:\s*([\d]+)", text).group(1) if re.search(r"HR:\s*([\d]+)", text) else "Unknown"
#     medical_data["weight"] = re.search(r"Weight:\s*([\d]+)", text).group(1) if re.search(r"Weight:\s*([\d]+)", text) else "Unknown"
#     medical_data["height"] = re.search(r"Height:\s*([\d'\" ]+)", text).group(1).strip() if re.search(r"Height:\s*([\d'\" ]+)", text) else "Unknown"
#     medical_data["spo2"] = re.search(r"SpO2:\s*([\d]+)", text).group(1) if re.search(r"SpO2:\s*([\d]+)", text) else "Unknown"
#     medical_data["temperature"] = re.search(r"Temperature:\s*([\d.]+)", text).group(1) if re.search(r"Temperature:\s*([\d.]+)", text) else "Unknown"
#     medical_data["blood_glucose"] = re.search(r"Blood Glucose:\s*([\d]+)", text).group(1) if re.search(r"Blood Glucose:\s*([\d]+)", text) else "Unknown"
#     medical_data["respirations"] = re.search(r"Respirations:\s*([\d]+)", text).group(1) if re.search(r"Respirations:\s*([\d]+)", text) else "Unknown"

#     data["medical_assistant_data"] = medical_data

#     return json.dumps(data, indent=4)

# # Run OCR on the uploaded image
# image_path = r'C:\Users\Ramya\Downloads\intern\internassingmentnew.png'
# text = extract_text_tesseract(image_path)  # Use Tesseract OCR

# # Uncomment to use EasyOCR for handwritten text
# # text = extract_text_easyocr(image_path)

# # Extract structured data
# structured_data = extract_key_data(text)

# # Print JSON output
# print(structured_data)

# # Save to a JSON file
# with open("/mnt/data/output.json", "w") as json_file:
#     json_file.write(structured_data)







# import cv2
# import pytesseract
# import easyocr
# import json
# import re
# import numpy as np

# # Set path to Tesseract (Windows users might need to specify the path)
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Path\to\tesseract.exe"

# # Preprocess the image for better OCR accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
#     # Optional: Apply morphological operations to enhance text visibility
#     kernel = np.ones((1, 1), np.uint8)
#     processed_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
#     return processed_img

# # Extract text using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img)
#     return text

# # Extract text using EasyOCR (better for handwriting)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Extract key information using regex
# def extract_key_data(text):
#     data = {}

#     # Extract patient details
#     name_match = re.search(r'Patient Name\s*:\s*(.*)', text)
#     dob_match = re.search(r'DOB\s*:\s*(\d{2}/\d{2}/\d{4})', text)
    
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

#     # Extract patient condition updates
#     patient_changes = re.search(r'Patient Changes since last treatment:\s*(.*)', text, re.IGNORECASE)
#     since_start = re.search(r'Patient changes since the start of treatment:\s*(.*)', text, re.IGNORECASE)
#     last_3_days = re.search(r'Describe any functional changes within the last three days \(good or bad\):\s*(.*)', text, re.IGNORECASE)

#     data["patient_changes"] = {
#         "since_last_treatment": patient_changes.group(1).strip() if patient_changes else "Unknown",
#         "since_start_of_treatment": since_start.group(1).strip() if since_start else "Unknown",
#         "last_3_days": last_3_days.group(1).strip() if last_3_days else "Unknown"
#     }

#     # Extract pain symptoms (0-10)
#     pain_match = re.search(r'Pain:\s*(\d+)', text)
#     numbness_match = re.search(r'Numbness:\s*(\d+)', text)
#     tingling_match = re.search(r'Tingling:\s*(\d+)', text)
#     burning_match = re.search(r'Burning:\s*(\d+)', text)
#     tightness_match = re.search(r'Tightness:\s*(\d+)', text)

#     data["pain_symptoms"] = {
#         "pain": int(pain_match.group(1)) if pain_match else 0,
#         "numbness": int(numbness_match.group(1)) if numbness_match else 0,
#         "tingling": int(tingling_match.group(1)) if tingling_match else 0,
#         "burning": int(burning_match.group(1)) if burning_match else 0,
#         "tightness": int(tightness_match.group(1)) if tightness_match else 0
#     }

#     # Extract vital signs
#     bp_match = re.search(r'Blood Pressure:\s*(\d+)', text)
#     hr_match = re.search(r'HR:\s*(\d+)', text)
#     weight_match = re.search(r'Weight:\s*(\d+)', text)
#     height_match = re.search(r'Height:\s*(\d+\'\d+)', text)
#     spO2_match = re.search(r'SpO2:\s*(\d+)', text)
#     temp_match = re.search(r'Temperature:\s*(\d+)', text)
#     glucose_match = re.search(r'Blood Glucose:\s*(\d+)', text)
#     respirations_match = re.search(r'Respirations:\s*(\d+)', text)

#     data["vital_signs"] = {
#         "blood_pressure": int(bp_match.group(1)) if bp_match else 0,
#         "heart_rate": int(hr_match.group(1)) if hr_match else 0,
#         "weight": int(weight_match.group(1)) if weight_match else 0,
#         "height": height_match.group(1) if height_match else "Unknown",
#         "SpO2": int(spO2_match.group(1)) if spO2_match else 0,
#         "temperature": int(temp_match.group(1)) if temp_match else 0,
#         "blood_glucose": int(glucose_match.group(1)) if glucose_match else 0,
#         "respirations": int(respirations_match.group(1)) if respirations_match else 0
#     }

#     return json.dumps(data, indent=4)

# # Run OCR and extract structured data
# image_path = r'C:\Users\Ramya\Downloads\intern\internassingmentnew.png'
# text_tesseract = extract_text_tesseract(image_path)
# text_easyocr = extract_text_easyocr(image_path)

# # Combine results for better accuracy
# combined_text = text_tesser



# import cv2
# import pytesseract
# import easyocr
# import json
# import re
# import numpy as np

# # Set path to Tesseract (Windows users may need to update this path)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Preprocess image for better OCR accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
#     # Apply morphological operations
#     kernel = np.ones((1, 1), np.uint8)
#     processed_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
#     return processed_img

# # Extract text using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     text = pytesseract.image_to_string(processed_img)
#     return text

# # Extract text using EasyOCR (for handwritten text)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Extract key data from text using regex
# def extract_key_data(text):
#     data = {}

#     # Extract patient details
#     name_match = re.search(r'Patient Name\s*:\s*([A-Za-z\s]+)', text)
#     dob_match = re.search(r'DOB\s*:\s*([\d/]+)', text)
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

#     # Extract injection & exercise therapy status
#     data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"

#     # Extract difficulty ratings (0-5)
#     ratings = {}
#     rating_labels = [
#         "Bending", "Putting on shoes", "Sleeping", "Standing", "Walking through a store",
#         "Driving", "Preparing a meal", "Yard work", "Picking up items off the floor"
#     ]
#     for label in rating_labels:
#         match = re.search(rf"{label}:\s*([\d])", text)
#         ratings[label.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

#     data["difficulty_ratings"] = ratings

#     # Extract patient changes
#     changes = {}
#     changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text)
#     changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text)
#     changes["last_3_days"] = re.search(r"Describe any functional changes within the last three days.*?:\s*([\w\s]+)", text)
    
#     data["patient_changes"] = {
#         "since_last_treatment": changes["since_last_treatment"].group(1).strip() if changes["since_last_treatment"] else "Unknown",
#         "since_start_of_treatment": changes["since_start_of_treatment"].group(1).strip() if changes["since_start_of_treatment"] else "Unknown",
#         "last_3_days": changes["last_3_days"].group(1).strip() if changes["last_3_days"] else "Unknown"
#     }

#     # Extract pain symptoms (0-10)
#     symptoms = {}
#     symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     for label in symptom_labels:
#         match = re.search(rf"{label}:\s*([\d]+)", text)
#         symptoms[label.lower()] = int(match.group(1)) if match else 0
    
#     data["pain_symptoms"] = symptoms

#     # Extract medical assistant data
#     medical_data = {
#         "blood_pressure": re.search(r"Blood Pressure:\s*([\d/]+)", text),
#         "hr": re.search(r"HR:\s*([\d]+)", text),
#         "weight": re.search(r"Weight:\s*([\d]+)", text),
#         "height": re.search(r"Height:\s*([\d'\" ]+)", text),
#         "spo2": re.search(r"SpO2:\s*([\d]+)", text),
#         "temperature": re.search(r"Temperature:\s*([\d.]+)", text),
#         "blood_glucose": re.search(r"Blood Glucose:\s*([\d]+)", text),
#         "respirations": re.search(r"Respirations:\s*([\d]+)", text),
#     }

#     # Clean extracted values
#     for key, value in medical_data.items():
#         medical_data[key] = value.group(1) if value else "Unknown"

#     data["medical_assistant_data"] = medical_data

#     return json.dumps(data, indent=4)

# # Run OCR and extract structured data
# image_path = r'C:\Users\Ramya\Downloads\intern\internassingmentnew.png'

# # Use Tesseract OCR
# text_tesseract = extract_text_tesseract(image_path)

# # Use EasyOCR for better handwritten text recognition
# text_easyocr = extract_text_easyocr(image_path)

# # Combine both results
# combined_text = text_tesseract + " " + text_easyocr

# # Extract structured information
# structured_data = extract_key_data(combined_text)

# # Print extracted data
# print(structured_data)

# # # Save to JSON file
# # output_path = r'C:\Users\Ramya\Downloads\intern\internassingmentnew.png'
# # with open(output_path, "w") as json_file:
# #     json_file.write(structured_data)

# # print(f"JSON output saved to: {output_path}")













# import cv2
# import pytesseract
# import easyocr
# import json
# import re

# # Set Tesseract Path (For Windows Users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Path to the uploaded image
# image_path = r"C:\Users\Ramya\Downloads\intern\internassingmentnew.png"

# # Function: Preprocess Image for Better OCR Accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Adaptive thresholding for improved text clarity
#     processed_img = cv2.adaptiveThreshold(
#         gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
#     )

#     # Denoise image to reduce artifacts
#     processed_img = cv2.fastNlMeansDenoising(processed_img, None, 30, 7, 21)

#     return processed_img

# # Function: Extract Text Using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     config = "--psm 6 --oem 3"  # Optimize OCR performance
#     text = pytesseract.image_to_string(processed_img, config=config)
#     return text

# # Function: Extract Text Using EasyOCR (For Handwritten Text)
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'], gpu=False)  # Force CPU
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Function: Extract Key Data Using Regex
# def extract_key_data(text):
#     data = {}

#     # Extract Patient Name & DOB
#     name_match = re.search(r'Patient Name\s*[:\-]\s*([A-Za-z\s]+)', text)
#     dob_match = re.search(r'DOB\s*[:\-]\s*([\d/]+)', text)
#     data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
#     data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"

#     # Extract Injection & Exercise Therapy Status
#     data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"

#     # Extract Difficulty Ratings (Scale 0-5)
#     ratings = {}
#     rating_labels = [
#         "Bending", "Putting on shoes", "Sleeping", "Standing", "Walking through a store",
#         "Driving", "Preparing a meal", "Yard work", "Picking up items off the floor"
#     ]
#     for label in rating_labels:
#         match = re.search(rf"{label}.*?(\d+)", text)
#         ratings[label.lower().replace(" ", "_")] = int(match.group(1)) if match else 0

#     data["difficulty_ratings"] = ratings

#     # Extract Patient Changes
#     changes = {}
#     changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text)
#     changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text)
#     changes["last_3_days"] = re.search(r"Describe any functional changes.*?:\s*([\w\s]+)", text)

#     for key in changes:
#         changes[key] = changes[key].group(1).strip() if changes[key] else "Unknown"

#     data["patient_changes"] = changes

#     # Extract Pain Symptoms (Scale 0-10)
#     symptoms = {}
#     symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     for label in symptom_labels:
#         match = re.search(rf"{label}:\s*([\d]+)", text)
#         symptoms[label.lower()] = int(match.group(1)) if match else 0

#     data["pain_symptoms"] = symptoms

#     # Extract Medical Assistant Data
#     medical_data = {}
#     medical_data["blood_pressure"] = re.search(r"Blood Pressure:\s*([\d/]+)", text)
#     medical_data["hr"] = re.search(r"HR:\s*([\d]+)", text)
#     medical_data["weight"] = re.search(r"Weight:\s*([\d]+)", text)
#     medical_data["height"] = re.search(r"Height:\s*([\d'\" ]+)", text)
#     medical_data["spo2"] = re.search(r"SpO2:\s*([\d]+)", text)
#     medical_data["temperature"] = re.search(r"Temperature:\s*([\d.]+)", text)
#     medical_data["blood_glucose"] = re.search(r"Blood Glucose:\s*([\d]+)", text)
#     medical_data["respirations"] = re.search(r"Respirations:\s*([\d]+)", text)

#     for key in medical_data:
#         medical_data[key] = medical_data[key].group(1) if medical_data[key] else "Unknown"

#     data["medical_assistant_data"] = medical_data

#     return json.dumps(data, indent=4)

# # Run OCR on Image
# text = extract_text_tesseract(image_path)  # Use Tesseract OCR

# # If handwriting is not extracted well, use EasyOCR
# # text = extract_text_easyocr(image_path)

# # Extract structured data
# structured_data = extract_key_data(text)

# # Print JSON Output
# print(structured_data)

# # # Save Output to JSON File
# # output_path = "/mnt/data/output.json"
# # with open(output_path, "w") as json_file:
# #     json_file.write(structured_data)

# # print(f"✅ Extraction Complete! JSON saved at: {output_path}")















# import cv2
# import pytesseract
# import easyocr
# import json
# import re

# # Path to the uploaded image
# image_path = "/mnt/data/internassingmentnew.png"

# # Function: Preprocess Image for Better OCR Accuracy
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     processed_img = cv2.adaptiveThreshold(
#         gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
#     )
#     processed_img = cv2.fastNlMeansDenoising(processed_img, None, 30, 7, 21)
#     return processed_img

# # Function: Extract Text Using Tesseract OCR
# def extract_text_tesseract(image_path):
#     processed_img = preprocess_image(image_path)
#     config = "--psm 6 --oem 3"
#     text = pytesseract.image_to_string(processed_img, config=config)
#     return text

# # Function: Extract Text Using EasyOCR
# def extract_text_easyocr(image_path):
#     reader = easyocr.Reader(['en'], gpu=False)
#     result = reader.readtext(image_path, detail=0)
#     return " ".join(result)

# # Function: Extract Key Data Using Regex
# def extract_key_data(text):
#     data = {}
    
#     # Extract Patient Name & DOB
#     name_match = re.search(r'Patient Name[\s:._-]+([A-Za-z]+)', text)
#     dob_match = re.search(r'DOB[\s:._-]+([\d/]+)', text)
#     data["patient_name"] = name_match.group(1) if name_match else "Unknown"
#     data["dob"] = dob_match.group(1) if dob_match else "Unknown"

#     # Extract Injection & Exercise Therapy Status
#     data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
#     data["exercise_therapy"] = "Yes" if "Exercise Therapy : YES" in text else "No"
    
#     # Extract Difficulty Ratings
#     ratings = {}
#     rating_labels = {
#         "Bending": "bending",
#         "Putting on shoes": "putting_on_shoes",
#         "Sleeping": "sleeping",
#         "Standing": "standing",
#         "Walking through a store": "walking_through_a_store",
#         "Driving": "driving",
#         "Preparing a meal": "preparing_a_meal",
#         "Yard work": "yard_work",
#         "Picking up items off the floor": "picking_up_items_off_the_floor"
#     }
#     for key, val in rating_labels.items():
#         match = re.search(rf"{key}.*?(\d+)", text)
#         ratings[val] = int(match.group(1)) if match else 0
#     data["difficulty_ratings"] = ratings
    
#     # Extract Patient Changes
#     changes = {}
#     changes["since_last_treatment"] = re.search(r"Patient Changes since last treatment:\s*([\w\s]+)", text)
#     changes["since_start_of_treatment"] = re.search(r"Patient changes since the start of treatment:\s*([\w\s]+)", text)
#     changes["last_3_days"] = re.search(r"Describe any functional changes.*?:\s*([\w\s]+)", text)
#     for key in changes:
#         changes[key] = changes[key].group(1).strip() if changes[key] else "Unknown"
#     data["patient_changes"] = changes
    
#     # Extract Pain Symptoms
#     symptoms = {}
#     symptom_labels = ["Pain", "Numbness", "Tingling", "Burning", "Tightness"]
#     for label in symptom_labels:
#         match = re.search(rf"{label}:\s*(\d+)", text)
#         symptoms[label.lower()] = int(match.group(1)) if match else 0
#     data["pain_symptoms"] = symptoms
    
#     # Extract Medical Assistant Data
#     medical_data = {}
#     medical_data["blood_pressure"] = re.search(r"Blood Pressure:\s*(\d+)", text)
#     medical_data["hr"] = re.search(r"HR:\s*(\d+)", text)
#     medical_data["weight"] = re.search(r"Weight:\s*(\d+)", text)
#     medical_data["height"] = re.search(r"Height:\s*([\d'\"]+)", text)
#     medical_data["spo2"] = re.search(r"SpO2:\s*(\d+)", text)
#     medical_data["temperature"] = re.search(r"Temperature:\s*(\d+)", text)
#     medical_data["blood_glucose"] = re.search(r"Blood Glucose:\s*(\d+)", text)
#     medical_data["respirations"] = re.search(r"Respirations:\s*(\d+)", text)
#     for key in medical_data:
#         medical_data[key] = medical_data[key].group(1) if medical_data[key] else "Unknown"
#     data["medical_assistant_data"] = medical_data
    
#     return json.dumps(data, indent=4)

# # Run OCR on Image
# text = extract_text_tesseract(image_path)

# # Extract structured data
# structured_data = extract_key_data(text)

# # Print JSON Output
# print(structured_data)






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

Optical Character Recognition (OCR) and Data Integration Project:

This project extracts and processes text data from scanned patient assessment forms using Optical Character Recognition (OCR). The extracted text is structured into JSON format and stored in a SQL database.

Features:
Extracts text from JPEG/PDF files using Tesseract OCR.

Parses and structures the extracted data into a JSON format.

Stores structured data in a SQL database.

Provides sample JSON output for reference.



Technologies Used:
Python
Tesseract OCR / EasyOCR
MySQL (for database storage)


Repository Structure:
├── ocr_script.py       # OCR implementation
├── database.sql        # SQL schema for database setup
├── sample_output.json  # Sample extracted JSON output
├── requirements.txt    # Required dependencies
├── README.md 

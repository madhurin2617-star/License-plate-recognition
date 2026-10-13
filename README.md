# License Plate Recognition System

## Project Overview
The License Plate Recognition System is a Python-based project that detects vehicle number plates from an input image and extracts the plate text using Optical Character Recognition (OCR).

The project uses OpenCV for image processing and number plate region detection, and EasyOCR to recognize the characters on the detected plate.

## Features
- Loads a vehicle image from the project folder.
- Detects a possible number plate region.
- Extracts text using EasyOCR.
- Displays the detected region with a bounding box.
- Shows the recognized number plate text on the image.

## Technologies Used
- Python 3.12
- OpenCV
- EasyOCR

## Project Structure
```text
Licence-Plate-Recognition/
├── main.py
├── README.md
└── images/
    └── car.jpg
```

## Installation

1. Install Python 3.12.
2. Open a terminal in the project directory.
3. Install the required libraries:

```bash
python -m pip install opencv-python==4.11.0.86 easyocr==1.7.2
```

## How to Run

Make sure the input image is available at `images/car.jpg`.

Run the following command from the project directory:

```bash
python main.py
```

The application displays the input image with the detected plate region and recognized text when detection and OCR succeed.

## Limitations
- Recognition accuracy depends on image quality, lighting, angle, and plate visibility.
- The current code processes the image at `images/car.jpg`.
- The detected text may not always match the actual number plate exactly.

## Author
GitHub:https://github.com/madhurin2617-star

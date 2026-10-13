
import cv2
import easyocr
import os
import re

reader = easyocr.Reader(['en'], gpu=False)

image_path = os.path.join("images", "car.jpg")
image = cv2.imread(image_path)

if image is None:
    print("ERROR: Image not found:", image_path)
    raise SystemExit

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade_path = (
    cv2.data.haarcascades
    + "haarcascade_russian_plate_number.xml"
)
detector = cv2.CascadeClassifier(cascade_path)

if detector.empty():
    print("ERROR: Number plate detector could not load.")
    raise SystemExit

plates = detector.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=8,
    minSize=(80, 20)
)

if len(plates) == 0:
    print("No number plate detected. Try a clearer image.")
else:
    # Choose the largest detected region
    x, y, w, h = max(plates, key=lambda p: p[2] * p[3])

    crop = gray[y:y+h, x:x+w]
    crop = cv2.resize(
        crop, None, fx=3, fy=3,
        interpolation=cv2.INTER_CUBIC
    )

    results = reader.readtext(
        crop,
        allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )

    # Keep plausible Indian-style registration strings
    candidates = []
    for _, text, confidence in results:
        cleaned = re.sub(r"[^A-Z0-9]", "", text.upper())
        if len(cleaned) >= 8:
            candidates.append((cleaned, confidence))

    if candidates:
        plate_text = max(candidates, key=lambda item: item[1])[0]
        print("Detected Number Plate:", plate_text)

        cv2.rectangle(
            image, (x, y), (x+w, y+h), (255, 0, 0), 2
        )
        cv2.putText(
            image, plate_text, (x, max(y-10, 25)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 255, 0), 2
        )
    else:
        print("Plate region found, but its text was not read clearly.")
        cv2.rectangle(
            image, (x, y), (x+w, y+h), (255, 0, 0), 2
        )

cv2.imshow("License Plate Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

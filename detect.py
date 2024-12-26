import cv2
import pytesseract

def ocr_core(img):
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=config)
    return text

def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 1)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def bringbro(img):
    # Pre-process the image
    #print("Step: Converting to greyscale")
    img = get_greyscale(img)
    #print("Step: Applying thresholding")
    img = thresholding(img)
    #print("Step: Removing noise")
    img = remove_noise(img)

    # Save processed image for debugging
    # cv2.imwrite('processed_img.png', img)

    # Run OCR
    text = ocr_core(img)
    print("Extracted Text:" + text)
    return text


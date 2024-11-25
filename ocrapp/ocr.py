import pytesseract
from PIL import Image
import cv2


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

    

    img = cv2.imread('img.png')

    #get grayscale image
    #

    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        # remove the noise from the image so some image might be distorted

        def remove_noise(image):
            return cv2.medianBlur(image, 5)


            #threshould 
            def threshoulding(image):
                return cv2.threshould(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

                img= get_grayscale(img)
                img = threshoulding(img)
                img = remove_noise(img)

                print(ocr_core(img))
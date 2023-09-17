import cv2
import numpy as np
import pytesseract
import mss
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# coordinates of the gene display in the game. These are the coordinates for a 1920x1080 screen
internal_boundbox = {'top': 300, 'left': 795, 'width': 160, 'height': 20}
external_boundbox = {'top': 365, 'left': 1170, 'width': 260, 'height': 30}


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def invert(image):
    return cv2.bitwise_not(image)


def threshold(image):
    return cv2.threshold(image, 145, 255, cv2.THRESH_BINARY)[1]


def pre_process(image):
    image = np.array(image)
    image = get_grayscale(image)
    image = invert(image)
    image = threshold(image)
    return image


def gene_is_valid(gene):
    if gene in ('W', 'X', 'Y', 'G', 'H'):
        return True
    else:
        return False


sct = mss.mss()

genes = []

while True:
     # TODO: add second scan location

    # internal_grab = sct.grab(internal_boundbox)   
    # internal_img = Image.frombytes('RGB', internal_grab.size, internal_grab.bgra, 'raw', 'BGRX')
    # cv2.imshow('screen', np.array(internal_grab))
    external_grab = sct.grab(external_boundbox)

    external_grab = pre_process(external_grab)
    cv2.imshow('screen2', external_grab)
    external_img = Image.fromarray(external_grab)

    try:
        text = pytesseract.image_to_string(external_img, config='--psm 11')
        gene = ''.join(letter.upper() for letter in text.split() if gene_is_valid(letter.upper()))
        
        if gene in genes:
            print('gene already in list') # TODO: remove
        elif len(gene) == 6:
            genes.append(gene)
            print(genes) # TODO: remove
    except:
        text = 'error'  # TODO: remove

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
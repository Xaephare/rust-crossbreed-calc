import cv2
import numpy as np
import pytesseract
import mss
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESS_CONFIG = '--psm 11'

# coordinates of the gene display in the game. These are the coordinates for a 1920x1080 screen
# internal and external refer to inside and outside of the inventory respectively
internal_boundbox = {'top': 300, 'left': 795, 'width': 160, 'height': 20}
external_boundbox = {'top': 365, 'left': 1170, 'width': 260, 'height': 30}


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def threshold(image):
    return cv2.threshold(image, 105, 255, cv2.THRESH_BINARY_INV)[1]


def upscale(image):
    return cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)


def pre_process(image):
    image = np.array(image)
    image = upscale(image)
    image = get_grayscale(image)
    image = threshold(image)
    return image


def gene_is_valid(gene):
    if gene in ('W', 'X', 'Y', 'G', 'H'):
        return True
    else:
        return False


def ocr_scan(image, genes_list):
    try:
        text = pytesseract.image_to_string(image, config=TESS_CONFIG)
        gene = ''.join(letter.upper() for letter in text.split() if gene_is_valid(letter.upper()))
        
        if gene in  genes_list:
            return
        elif len(gene) == 6:
            return gene
    except:
        print('error')
    return

sct = mss.mss()

genes = []

while True:
    internal_grab = sct.grab(internal_boundbox)
    internal_grab = pre_process(internal_grab)
    internal_img = Image.fromarray(internal_grab)
    cv2.imshow('Internal', internal_grab)

    external_grab = sct.grab(external_boundbox)
    external_grab = pre_process(external_grab)
    external_img = Image.fromarray(external_grab)
    cv2.imshow('External', external_grab)

    if ocr_scan(internal_img, genes) :
        genes.append(ocr_scan(internal_img, genes))
        print(genes)
    if ocr_scan(external_img, genes):
        genes.append(ocr_scan(external_img, genes))
        print(genes)
    
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
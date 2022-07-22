import pytesseract
from PIL import Image
from config import profit_coords
from session import tesseract_path


pytesseract.pytesseract.tesseract_cmd = tesseract_path
tess_config = r'-c tessedit_char_whitelist=0123456789+-.'


def recognize(img_path):
    img = Image.open(img_path)

    # crop image
    img = img.crop((profit_coords[0], profit_coords[1], profit_coords[2], profit_coords[3]))

    text = pytesseract.image_to_string(img, config=tess_config)
    text = text.strip()
    return text

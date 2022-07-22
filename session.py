from get_adb import get_adb_path


adb_path = get_adb_path()
default_tesseract_path = r'D:\Python\Tesseract\tesseract.exe'
tesseract_path = default_tesseract_path or input(f'Tesseract path: [{default_tesseract_path}]')

import pytesseract as tr
import cv2
from PIL import Image
import csv

list_photo = ['1.jpg', '2.jpg', '3.jpg', '4.jpg',
                '5.jpg', '6.jpg', '7.jpg','8.jpg',
                '9.jpg', '10.webp', '11.png', '12.jpg', '13.png']


def create_csv():
    with open(f'ocr.csv', 'w', newline='') as f:
        fieldnames = ['PIL', 'CV2']
        thewritter = csv.DictWriter(f, fieldnames=fieldnames)
        thewritter.writeheader()

def insert_to_csv(data):
    with open(f'ocr.csv', 'a') as f:
        thewritter = csv.writer(f)
        thewritter.writerow(data)

def main():
    create_csv()
    for x in list_photo:
        im = cv2.imread(x)
        pl = Image.open(x)
        str_from_img_cv2 = tr.image_to_string(im)
        str_from_img_pil = tr.image_to_string(pl)
        res = [str_from_img_pil, str_from_img_cv2]
        insert_to_csv(res)


if __name__ == "__main__":
    main()
    print('finish')
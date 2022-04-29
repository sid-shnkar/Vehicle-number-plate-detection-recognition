import cv2
import imutils
import pytesseract
import csv
import string
import os
import glob
from collections import Counter

# specify the path where tesseract.exe is located as shown below
pytesseract.pytesseract.tesseract_cmd='D:\\Users\\Siddharth\\Documents\\ml_ds_projects\\tesseract.exe'

#------------------------------------------------------------------------------------------------------

class vehicleType():
    def __init__(self, image_location):
        self.img = cv2.imread(image_location, 1)
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels_image = self.w*self.h
        self.colour_count = {}

    def rgb_count(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                rgb_value = (self.img[x, y, 2], self.img[x, y, 1], self.img[x, y, 0])
                if rgb_value in self.colour_count:
                    self.colour_count[rgb_value] += 1
                else:
                    self.colour_count[rgb_value] = 1

    def get_colour(self):
        self.rgb_count()
        self.number_counter = Counter(self.colour_count).most_common(20)

        red = 0
        green = 0
        blue = 0
        total_count = 10

        for i in range(0, total_count):
            red += self.number_counter[i][0][0]
            green += self.number_counter[i][0][1]
            blue += self.number_counter[i][0][2]

        average_red = red / total_count
        average_green = green / total_count
        average_blue = blue / total_count

        temp_list=[]
        temp_list.append(average_red)
        temp_list.append(average_green)
        temp_list.append(average_blue)

        return temp_list


# ----------------------------------------------------------------------------------------------------
def process_image(image):
    image = imutils.resize(image, width=300)
    cv2.imshow("Original image", image)
    cv2.waitKey(500)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Greyed image", grayscale_image)
    cv2.waitKey(500)

    flattened_image = cv2.bilateralFilter(grayscale_image, 11, 17, 17)
    cv2.imshow("Flattened image", grayscale_image)
    cv2.waitKey(500)

    edged_image = cv2.Canny(flattened_image, 30, 200)
    cv2.imshow("Image with edges", edged_image)
    cv2.waitKey(500)

    contours, temp = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_replica = image.copy()
    cv2.drawContours(image_replica, contours, -1, (255, 255, 0), 3)
    cv2.imshow("All Contours", image_replica)
    cv2.waitKey(500)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
    number_plate_contour = None
    image_replica = image.copy()
    cv2.drawContours(image_replica, contours, -1, (255, 255, 0), 3)
    cv2.imshow("Top 30 contours", image_replica)
    cv2.waitKey(500)


    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)
        if len(approx) == 4:
            number_plate_contour = approx
            x, y, w, h = cv2.boundingRect(contour)
            cropped_image = image[y:y + h, x:x + w]
            cv2.imwrite('./' + 'result' + '.png', cropped_image)
            break

    cv2.drawContours(image, [number_plate_contour], -1, (255, 255, 0), 3)
    cv2.imshow("Detected number plate", image)
    cv2.waitKey(500)

    cropped_image_location = 'result.png'
    cv2.imshow("Cropped image", cv2.imread(cropped_image_location))
    plate = pytesseract.image_to_string(cropped_image_location, lang='eng')
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    return plate


# -----------------------------------------------------------------------------------------

def show_details(plate):
    table = str.maketrans('', '', string.ascii_lowercase)
    plate = plate.translate(table)
    plate = ''.join(ch for ch in plate if ch.isalnum())

    vehicle_code = plate
    vehicle_code = ''.join(vehicle_code.split())
    vehicle_plate = vehicle_code
    vehicle_code = vehicle_plate[0:4]

    vehicle_district = "Not available"
    vehicle_state = "Not available"

    for key, value in vehicle_dict.items():
        new_value = value.split('-')
        if key == vehicle_code:
            vehicle_district = new_value[1]
            vehicle_state = new_value[0]


    print("Number plate:", vehicle_plate)

    plate_colour = []
    plate_background= vehicleType('result.png')
    plate_colour = plate_background.get_colour()
    red_value = round(plate_colour[0])
    green_value = round(plate_colour[1])
    blue_value = round(plate_colour[2])
    vehicle_type=""
    if red_value >= 210 and green_value >= 186 and blue_value <= 40:
        vehicle_type="COMMERCIAL"
    elif red_value >= 124 and green_value >= 135 and blue_value >= 148:
        vehicle_type = "PRIVATE"
    else:
        vehicle_type = "OTHERS"

    print("Category of vehicle: {}".format(vehicle_type))
    print("State corresponding to the number plate: {}".format(vehicle_state.upper()))
    print("District corresponding to the number plate: {}".format(vehicle_district.upper()))
    print("****************************************************************************************\n")


# _--------------------------------------------------------------------------------

print("\n************ Welcome to vehicle number plate detection-recognition system *************\n")
vehicle_dict = {}

with open('state_district.csv', mode='r') as infile:
    reader = csv.reader(infile)
    vehicle_dict = {rows[0]: rows[1] for rows in reader}


dir = os.path.dirname(__file__)
for img in glob.glob(dir + "/test_images/*.jpg"):
    image = cv2.imread(img)
    plate_returned = process_image(image)
    show_details(plate_returned)

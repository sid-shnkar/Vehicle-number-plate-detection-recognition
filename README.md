# Vehicle-number-plate-detection-recognition
A computer vision project to automatically detect and recognize the text written on the number plate from an input image of a vehicle and also display the details like state and district to which the number plate is registered.

**Programming language used:** Python

**Libraries used:** OpenCV, Pytesseract, Imutils

## Steps to run the program:
To install the python libraries required by the program, open the terminal and type the following command then hit enter:
```
 pip install opencv-contrib-python
 pip install imutils
 pip install pytesseract
```

Then download and install the software called tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)

## Implementation
This project is implemented in four phases:

### 1. Pre-processing

We take the images present in a folder called 'test_images' one by one as our input and resize the width to be equal to 300 pixels, and then we display on the screen. Next we convert our image to grayscale using cv2.COLOR_BGR2GRAY and display the converted image. Then we reduce the noise in the grayscale image with the help of cv2.bilateralFilter and display the flattened image on the screen.  

### 2. Detection

We pass the flattened image obtained in previous step cv2.canny to detect the edges in it. Then we find the contours from the edged image by removing all the redundant points on the contours detected. We then draw the identified contours on our image and display the image with the identified contours drawn around it.
Next we sort the contours based on the minimum area which is set to be 30 and ignore the ones below that. We draw the sorted contours on the image and display the image which contains the top 30 contours drawn around it. Then we find contour with 4 sides by using cv2.arcLength and cv2.approxPolyDP functions. After completing these steps, we crop the rectangular part identified as number plate. Finally we draw and display the final image that has a contour drawn over the number plate.

### 3. Recognition

In this phase, we extract the text from the image of the cropped number plate. For this task, we use the pytesseract library which is an optical character recognition (OCR) tool for python to extract and display the number plate on the screen.

### 4. Searching

In this phase, we search for the state and district in which the number plate was registered by taking the first 4 characters of the plate and searching it in the external database which is present in 'state_district.csv' file. It contains the RTO codes for each state and their respective districts. 

## Applications

Vehicle number plate detection and recognition system has a wide range of applications since the number plate also called as the license plate is the primary and the most widely accepted mandatory identifier of motor vehicles. Following are some of the applications:

* Road Tolling: Tolls are a common way of funding the improvements of highways, motorways, roads and bridges. Efficient road tolling reduces fraud related to non-payment, makes charging effective, reduces required manpower to process events of exceptions and these can be implemented using this system.

* Housing societies: It can be used in housing societies to let in resident's vehicles inside by storing the number plate details in the database. This can reduce the man-force near the security gate.

* Parking; Parking access automation, vehicle location guidance, parking fee charging, etc. are some of the areas in which this system is helpful.

## Program execution pics
![vndr-p1](https://user-images.githubusercontent.com/104520126/166226824-a186bc82-339a-4342-9430-004b75fd47b9.jpg)






![vndr-p2](https://user-images.githubusercontent.com/104520126/166226836-d228a55d-c97d-44d4-932d-5c4a9b10ce50.jpg)




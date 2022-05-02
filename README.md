# Vehicle-number-plate-detection-recognition
A computer vision project to automatically detect and recognize the text written on the number plate from an input image of a vehicle.

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

### 1. Image pre-processing

We take the images present in a folder called 'test_images' one by one as our input and resize the width to be equal to 300 pixels, and then we display it to the user. Next we convert our image to grayscale using cv2.COLOR_BGR2GRAY and display the converted image. Then we reduce the noise in the grayscale image with the help of cv2.bilateralFilter and display the flattened image on the screen.  

### 2. Detection

We pass the flattened image obtained in previous step cv2.canny to detect the edges in it. Then we find the contours from the edged image by removing all the redundant points on the contours detected.
### 3. Recognition

### 4. Searching


## Applications

Vehicle number plate detection and recognition system has a wide range of applications since the number plate also called as the license plate is the primary and the most widely accepted mandatory identifier of motor vehicles. Following are some of the applications:

* Road Tolling: Tolls are a common way of funding the improvements of highways, motorways, roads and bridges. Efficient road tolling reduces fraud related to non-payment, makes charging effective, reduces required manpower to process events of exceptions and these can be implemented using this system.

* Housing societies: It can be used in housing societies to let in resident's vehicles inside by storing the number plate details in the database. This can reduce the man-force near the security gate.

* Parking; Parking access automation, vehicle location guidance, parking fee charging, etc. are some of the areas in which this system is helpful.

## Program execution pics
![vndr-p1](https://user-images.githubusercontent.com/104520126/166226824-a186bc82-339a-4342-9430-004b75fd47b9.jpg)






![vndr-p2](https://user-images.githubusercontent.com/104520126/166226836-d228a55d-c97d-44d4-932d-5c4a9b10ce50.jpg)




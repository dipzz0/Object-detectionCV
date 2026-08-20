Object Detection is a computer vision technique used to identify and locate one or more objects in an image or video. Unlike image classification, object detection not only identifies the object but also draws a bounding box around it and displays its class label.
YOLO (You Only Look Once) is a fast and accurate deep learning algorithm for object detection. It processes the entire image in a single pass, making it suitable for real-time applications. YOLO can detect multiple objects simultaneously, such as people, cars, bicycles, dogs, buses, and many other objects.
YOLOv8 is a version of the YOLO family that provides improved speed, accuracy, and ease of use for various object detection applications.

Software Requirements
- Google Colab
- Python 3.x
- Ultralytics YOLOv8
- OpenCV
- Image containing one or more objects

Procedure (Step-by-Step)

Step 1:
Open Google Colab.

Step 2:
Install the Ultralytics library.

Step 3:
Import the required libraries.

Step 4:
Load the pre-trained YOLOv8 model.

Step 5:
Upload an image containing one or more objects.

Step 6:
Run the YOLO model to detect objects.

Step 7:
Draw bounding boxes and display the corresponding object names.

Step 8:
Display the final output image with the detected objects.

Example

Input Image:

Upload an image containing objects.

<img width="455" height="304" alt="image" src="https://github.com/user-attachments/assets/a377bf5f-877b-42fe-855f-4258e21110bc" />


Output Image:

Image with detected objects, bounding boxes, and class labels

<img width="453" height="302" alt="image" src="https://github.com/user-attachments/assets/e7333d8d-f9b0-4ce1-8ee4-9e29fc0a3d45" />

Result

The YOLOv8 model successfully detects multiple objects in the input image and highlights them using bounding boxes with their corresponding class labels.



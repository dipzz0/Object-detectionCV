# Install YOLOv8
!pip install ultralytics -q

# Import Libraries
from ultralytics import YOLO
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Load YOLOv8 Model
model = YOLO("yolov8n.pt")

# Upload Image
print("Upload an Image")
uploaded = files.upload()

# Read Image
image_name = list(uploaded.keys())[0]
img = cv2.imread(image_name)

# Detect Objects
results = model(img)

# Draw Bounding Boxes
output = results[0].plot()


# Display Output
cv2_imshow(output)

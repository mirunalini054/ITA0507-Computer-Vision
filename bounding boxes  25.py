from ultralytics import YOLO
import cv2

# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

# Read the image
image = cv2.imread("C:/Users/mohan/Downloads/MINIIII.webp")

if image is None:
    print("Error: Could not load watch.jpg")
    exit()

# Detect objects
results = model(image)

# Draw detected objects
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])

        # Detect only watch
        if class_name == "clock" and confidence > 0.30:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                f"{class_name} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

# Display result
cv2.imshow("Detected Watch", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

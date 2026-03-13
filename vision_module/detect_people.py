from ultralytics import YOLO
import cv2
from ultralytics import YOLO
import cv2
import requests
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)[0]

    people_count = 0

    for box in results.boxes:
        cls = int(box.cls)

        if cls == 0:   # person
            people_count += 1

    # Crowd level logic
    if people_count <= 3:
        crowd_level = "LOW"
    elif people_count <= 7:
        crowd_level = "MEDIUM"
    else:
        crowd_level = "HIGH"
    if people_count > 6:
     queue_detected = True
else:
    queue_detected = False    
data = {
    "people_count": people_count,
    "crowd_level": crowd_level,
    "queue_detected": queue_detected
}
try:
    requests.post("http://127.0.0.1:5000/update", json=data)
except:
    pass

    annotated_frame = results.plot()

    cv2.putText(
        annotated_frame,
        f"People: {people_count}",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Crowd: {crowd_level}",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )
    cv2.putText(
    annotated_frame,
    f"Queue: {queue_detected}",
    (20,130),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,0,0),
    2
)

    cv2.imshow("Crowd Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import cvlib as cv

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
video = cv2.VideoWriter("rec_out.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20, (frame.shape[1], frame.shape[0]))

while True:
	ret, frame = cap.read()
	face, confidence = cv.detect_face(frame)


	for (i, (x, y, w, h)) in enumerate(face):
		cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
	video.write(frame)

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Release handle to the webcam
cap.release()
cv2.destroyAllWindows()

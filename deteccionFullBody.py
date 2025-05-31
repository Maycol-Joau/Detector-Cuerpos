import cv2

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

cap = cv2.VideoCapture(1) # Valor en "1" para que reconozca mi celular como cámara

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Detección de Cuerpo Completo', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Presionar 'q' para salir.
        break

cap.release()
cv2.destroyAllWindows()

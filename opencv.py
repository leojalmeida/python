import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def show_image(image):
    cv2.imshow('Teste', image)
    while True:
        key = cv2.waitKey(10)
        if key % 256 == 27:
            print("Escaping")
            break
    return


def face_detection(img):


    # img = cv2.imread('imagem_0.png')
    # show_image(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def simple_video():
    capture = cv2.VideoCapture(0)
    counter = 0
    while True:

        ret, frame = capture.read()
        face_detection(frame)
        # cv2.imshow('teste', frame)

        key = cv2.waitKey(10)
        if key % 256 == 27:
            print("Escaping")
            break
        elif key % 256 == 32:
            img_name = "imagem_{}.png".format(counter)
            cv2.imwrite(img_name, frame)
            counter += 1

    capture.release()
    cv2.destroyAllWindows()


simple_video()

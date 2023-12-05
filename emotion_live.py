# # # face emotion detection in live camera

# import cv2

# # You sould install the deep face library
# # pip install deepface
# # this code was tested in Python 3.8
# from deepface import DeepFace
# import pyfirmata
# import time


# # You can download the file 'haarcascade_frontalface_default.xml'
# # from cv2 Git hub

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# cap = cv2.VideoCapture(0)
# # board = pyfirmata.Arduino('COM5')
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     font_path = "NotoColorEmoji-Regular.ttf"  # Replace with the actual path or filename
#     font_size = 40
#     for x, y, w, h in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
#         try:
#             result = DeepFace.analyze(
#                 img_path=frame, actions=["emotion"], enforce_detection=False
#             )
#         except:
#             print("no face")

#         result1 = result[0]
#         emotion = result1["dominant_emotion"]
#         if emotion == "happy":
#             emotion = "😊"

#         txt = str(emotion)
#         # time.sleep(1)
#         # if(txt=="happy"):
#         #     board.digital[13].write(1)
#         # else :
#         #     board.digital[13].write(0)

#         cv2.putText(frame, txt, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
#     cv2.imshow("frame", frame)
#     # time.sleep(1)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

import cv2
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from deepface import DeepFace


class EmotionApp:
    def __init__(self, root, cap, font_path):
        self.root = root
        self.root.title("Emotion Recognition")
        self.cap = cap
        self.font_path = font_path

        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.judul = tk.Label(root, text="", font=("Arial", 60))
        self.judul.place(relx=0.38, rely=0.05)

        self.update()

    def update(self):
        ret, frame = self.cap.read()

        try:
            result = DeepFace.analyze(
                img_path=frame, actions=["emotion"], enforce_detection=False
            )
        except:
            print("no face")

        result1 = result[0]
        emotion = result1["dominant_emotion"]
        if emotion == "happy":
            self.judul.config(text="😊")
        elif emotion == "neutral":
            self.judul.config(text="😐")
        elif emotion == "surprise":
            self.judul.config(text="😯")
        elif emotion == "sad":
            self.judul.config(text="😞")
        # Convert frame to Pillow Image
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_img)

        # Load the font
        font_size = 40
        font = ImageFont.truetype(self.font_path, font_size)

        # Add Unicode text (emoticon) to the image

        # Convert the image back to Tkinter format
        img_tk = ImageTk.PhotoImage(pil_img)

        # Update the label with the new image
        self.video_label.img = img_tk
        self.video_label.configure(image=img_tk)

        # Repeat the update after a delay (e.g., 30 milliseconds)
        self.root.after(30, self.update)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Specify the path to the font file (replace with the actual path)
    font_path = "NotoColorEmoji-Regular.ttf"

    root = tk.Tk()
    app = EmotionApp(root, cap, font_path)
    app.run()

    cap.release()
    cv2.destroyAllWindows()


# cap.release()
# cv2.destroyAllWindows()

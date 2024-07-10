import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text,lang= language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


video = cv2.VideoCapture(1)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Object Detection", output_image)

    for item in label:
        if item in label:
            pass
        else:
            labels.append(item)  # but object are not in list after adding list

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q e click and process end
        break

# this part in voice
i = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I found  a {label}, and, ")
    else:
        new_sentence.append(f" A {label}")

    i += 1

print(" ".join(new_sentence))
# but you have in object detection in voice ->
speech(" ".join(new_sentence))


# print (labels)

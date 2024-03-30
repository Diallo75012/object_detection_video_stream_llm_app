# firt run is going to download the model automatically so need second run to start the app
# test video https://www.youtube.com/watch?v=q6njK5acv-A
from ultralytics import YOLO
import cv2
import itertools
import os
import time


# helper functions
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

# 1_load yolov8 model
model = YOLO('yolov8n.pt')

# 2_load video
video_path = 'https://www.youtube.com/watch?v=q6njK5acv-A'
cap = cv2.VideoCapture(video_path)

# 3_define variables
ret=True
key_0 = cv2.waitKey(0)
key_25 = cv2.waitKey(25)
count = 1
number = 1
folder = "./frames/"
detected_objects = []  # List to store detected object names

# 4_read frames
while ret:
  ret, frame = cap.read()
  # 5_detect and track object
  # Perform tracking with the model
  results = model.track(source=video_path, show=True, persist=True, stream=True)  # Tracking with default tracker. with stream true results variable is returning a generator, without it is a list returned but you can loop on the generator using the python library itertools

 # Process results generator: here we just get the 10 first frames otherwise there is too many images and can't control or hard to stop process...
  # for generator so stream=True or otherwise just turn it into a list by using  list(results) and iterating through it to not exaust the generator
  for result in itertools.islice(results, 0, 10, 3): # change count increment to match step (here every 3 frames)
  # for result in list(results)[:10]:
  # for list so stream=False
  #for result in results[:10]:

    # save result variable in a file to check it
    with open("results_check_variable.txt", "w") as f:
      f.write(f"result{number}: {result.orig_img}")

    boxes = result.boxes  # Boxes object for bounding box outputs
    print("Boxes: ", boxes)
    masks = result.masks  # Masks object for segmentation masks outputs
    print("Masks: ", masks)
    keypoints = result.keypoints  # Keypoints object for pose outputs
    print("Keypoints: ", keypoints)
    probs = result.probs  # Probs object for classification outputs
    print("Probs: ", probs)
    result.show()  # display to screen
    result.save(filename=f"{folder}result{count}.jpg")  # save to disk
    count += 3
    time.sleep(10)

    detect_frame = model.predict(frame)
    for elem in detect_frame:
      print("Elem: ", elem)
      boxes = elem.boxes
      print("Boxes: ", boxes)
      for box in boxes:
        print("Box: ", box)
        c = box.cls
        print("C: ", c)
        print(model.names[int(c)])
        with open("detect_frame_name.txt", "w") as f:
          f.write(f"{numebr}: {model.names[int(c)]}")
          number += 1
    """"
    # save the names of what has been detected to a file
    class_id = result  # Assuming detection[0] is the class ID
    print("Class_id: ", class_id)
    classes = result.names
    print("Classes: ", classes)
    object_name = classes[class_id]  # 'classes' is a list of class names indexed by class ID
    print("Object_name: ", object_name)
    detected_objects.append(object_name)
    print("Detected_objects: ", detected_objects)
    # Optionally, save detected object names to a file
    with open('detected_objects.txt', 'w') as file:
      for object_name in detected_objects:
        file.write(f"{number}: {object_name}\n")
        number += 1
    """
    if ret:
      result_plot = results[0].plot()
      cv2.imshow('frame', frame_)
      if key_0 & 0xFF == ord('q'):
        ret = False
        print("key 'q' has been hit, exiting first loop")
        pass
print("Exited to video frame collection. All frames are in the ./frames/ folder\n next loop will read it and try to identify what is detected in those images")
"""
while True:
  ret, frame = cap.read()
  trackings = model.track(frame, persist=True)
  # 6_plot results
  # cv2.rectangle
  # cv2.putText
  frame_ = trackings.plot()

  # 7_visualize
  cv2.imshow('frame', frame_)

  tracking_plot = trackings[0].plot()
  cv2.imshow('frame', frame_)
  time.sleep(10)
  if key_0 & 0xFF == ord('q'):
    break 
# need to add art that will use the function helper load_images_from_folder(f"{folder}")

print("Work Done!")
"""

"""
cap = cv2.VideoCapture(video_path)

ret = True
# 3_read frames
while ret:
    ret, frame = cap.read()

    if ret:

        # 4_detect objects
        # 5_track objects
        results = model.track(frame, persist=True)

        # 6_plot results
        # cv2.rectangle
        # cv2.putText
        frame_ = results[0].plot()

        # 7_visualize
        cv2.imshow('frame', frame_)
        
        # stops if 'q' keyboard letter pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
"""

"""

"""

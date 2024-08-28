import threading
import numpy as np
import cv2
import tensorflow as tf
import time
from collections import Counter
from Module.music import EmotionMusicPlayer, emotion_dict, music_library
from Module.UI import EmotionMusicUI

# Initialize the EmotionMusicPlayer
player = EmotionMusicPlayer(emotion_dict, music_library)

# Create the UI and pass the player
ui = EmotionMusicUI(player)

# Buffer to hold recognized emotions over a short period
emotion_buffer = []
buffer_duration = 5  # seconds
start_time = time.time()

# Start the webcam feed
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
facecasc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def emotion_detection():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(48, 48, 1)),
        tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.25),

        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.25),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(7, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])
    model.load_weights('model/emotion_model.h5')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray_frame[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi_gray = roi_gray.astype("float") / 255.0
            roi_gray = np.expand_dims(roi_gray, axis=-1)
            roi_gray = np.expand_dims(roi_gray, axis=0)

            prediction = model.predict(roi_gray)[0]
            emotion_index = int(np.argmax(prediction))
            emotion_buffer.append(emotion_index)

        # Check if the buffer is full
        if time.time() - start_time > buffer_duration:
            # Most common emotion in buffer
            most_common_emotion = Counter(emotion_buffer).most_common(1)[0][0]
            emotion_buffer.clear()
            ui.update_emotion_display(most_common_emotion)
            player.play_music(most_common_emotion)

            # Reset the timer
            start_time = time.time()

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the emotion detection in a separate thread
detection_thread = threading.Thread(target=emotion_detection)
detection_thread.start()

# Run the UI in the main thread
ui.run()

# Wait for the detection thread to finish
detection_thread.join()

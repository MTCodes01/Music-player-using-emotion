import numpy as np
import cv2
import tensorflow as tf
import time
from collections import Counter
from Module.music import EmotionMusicPlayer, emotion_dict, music_library

# Set mode
mode = 'display'

# Create the model
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

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              metrics=['accuracy'])

# Display mode
model.load_weights('model.weights.h5')
# prevents OpenCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)
# dictionary which assigns each label an emotion
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Surprised", 6: "Sad"}

# Initialize the EmotionMusicPlayer
player = EmotionMusicPlayer(emotion_dict, music_library)

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

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't grab frame.")
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        
        # Store recognized emotion in the buffer
        emotion_buffer.append(maxindex)

    # Update the emotion buffer and check if time exceeds the buffer duration
    if time.time() - start_time > buffer_duration:
        most_common_emotion = Counter(emotion_buffer).most_common(1)[0][0]
        print(f"Most Common Emotion: {emotion_dict[most_common_emotion]}")

        # Play music based on the most common emotion
        player.play_music(most_common_emotion)

        # Clear buffer and reset timer
        emotion_buffer = []
        start_time = time.time()

        # Stop analyzing while music is playing
        if player.is_playing:
            break

    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

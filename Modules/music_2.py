import os

# Emotion dictionary
emotion_dict = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Sad",
    5: "Surprise",
    6: "Neutral"
}

path = os.getcwd()

# Offline music library paths
emotion_folders = {
    0: f'{path}\\Music\\Angry',
    1: f'{path}\\Music\\Disgust',
    2: f'{path}\\Music\\Fear',
    3: f'{path}\\Music\\Happy',
    4: f'{path}\\Music\\Sad',
    5: f'{path}\\Music\\Surprise',
    6: f'{path}\\Music\\Neutral'
}

# Function to load songs from a folder
def load_songs_from_folder(folder_path):
    songs = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            songs.append(os.path.join(folder_path, file_name))
    return songs

# Load all songs into a dictionary
all_songs = {}
for emotion, folder in emotion_folders.items():
    all_songs[emotion] = load_songs_from_folder(folder)

# Placeholder function to determine the emotion of a song
def determine_emotion(song):
    # In a real-world scenario, replace this with actual emotion detection logic
    return 3  # For demonstration purposes, return the integer for 'Happy'

# Recommend songs based on the emotion of a given song
def recommend_songs_based_on_emotion(song):
    emotion = determine_emotion(song)
    if emotion in all_songs:
        return all_songs[emotion]
    else:
        return []
 
# Example usage
song_to_recommend = 'test'
recommended_songs = recommend_songs_based_on_emotion(song_to_recommend)
print("Recommended Songs:")
for song in recommended_songs:
    print(song)

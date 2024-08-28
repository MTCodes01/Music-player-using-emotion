import pygame
import os
import random
import time

class EmotionMusicPlayer:
    def __init__(self, emotion_dict, music_library):
        self.emotion_dict = emotion_dict
        self.music_library = music_library
        self.current_emotion = None
        self.current_track = None
        self.is_playing = False
        self.is_paused = False

        pygame.mixer.init()

    def play_music(self, emotion_index):
        print(f"play_music called with emotion_index: {emotion_index}")
        emotion = self.emotion_dict.get(emotion_index, "Neutral")
        print(f"Resolved emotion: {emotion}")

        if emotion != self.current_emotion or not self.is_playing:
            self.current_emotion = emotion
            self.switch_track(emotion)
        elif self.is_paused:
            self.resume_music()

    def switch_track(self, emotion):
        if self.current_track:
            pygame.mixer.music.fadeout(3000)
            time.sleep(3)

        tracks = self.music_library.get(emotion, [])
        if tracks:
            track_path = random.choice(tracks)
            if track_path and os.path.exists(track_path):
                try:
                    pygame.mixer.music.load(track_path)
                    pygame.mixer.music.play(loops=0)
                    self.current_track = track_path
                    self.is_playing = True
                    print(f"Playing {emotion} song: {track_path}")

                except pygame.error as e:
                    print(f"Error playing {track_path}: {e}")
            else:
                print(f"Track not found or does not exist: {track_path}")
        else:
            print(f"No tracks available for emotion: {emotion}")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.current_emotion = None
        self.current_track = None

    def pause_music(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("Music paused.")

    def resume_music(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("Music resumed.")

    def next_track(self):
        self.switch_track(self.current_emotion)

    def quit_player(self):
        pygame.mixer.quit()

def get_file_paths(folder_path):
    audio_extensions = ('.mp3', '.wav', '.ogg', '.flac')
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(audio_extensions):
                file_paths.append(os.path.join(root, file))
    return file_paths

# Emotion dictionary
emotion_dict = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Sad",
    5: "Surprised",
    6: "Neutral"
}

# Offline music library paths
music_folders = {
    0: 'D:\\Github\\Parasseri-Techies\\Music\\Angry',
    1: 'D:\\Github\\Parasseri-Techies\\Music\\Disgust',
    2: 'D:\\Github\\Parasseri-Techies\\Music\\Fear',
    3: 'D:\\Github\\Parasseri-Techies\\Music\\Happy',
    4: 'D:\\Github\\Parasseri-Techies\\Music\\Sad',
    5: 'D:\\Github\\Parasseri-Techies\\Music\\Surprised',
    6: 'D:\\Github\\Parasseri-Techies\\Music\\Neutral'
}

# Create the music library
music_library = {emotion_dict[i]: get_file_paths(j) for i, j in music_folders.items()}

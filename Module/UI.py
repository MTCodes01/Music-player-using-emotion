# UI.py
import tkinter as tk
from music import EmotionMusicPlayer, emotion_dict, music_library

# Example usage
player = EmotionMusicPlayer(emotion_dict, music_library)

def update_emotion_display(emotion_index):
    emotion_display.config(text=f"Current Emotion: {emotion_dict[emotion_index]}")

def on_play_pause():
    if player.is_playing and not player.is_paused:
        player.pause_music()
        play_button.config(text="Resume")
    else:
        emotion_index = emotion_index.get()
        player.play_music(emotion_index)
        update_emotion_display(emotion_index)
        play_button.config(text="Pause")

def on_stop():
    player.stop_music()
    play_button.config(text="Play")

def on_next():
    player.next_track()
    play_button.config(text="Pause")

def on_quit():
    player.quit_player()
    root.destroy()

# Initialize the Tkinter window
root = tk.Tk()
root.title("Emotion-Based Music Player")
root.geometry("400x500")
root.configure(bg="#121212")

# Header
header = tk.Label(root, text="Emotion-Based Music Player", font=("Arial", 20, "bold"), bg="#121212", fg="white")
header.pack(pady=20)

# Now Playing section
now_playing_frame = tk.Frame(root, bg="#121212", relief="groove")
now_playing_frame.pack(pady=20, padx=20, fill="x")

song_info_frame = tk.Frame(now_playing_frame, bg="#121212")
song_info_frame.pack(pady=10)

song_title = tk.Label(song_info_frame, text="Song Title", font=("Arial", 14, "bold"), bg="#121212", fg="white")
song_title.pack(anchor="w")

artist_name = tk.Label(song_info_frame, text="Artist Name", font=("Arial", 10), bg="#121212", fg="gray")
artist_name.pack(anchor="w", pady=5)

# Emotion Display
emotion_display = tk.Label(root, text="Current Emotion: Neutral", font=("Arial", 14), bg="#121212", fg="white")
emotion_display.pack(pady=20)

# Control buttons
controls_frame = tk.Frame(root, bg="#121212")
controls_frame.pack(pady=10)

btn_style = {"bg": "#00a239", "fg": "white", "width": 8, "height": 2, "bd": 0, "font": ("Arial", 12, "bold")}
play_button = tk.Button(controls_frame, text="Play", **btn_style, command=on_play_pause)
play_button.pack(side="left", padx=10)
tk.Button(controls_frame, text="Next", **btn_style, command=on_next).pack(side="left", padx=10)

# Quit button
tk.Button(root, text="Quit", **btn_style, command=on_quit).pack(pady=20)

root.mainloop()

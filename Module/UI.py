import tkinter as tk
from music import EmotionMusicPlayer, emotion_dict, music_library

class EmotionMusicUI:
    def __init__(self, player):
        self.player = player
        self.root = tk.Tk()
        self.root.title("Emotion-Based Music Player")
        self.root.geometry("400x500")
        self.root.configure(bg="#121212")

        self.current_emotion = None

        # Header
        header = tk.Label(self.root, text="Emotion-Based Music Player", font=("Arial", 20, "bold"), bg="#121212", fg="white")
        header.pack(pady=20)

        # Now Playing section
        now_playing_frame = tk.Frame(self.root, bg="#121212", relief="groove")
        now_playing_frame.pack(pady=20, padx=20, fill="x")

        song_info_frame = tk.Frame(now_playing_frame, bg="#121212")
        song_info_frame.pack(pady=10)

        self.song_title = tk.Label(song_info_frame, text="Song Title", font=("Arial", 14, "bold"), bg="#121212", fg="white")
        self.song_title.pack(anchor="w")

        self.artist_name = tk.Label(song_info_frame, text="Artist Name", font=("Arial", 10), bg="#121212", fg="gray")
        self.artist_name.pack(anchor="w", pady=5)

        # Emotion Display
        self.emotion_display = tk.Label(self.root, text="Current Emotion: Neutral", font=("Arial", 14), bg="#121212", fg="white")
        self.emotion_display.pack(pady=20)

        # Control buttons
        controls_frame = tk.Frame(self.root, bg="#121212")
        controls_frame.pack(pady=10)

        btn_style = {"bg": "#00a239", "fg": "white", "width": 8, "height": 2, "bd": 0, "font": ("Arial", 12, "bold")}
        self.play_button = tk.Button(controls_frame, text="Play", **btn_style, command=self.on_play_pause)
        self.play_button.pack(side="left", padx=10)
        tk.Button(controls_frame, text="Next", **btn_style, command=self.on_next).pack(side="left", padx=10)

        # Quit button
        tk.Button(self.root, text="Quit", **btn_style, command=self.on_quit).pack(pady=20)

    def update_emotion_display(self, emotion_index):
        self.current_emotion = emotion_index
        self.emotion_display.config(text=f"Current Emotion: {emotion_dict[emotion_index]}")

    def on_play_pause(self):
        if self.player.is_playing and not self.player.is_paused:
            self.player.pause_music()
            self.play_button.config(text="Resume")
        else:
            emotion_index = self.current_emotion if self.current_emotion is not None else 3
            self.player.play_music(emotion_index)
            self.update_emotion_display(emotion_index)
            self.play_button.config(text="Pause")

    def on_next(self):
        self.player.next_track()
        self.play_button.config(text="Pause")

    def on_quit(self):
        self.player.quit_player()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

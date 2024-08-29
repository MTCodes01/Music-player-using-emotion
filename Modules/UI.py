import tkinter as tk
from tkinter import ttk
from Modules.music import EmotionMusicPlayer, emotion_dict, music_library

class EmotionMusicUI:
    def __init__(self, player):
        self.player = player
        self.root = tk.Tk()
        self.root.title("Emotion-Based Music Player")
        self.root.geometry("400x350")
        self.root.configure(bg="#121212")

        self.current_emotion = None

        # Header
        header = tk.Label(self.root, text="Emotion-Based Music Player", font=("Arial", 20, "bold"), bg="#121212", fg="white")
        header.pack(pady=20)

        # Emotion Display
        self.emotion_display = tk.Label(self.root, text="Current Emotion: Neutral", font=("Arial", 14), bg="#121212", fg="white")
        self.emotion_display.pack(pady=20)

        # Dropdown for manual emotion selection
        self.emotion_var = tk.StringVar()
        self.emotion_dropdown = ttk.Combobox(self.root, textvariable=self.emotion_var, state="readonly", font=("Arial", 12))
        self.emotion_dropdown['values'] = list(emotion_dict.values())
        self.emotion_dropdown.set("Select Emotion")
        self.emotion_dropdown.pack(pady=10)
        self.emotion_dropdown.bind("<<ComboboxSelected>>", self.on_emotion_select)

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
        print("Ok then!")
        self.player.quit_player()
        self.root.destroy()

    def on_emotion_select(self, event):
        selected_emotion = self.emotion_var.get()
        emotion_index = list(emotion_dict.values()).index(selected_emotion)
        self.update_emotion_display(emotion_index)
        self.player.play_music(emotion_index)
        self.play_button.config(text="Pause")

    def run(self):
        self.root.mainloop()

# Example usage
# player = EmotionMusicPlayer(emotion_dict, music_library)
# ui = EmotionMusicUI(player)
# ui.run()

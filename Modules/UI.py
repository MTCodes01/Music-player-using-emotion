import tkinter as tk
from tkinter import ttk
from Modules.music import EmotionMusicPlayer, emotion_dict, music_library

class EmotionMusicUI:
    def __init__(self, player):
        self.player = player
        self.root = tk.Tk()
        self.root.title("Vibify")
        self.root.geometry("512x850+650+100")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        self.current_emotion = 6  # Assuming Neutral as the default initial emotion

        # Header
        header = tk.Label(self.root, text="Vibify", font=("Arial", 50, "underline", "bold"), bg="#121212", fg="ghostwhite")
        header.pack(pady=20)

        # Emotion Display
        self.emotion_display = tk.Label(self.root, text=f"Current Emotion: {emotion_dict[self.current_emotion]}", font=("Arial", 25), bg="#121212", fg="white")
        self.emotion_display.pack(pady=20)

        # Style for the Combobox
        style = ttk.Style()
        style.theme_use('clam')  # Use a modern theme for better appearance
        style.configure("TCombobox",
                        fieldbackground="#333333",  # Background color of the dropdown field
                        background="#333333",  # Background color of the dropdown list
                        foreground="black",  # Text color
                        arrowcolor="white",  # Arrow color
                        selectbackground="gray",  # Selected item background color
                        selectforeground="white",  # Selected item text color
                        padding=(15, 12, 15, 12),  # Padding around the text
                        font=("Arial", 20))

        # Dropdown for manual emotion selection
        self.emotion_var = tk.StringVar()
        self.emotion_dropdown = ttk.Combobox(self.root, textvariable=self.emotion_var, state="readonly", style="TCombobox")
        self.emotion_dropdown['values'] = list(emotion_dict.values())
        self.emotion_dropdown.set(emotion_dict[self.current_emotion])  # Set the dropdown to the current emotion
        self.emotion_dropdown.pack(pady=10)
        self.emotion_dropdown.bind("<<ComboboxSelected>>", self.on_emotion_select)

        # Control buttons
        controls_frame = tk.Frame(self.root, bg="#121212")
        controls_frame.pack(pady=10)

        self.play_button = tk.Button(controls_frame, text="Play", command=self.on_play_pause, font=("Arial", 12, "bold"), bg="lime", fg="black", padx=10, pady=5)
        self.play_button.pack(side="left", padx=10)

        next_button = tk.Button(controls_frame, text="Next", command=self.on_next, font=("Arial", 12, "bold"), bg="lime", fg="black", padx=10, pady=5)
        next_button.pack(side="left", padx=10)

        # Quit button
        quit_button = tk.Button(self.root, text="Quit", command=self.on_quit, font=("Arial", 12, "bold"), bg="red", fg="black", padx=10, pady=5)
        quit_button.pack(pady=20)

    def update_emotion_display(self, emotion_index):
        self.current_emotion = emotion_index
        self.emotion_display.config(text=f"Current Emotion: {emotion_dict[emotion_index]}")
        self.emotion_var.set(emotion_dict[emotion_index])  # Update the dropdown to show the selected emotion

    def update_not_found(self):
        self.emotion_display.config(text="Emotion not recogonised!")
        self.emotion_var.set(None)

    def on_play_pause(self):
        if self.player.is_playing and not self.player.is_paused:
            self.player.pause_music()
            self.play_button.config(text="Resume")
        else:
            emotion_index = self.current_emotion if self.current_emotion is not None else 6
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

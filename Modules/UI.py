import tkinter as tk
from tkinter import ttk
from music import EmotionMusicPlayer, emotion_dict, music_library

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, radius=25, padding=5, **kwargs):
        super().__init__(parent, **kwargs)

        self.command = command
        self.radius = radius
        self.padding = padding

        # Calculate dimensions
        self.text_id = self.create_text(0, 0, text=text, anchor="center", font=("Arial", 12, "bold"), fill="black")
        bbox = self.bbox(self.text_id)
        width = bbox[2] - bbox[0] + 2 * padding
        height = bbox[3] - bbox[1] + 2 * padding

        # Draw rounded rectangle
        self.round_rect(0, 0, width, height, radius=self.radius, fill="lime", outline="")

        # Center text on the rounded rectangle
        self.coords(self.text_id, width / 2, height / 2)

        # Set button size
        self.config(width=width, height=height)

        # Bind click event
        self.bind("<Button-1>", self.on_click)

    def round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_click(self, event):
        if self.command:
            self.command()

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
                        padding=(5, 2, 5, 2),  # Padding around the text
                        font=("Arial", 12))

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

        self.play_button = RoundedButton(controls_frame, text="Play", command=self.on_play_pause, radius=20, padding=10, bg="#121212", highlightthickness=0)
        self.play_button.pack(side="left", padx=10)

        next_button = RoundedButton(controls_frame, text="Next", command=self.on_next, radius=20, padding=10, bg="#121212", highlightthickness=0)
        next_button.pack(side="left", padx=10)

        # Quit button
        quit_button = RoundedButton(self.root, text="Quit", command=self.on_quit, radius=20, padding=10, bg="#121212", highlightthickness=0)
        quit_button.pack(pady=20)

    def update_emotion_display(self, emotion_index):
        self.current_emotion = emotion_index
        self.emotion_display.config(text=f"Current Emotion: {emotion_dict[emotion_index]}")
        self.emotion_var.set(emotion_dict[emotion_index])  # Update the dropdown to show the selected emotion

    def on_play_pause(self):
        if self.player.is_playing and not self.player.is_paused:
            self.player.pause_music()
            self.play_button.itemconfig(self.play_button.text_id, text="Resume")
        else:
            emotion_index = self.current_emotion if self.current_emotion is not None else 6
            self.player.play_music(emotion_index)
            self.update_emotion_display(emotion_index)
            self.play_button.itemconfig(self.play_button.text_id, text="Pause")

    def on_next(self):
        self.player.next_track()
        self.play_button.itemconfig(self.play_button.text_id, text="Pause")

    def on_quit(self):
        print("Ok then!")
        self.player.quit_player()
        self.root.destroy()

    def on_emotion_select(self, event):
        selected_emotion = self.emotion_var.get()
        emotion_index = list(emotion_dict.values()).index(selected_emotion)
        self.update_emotion_display(emotion_index)
        self.player.play_music(emotion_index)
        self.play_button.itemconfig(self.play_button.text_id, text="Pause")

    def run(self):
        self.root.mainloop()

# Example usage
player = EmotionMusicPlayer(emotion_dict, music_library)
ui = EmotionMusicUI(player)
ui.run()

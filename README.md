# Vibify

## Project Description

The **Vibify** is an program that uses facial emotion recognition to create a personalized music experience. By detecting the user's emotional state through a camera, the player automatically selects and plays music that matches or enhances the detected mood.

## Features

- **Real-Time Emotion Detection:** 
  - Uses a camera to capture and analyze facial expressions to determine the user's current emotion.
  - Supports emotions like Happy, Sad, Fearful, Disgusted, Surprised, Angry, and Neutral.
  
- **Mood-Based Playlist Generation:** 
  - Automatically selects and plays a playlist from a predefined set of mood-based playlists corresponding to the detected emotion.
  
- **User Interface:** 
  - Simple and intuitive interface to pause/play the current playing song, rendomly choose a song from the same emotion playlist and view the detected emotion.
<!--
 - **User Input Override:**
  - Allows users to manually select a mood if they prefer a different playlist than what is suggested.
-->
## Installation

1. Navigate to the desired directory using the shell/command prompt.
2. Clone the repository:
    ```sh
    git clone https://github.com/MTCodes01/Parasseri-Techies.git
    ```
3. Navigate to the project directory:
    ```sh
    cd Parasseri-Techies
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Install the pre-trained model [Click here](https://drive.google.com/file/d/1ovr_qhyfKxpqIdyd5WFfvHA807Jln9Nr/view?usp=sharing) `Only Needed if you don't want to train a new model`
6. Install the pre-defined music library [Click here](https://drive.google.com/drive/folders/1vqBbMODw54qFj-yE4OlC9n_98m6mT7_L?usp=sharing) `place the folder in the same directory as the main.py`

## Usage

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. `Run the train script`(Ignore if you installed the pre-trained model)
   ```sh
   python train.py
   ```
4. `Run the main script`(After either the training/Download of the pre-trained model is done and `model.weights.h5` is in the same directory as the `main.py`):
    ```sh
    python main.py
    ```
5. The camera will start capturing your facial expressions, and the system will detect your emotion.
6. Based on the detected emotion, the corresponding song will start playing automatically.
7. Use the user interface to pause/play the current playing song, rendomly choose a song from the same emotion playlist and view the detected emotion.
   
> [!NOTE]
> ## Emotion-Based Playlists
>
> The player selects music based on the following emotions:
> - **Happy:**
> - **Sad:**
> - **Fearful:**
> - **Disgusted:**
> - **Surprised:**
> - **Angry:**
> - **Neutral:**
>
> You can customize the playlists by adding or modifying the songs in the respective folders.

## Directory Structure

- `Module/`
  - `__init__.py`
  - `music.py` - Handles the music playback and playlist management.
  - `UI.py` - Manages the user interface, displaying the detected emotion and controls.

- `music/`
  - `Happy/` - Contains songs for the Happy mood.
  - `Sad/` - Contains songs for the Sad mood.
  - `Fearful/` - Contains songs for the Fearful mood.
  - `Disgusted/` - Contains songs for the Disgusted mood.
  - `Surprised/` - Contains songs for the Surprised mood.
  - `Angry/` - Contains songs for the Angry mood.
  - `Neutral/` - Contains songs for the Neutral mood.

- `Concept.md` - Detailed description of the project and its concept.
- `main.py` - The entry point of the application, integrates emotion detection and music playback.
- `model.weights.h5` - Contains the model weights.
- `LICENSE` - The license file for the project.
- `README.md` - The file you're currently reading.

<div align="center"> Made for a project expo in 4 days!</div>

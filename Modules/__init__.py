# import os
# import subprocess

# def convert_mp3_to_wav(input_file, output_file):
#     try:
#         # Construct the command to run ffmpeg
#         command = ['ffmpeg', '-i', input_file, output_file]
        
#         # Execute the command
#         subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
#         print(f"Conversion successful: {input_file} to {output_file}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during conversion: {e}")
#     except FileNotFoundError:
#         print("ffmpeg not found. Please ensure ffmpeg is installed and accessible.")

# def convert_all_mp3_in_folder(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.lower().endswith('.mp3'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, file.rsplit('.', 1)[0] + '.wav')
#                 convert_mp3_to_wav(input_file, output_file)

# # Music folders dictionary
# music_folders = {
#     0: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Angry',
#     1: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Disgusted',
#     2: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Fearful',
#     3: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Happy',
#     4: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Neutral',
#     5: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Surprised',
#     6: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Sad'
# }

# # Convert all MP3 files in each specified folder
# for folder_path in music_folders.values():
#     convert_all_mp3_in_folder(folder_path)




# import os

# def delete_mp3_files(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.lower().endswith('.mp3'):
#                 file_path = os.path.join(root, file)
#                 try:
#                     os.remove(file_path)
#                     print(f"Deleted: {file_path}")
#                 except Exception as e:
#                     print(f"Error deleting {file_path}: {e}")

# # Music folders dictionary
# music_folders = {
#     0: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Angry',
#     1: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Disgusted',
#     2: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Fearful',
#     3: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Happy',
#     4: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Neutral',
#     5: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Surprised',
#     6: 'D:\\Github\\Emotion-detection\\src\\Webpage\\Music\\Sad'
# }

# # Delete all MP3 files in each specified folder
# for folder_path in music_folders.values():
#     delete_mp3_files(folder_path)






# import os

# def get_file_paths(folder_path):
#     file_paths = []
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             file_paths.append(os.path.join(root, file))
#     return file_paths

# folder_path = r'D:\\Github\\Emotion-detection\\src\\Webpage\\Music'
# file_paths = get_file_paths(folder_path)

# for file_path in file_paths:
#     print(file_path)
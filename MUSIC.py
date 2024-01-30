
import os
from pytube import YouTube
from pytube.helpers import safe_filename

def download_audio(video_url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Construct the filename using the sanitized video title
        audio_filename = safe_filename(yt.title) + ".mp3"

        # Download the audio to the specified path with the constructed filename
        audio_stream.download(output_path=save_path, filename=audio_filename)

        print(f"Download complete. Audio saved at: {os.path.join(save_path, audio_filename)}")

        # Print the video title
        print(f"Video title: {yt.title}")

        return os.path.join(save_path, audio_filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    link = "https://youtu.be/PIF2U5rCPl4"
    # Get the YouTube video URL from the user
    video_url = link
    # Specify the location to save the audio
    save_path = r"C:\\Users\\Admin\\programmer\\code-programmer\\ALL CODES\\PROJECT\\VIDEO CLONING\\CLONED MUSIC & AUDIO"


    # Download the audio
    downloaded_audio_path = download_audio(video_url, save_path)
# exe pyinstaller --onefile your_script.py replace your_script with file name




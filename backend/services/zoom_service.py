import requests

def download_zoom_recording(url):

    response = requests.get(url)

    file_path = "uploads/zoom_recording.mp4"

    with open(file_path, "wb") as f:
        f.write(response.content)

    return file_path
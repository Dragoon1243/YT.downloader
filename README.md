# YouTube Video Downloader

This repository contains a Flask-based web application called **YouTube Video Downloader** that allows users to download YouTube videos by providing a video URL. The application processes the link, downloads the video, and provides the user with an easy way to access the video file.

## Contents

- `app.py` - The Flask application that handles the backend logic for downloading YouTube videos.
- `index.html` - The front-end HTML page for user interaction where users can input video links.
- `styles.css` - The CSS file for styling the HTML interface of the web application.

## Getting Started

### Prerequisites

To run this application, you’ll need to have the following installed:

- **Python 3.7+**
- Required Python libraries (install with `pip install -r requirements.txt`):
  - `Flask`
  - `yt-dlp`

### Running the Application

1. Clone this repository:

    ```bash
    git clone https://github.com/Dragoon1243/YouTube-Video-Downloader.git
    cd YouTube-Video-Downloader
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your browser and visit `http://127.0.0.1:5000/` to access the web interface.

## Features

- **Easy to Use**: Simply paste a YouTube video link and click to download.
- **Fast Processing**: Downloads the video in the best available quality and provides direct download links.
- **Lightweight**: Runs as a local web application, with minimal setup and dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

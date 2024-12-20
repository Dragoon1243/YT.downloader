from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    link = data.get('link')
    if not link:
        return jsonify({'error': 'No link provided'}), 400

    video_id = "video_" + link.split('v=')[-1]
    output_path = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.mp4")
    youtube_dl_options = {
        'format': 'best',
        'outtmpl': output_path
    }

    try:
        with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([link])
        return jsonify({'message': 'Download completed', 'filename': f"{video_id}.mp4"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/downloads/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)

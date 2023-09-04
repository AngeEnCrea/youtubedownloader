from flask import Flask, render_template, request
import youtube_downloader

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/download', methods=['POST'])
def download():

  url = request.form['url']

  if 'mp4' in request.form:
    youtube_downloader.download_video(url)
  elif 'mp3' in request.form:
    youtube_downloader.download_audio(url)

  return render_template('success.html')

@app.route('/static/<path:filename>')
def static_files(filename):
  return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
  app.run(debug=True)

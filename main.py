from flask import Flask, jsonify, abort
import os
import json
from pathlib import Path
import mutagen
from mutagen.easyid3 import EasyID3

app = Flask(__name__)

DATA_DIR = "data"

global library

def songDiscovery():
    # Clear Library var
    library = []

    # Find all songs
    for path in Path('library').rglob('*'):
        if not(path.is_dir()):
            try:
                metadata = EasyID3(path)
                library.append(metadata)
            except mutagen.id3._util.ID3NoHeaderError:
                library.append({"name": path.name, "path": path})

@app.route('/active', methods=['GET'])
def active():
    return jsonify()

@app.route('/about', methods=['GET'])
def about():
    aboutinfo = {"version": "dev", "github": "https://github.com/RestartB/MusicAPI"}
    return jsonify(aboutinfo)

@app.route('/playlists', methods=['GET'])
def playlists():
    playlists = os.listdir("data/playlist")
    playlistsData = []

    for playlist in playlists:
        try:
            with open(os.path.join(DATA_DIR, "playlist", playlist, 'playlist.json'), mode='r') as playlistFile:
                playlistsData.append(json.load(playlistFile))
        except FileNotFoundError:
            pass
    
    return jsonify({"amount": len(playlistsData), "playlists": playlistsData})

if __name__ == "__main__":
    songDiscovery()
    app.run(debug=True, port=5050)
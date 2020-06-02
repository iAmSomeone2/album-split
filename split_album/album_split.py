#!/usr/bin/env python3

"""
   Copyright 2020 Brenden Davidson

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import ffmpeg
import json
from datetime import datetime
from sys import argv, stderr

def get_album_json(json_file_name):
    album_data = None
    with open(json_file_name, "r") as file:
        album_data = json.load(file)
    
    return album_data

def make_timestamp(time_ms):
    num_secs = float(time_ms) / 1000.0
    num_hours = int(num_secs // 60 // 60)
    num_secs -= num_hours * 360
    num_mins = int(num_secs // 60)
    num_secs -= num_mins * 60

    return "{}:{}:{:.3f}".format(num_hours, num_mins, num_secs)

def split_album(album_audio, album_data):
    ext = album_data.split('.')[-1]
    media = album_data["media"]
    current_ms = 0
    for item in media:
        tracks = item["tracks"]
        for track in tracks:
            stream = ffmpeg.input(str(album_audio))

            start_time = make_timestamp(int(current_ms))
            end_time = make_timestamp(int(track['length']))

            track_name = str(track['number']) + " - " + str(track['title']) + "." + ext
            
            stream = ffmpeg.output(stream, track_name, acodec="copy", ss=start_time, t=end_time)
            ffmpeg.run(stream)

            current_ms += int(track['length'])


if __name__ == "__main__":
    if len(argv) < 3:
        print("Input files required.", file=stderr)
        exit(1)

    json_file = argv[2]
    audio_file = argv[1]

    album_data = get_album_json(json_file)
    split_album(audio_file, album_data)

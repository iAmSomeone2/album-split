# Split Album

Uses MusicBrainz JSON data and FFmpeg to split audio files into individual tracks.

## Usage

1. Locate MusicBrainz JSON data for your album. For example: https://musicbrainz.org/release/1febc5df-e7ab-4f31-9abb-f68c14cdc7c8/details

2. Confirm that the single audio file for the album begins exactly where the first song is supposed to begin.

3. Confirm that there are no playback gaps between songs in the album file.

4. Feed the album file and JSON data to the program like this:
``` bash
python split_album [album_file] [json_data_file]
```

5. Wait for the program to finish outputting the exported files.
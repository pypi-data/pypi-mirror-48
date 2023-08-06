# deezloader
This project has been created to download songs, albums or playlists with Spotify or Deezer link from Deezer.
* ### OS Supported ###
    ![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
    ![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg)
* ### Installation ###
      pip3 install deezloader
### Download song
Download track by Spotify link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_trackspo("Insert the Spotify link of the track to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
Download track by Deezer link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_trackdee("Insert the Deezer link of the track to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
### Download album
Download album by Spotify link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_albumspo("Insert the Spotify link of the album to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
Download album from Deezer link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_albumdee("Insert the Deezer link of the album to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
### Download playlist
Download playlist by Spotify link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_playlistspo("Insert the Spotify link of the playlist to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
Download playlist from Deezer link
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_playlistdee("Insert the Deezer link of the playlist to download", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
### Download name
Download by name
```python
import deezloader
downloa = deezloader.Login("YOUR DEEZER EMAIL", "YOUR DEEZER PASSWORD", "YOUR ARL TOKEN DEEZER") #how get arl token https://www.youtube.com/watch?v=pWcG9T3WyYQ the video is not mine
downloa.download_name(artist="Eminem", song="Berzerk", output="SELECT THE PATH WHERE SAVE YOUR SONGS", quality="MP3_320", recursive_quality=True, recursive_download=True)
#check=False for not check if song already exist
#quality can be FLAC, MP3_320, MP3_256 or MP3_128
#recursive=False for download the song if quality seletecd chose doesn't exist
```
# Disclaimer
- I am not responsible for the usage of this program by other people.
- I do not recommend you doing this illegally or against Deezer's terms of service.
- This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
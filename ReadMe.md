#Spotify-At-Home
A small python project to automate installation of music from your favourite artists to mp3 from youtube music, e.g. for use on an MP3 player.

#How to use
Designed for mac/linux. 
Ensure you have a version of python 3 installed
First make the script executable < chmod +x run.sh
To download, modify run_scraper.py as needed with the necessary functions defined below, then run ./run_script.sh
Note that on Windows this probably won't work even in a bash terminal, so would probably require a rewrite as a .bat file.

#Useful Functions:
scrapeAristsWithSearch(artists)
Takes in list of artists and scrapes all of their albums. Probably the most useful individual function, however it can add a lot of bloat by adding unwanted albums. If you are worried about storage use downloadPlaylist and provide artist title

scrapeAristsWithUrls(artists, artist_urls)
Take in list of artist URLs and their names. Especially useful for obscure artists who may not show up with search.

downloadPlaylist(playlist_url, playlist_title=, artist_title=)
For when you need to download a custom playlist on YT Music. One of YT Music's best features is its plethora of unofficial music either made by small artists or just music unlikely to get licensed for use on Spotify. This allows you to download these playlists given their URL. 
There is the option to pass in a specific playlist name with playlist_title, otherise defaulting to the playlist's name on youtube. There is also the option to add it to a specific artist's folder with artist_title.

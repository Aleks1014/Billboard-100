# Billboard-100

## Introduction
Simple Python app that creates Spotify playlist with the top Billboard 100 songs for a given day. It's using BeautifulSoup to scrape the song titles and Spotify API to authenticate the user, find the songs, create the playlist, add the songs to it and change the playlist image cover. 
The date is chosen from a Tkinter calendar.

## Getting Started
- Clone the repository
- Install the needed packages (pip install -r requirements.txt)

## Getting API keys
### Open Weather
You need Spotify account for this app. If you don't have, you need to create one at http://spotify.com/signup/. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:
https://developer.spotify.com/dashboard/ . Create Spotify app and get the CLIENT_ID and CLIENT_SECRET and add them to you .env file. 
* Use http://example.com as your Redirect URI. It will return you an URL and you need to paste the URL into the prompt in the IDE. Now if you close your IDE and restart, you should see a new file in this project called token.txt


## Running the app
Once you run the app, a Tkinter window with a calendar will show up and ask you to choose a date in the past for your playlist. 
* Currently the app has the option to change the playlist cover once it's created, you need to add the image into the code at line 80 (sp.playlist_upload_cover_image). The image format should be Base64 encoded JPEG image data, maximum payload size is 256 KB.

## Room for development

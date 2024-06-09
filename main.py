from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
import environ
env = environ.Env()
environ.Env.read_env()

window = Tk()
window.geometry('400x400')
calendar = Calendar(window, selectmode='day')
calendar.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + calendar.get_date())
    window.destroy()

Button(window, text="Select Date",
       command=grad_date).pack(pady=20)

date = Label(window, text="")
date.pack(pady=20)


window.mainloop()

day = calendar.get_date()
date_obj = datetime.strptime(day, '%m/%d/%y')
requested_date = date_obj.date()

# requested_date = input('Which day would you like to travel to? Type the date in the format YYYY-MM-DD.: ')

CLIENT_ID = env('CLIENT_ID')
CLIENT_SECRET = env('CLIENT_SECRET')
url = f'https://www.billboard.com/charts/hot-100/{requested_date}'

page_data = requests.get(url).text
soup = BeautifulSoup(page_data, 'html.parser')
songs = soup.select('ul li ul li h3')
song_titles = [song.getText().strip() for song in songs]

# print(song_titles)


sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope='playlist-modify-private ugc-image-upload',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=env('username'),
        redirect_uri='http://example.com',
        cache_path='token.txt'
    )
)

user_id = sp.current_user()['id']

song_uris = []
for song in song_titles:
    result = sp.search(q=f'track:{song}', type='track')
    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'{song} was not found.')

# print(song_uris)

playlist = sp.user_playlist_create(
    user=user_id,
    name=f'{requested_date} Billboard 100',
    public=False,
    description='Billboard top 100 songs.'
)

sp.playlist_upload_cover_image(
    playlist_id=playlist['id'],
    image_b64='',
)

# print(playlist['id'])

sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=song_uris
)



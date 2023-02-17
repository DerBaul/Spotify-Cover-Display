import tkinter
import time
import requests
from tkinter import *
from pprint import pprint
import os
from PIL import ImageTk, Image  


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = #your token comes here

def get_current_track(acces_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers = {
            "Authorization": f"Bearer {acces_token}"
        }
    )
    resp_json = response.json()
    print(resp_json)
    album_pic_url = resp_json['item']['album']['images'][0]['url']
    pprint(album_pic_url)
    return album_pic_url
    
def main():
    window = Tk()
    window.title("COVER")
    window.configure(width=640, height=640)
    window.configure(bg="blue")
        
    while True:
        current_track_info = get_current_track(
            SPOTIFY_ACCESS_TOKEN
        )


        image1 = Image.open(requests.get(current_track_info, stream=True).raw)
        cover = ImageTk.PhotoImage(image1)

        labl1 = tkinter.Label(image=cover)
        labl1.image = cover

        labl1.place(x=0,y=0)
        window.update_idletasks()
        window.update()
        time.sleep(2)

if __name__ == '__main__':
    main()

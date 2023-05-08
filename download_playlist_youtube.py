from pytube import Playlist
from download_video_from_youtube import download_video


def get_list(url):
    try:
        links = Playlist(url)

        if links:
            for x in links:
                download_video(x)
        else:
            print("Error al descargar el video")
    except Exception as e:
        print(f"Ha ocurrido un error al descargar el video. Error {e}")

get_list("https://www.youtube.com/watch?v=E_s5GkzIm4A&list=PLdmCVpXQDH1ynn9O68hysmLU8D06zVJKs")
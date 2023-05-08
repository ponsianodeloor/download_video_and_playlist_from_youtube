from pytube import YouTube

def download_video(url):
    try:
        result = (
            YouTube(url)
            .streams.filter(progressive=True, file_extension="mp4", res="720p")
            .first()
            .download()
        )

        if result:
            print("Video descargado de manera exitosa")
        else:
            print("Error al descargar el video")
    except Exception as e:
        raise NameError(f"Ha ocurrido un error al descargar el video. Error {e}")


download_video("https://www.youtube.com/watch?v=rPytWpX9m04&list=PLdmCVpXQDH1zRfBDT3LtJDdzsPPjn2KzO")


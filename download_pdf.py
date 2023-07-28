import os
import requests
import io


def download(url):
    try:
        with requests.get(url, stream=True, timeout=5) as r:
            r.raise_for_status()
            file = io.BytesIO()
            for chunk in r.iter_content(chunk_size=8192): 
                file.write(chunk)
            file.seek(0)
        return file
    except Exception as e:
        print(e)
        print("Error downloading file")
        return

def download_pdf(url: str, file_name: str) -> None:
    # Download the PDF file if it doesn't exist
    if not os.path.exists(file_name):
        print("Downloading PDF")
        file = download(url)
        if file is not None:
            with open(file_name, "wb") as f:
                f.write(file.read())
            
        print("PDF downloaded")
    else:
        print("PDF already downloaded")
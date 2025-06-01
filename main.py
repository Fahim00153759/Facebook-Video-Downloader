from facebook_video_downloader import FacebookVideoDownloader
from config import API_URL

def main():
    downloader = FacebookVideoDownloader(API_URL)

    video_url = input("https://www.facebook.com/your_video_url")
    downloader.download_video(video_url)

if __name__ == "__main__":
    main()

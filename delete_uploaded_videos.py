# delete_uploaded_videos.py
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courage.settings")
django.setup()

from plumbing.models import Video

def delete_uploaded_videos():
    videos = Video.objects.all()
    for video in videos:
        if video.video_file and os.path.isfile(video.video_file.path):
            print(f"Deleting file: {video.video_file.path}")
            os.remove(video.video_file.path)
        else:
            print(f"File not found for: {video.title}")
        video.delete()
    print("All uploaded videos and records deleted.")

if __name__ == "__main__":
    delete_uploaded_videos()

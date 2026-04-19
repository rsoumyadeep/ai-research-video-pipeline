import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.http

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def upload_video(video_path, title, description):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    CLIENT_SECRET_PATH = os.path.join(BASE_DIR, "config", "client_secret.json")

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_PATH,
                                                                                SCOPES)

    
    credentials = flow.run_local_server(port=8080)

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["AI", "Machine Learning"],
                "categoryId": "28"
            },
            "status": {
                "privacyStatus": "private"  # change later to public
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(video_path)
    )

    response = request.execute()
    print("📺 Uploaded:", response["id"])
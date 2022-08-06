import googleapiclient.discovery
import pandas as pd

def get_video_id(video_url):

    return video_url.split('watch?v=')[1]

def get_comments(video_url):

    # API details and credentials
    youtube = googleapiclient.discovery.build(
        serviceName = "youtube", 
        version = "v3", 
        developerKey = "AIzaSyAVmaYn3dwMc3KEnqHX5FHdypUlXcoE-ss"
    )

    # define API request
    request = youtube.commentThreads().list(
        part = "snippet", 
        maxResults = 100, 
        videoId = get_video_id(video_url)
    )

    # get response
    response = request.execute()

    # return as pandas dataframe
    return pd.json_normalize(response["items"])

def get_channel_details(channel_id):

    pass
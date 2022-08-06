import googleapiclient.discovery
from credentials import API_KEY

# API details and credentials
youtube = googleapiclient.discovery.build(
    serviceName = "youtube", 
    version = "v3", 
    developerKey = API_KEY
)

def get_video_id(video_url):

    return video_url.split('watch?v=')[1]

def get_comments(video_url):

    # define API request
    request = youtube.commentThreads().list(
        part = "snippet", 
        maxResults = 100, 
        videoId = get_video_id(video_url)
    )

    # return response
    return request.execute()["items"]

def get_channel_details(channel_id):
  
    # define API request
    request = youtube.channels().list(
        part = "snippet",  
        id = channel_id
    )

    # return response
    return request.execute()["items"]
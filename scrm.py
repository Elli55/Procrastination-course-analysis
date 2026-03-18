import requests as rq

URL = 'https://www.googleapis.com/youtube/v3/search'
KEYWORD = 'Procrastination'
API =''
video_ids = []


params = {

    'part':'snippet',
    'q':KEYWORD,
    'type':'video',
    'maxResults':'50',
    'key':API
}


result = rq.get(URL, params=params).json()

for video in result['items']:
    video_ids.append(video['id']['videoId'])


URL_SECOND = 'https://www.googleapis.com/youtube/v3/videos'

params_second = {

    'part':'statistics',
    'id':','.join(video_ids),
    'key':API
}   

result_second = rq.get(URL_SECOND, params=params_second).json()

data_csv = []

for statistic in zip(result_second['items'], result['items']):
    data_csv.append(
        {
            'id':statistic[0]['id'],
            'title':statistic[1]['snippet']['title'],
            'description':statistic[1]['snippet']['description'],
            'views':statistic[0]['statistics']['viewCount'],
            'likesCount':statistic[0]['statistics']['likeCount'],
            'commentsCount':statistic[0]['statistics']['commentCount'],
            'publishedAt':statistic[1]['snippet']['publishedAt'],
            'channelTitle':statistic[1]['snippet']['channelTitle'],
            'URL':'https://www.youtube.com/watch?v=' + statistic[0]['id']
        }
    )


import pandas as pd


df = pd.DataFrame(data_csv)

df.to_csv('power_bi/poyoutube_statistic_Procrastination.csv', index=False)
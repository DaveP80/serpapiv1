from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd

def youtube_data():
    session1 = HTMLSession()
    

    search = "python no way there is a relevant video 666 is an evil number no chance"
    
    url = f"https://www.youtube.com/results?search_query={search}&sp=CAMSBggDEAEYAg%253D%253D"
    response = session1.get(url)
    video_results = []
    res_list = []
    count = 0
    # soup = BeautifulSoup(response.text)
    
    # soup= BeautifulSoup(response, 'lxml')
    
    response.html.render(sleep=1, keep_page = True, scrolldown = 1)

    for links in response.html.find('a#video-title'):
            link = next(iter(links.absolute_links))
            # description = str(soup.find('title'))
            videotitles = links.text
            video_results.append({link: videotitles})

    if len(video_results) == 0:
        print(f"no video results\n ")
        quit()

    for i in range(len(video_results)):
            if video_results[i] not in video_results[i + 1:]:
                res_list.append(video_results[i])
    for val in res_list:
            count += 1
            print(val)
            if count == 10:
                print(f"enjoy the video links\n ")
                quit()

youtube_data()

from requests_html import HTMLSession
import re
import runpy
from flask import Flask
import asyncio
import io


def youtube_scrape():
    count = 0
    if count==1:
        quit()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# request_json = request.get_json()
    if False:
        return request.args.get('message')
    elif False:
        return request_json['message']
    else:
        session1 = HTMLSession()
        url = "https://www.youtube.com/results?search_query=python+tutorial&sp=CAMSBggDEAEYAg%253D%253D"
        response = session1.get(url)
        
        video_results = []
        res_list = []
        count2 = 0
        stream.response.html.render()
        # return f'end of program'
        #response.html.render()
        session1.close
        for links in response.html.find('a#video-title'):
                link = next(iter(links.absolute_links))
                videotitles = links.text
                video_results.append({link: videotitles})
                if count2 == 10:
                    break;
                for var in video_results:
                    count2 += 1


        if len(video_results) == 0:
            count += 1
            return f'no video results'

        for i in range(len(video_results)):
                if video_results[i] not in video_results[i + 1:]:
                    res_list.append(video_results[i])
        # loop.close()
        print(res_list)
        count += 1
        return res_list
    
                # if count == 10:
                #     return f'enjoy the video links'
youtube_scrape()


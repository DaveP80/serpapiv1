from requests_html import HTMLSession

def youtube_scrape():
    session1 = HTMLSession()
    query_input = "example"
    url = f"https://www.youtube.com/results?search_query={query_input}&sp=CAMSBggDEAEYAg%253D%253D"

    response = session1.get(url)
    
    video_results = []
    res_list = []
    count = 0

    response.html.render()

    for links in response.html.find('a#video-title'):
            link = next(iter(links.absolute_links))
            videotitles = links.text
            video_results.append({link: videotitles})
            if count == 15:
                break;
            for var in video_results:
                count += 1

    if len(video_results) == 0:
        count += 1
        return f'no video results'

    for i in range(len(video_results)):
            if video_results[i] not in video_results[i + 1:]:
                res_list.append(video_results[i])
                res_list.reverse()
    print(res_list)
    print("enjoy the video links")

youtube_scrape()


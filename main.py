from requests_html import HTMLSession
import re
import runpy

def youtube_data():
    while True: 
        print(f"Welcome to video search, 5 most recent uploads.\n Type Java, Python or Javascript")
        lang = input("What's the programming language you want to learn? ")

        match lang:
            case "Javacript":
                search = input(f"you want to learn about {lang} input search term: ")
            case "javascript":
                search = input(f"you want to learn about {lang} input search term: ")

            case "Python":
                search = input(f"you want to learn about {lang} input search term: ")
            case "python":
                search = input(f"you want to learn about {lang} input search term: ")

            case "Java":
                search = input(f"you want to learn about {lang} input search term: ")
            case "java":
                search = input(f"you want to learn about {lang} input search term: ")
            case _:
                print(f"Please make a valid selection.\n")
                runpy.run_path('main.py', run_name='__main__')

        regex = rf"(?i){lang}(.*)"
        if re.match(regex, search):
            print(f"\n")
            runpy.run_path('main.py', run_name='__main__')
        session1 = HTMLSession()

        search_query = lang + " " + search

        url = f"https://www.youtube.com/results?search_query={search_query}&sp=CAMSBggDEAEYAg%253D%253D"
        response = session1.get(url)
        video_results = []
        res_list = []
        count = 0

        response.html.render(sleep=1, keep_page = True, scrolldown = 1)

        for links in response.html.find('a#video-title'):
                link = next(iter(links.absolute_links))
                videotitles = links.text
                video_results.append({link: videotitles})

        if len(video_results) == 0:
            print(f"no video results\n ")
            runpy.run_path('main.py', run_name='__main__')

        for i in range(len(video_results)):
                if video_results[i] not in video_results[i + 1:]:
                    res_list.append(video_results[i])
        for val in res_list:
                count += 1
                print(val)
                if count == 10:
                    print(f"enjoy the video links\n ")
                    runpy.run_path('main.py', run_name='__main__')
youtube_data()

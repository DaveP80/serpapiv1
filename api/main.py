from runpy import run_path
from serpapi import GoogleSearch
import re
import runpy

def youtubeScrape():

    while True:
        print(f"Welcome to video search, 5 most recent uploads.\n Type Java, Python or Javascript")
        lang = input("What's the programming language you want to learn? ")

        match lang:
            case "Javascript":
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
                print(f"Please enter a valid language and search query.\n")
                runpy.run_path('main.py', run_name='__main__')

        regex = rf"(?i){lang}(.*)"
        if re.match(regex, search):
            print(f"\n")
            runpy.run_path('main.py', run_name='__main__')
        params = {
        "engine": "youtube",
        "sp": "CAMSBggDEAEYAg%253D%253D",
        "search_query": lang + " " + search,
        "api_key": "d91009efe6efd4d9456cafc777cd93a5f29ce3530558854a91f8e272f4ffeacd"
        }

        search = GoogleSearch(params)
        video_results = []
        res_list = []
        count = 0
        print(params.get("search_query"))

        results = search.get_dict()

        for result in results.get("video_results", []):

            video_results.append({"title": result.get("title")})
            video_results.append({"link": result.get("link")})
            
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
youtubeScrape()
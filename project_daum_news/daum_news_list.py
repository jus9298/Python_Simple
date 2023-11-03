# 다음 실시간 뉴스 목록 (15개) 기사 [제목, 본문, 날짜] 수집기

import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

count = 0  #수집 된 전체기사 수
url = "https://news.daum.net/breakingnews/digital"
result = requests.get(url)

# 예외처리
if result.status_code == 200:
    print("URL 접속 성공 -> 데이터를 수집합니다.")
    doc = BeautifulSoup(result.text, "html.parser")
    # url_list = doc.select("a.link_txt") #15개만 가져올거임
    url_list = doc.select("ul.list_news2 a.link_txt") #자손. 언더바로. >아님.
    # print(len(url_list))

    for url in url_list:
        count += 1
        print(f"{count}.", "="*100)
        get_news(url["href"]) #함수화
        # print(url["href"]) #태그 안의 txt 말고 속성 필요.
else:
    print("잘못된 URL 경로입니다. 다시 한 번 확인해주세요.")


print(result)

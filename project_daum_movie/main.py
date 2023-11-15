# 2. 실시간(코드) 다운로드

import math
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Selenium 전용 웹 브라우저 구동
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# 2. URL 접속
url = "https://movie.daum.net/moviedb/main?movieId=165591"
driver.get(url)
time.sleep(2)

# 3. 페이지 전체 코드 가져오기
doc_html = driver.page_source
# print(doc_html)

# 4. Selenium -> BeautifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5. 영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
# print(movie_title)
print("="*100)
print(f"= 영화 제목: {movie_title}")
print("="*100)

# 6. 전체 리뷰 출력("평점 더보기" 클릭)
#     - 다음 영화 최초 페이지 -> 10개
#     - "평점 더보기" 클릭 -> 30개
#     - "평점 더보기" 몇 번 클릭? -> 전체 리뷰 출력
#
#     ex) 전체 리뷰: 187개
#     올림((187 - 10) / 30) = 6

# 6-1. 전체 리뷰 수집
total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
print(total_review_cnt)

# 6-2. 전체 리뷰에서 숫자만 추출
#     - 문자열 슬라이싱
#     예) (187명)
# print(total_review_cnt[1:-2])
#     - 정규식 -> 숫자만 추출
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# 6-3. "평점 더보기" 클릭 횟수 계산(모든 리뷰 출력)
click_cnt = math.ceil((num_review - 10) / 30)

# 7. Selenium을 통해서 "평점 더보기" 클릭
for i in range(click_cnt):
    # "평점 더보기" 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)

# 8. 전체 소스코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("")
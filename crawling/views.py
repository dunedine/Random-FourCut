from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlretrieve
import os
import base64
import random

def crawling(request):
    search = request.GET.get('word')
    if search is None:
        return render(request, 'crawling.html')
    else:
        # ChromeDriver 설정 및 크롤링
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 브라우저를 띄우지 않고 실행
        chrome_options.add_argument("--no-sandbox")  # 리눅스에서 권한 문제 방지
        chrome_options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 사용 비활성화
        chrome_options.add_argument("--disable-gpu")  # GPU 사용 비활성화 (headless 모드 이슈 해결)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        url = "https://www.google.co.kr/imghp?hl=ko&ogbl"
        driver.get(url)
        elem = driver.find_element(By.NAME, 'q')
        elem.send_keys(search)
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(3)  # 페이지 로딩 대기
        
        # 이미지 저장 디렉토리 설정
        img_dir = './crawling/static/img/'
        os.makedirs(img_dir, exist_ok=True)

        # 이미지 크롤링 및 저장
        images = driver.find_elements(By.CSS_SELECTOR, 'img')
        cnt = 1
        for image in images:
            src = image.get_attribute('src')
            if src and src.startswith('data:image/jpeg;base64,'):
                # Base64 데이터 처리
                base64_data = src.split(',')[1]  # base64 데이터 부분만 가져오기
                img_data = base64.b64decode(base64_data)
                with open(f'{img_dir}/{cnt}.jpg', 'wb') as f:
                    f.write(img_data)
                cnt += 1
            elif src and src.startswith('http'):  # 일반 URL 형식 이미지
                try:
                    urlretrieve(src, f'{img_dir}/{cnt}.jpg')
                    cnt += 1
                except Exception as e:
                    print(f"Error downloading image {cnt}: {e}")
            if cnt > 10:  # 원하는 이미지 개수로 제한
                break

        driver.quit()  # 드라이버 종료

        # 이미지 파일 목록 가져오기
        img_list = os.listdir(img_dir)

        # 리스트가 비어 있거나 이미지가 4개 미만일 경우 예외 처리
        if len(img_list) == 0:
            # 이미지가 없는 경우 처리
            return render(request, 'error.html', {'error': '이미지를 찾을 수 없습니다.'})
        elif len(img_list) < 4:
            selected_imgs = img_list  # 이미지가 4개 미만이면 전체 리스트 사용
        else:
            selected_imgs = random.sample(img_list, 4)  # 네 장의 이미지를 랜덤하게 선택

        # 선택된 이미지 파일명을 컨텍스트로 전달
        contents = {'images': selected_imgs}
        return render(request, 'cone.html', contents)

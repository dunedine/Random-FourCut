# 랜덤네컷 - 검색어기반 랜덤 네컷 추출 🖨️ 
![서비스 이미지](https://github.com/dunedine/Random-FourCut/blob/main/서비스이미지.GIF)

## 프로젝트 소개
### 개요
- 사용자가 입력한 검색어를 기반으로 웹에서 이미지를 검색하여 무작위로 4장의 이미지를 보여주는 서비스입니다.
- 기획 의도: 네컷사진이 활성화된 트렌드에 맞춰 사용자에게 특정 검색어에 대한 랜덤한 네컷을 제공하는 서비스를 제공하자
- 개발기간: 2023.03.23 - 2023.03.25
### 타겟
- 특정 검색어에 대한 다양한 이미지를 손쉽게 보고 싶은 사용자
- 이미지 검색 및 수집을 자동화하고 싶은 사용자
<br>

## 프로젝트 진행 기간
- 2023.03.23-2023.03.25
<br>

## 개발 환경
- Back-end: Django, Selenium, Python
- Front-end: HTML, CSS, JavaScript
- DB: 사용하지 않음 (이미지 크롤링을 통한 저장 방식)
<br>

## 기능 소개
- 이미지 검색: 사용자가 입력한 검색어를 기반으로 이미지를 검색합니다.
- 이미지 랜덤 선택 및 다운로드: 검색된 이미지 중에서 무작위로 4장의 이미지를 선택하고, 선택된 이미지를 다운로드하여 로컬 서버에 저장합니다.
- 이미지 출력: 저장된 이미지를 HTML 페이지에서 출력하여 사용자에게 제공합니다.
<br>

## 화면 구현
메인 화면: 검색어 입력 및 이미지 검색 버튼 제공
결과 화면: 무작위로 선택된 4장의 이미지를 출력
<br>

## 프로젝트 구조도

```plaintext
📦 myproject
 ┣ 📂 config
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 asgi.py
 ┃ ┣ 📜 settings.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 wsgi.py
 ┣ 📂 crawling
 ┃ ┣ 📂 migrations
 ┃ ┣ 📂 static
 ┃ ┃ ┗ 📂 img
 ┃ ┣ 📂 templates
 ┃ ┃ ┣ 📜 crawling.html
 ┃ ┃ ┗ 📜 cone.html
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 tests.py
 ┃ ┗ 📜 views.py
 ┣ 📂 venv
 ┃ ┣ 📂 Include
 ┃ ┣ 📂 Lib
 ┃ ┗ 📂 Scripts
 ┣ 📜 manage.py
 ┗ 📜 README.md

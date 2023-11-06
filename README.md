# Maple Diary
- 넥슨에서 운영중인 게임 [메이플스토리](https://maplestory.nexon.com/Home/Main)를 플레이하며 본인의 이야기를 공유하는 서비스

___
# 1. 프로젝트 소개
  
## 개발 기간
2023.10.25 ~ 2023.11.06

## 역할
고동우: 서비스 기획 및 구현

## 설명
- 글 작성, 수정, 삭제, 조회 등 블로그의 기본적인 기능을 기반으로 둔 커뮤니티 서비스 
- 강화 아이템 '큐브' 사용기록을 공식에서 제공하는 API를 통해 기록을 확인하거나 게시글에 작성하여 공유 가능
- 사용자는 본인의 프로필 작성, 댓글 및 대댓글 작성 가능
___


# 2. 개발 환경
## 사용언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
<br>
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

## 에디터
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

# 3. DB
[dbDiagram](https://dbdiagram.io/d/Maple-Diary-6538d350ffbf5169f068db08)
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/2ffdb5bf-b7e6-45d1-b0d0-1eca3e01a652)



# 4. WBS
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/8d16b0cf-79e2-41ff-ad1f-8ed63daabac6)
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/fbe71c81-12f8-43c5-896b-152d08c7aeb3)



# 5. 아키텍처

## 프로젝트 구조
___
```📦TodayWatch
 ┣ 📂css
 ┃ ┣ 📜common.css
 ┃ ┣ 📜function.css
 ┃ ┣ 📜list.css
 ┃ ┣ 📜login.css
 ┃ ┗ 📜view.css
 ┣ 📂fonts
 ┃ ┣ 📜Jua-Regular.ttf
 ┃ ┗ 📜OFL.txt
 ┣ 📂js
 ┃ ┣ 📜api.js
 ┃ ┗ 📜control.js
 ┣ 📂resource
 ┃ ┣ 📜felix-mooneeram-evlkOfkQ5rE-unsplash.jpg
 ┃ ┣ 📜loading.gif
 ┃ ┣ 📜리얼_포스터.jpg
 ┃ ┣ 📜멜로가체질_포스터.jpg
 ┃ ┣ 📜바닐라스카이_포스터.jpg
 ┃ ┣ 📜사람 아이콘.png
 ┃ ┣ 📜직접검색.gif
 ┃ ┗ 📜커뮤니티.gif
 ┣ 📜index.html
 ┗ 📜README.md
```

## 시스템 아키텍처
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/bdef7f1c-fd2c-4b1c-adc3-f153f69279cc)


## 배포
GitHub Pages
- [오늘은 뭐 볼까?](https://ko-udon.github.io/TodayWatch/)


___
# 6. URL 및 요구사항 분석

## 목업 페이지

## url 구조

## 기능 설계 
![image](https://github.com/Ko-udon/TodayWatch/assets/79897135/b46115dc-1e54-4484-a3ae-a1ddce462029)


(기능 목록)
- 로그인/로그아웃의 경우, 현제 서버에 유저 정보를 저장할 수 없기 때문에 기본적인 기능만 구현
- 커뮤니티 기능은 글 조회가 가능하게끔 뼈대만 맞추고 게시글 작성같은 기능은 생략


## 목업 페이지
[목업 페이지 이동](https://ovenapp.io/view/jEy2OwO4tz6mrygT4mDOLtEDxuMEzGEE/)
![image](https://github.com/Ko-udon/ormi_project1/assets/79897135/d25810f4-53b5-45c7-9635-7b76602f78f4)

___

# 7. 구현



___
# 8. 리소스 출처
- bootstrap 템플릿: https://startbootstrap.com/template/blog-home
- maplestory 배경화면 및 favicon: https://m.maplestory.nexon.com/Media/MobileWallPaper

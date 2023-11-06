# [Maple Diary](http://43.202.121.54:8000/)
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
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/2ffdb5bf-b7e6-45d1-b0d0-1eca3e01a652)
<br>
[dbDiagram](https://dbdiagram.io/d/Maple-Diary-6538d350ffbf5169f068db08)


# 4. WBS
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/8d16b0cf-79e2-41ff-ad1f-8ed63daabac6)
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/fbe71c81-12f8-43c5-896b-152d08c7aeb3)



# 5. 아키텍처

## 프로젝트 구조
___
```
📦MINIPROJECT_BLOG
 ┣ 📂blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂maple_diary
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┣ 📂blog
 ┃ ┗ 📂UserCharacter
 ┣ 📂static
 ┃ ┣ 📂assets
 ┃ ┃ ┣ 📜artwork_111.jpg
 ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┣ 📜main_bg.jpg
 ┃ ┃ ┣ 📜maple-favicon.ico
 ┃ ┃ ┣ 📜maple-favicon.png
 ┃ ┃ ┗ 📜No_img.png
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┗ 📜index.html
 ┣ 📂templates
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜blog.html
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┗ 📜post_list.html
 ┃ ┣ 📂user
 ┃ ┃ ┣ 📜cube_history.html
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┗ 📜profile_detail.html
 ┃ ┣ 📜404.html
 ┃ ┣ 📜500.html
 ┃ ┗ 📜main.html
 ┣ 📂user
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂venv
 ┃ ┣ 📂Include
 ┃ ┣ 📂Lib
 ┃ ┣ 📂Scripts
 ┃ ┗ 📜pyvenv.cfg
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

## 시스템 아키텍처
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/bdef7f1c-fd2c-4b1c-adc3-f153f69279cc)


___
# 6. URL 구조 및 목업

## url 구조
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/05546909-05e9-4450-9de1-f54dd0ce4903)

![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/b4511e21-2c77-4a53-a74f-9e1192bfaa4d)

## 기능설계
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/be00de58-47e8-44ed-b2fc-3d2dac55cf8f)


## 목업 페이지
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/6cf4b55d-5332-4f16-b7a7-5364dfb069be)
<br>
[목업 페이지 이동](https://ovenapp.io/project/AuTOhRVaWIshS0Pz6F2esakzUYXEwo0H#wWD2p)


___

# 7. 구현
## 공통
### 없는 페이지에 접근시 '잘못된 접근입니다' 라는 문구가 뜨는 페이지로 이동 (500)
![404-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/e1f5982a-e363-4263-b65f-e5601ebffd51)

### 없는 게시글에 접근시 '존재하지 않는 게시글입니다' 라는 문구가 뜨는 페이지로 이동 (404)
![500-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/a173dea1-0d56-487a-ac85-c55e8835d17a)


### 반응형 페이지
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/38c3ed9d-f517-455d-a494-042b48506264)
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/4bc91f74-0044-4831-85b7-e4dfd2f34ce3)

___

## 사용자
### 회원가입
- 아이디와 비밀번호로 회원가입 가능
- 회원가입에 성공하면 자동으로 로그인 되어 프로필 작성 페이지로 이동
![회원가입-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/f3d28cee-2888-44ed-9500-5e0a7809fa0c)

### 프로필
- 닉네임, 게임을 플레이 중인 서버를 선택, 캐릭터 이미지, 자기소개, api 키를 작성함
- 캐릭터 이미지와 api키는 작성하지 않아도 됨
- 프로필은 수정 가능

![프로필 수정수정-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/f1b14ff5-d119-4245-b967-cecc377063d7)


### 로그인/로그아웃
![로그인_로그아웃-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/926ed3f9-e07b-4a78-a243-c621426c342e)

## API
- 넥슨게임 '메이플스토리'에서 공식으로 제공하는 API를 활용
- 게임 아이템을 강화하는 '큐브'를 사용한 기록을 조회
- 키를 등록한 사용자들은 날짜를 선택해 그날 강화한 아이템 기록을 볼 수 있음
- 복사 버튼을 눌러 강화 기록을 클립보드에 저장해 글 작성시 붙여넣기 할 수 있음(현재 복사기능은 로컬에서만 가능,,,)
- 키를 등록하지 않은 사용자들은 이용 불가
![api-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/979bbfae-4192-4fdc-b00f-730ce111b6e0)

___

## 블로그
### 글 작성
- 글쓰기 링크로 이동하여 작성 가능
->  공개/비공개 여부 선택, 글 제목, 이미지, 글 내용, 태그(여러개 선택 가능)로 작성가능
![글작성-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/1d41abc7-b102-4a8e-a8c9-afe759804612)
<br>
- 작성된 글은 작성자만이 수정 및 삭제 가능



### 글 조회
- 게시글 제목으로 검색
-> 글 제목에 포함된 내용으로 글 조회
![image](https://github.com/Ko-udon/miniproject_blog/assets/79897135/aad0302e-b181-4a84-bc28-600ef1386fd8)

<br>

- 태그로 검색
-> 해당 태그로 작성한 게시글 조회
![태그검색-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/268f8d9b-196d-4144-b488-d855f59089ce)


### 글 상세
- 작성날짜, 작성자, 조회수, 태그, 이미지, 글 내용으로 구성된 상세 페이지로 이동
![글상세조회-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/2fede186-f41b-423c-81c4-654195bda332)
<br>
- 작성글에 있는 태그를 클릭하여 태그로 게시글 검색으로 바로 이동 가능
![게시글에서 바로 태그검색-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/6e4a5a6b-9a77-46a4-b575-a44a7b463b5d)

### 글 편집
- 수정과 편집은 모두 작성자만 가능
- 글 수정
![글 수정-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/cbb50785-d5d3-495f-b6a3-4547d3f9cb43)
<br>
- 글 삭제
![글 삭제 - gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/c45740e1-7aea-4ebf-a1e7-0a09f72affa8)


### 댓글
- 로그인한 사용자들은 게시글 하단에 댓글 작성 가능
- 댓글은 작성자: 작성날짜, 내용 으로 구성하여 출력
![댓글작성-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/1301fe32-b4fa-46d6-873d-a687dd83ba14)
<br>
- 로그인하지 않은 사용자들은 댓글 작성 불가능, 글 조회만 가능
![비로그인댓글불가-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/571ae5b1-4865-4bdb-8bdf-e8eed5376f12)


### 대댓글
- 작성된 댓글 밑에 대댓글 작성 가능
- 대댓글은 댓글 밑에 ㄴ 표시 밑에 작성자: 작성날짜, 내용 으로 구성하여 출력
![대댓글-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/15e64dcb-1035-4581-9740-9aceab3f17d5)


### 비공개 글
- 게시글 제목 뒤에 by (닉네임) 으로 표시 
- 비공개 글은 댓글 사용 불가
- 작성자만 상세 페이지 조회 가능
![비공개글-gif](https://github.com/Ko-udon/TodayWatch/assets/79897135/181e2e7e-6b7a-4921-aab2-d75cbea03aab)

- 작성자가 아닌 사람은 상세 페이지 조회 불가능
![비공개글-조회불가능](https://github.com/Ko-udon/TodayWatch/assets/79897135/380f7ee0-7009-4e6c-a636-3bfb13086051)





___
# 8. 리소스 출처
- bootstrap 템플릿: https://startbootstrap.com/template/blog-home
- maplestory 배경화면 및 favicon: https://m.maplestory.nexon.com/Media/MobileWallPaper

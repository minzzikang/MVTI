# Django와 Vue.js를 활용한 영화 추천 서비스 설계

### :calendar: 일시 : 2023.11.16.(목) ~ 2023.11.23.(목)  

### :star: 팀원
| 이름 | 역할 |
| ---- | ---- |
| 강민지 | - 프론트엔드 중심<br>- 백엔드 데이터 받아서 프론트엔드 기능 구현, CSS |
| 김민욱 | - 백엔드 중심<br>- DB 모델링, API 서버 데이터 받아오기 |

### :pushpin: 목표
- TMDB API와 Youtube API를 활용한 영화 추천 서비스 구성
- 사용자의 MBTI, 나이 등 사용자 입력 데이터 기반 및 현재 날짜 기준 추천 알고리즘 설계

### :love_letter: 설치 안내
서비스 사용을 위해 아래의 방법으로 실행합니다.
레퍼지토리를 clone 받습니다.
#### [BACK-END]
1. final-pjt-back 폴더에 필요한 프로그램을 설치합니다.
```
pip install -r requirements.txt
```
2. 서버 실행 전 필요한 데이터를 받습니다.
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata datas.json
```
3. 설치 완료 후, 백엔드 서버를 실행합니다.
```
python manage.py runserver
```
#### [FRONT-END]
1. final-pjt-front/mvti-service 폴더에서 package.json에 정의된 패키지 및 모듈을 설치합니다.
```
npm install
```
2. 설치 완료 후, 프론트엔드 서버를 실행합니다.
```
npm run dev
```

### :hammer: 기술 스택
#### FRONT-END
    - Vue 3
    - JavaScript
    - HTML, CSS
    - BootStrap

#### BACK-END
    - Python
    - Django
    - TMDB API
    - YOUTUBE API

### :thumbsup: 기능 소개
| 구분 | 기능 | 설명 | 담당 |
| --- | ----- | ---- | -- |
| 회원 | - 회원가입<br>- 로그인<br>- 로그아웃 |  | 강민지, 김민욱 |
| 영화 정보 | - TMDB API 활용<br>- 영화 포스터, 개봉일, 장르, 감독, 줄거리, 출연 배우, TMDB 평균 평점 등 조회|  | 김민욱 |
| 영화 평점 | 영화별 평점 및 한 줄 리뷰 등록 |  | 강민지 |
| 영화 추천 | 영화 추천 알고리즘 | - 사용자 정보(mbti, 나이)에 따른 추천<br>- 현재 날짜 기준 추천| 김민욱 |
| 커뮤니티 | 게시글 | - 게시글 조회 및 작성, 수정, 삭제<br>- 게시글 좋아요 | 강민지 |
| 커뮤니티 | 댓글 | 댓글 작성, 수정, 삭제 | 강민지 |
| 유저페이지 | 사용자 | - 좋아요한 영화 조회<br>- 평점 남긴 영화 조회<br>- 좋아요한 게시글 조회<br>- 댓글 남긴 게시글 조회 | 김민욱 |

### :closed_book: 데이터베이스 모델링 (ERD)
![erd](ERD.png)

### :green_book: 컴포넌트 구조
![component](컴포넌트 관계.png)

### :boom: 이슈 관리
| 날짜 | 담당자 | 내용 | 해결 방법(원인) |
| --- | ----- | ---- | -------------- |
|     |       |      |                |

### :thought_balloon: 느낀점
#### 강민지

#### 김민욱

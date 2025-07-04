# django-youtube-restapi

## (1) Project Settings

- Github


## Docker란?

- 컨테이너 기반의 가상화 플랫폼으로, 애플리케이션을 컨테이너라는 격리된 환경에서 실행할 수 있게 해주는 도구.

## Docker 구성요소

- Docker Engine
- Docker Image
- Docker Container
- Dockerfile
- Docker Hub

## Docker Image 와 Docker Container 

- Docker Image
    탬플릿 역할을 하며 레이어 구조로 효율적인 저장이 가능.

- Docker Container
    상태가 변경 가능하며 생성, 시작, 중지, 삭제가 가능.

## Model 구조 -> ORM 

(1) User => users
- email
- password
- nickname
- is_business

(2) Video => videos
- title
- description
- link
- view_count
- thumbnail
- video_file
- User : FK

ex) 파일 (이미지, 동영상) 
=> 장고에 부하가 걸림
=> S3 Bucket(저렴, 속도가 빠름) -> 결과물 : 링크

(3) Reaction => reactions
- User: FK
- Video: FK
- reaction ( like, dislike, cancel) => 실제 youtube rest api

(4) Comment => comments
- User: Fk
- Video: FK
- content
- like
- dislike

(5) Subscription subscriptions
- User : FK => subscriber (내가 구독한 사람)
- User : FK => subscribed_to (나를 구독한 사람)

(6) Common => common
- created_at
- updated_at


모델을 먼저 정의한 이유는 DB migration (테이블 구조 정의) => REST API
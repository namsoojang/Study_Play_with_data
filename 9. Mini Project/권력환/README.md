# Mini project - Github Repository Crawler 

## Purpose 
- 특정 query와 연관된 github repository 정보를 수집하여, 다양한 관점에서 분석해보자.

## Todo List
- github api 내용을 살펴보자. 
  - [https://developer.github.com/v3/](https://developer.github.com/v3/)
- 예시로, github에 올라와있는 pytorch 관련 repo 정보를 모아보자.
- repo 소개글을 보고 유사한 repo끼리 그룹핑해보자.
  - 그룹핑 기준: tutorial / pytorch application / wrapping 등
- 각 그룹별 특징을 분석해보자.
  - 분석 주제: TBD
- 분석에 불필요한 repo는 제외하자. 
  - 제외 기준: 업데이트 주기, star 갯수 등

## Progress
- 2017.11.30(목)
  - github api를 통해 검색결과 가져오기
  - 검색결과 중 향후 사용할 필드 정보만 남기기 
  - 추가 필드정보 추출하기

## Code Repository
- [https://github.com/vics-kwon/github_repo_crawler](https://github.com/vics-kwon/github_repo_crawler)
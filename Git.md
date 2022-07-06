# Git (분산 버전 관리 시스템)

`기본 적인 구성은 Working Directory, Staging Area, Repository 로 구분 되어 있음.`

## 개요

#### 1. Working Directory

- **파일의 변경 사항(처음)**

#### 2. Staging Area

- **임시서버, 임시적인 공간(중간)**

#### 3. Repository

- **커밋(버전)들이 기록 되는곳(최종)**



## Git 사용 방법

#### 처음 이메일 및 닉네임 설정 방법

```base
git config --global user.name 'GitHub ID'

git config --global user.email 'GitHub Email'
```

---

#### git 용어 설명

1. `git init` : **git 접속**

2. `git add 파일명` : **WD에서 SA로 보낼 때 사용**

3. `git commit -m '커밋메세지'` : **무슨 일을 했는 지 남기는 곳**

> git commit 을 친 후 엔터를 누르면 커밋메세지를 많이 남길 수 있음.

4. `git status` : **현재 파일들의 위치를 확인할 때 사용**

5. `git .` : **폴더 안 모든 파일 추가**

6. `git log` : **무슨 일을 했는지 확인 할 때 사용**

7. `git log -원하는 숫자` : **최근 작업 숫자 적은 만큼 표시**

8. `git log --oneline` : **1줄로 보기**

- 예) `git log -2 --oneline` : 최근 작업 2개를 1줄로 보여줘

9. `git remote add origin GitHub 주소` : **원격 저장소에 추가해줘 오리진이란 이름으로 내 주소를 **
10. `git remote -v` : **원격 저장소 주소 확인**
11. `git push origin master` : **보내기**
12. `git pull origin master` : **받기**

#### 설정 확인

- `git config -l, git config --global -l, git config user.name(등록한 아이디 확인)`

  > 아직 뜨는 메세지가 무엇을 의미하는 지는 잘 모름.



#### 유의 사항

- **빈 폴더는 Status 에 표시 X**

  -  만약 작업이 대기 중인 빈 폴더이면 관용적으로 **.gitkepp** 이란 파일을 만든다.

- **명령어에 ctrl + c 하면 실수 했을 시 그냥 넘어 갈 수 있다.**

- **폴더 안에 있는 파일을 add 하고 싶지 않을 때 .gitignore 을 생성 뒤 그 안에 파일 이름 넣으면 깃으로 부터 숨길수 있음! 폴더는 /폴더이름**

  - > 모든 .txt 파일을 숨기고 싶을 시 *.txt 로 설정해두면 모든 .txt 파일이 숨겨짐.
# Git (분산 버전 관리 시스템)

`기본 적인 구성은 Working Directory, Staging Area, Repository 로 구분 되어 있음.`



## 목차

- ### 개요

- ### Git 사용 방법

---

### 개요



#### 1. Working Directory

- **파일의 변경 사항(처음)**

#### 2. Staging Area

- **임시서버, 임시적인 공간(중간)**

#### 3. Repository

- **커밋(버전)들이 기록 되는곳(최종)**

---



### Git 사용 방법

#### 처음 이메일 및 닉네임 설정 방법

```base
git config --global user.name 'GitHub ID'

git config --global user.email 'GitHub Email'
```
---

- ####  git 기본 용어 설명

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
12. `git restore --staged 파일이름` : **add 제외**
12. `git restore 파일이름` : **되돌리기**

---

- #### git branch 용어 설명

1. `git clone 상대 깃 허브 주소` : **내 컴퓨터에 클론 만드는 방법**
2. `git branch 이름` : **브랜치 생성 방법**
3. `git branch` : **브랜치 조회**
4. `git checkout 이름` : **이름 이라는 브랜치로 이동**
5. `git checkout -b 이름` : **이름 이라는 브랜치 생성 뒤 바로 이동**
6. `git merge 브랜치이름` : **브랜치이름과 master가 병합**
6. `git branch -d 브랜치이름` : **브랜치 삭제**

---

- #### 설정 확인

- `git config -l, git config --global -l, git config user.name(등록한 아이디 확인)`

  > 아직 뜨는 메세지가 무엇을 의미하는 지는 잘 모름.

---

- #### 유의 사항

  - **빈 폴더는 Status 에 표시 X**
  - 만약 작업이 대기 중인 빈 폴더이면 관용적으로 **.gitkepp** 이란 파일을 만든다.
  - **명령어에 ctrl + c 하면 실수 했을 시 그냥 넘어 갈 수 있다.**
  - **폴더 안에 있는 파일을 add 하고 싶지 않을 때 .gitignore 을 생성 뒤 그 안에 파일 이름 넣으면 깃으로 부터 숨길수 있음! 폴더는 /폴더이름**
  - 브랜치를 사용 한 뒤에는 의미가 없으므로 **브랜치 삭제!**

  > 모든 .txt 파일을 숨기고 싶을 시 *.txt 로 설정해두면 모든 .txt 파일이 숨겨짐.

- #### Feature Branch Workflow (소유권이 있는 경우)

  - **소유권이 있는 상태의 경우**
    - `git checkout -b 브랜치 이름 > 파일 git add . > git commit -m 하고 브랜치 상태에서 > git push origin 브랜치이름 > Github 사이트에서 branch 와 merge가 가능하다. Pull requests. 창에서 확인.`

- #### Forking Workflow (소유권이 없는 경우)

  - **소유권이 없는 경우**
    - `상대 Github에 들어가서 Fork를 누른 뒤, 내 주소로 들어가서 주소를 복사 한 뒤 클론을 생성한다.
      git clone 주소 > 수정이나 파일을 생성 뒤, git add . > git commit -m > git push origin (파란괄호안에 명령어) > 주소 들어가서 Pull requests 요청`
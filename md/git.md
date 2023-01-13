# Git과 Github의 차이점



### 버전 관리

- 버전 관리란 시간에 따라 파일의 변경 사항을 추적하고 기록하는 것.

  버전 관리 시스템은 이전 버전으로 복구하거나 조회할 수 있는 기능을 제공

  버전 관리는 프로젝트의 수정이 있을 때마다 snapshot을 찍기때문에, 필요한 것을 복구하거나 비교할 때 다양한 버전들을 확인할 수 있음.



### Git

- Git은 **'본인'** 컴퓨터에서 돌아가는 Version Control System
  - 계정을 등록할 필요도 없고, 인터넷을 연결할 필요도 없다.



### Github

- Github라 불리는 회사에서 서비스하고 있는 서버에 올라간 Git
  - 개인 계정을 등록해야 하며, 인터넷에 연결되어야 사용할 수 있다.



- 즉, Github는 Git 소프트웨어를 지원하는 일종의 클라우드 서비스



### Local Git과 Remote Git

- 개인 컴퓨터에서 사용하는 Git을 Local Git이라 부르며, Github나 Gitlab과 같은 클라우드에

  저장하는 Git을 Remote Git이라 부른다. 로컬에 저장되는 Git은 공유가 되지 않으며,

  공유를 위해서는 Remote Git 서비스를 제공하는 Github나 Gitlab에 올려야한다.



### UI를 지원하는 Github

- Local Git은 기본적으로 터미널을 사용한다. 따라서 Local Git은 File Managing을 위해 UI 요소가 지원되지 않는다.

  반대로 Github는 Git을 터미널로 이용할 수 있는 방식 뿐만 아니라, github.com 사이트를 통해 UI적으로 사용할 수 있도록 돕는다.

> 로컬 Git을 시각적으로 조작할 수 있는 서비스를 제공하는 IDE들이 존재 하긴 함. Git에서 자체적으로 제공하는 것이 아닌 외부 IDE가 제공하는 것.



### PR 기능을 지원하는 Github

- PR이란 Pull Request의 약자로 특정 코드 버전에 코드를 통합할 수 있도록 다른 개발자들에게 리뷰를 요청하는 기능.

  Git에는 기본적으로 PR기능이 없으며, PR 기능은 코드 리뷰를 돕기 위해 Github에서 만들어낸 기능.

  같은 기능으로 Gitlab의 MR(Merge Request) 기능 등이 있음.

  

### Github의 다양한 기능들

- Git 자체는 코드의 버전 관리를 위한 시스템이지만, Git 위에 CI/CD를 강화하기 위해 Git Action 과 같은 자동 빌드 및 배포 기능, 프로젝트 매니징을 위한 칸반 보드 기능 등을 넣었다.

  따라서 Github는 Git을 서비스하지만 추가적인 여러 기능들을 지원하는 시스템이라 보는 것이 맞음.





-출처-

[너도 나도 함께 성장하자](https://escapefromcoding.tistory.com/)

[Kotlin World](https://kotlinworld.com/)


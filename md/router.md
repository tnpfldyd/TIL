# Router 란?

- 지능을 가진 경로 배정기
  - 자신이 가야 할 길을 자동으로 찾아서 갈 수 있는 능력을 가진 것



### 라우터의 하는 일

- Path Determintation(경로 결정)
  - 데이터 패킷이 목적지까지 갈 수 있는 길을 검사하고 어떤 길로 가는 것이 가장 적절한지 결정
  - 라우팅 알고리즘(라우팅 프로토콜)이 사용된다 - 가장 좋은 길을 찾는 방법
    - 라우팅 테이블이란 것을 만들어서 관리
    - 라우팅 테이블에는 어디로 가려면 어떻게 가라는 지도 정보가 들어있다.
    - 라우팅 프로토콜에는 RIP(Routing Information Protocol), IRGP(Interior Gatway Routing Protocol), OSPF(Open Shortes Path First), EIGRP(Enhanced Interior Gateway Routing Protocol) 등이 있다.
- Switching
  - 경로가 결정되면 그쪽으로 데이터 패킷을 스위칭한다



### 라우팅 프로토콜과 라우티드 프로토콜

- TCP/IP와 IPX, AppleTalk 등 우리가 아는 모든 프로토콜은 전부 라우티드 프로토콜
- 라우티드 프로토콜이란 말 그대로 라우팅을 당하는, 즉 라우터가 라우팅을 해주는 고객을 뜻한다.



### AS, 내부용 과 외부용 라우팅 프로토콜

- AS는 'Autonomous System'의 약자로, 하나의 네트워크 관리자에 의해서 관리되는 라우터들의 집단

- AS 안에서는 Interior Routing Protocol, 즉 내부용 라우팅 프로토콜을 사용한다.
- AS와 AS간의 통신에는 라우터에서 BGP 같은 Exterior Routing Protocol, 즉 외부용 라우팅 프로토콜을 사용한다.
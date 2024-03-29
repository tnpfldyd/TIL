# MSA(MicroService Architecture)

### MSA 의 특징

- MSA는 API를 통해서만 상호작용할 수 있다. 즉, 마이크로 서비스는 서비스의 end-point(접근점)을 API 형태로 외부에 노출하고, 실질적인 세부 사항은 모두 추상화한다. 내부의 구현 로직, 아키텍처와 프로그래밍 언어, 데이터베이스, 품질 유지 체계와 같은 기술적인 사항들은 서비스 API에 의해 철저하게 가려진다. 

### MSA 의 등장 배경



- **Monolithic Architecture**는 소프트웨어의 모든 구성요소가 한 프로젝트에 통합되어 있는 형태이다. 웹 개발을 예로 들면 웹 프로그램을 개발하기 위해 모듈별로 개발을 하고, 개발이 완료된 웹 어플리케이션을 하나의 결과물로 패키징하여 배포되는 형태를 말한다. 이런 어플리케이션을 모놀리식 어플리케이션이라 하며, 웹의 경우 WAR파일로 빌드되어 WAS에 배포하는 형태를 말한다. 주로 소규모 프로젝트에서 사용된다.

- **부분 장애가 전체 서비스의 장애로 확대될 수 있다.** 
  - 개발자의 잘못된 코드 배포 또는 갑작스런 트래픽 증가로 인해 성능에 문제가 생겼을 때, 서비스 전체의 장애로 확대될 수 있다.
- **부분적인 \*Scale-out(여러 server로 나누어 일을 처리하는 방식)이 어렵다.**
  - Monolithic Architecture에서는 사용되지 않는 다른 모든 서비스가 Scale-out되어야 하기 때문에 부분 Scale-out이 어렵다.
- **서비스의 변경이 어렵고, 수정 시 장애의 영향도 파악이 힘들다.** 
  - 여러 컴포넌트가 하나의 서비스에 강하게 결합되어 있기 때문에 수정에 대한 영향도 파악이 힘들다.
- **배포 시간이 오래 걸린다.** 
  - 최근 어플리케이션 개발 방법은 CI/CD를 통한 개발부터 배포까지 빠르게 반영하는 추세이다. 그러나 규모가 커짐에 따라 작은 변경에도 높은 수준의 테스트 비용이 발생하기도 하며, 많은 사람이 하나의 시스템을 개발하여 배포하기 때문에 영향을 줄 수 밖에 없다.
- **한 Framework와 언어에 종속적이다.**
  - Spring framework를 사용할 경우, blockchain 연동 모듈을 추가할 때 node.js를 사용하는 것이 일반적이며 강세이다. 그러나 java를 이용하여 해당 모듈을 작성할 수 밖에 없다. 선정했던 framework가 Spring이기 때문이다.

- 이러한 Monolithic Architecture의 문제점들을 보완하기 위해 MSA가 등장하게 되었다. 기존의 특정한 물리적인 서버에 서비스를 올리던 on-promise 서버 기반의 Monolithic Architecture에서 이제는 클라우드 환경을 이용하여 서버를 구성하는 MicroService Architecture로 많은 서비스들이 전환되고 있다. 



## 장점

- 각각의 서비스는 모듈화가 되어있으며 이러한 모듈까리는 RPC 또는 message-driven API등을 이용하여 통신한다. 이러한 MSA는 각각 개별의 서비스 개발을 빠르게 하며, 유지보수도 쉽게할 수 있도록 한다. 

- 팀 단위로 적절한 수준에서 기술 스택을 다르게 가져갈 수 있다. 회사가 java의 spring 기반이라도 MSA를 적용하면 node.js로 블록체인 개발 모듈을 연동함에 무리가 없다. 

- 마이크로서비스는 서비스별로 독립적 배포가 가능하다. 따라서 지속적인 배포 CD도 모놀로식에 비해서 가볍게 할 수 있다.

- 마이크로서비스는 각각 서비스의 부하에 따라 개별적으로 scale-out이 가능하다. 메모리, CPU적으로 상당부분 이득이 된다.



### 단점

- MSA는 모놀리식에 비해 상대적으로 많이 복잡하다. 서비스가 모두 분산되어 있기 때문에 개발자는 내부 시스템의 통신을 어떻게 가져가야 할지 정해야한다. 또한, 통신의 장애와 서버의 부하 등이 있을 경우 어떻게 transaction을 유지할지 결정하고 구현해야한다. 

- 모놀리식에서는 단일 트랜잭션을 유지하면 됐지만 MSA에서는 비즈니스에 대한 DB를 가지고 있는 서비스도 각기 다르고, 서비스의 연결을 위해서는 통신이 포함되기 때문에 트랜잭션을 유지하는게 어렵다. 

- 통합 테스트가 어렵다. 개발 환경과 실제 운영환경을 동일하게 가져가는 것이 쉽지 않다. 

- 실제 운영환경에 대해서 배포하는 것이 쉽지 않다. 마이크로서비스의 경우 서비스 1개를 재배포 한다고 하면 다른 서비스들과의 연계가 정상적으로 이루어지고 있는지도 확인해야한다. 
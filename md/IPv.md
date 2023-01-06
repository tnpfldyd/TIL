# IPv4, IPv6 이란?



## IPv4

- 현재 네트워크 계층의 프로토콜은 Internet Protocal version4 를 사용한다.(현재 대부분 사용되고 있는 아이피)

  4영역으로 나누어진 최대 12자리의 번호로 이루어져 있다.

- 숫자로 구성된 인터넷 공인 주소이고 점으로 구분한다.

  각 영역의 숫자는 0 ~ 255 까지의 숫자로 표현할 수 있고, 한 영역의 256(2^8) 가지의 경우의 수를

  표현할 수 있다. 비트로 표현하면 각 영역은 8비트로 이루어지며 총 4영역이므로

  8 * 4 = 32 비트 체계이다. 최대 약 40억개(2^32 = 4,294,967,296)의 서로 다른 주소를 부여할 수 있다.

  즉, IPv4 는 32비트의 약 40억개 주소로 구성된다.

  그러나 기존의 IPv4 체계로는 계속해서 요구되는 인터넷 주소 할당 수요를 충족시킬 수 없다는 문제점이 생기기 시작했다.

  이미 IPv4 주소체계는 포화상태에 이르렀고 이러한 문제점을 해결하고자 새로운 IP 추소 체계인 IPv6이 등장하게 되었다.



> ### *** IPv4 주소의 구성?**
>
> **Network ID** : 해당 컴퓨터가 소속된 네트워크에 배정된 이름과 
>
> **Host ID** : 해당 물리적 컴퓨터에 배정된 이름 으로 구분한다. 
>
> IP주소는 5개 (A-E) 클래스로 나누어지며 각 클래스의 의미는 해당클래스의 형식을 가진 IP주소가 표현할 수 있는
>
> 네트워크와 호스트의 수이다. 현재 인터넷에서는 A/B/C 클래스 주소가 사용된다.



## IPv6



- IETF (국제 인터넷 표준화 기구) 에서는 2008 - 2011년 사이에 IPv4 주소가 고갈될 것으로 예측하고 IP next generation 이라는 그룹을 만들어 1994년부터 활동해왔다. 이 결과로 95년도에 표준이 제안되면서 IPv6 이 등장하게 된다. 

- Internet Protocal version6. IPv6주소는 128 비트체계로 구성되어 있다.

  기존의 IPv4 의 32비트 주소보다 4배나 많은 정보를 수용할 수 있는 차세대 IP이다.

  표현방법은 128비트는 16비트씩 8부분으로 나누어 각 부분을 콜론(:)으로 구분하여 표현하며 각 16진수로 표현한다.

  > ex)
  >
  > 0:0:0:0:0:0:0:1 

- 128비트 주소체계인 IPv6는 최대 1조개 이상(2^128. 거의 무한대.)을 부여할 수 있다는 점이 가장 큰 강점이다.

  IPv6가 쓰이면 장차 일상생활에 사용하는 모든 전자사물 회로가 서로 다른 IP주소를 가질 수 있다고 볼 수 있다.

  서비스에 따라 각기 다른 대역폭을 확보할 수 있도록 지원, 일정수준의 서비스품질을 요구하는 실시간 서비스를 더욱 쉽게 제공할 수 있고 인증, 데이터무결성, 데이터기밀성 등을 지원하도록 보안기능을 강화한것이 IPv6이다. 

  또한 인터넷주소를 기존 IPv4의 A/B/C/D 클래스별 할당이 아닌, 

  유니캐스트, 애니캐스트, 멀티캐스트 형태의 유형으로 할당하기 때문에 할당된 주소의 낭비자원이 사라지고,

  더욱 간단하게 주소를 자동 설정할 수 있다.

  앞으로의 유비쿼터스에서는 모든 전자사물들이 고유IP를 갖기되는 IoT환경에 적용하기에 적합하다고 보여진다.



## IPv4 와 IPv6 의 차이점

![image-20230105114209950](IPv.assets/image-20230105114209950.png)
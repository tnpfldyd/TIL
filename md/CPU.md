# CPU란?
컴퓨터 내부에서 시스템들을 통제함과 동시에 프로그램들을 실행하는 가장 기본적인 부품이며 메인보드에 장착됩니다.
인체에 비유했을때 컴퓨터의 두뇌라고 할 수 있으며, 컴퓨터로 들어오거나 나가는 모든 정보를 기억하고 출력하며 프로그램의 연산을 실행하는 장치입니다.
쉽게 풀어서 설명하자면 컴퓨터의 모든 동작을 제어하는 장치이기 때문에, 성능이 좋은 CPU를 사용할수록 PC의 속도와 성능을 좌우하게 됩니다.

## CPU 코어, 쓰레드, 클럭, 캐시메모리

코어(core)는 CPU 안에서 물리적인 연산(데이터 처리)을 담당하는 곳입니다. 쓰레드(thread)는 운영체계(OS, Operating System)가 이해하고 있는 작업 단위를 뜻합니다. 최초에는 코어 1개 당 쓰레드도 1개였는데, 작업의 효율을 올리기 위해서 점차 2개 이상의 쓰레드를 사용할 수 있게 만들었습니다.

라면 음식점에서 만들어 내는 라면에 빗대어 설명해보겠습니다. 코어는 주방에 있는 요리사입니다. 쓰레드는 라면을 끓일 수 있는 가스렌지의 가스불 입니다. 이 주방에서의 작업 목표는 주문받은 라면을 빠르게 요리해서 주방 밖으로 내보내는 것입니다.

### **▶ CPU 코어, 쓰레드**

요리사의 능력이 좋으면, 좋은 품질의 라면 한그릇을 빠르게 만들어낼 수 있습니다. 이는 코어의 능력이 좋으면 복잡한 연산을 빠르게 수행할 수 있다는 것과 연결됩니다. 또한 요리사가 많으면 주문 받은 라면을 빠르게 만들 수 있듯이, 코어가 많으면 컴퓨터의 처리속도가 빨라집니다. 마찬가지로 가스렌지의 가스불 개수가 많아지면 라면을 빠르게 만들 수 있습니다. 쓰레드가 많을수록 작업을 처리하는 속도가 빨라집니다. 가스불 개수가 2개인 것이 쓰레드가 2개인 것과 대응된다고 보시면 됩니다.

최초에는 코어 1개 당, 쓰레드도 1개였습니다. 이 말은 요리사 1명이 가스렌지 가스불 1개로 끓여냈다는 것과 같은 의미입니다. 요리사와 가스렌지를 늘려가다가, 요리사 수를 더 이상 늘릴 수 없는 상황에서, 주문 처리 속도를 더 높이기 위해서 요리사 1명당 가스불 2개인 가스렌지를 지급했습니다. 이는 컴퓨터도 코어 숫자를 늘려서 처리속도를 높이다가, 더 이상 효율이 좋아지지 않자, 쓰레드를 늘린 것이 바로 가스불 2개로 늘린 것과 같은 개념입니다.

### **▶ 클럭**

CPU의 클럭에 나와 있는 숫자는 코어 하나 당 일을 처리하는 속도를 의미합니다. 요리사의 요리속도가 이에 대응됩니다. 주방에 많은 요리사가 있더라도, 요리사들의 요리속도가 느리다면, 주문을 처리하는 속도가 떨어집니다. 좀더 능력있는 요리사일수록 더 많은 라면을 끓여낼 수 있듯이 말입니다. 코어가 일을 처리할 수 있는 능력을 클럭이라고 보시면 됩니다.

클럭과 코어수를 늘린다면 그만큼 처리속도는 빨라집니다. 그런데, 요리사가 빠르게 움직이는 만큼 땀도 많이 나듯이, CPU에서 클럭 속도수가 늘어나면 열도 많이 발생되고, 함께 관리할 것들이 늘어나기 때문에 적절한 조화가 중요합니다. 보통 코어 수가 적은 CPU일 때, 클럭 수가 높은 편입니다.

### **▶ 캐시메모리**

캐시메모리는 속도가 빠른 장치와 느린 장치의 사이에서 두 장치의 속도차로 인한 병목 현상을 줄이기 위해서 설치한 메모리입니다. CPU는 빠르고 메모리는 CPU보다 느리기 때문에 CPU와 메모리 사이에 캐시메모리가 있습니다. 캐시메모리는 CPU에서 빠르게 처리된 데이터를 메모리로 옮길 때 점진적으로 속도를 줄일 수 있도록 합니다. 라면 음식점 주방에서 끓여진 라면이 손님에게로 가기 전 놓여지는 테이블이라고 생각하시면 되겠습니다. 테이블이 클수록 좀 더 매끄럽게 일이 진행되듯이, 컴퓨터에서도 캐시메모리의 용량이 클수록 좋다고 생각하시면 되겠습니다.
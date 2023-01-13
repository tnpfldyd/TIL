# TCP 연결과 종료



**1. TCP 연결 3 way handshake** 

client와 server와 같이 네트워크를 사용한 통신시에 tcp 통신이 많이 사용된다.

tcp 통신을 위해 **3 way handshake** 과정을 통해 네트워크가 연결된다.



![img](https://t1.daumcdn.net/cfile/tistory/9957DF345CD2DB0233)





먼저 server에서 포트는 litsen 상태이고 client에서는 closed 상태이다.



1. 클라이언트에서 서버에 연결 요청을 하기 위해 SYN을 보낸다.



2. 서버의 해당 포트는 LISTEN 상태에서 SYN 데이터를 받고 SYN_RCV 상태로 변경된다.

   이후 정상적으로 받았다는 대답으로 SYN + ACK를 보낸다.



3. 클라이언트에서는 SYN + ACK를 받고 ESTABLISHED 상태로 변경되고, 그 응답으로 ACK를 보낸다.

   이후 ACK를 받은 서버는 ESTABLISHED 상태로 변경된다.



이 3단계를 정상적으로 마치면, 서로 ESTABLISHED 되면서 연결이 성립된다.



> **STATE** 
>
> \- CLOSED : 연결이 되어있지 않음을 나타내는 상태
>
> 
>
> \- LISTEN : 원격 TCP application으로부터 연결 요청을 기다리고 있는 상태 
>
> 
>
> \- SYN_SENT : SYN(연결 요청)을 보낸 후 ACK(응답)을 기다리고 있는 상태 
>
>  3 way handshake의 첫번째 단계 후의 결과이다.
>
> 
>
> \- SYN_RCV : 연결 요청을 받은 후 ACK를 보낸 후이며, 최종 ACK를 기다리고 있는 상태
>
> 3 way handshake의 두번째 단계 후의 결과이다.
>
> 
>
> \- ESTABLISHED : 완전히 연결이 성립되었음을 나타내는 상태
>
> 데이터 전송 단계에 대한 정상적인 상태를 나타낸다.





**2. TCP 연결 종료 4 way handshake**

tcp 연결 때와는 다르게 서로 연결을 종료할 때는 **4 way handshake** 과정이 필요하다.



![img](https://t1.daumcdn.net/cfile/tistory/997BBD395CD2E5491B)

TCP 연결 종료는 서로 ESTABLISHED 즉, 연결이 성립된 상태에서 시작한다.



1. 통신을 종료하고자 하는 클라이언트가 서버에게 FIN을 보낸 후, FIN_WAIT 1 상태로 대기한다.



2. FIN을 받은 서버는 상태를 CLOSE_WAIT로 변경하고, 응답으로 ACK를 보낸다. 

   해당 ACK를 받은 클라이언트는 상태를 FIN_WAIT 2로 변경한다. 

   이와 동시에 서버는 해당 포트에 연결되어 있는 애플리케이션에게 CLOSE()를 요청한다.



3. CLOSE() 요청을 받은 애플리케이션은 종료 프로세스를 통해 최종적으로 close되고 서버는 FIN을 클라이언트에게 보낸 후 상태를 LAST_ACK로 변경한다.



4. FIN_WAIT 2 상태에서 서버로부터 FIN을 받으면 이에 대한 응답으로 ACK를 보낸 후 상태를 TIME_WAIT로 변경한다.

최종 ACK를 받은 서버는 CLOSED로 상태를 변경하고, 클라이언트도 일정 시간이 지나면 CLOSED로 상태를 변경한다.

 

> **STATE**
>
> \- FIN_WAIT_1 : 연결 종료 요청에 대한 응답(ACK)을 기다리고 있는 상태 
>
> 
>
> \- FIN_WAIT_2 : 연결을 종료했다는 FIN(애플리케이션 종료)을 기다리고 있는 상태
>
>   FIN을 받지 못했다면 서버에서 CLOSE()를 처리하지 못한 경우일 수도 있으며, 이 경우 
>
>   FIN_WAIT 상태가 계속해서 지속될 수 있다.
>
> 
>
> \- CLOSE_WAIT : 연결 종료 요청을 받았으며, 로컬 애플리케이션의 종료(CLOSE())를 기다리고 있는 상태
>
> 
>
> \- LAST_ACK : 연결 종료 요청을 보냈으며 이에 대한 응답(ACK)을 기다리고 있는 상태 
>
>  주로 서버에서 로컬 애플리케이션이 종료가 되고 클라이언트로 종료 요청을 보낸 후의 상태이다.
>
> 
>
> \- TIME_WAIT : FIN에 대한 ACK를 보낸 후, 이를 원격지에서 받기까지 충분한 시간을 기다리고 있는 상태
>
>  일정 시간이 지나면 CLOSED 상태로 변경한다.



-출처-

[Aldo](https://hanaldo.tistory.com/) 

> 내용을 너무 잘 정리해 놓으셔서 따로 수정 할게 없었다..
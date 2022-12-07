# [Gold II] Parity Constraint Shortest Path - 20128 

[문제 링크](https://www.acmicpc.net/problem/20128) 

### 성능 요약

메모리: 196880 KB, 시간: 2836 ms

### 분류

다익스트라(dijkstra), 그래프 이론(graphs)

### 문제 설명

<p>2019년에 연세대학교 최적화 연구실에서는 갑자기 특정 문제에 Parity Constraint(홀짝 제약)을 넣은 상태로 문제를 푸는 것이 유행한 적이 있었고, 졸업하신 김강산 선배도 Parity Constraint 관련 논문을 작성하셨다. 이를 기념하기 위해서 국렬이는 연세대학교 프로그래밍 경진대회에 Parity Constraint 문제를 내기로 하였다.</p>

<p>정점이 <em>N</em>개, 비용이 있는 무방향 간선이 <em>M</em>개 있는 그래프가 주어진다. 모든 정점에는 1부터 <em>N</em>까지 번호가 매겨져 있다. 임의의 정점을 선택했을 때 다른 정점으로 가는 경로는 항상 존재하며, 서로 다른 두 정점 사이에는 최대 한 개의 간선이 존재한다.</p>

<p>정점 1에서 출발해서 다른 정점으로 이동하려고 한다. 이미 지나갔던 정점이나 간선도 다시 지나갈 수 있으며, 지나갈 때마다 비용이 추가된다. 경로를 구성하는 간선의 비용의 합을 편의상 '경로의 비용'이라 정의하자. 경로의 비용이 홀수면 홀수 경로, 짝수면 짝수 경로라고 부르자. 각 정점으로 이동할 때 비용이 최소가 되는 홀수 경로의 비용과 짝수 경로의 비용을 구하려고 한다.</p>

### 입력 

 <p>다음과 같이 입력이 주어진다.</p>

<div style="background:#eeeeee;border:1px solid #cccccc;padding:5px 10px;"><em>N</em> <em>M</em><br>
<i>u<sub>1</sub></i> <i>v<sub>1</sub></i> <i>w<sub>1</sub></i><br>
. . .<br>
<i>u<sub>M</sub></i> <i>v<sub>M</sub></i> <i>w<sub><span style="font-size: 10.8333px;">M</span></sub></i></div>

### 출력 

 <p>첫째 줄부터 <em>N</em>개의 줄에 걸쳐, <em>i</em>번째 줄에 1번 정점에서 <em>i</em>번 정점으로 이동하는 최소의 홀수 경로의 비용과, 최소의 짝수 경로의 비용을 공백으로 구분하여 출력한다. 해당 경로가 존재하지 않는 경우 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>


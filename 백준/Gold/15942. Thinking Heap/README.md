# [Gold II] Thinking Heap - 15942 

[문제 링크](https://www.acmicpc.net/problem/15942) 

### 성능 요약

메모리: 113412 KB, 시간: 156 ms

### 분류

해 구성하기, 그리디 알고리즘

### 제출 일자

2024년 10월 16일 09:05:52

### 문제 설명

<p>Binary heap은 Heap을 구현하는 방법의 하나이며 Complete binary tree 형태로 만들어진다. Complete binary tree는 Binary tree의 종류 중 하나로, 마지막 레벨을 제외한 나머지 레벨에는 노드가 꽉 차 있고 마지막 레벨에는 노드들이 왼쪽으로 쏠려있는 모습을 하고 있다.</p>

<p align="center" style="text-align:center"><img alt="" src="" style="width: 550px; height: 166px;"><br>
<그림> Complete binary tree의 예</p>

<p>Complete binary tree는 1차원 배열을 이용하면 쉽게 구현할 수 있다. Complete binary tree의 각 노드에 아래 그림과 같은 식으로 번호를 붙이고 이를 1차원 배열에서의 index로 삼으면 자연스럽게 구현할 수 있다.</p>

<p align="center" style="text-align:center"><img alt="" src="" style="width: 300px; height: 204px;"><br>
<그림> Complete binary tree에 번호를 붙인 모습</p>

<p>이를 이용하면 Binary min-heap에 원소를 삽입하는 알고리즘을 간단하게 구현할 수 있다. 아래 코드는 삽입 알고리즘을 C++로 구현한 코드이다(코드의 자잘한 문제들은 신경 쓰지 않기로 한다). 코드의 insert_heap() 함수를 호출하면 우리가 만든 Binary min-heap에 원소가 적절히 삽입된다.</p>

<p align="center" style="text-align:center"><img alt="" src=""><br>
<그림> Binary min-heap에 원소를 삽입하는 알고리즘을 구현한 코드</p>

<p>비어있는 Binary min-heap에 1 이상 N 이하의 서로 다른 자연수 N개를 insert_heap() 함수를 이용해 삽입할 것이다. N개의 자연수를 전부 다 삽입한 후에, 자연수 k가 heap 배열의 p번째(배열의 맨 처음 공간을 0번째로 생각한다)에 위치하도록 하고 싶다. 이렇게 만드는 삽입 순서를 찾는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 자연수 N(1 ≤ N ≤ 200,000)이 주어진다. 두 번째 줄에 자연수 k와 p(1 ≤ k, p ≤ N)가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>자연수 k가 heap 배열의 p번째에 위치하도록 하는 삽입 순서가 존재한다면 i번째 줄에 i번째로 삽입할 수를 출력한다. 가능한 삽입 순서가 여러 가지라면 그중 아무거나 하나를 출력해도 된다. 만약 그렇게 만드는 삽입 순서가 존재하지 않는다면 첫 번째 줄에 -1을 출력한다.</p>


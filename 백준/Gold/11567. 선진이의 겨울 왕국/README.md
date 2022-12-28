# [Gold II] 선진이의 겨울 왕국 - 11567 

[문제 링크](https://www.acmicpc.net/problem/11567) 

### 성능 요약

메모리: 128748 KB, 시간: 172 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>겨울 왕국에 나오는 올라프의 유일한 후손인 선진이는 현재 엘사가 얼려놓은 빙판길 위에 서 있다.</p>

<p>빙판길은 n×m의 크기를 갖는 직사각형 격자모양이고, 빙판길의 각 칸은 손상되거나 손상되지 않은 상태이다. 손상된 칸은 영대문자 <code>X</code>로, 손상되지 않은 칸은 <code>.</code> 으로 주어진다.</p>

<p>빙판길은 크기가 n×m인 직사각형 격자모양이고, 빙판길 각 칸의 얼음은 이미 손상되어 있거나, 손상되지 않은 상태이다.</p>

<p>그리고 직사각형의 행을 위에서부터 아래로 1부터 n까지, 열을 왼쪽에서부터 차례대로 1부터 m이라 가정한다.</p>

<p>만약 선진이가 빙판길에서 손상된 칸으로 이동하면 빙판길 아래로 추락하여 동사하기 때문에, 각 칸에 상하좌우로 인접하면서 손상되지 않은 얼음이 있는 칸으로 이동해야만 한다.</p>

<p>그리고 빙판의 상태가 약하기 때문에, 현재 위치에서 다른 칸으로 이동을 하면 이동하기 전 위치의 얼음은 손상된 상태로 바뀌게 된다.</p>

<table class="table table table-bordered">
	<tbody>
		<tr>
			<td style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11567/1.png" style="height:203px; width:216px"></td>
			<td style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11567/2.png" style="height:200px; width:223px"></td>
		</tr>
		<tr>
			<td style="text-align:center">(a)</td>
			<td style="text-align:center">(b)</td>
		</tr>
	</tbody>
</table>

<p>예를 들어서 그림(a)와 같이 (1, 1)에 서 있는 선진이가 그림(b)와 같이 오른쪽으로 한 칸 이동하게 되면, 선진이의 위치는 (1, 2)가 되고 (1, 1)의 얼음은 손상되어 더 이상 지나갈 수 없게 된다. </p>

<p>그리고 (r<sub>2</sub>, c<sub>2</sub>) 에 위치한 올라프가 만든 탈출구는 빙판길 밑에 있기 때문에 (r<sub>2</sub>, c<sub>2</sub>)의 얼음을 손상 시키고, 손상된 얼음을 다시 밟아 추락해야지 탈출구를 이용할 수 있게 된다.(이미 탈출구 위의 얼음이 손상되어 있을 수도 있다.)</p>

<p>선진이가 있는 빙판길의 상태가 주어지고, 시작 위치 (r<sub>1</sub>, c<sub>1</sub>)와 탈출구가 있는 지점 (r<sub>2</sub>, c<sub>2</sub>) 가 주어져 있을 때, 선진이가 탈출구를 이용해 탈출이 가능한지 불가능한지 판별하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄은  두 개의 정수 n, m (1 ≤ n, m ≤ 500)이 주어진다. n은 격자에서 행의 개수를 의미하고, m은 열의 개수를 의미한다.</p>

<p>다음 n개의 줄에는 각각 m개의 문자로 이루어진 빙판길의 초기 상태가 주어진다. (손상된 얼음이면 '<code>X</code>'로 표시되고, 손상되지 않은 얼음은 '<code>.</code>' 으로 표시된다.)</p>

<p>다음 줄은 두개의 정수 r<sub>1</sub>과 c<sub>1</sub> (1 ≤ r<sub>1</sub> ≤ n, 1 ≤ c<sub>1</sub> ≤ m)이 주어진다. 이는 선진이의 초기위치를 나타내고, 초기위치의 빙판길의 상태는 ‘<code>X</code>’로 주어진다.</p>

<p>다음 줄은 두개의 정수 r<sub>2</sub>과 c<sub>2</sub> (1 ≤ r<sub>2</sub> ≤ n, 1 ≤ c<sub>2</sub> ≤ m)가 주어진다. 이는 올라프가 만들어 놓은 탈출구의 위치를 나타내며, 초기 위치와 일치할 수도 있다.</p>

### 출력 

 <p>선진이가 탈출 할 수 있다면, YES를 출력하고, 없다면 NO를 출력한다.</p>


# [Gold V] Clear And Present Danger - 6185 

[문제 링크](https://www.acmicpc.net/problem/6185) 

### 성능 요약

메모리: 110664 KB, 시간: 136 ms

### 분류

플로이드–워셜, 그래프 이론, 최단 경로

### 제출 일자

2024년 4월 25일 13:58:52

### 문제 설명

<p>Farmer John is on a boat seeking fabled treasure on one of the N (1 <= N <= 100) islands conveniently labeled 1..N in the Cowribbean Sea.</p>

<p>The treasure map tells him that he must travel through a certain sequence A_1, A_2, ..., A_M of M (2 <= M <= 10,000) islands, starting on island 1 and ending on island N before the treasure will appear to him. He can visit these and other islands out of order and even more than once, but his trip must include the A_i sequence in the order specified by the map.</p>

<p>FJ wants to avoid pirates and knows the pirate-danger rating (0 <= danger <= 100,000) between each pair of islands. The total danger rating of his mission is the sum of the danger ratings of all the paths he traverses.</p>

<p>Help Farmer John find the least dangerous route to the treasure that satisfies the treasure map's requirement.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..M+1: Line i+1 describes the i_th island FJ must visit with a single integer: A_i</li>
	<li>Lines M+2..N+M+1: Line i+M+1 contains N space-separated integers that are the respective danger rating of the path between island i and islands 1, 2, ..., and N, respectively. The ith integer is always zero.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The minimum danger that Farmer John can encounter while obtaining the treasure.</li>
</ul>


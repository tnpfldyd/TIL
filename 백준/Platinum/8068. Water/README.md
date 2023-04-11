# [Platinum V] Water - 8068 

[문제 링크](https://www.acmicpc.net/problem/8068) 

### 성능 요약

메모리: 33324 KB, 시간: 92 ms

### 분류

자료 구조, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 데이크스트라, 우선순위 큐

### 문제 설명

<p>On a rectangular mesh comprising n x m fields, n⋅m cuboids were put, one cuboid on each field. A base of each cuboid covers one field and its surface equals to one square inch. Cuboids on adjacent fields adhere one to another so close that there are no gaps between them. A heavy rain pelted on a construction so that in some areas puddles of water appeared.</p>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input a size of the chessboard and heights of cuboids put on the fields,</li>
	<li>computes maximal water volume, which may gather in puddles after the rain,</li>
	<li>writes results to standard output.</li>
</ul>

### 입력 

 <p>In the first line of the standard input two positive integers n and m, 1 ≤ n ≤ 100, 1 ≤ m ≤ 100 are written. They are the size of the mesh. In each of the following n lines there are m integers from the interval [1, 10,000]; i-th number in j-th line denotes a height of a cuboid given in inches put on the field in the i-th column and j-th raw of the chessboard.</p>

### 출력 

 <p>Your program should write in the first and the only line of the standard output one integer equal to the maximal volume of water (given in cubic inches), which may gather in puddles on the construction.</p>


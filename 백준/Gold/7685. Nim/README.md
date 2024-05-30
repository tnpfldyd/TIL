# [Gold II] Nim - 7685 

[문제 링크](https://www.acmicpc.net/problem/7685) 

### 성능 요약

메모리: 110404 KB, 시간: 128 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2024년 5월 30일 10:35:42

### 문제 설명

<p>Nim is a 2-player game featuring several piles of stones. Players alternate turns, and on his/her turn, a player’s move consists of removing one or more stones from any single pile. Play ends when all the stones have been removed, at which point the last player to have moved is declared the winner. Given a position in Nim, your task is to determine how many winning moves there are in that position.</p>

<p>A position in Nim is called “losing” if the first player to move from that position would lose if both sides played perfectly. A “winning move,” then, is a move that leaves the game in a losing position. There is a famous theorem that classifies all losing positions. Suppose a Nim position contains n piles having k<sub>1</sub>, k<sub>2</sub>, . . . , k<sub>n</sub> stones respectively; in such a position, there are k<sub>1</sub> + k<sub>2</sub> + . . . + k<sub>n</sub> possible moves. We write each k<sub>i</sub> in binary (base 2). Then, the Nim position is losing if and only if, among all the k<sub>i</sub> ’s, there are an even number of 1’s in each digit position. In other words, the Nim position is losing if and only if the xor of the k<sub>i</sub>’s is 0.</p>

<p>Consider the position with three piles given by k<sub>1</sub> = 7, k<sub>2</sub> = 11, and k<sub>3</sub> = 13. In binary, these values are as follows:</p>

<ul>
	<li>111</li>
	<li>1011</li>
	<li>1101</li>
</ul>

<p>There are an odd number of 1’s among the rightmost digits, so this position is not losing. However, suppose k<sub>3</sub> were changed to be 12. Then, there would be exactly two 1’s in each digit position, and thus, the Nim position would become losing. Since a winning move is any move that leaves the game in a losing position, it follows that removing one stone from the third pile is a winning move when k<sub>1</sub> = 7, k<sub>2</sub> = 11, and k<sub>3</sub> = 13. In fact, there are exactly three winning moves from this position: namely removing one stone from any of the three piles.</p>

### 입력 

 <p>The input test file will contain multiple test cases, each of which begins with a line indicating the number of piles, 1 ≤ n ≤ 1000. On the next line, there are n positive integers, 1 ≤ k<sub>i</sub> ≤ 1, 000, 000, 000, indicating the number of stones in each pile. The end-of-file is marked by a test case with n = 0 and should not be processed.</p>

### 출력 

 <p>For each test case, write a single line with an integer indicating the number of winning moves from the given Nim position.</p>


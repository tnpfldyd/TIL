# [Platinum IV] Illumination - 13744 

[문제 링크](https://www.acmicpc.net/problem/13744) 

### 성능 요약

메모리: 33508 KB, 시간: 160 ms

### 분류

2-sat(2_sat), 그래프 이론(graphs), 강한 연결 요소(scc)

### 문제 설명

<p>You inherited a haunted house. Its floor plan is an n-by-n square grid with l lamps in fixed locations and no interior walls. Each lamp can either illuminate its row or its column, but not both simultaneously. The illumination of each lamp extends by r squares in both directions, so a lamp unobstructed by an exterior wall of the house can illuminate as many as 2r + 1 squares.</p>

<p>If a square is illuminated by more than one lamp in its row, or by more than one lamp in its column, the resulting bright spot will scare away ghosts forever, diminishing the value of your property. Is it possible for all lamps to illuminate a row or column, without scaring any ghosts? Note that a square illuminated by two lamps, one in its row and the other in its column, will not scare away the ghosts.</p>

### 입력 

 <p>The first line of input contains three positive integers, n, r and l (1 ≤ n, r, l ≤ 1,000).</p>

<p>Each of the next l lines contains two positive integers r<sub>i</sub> and c<sub>i</sub> (1 ≤ r<sub>i</sub>, c<sub>i</sub> ≤ n), indicating that there is a lamp in row r<sub>i</sub> and column c<sub>i</sub>.</p>

<p>It is guaranteed that all lamps are in distinct locations.</p>

### 출력 

 <p>Print, on a single line, 1 if it is possible to illuminate all lamps as stated above; otherwise, print 0.</p>


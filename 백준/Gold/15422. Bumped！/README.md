# [Gold I] Bumped! - 15422 

[문제 링크](https://www.acmicpc.net/problem/15422) 

### 성능 요약

메모리: 154448 KB, 시간: 760 ms

### 분류

다익스트라(dijkstra), 그래프 이론(graphs)

### 문제 설명

<p>Peter returned from the recently held ACM ICPC World Finals only to find that his return flight was overbooked and he was bumped from the flight! Well, at least he wasn’t beat up by the airline and he’s received a voucher for one free flight between any two destinations he wishes.</p>

<p>He is already planning next year’s trip. He plans to travel by car where necessary, but he may be using his free flight ticket for one leg of the trip. He asked for your help in his planning.</p>

<p>He can provide you a network of cities connected by roads, the amount it costs to buy gas for traveling between pairs of cities, and a list of available flights between some of those cities. Help Peter by finding the minimum amount of money he needs to spend to get from his hometown to next year’s destination!</p>

### 입력 

 <p>The input consists of a single test case. The first line lists five space-separated integers n, m, f, s, and t, denoting the number of cities n (0 < n ≤ 50 000), the number of roads m (0 ≤ m ≤ 150 000), the number of flights f (0 ≤ f ≤ 1 000), the number s (0 ≤ s < n) of the city in which Peter’s trip starts, and the number t (0 ≤ t < n) of the city Peter is trying to travel to. (Cities are numbered from 0 to n − 1.)</p>

<p>The first line is followed by m lines, each describing one road. A road description contains three space separated integers i, j, and c (0 ≤ i, j < n, i ≠ j and 0 < c ≤ 50 000), indicating there is a road connecting cities i and j that costs c cents to travel. Roads can be used in either direction for the same cost. All road descriptions are unique.</p>

<p>Each of the following f lines contains a description of an available flight, which consists of two space separated integers u and v (0 ≤ u, v < n, u ≠ v) denoting that a flight from city u to city v is available (though not from v to u unless listed elsewhere). All flight descriptions are unique.</p>

### 출력 

 <p>Output the minimum number of cents Peter needs to spend to get from his home town to the competition, using at most one flight. You may assume that there is a route on which Peter can reach his destination.</p>


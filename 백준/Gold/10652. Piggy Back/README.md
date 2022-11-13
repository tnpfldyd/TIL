# [Gold III] Piggy Back - 10652 

[문제 링크](https://www.acmicpc.net/problem/10652) 

### 성능 요약

메모리: 122524 KB, 시간: 376 ms

### 분류

너비 우선 탐색(bfs), 다익스트라(dijkstra), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>Bessie and her sister Elsie graze in different fields during the day, and in the evening they both want to walk back to the barn to rest. Being clever bovines, they come up with a plan to minimize the total amount of energy they both spend while walking.</p>

<p>Bessie spends B units of energy when walking from a field to an adjacent field, and Elsie spends E units of energy when she walks to an adjacent field.  However, if Bessie and Elsie are together in the same field, Bessie can carry Elsie on her shoulders and both can move to an adjacent field while spending only P units of energy (where P might be considerably less than B+E, the amount Bessie and Elsie would have spent individually walking to the adjacent field).  If P is very small, the most energy-efficient solution may involve Bessie and Elsie traveling to a common meeting field, then traveling together piggyback for the rest of the journey to the barn.  Of course, if P is large, it may still make the most sense for Bessie and Elsie to travel separately.  On a side note, Bessie and Elsie are both unhappy with the term "piggyback", as they don't see why the pigs on the farm should deserve all the credit for this remarkable form of transportation.</p>

<p>Given B, E, and P, as well as the layout of the farm, please compute the minimum amount of energy required for Bessie and Elsie to reach the barn.</p>

### 입력 

 <p>The first line of input contains the positive integers B, E, P, N, and M.  All of these are at most 40,000.  B, E, and P are described above. N is the number of fields in the farm (numbered 1..N, where N >= 3), and M is the number of connections between fields.  Bessie and Elsie start in fields 1 and 2, respectively.  The barn resides in field N.</p>

<p>The next M lines in the input each describe a connection between a pair of different fields, specified by the integer indices of the two fields.  Connections are bi-directional.  It is always possible to travel from field 1 to field N, and field 2 to field N, along a series of such connections.  </p>

### 출력 

 <p>A single integer specifying the minimum amount of energy Bessie and Elsie collectively need to spend to reach the barn.  In the example shown here, Bessie travels from 1 to 4 and Elsie travels from 2 to 3 to 4.  Then, they travel together from 4 to 7 to 8.</p>


# [Gold V] Packet Routing - 6951 

[문제 링크](https://www.acmicpc.net/problem/6951) 

### 성능 요약

메모리: 110688 KB, 시간: 160 ms

### 분류

플로이드–워셜, 그래프 이론, 최단 경로

### 제출 일자

2024년 4월 26일 09:53:23

### 문제 설명

<p>The date is October 29th, 1969. Today, scientists at UCLA made history by exchanging data between two computers over a network. The transmission wasn't very spectacular: only the first two letters of the word <code>login</code> were received before the system crashed. Nevertheless, the researchers are beginning to design larger computer networks and they need your help.</p>

<p>A computer network is a collection of $N$ $(2 \le N \le 100)$ computers and $W$ wires. The computers are identified by the numbers $1, 2, \dots, N$. Each wire connects exactly two computers, allowing packets of data to flow in both directions between the computers. The wires are placed so that it is possible to send packets (directly or indirectly by passing through other computers) between every pair of computers. In fact, the placement of the wires has been optimized so that there is exactly one path between every pair of computers. If the packet travels along several wires to get from the source computer to the destination computer, the time needed for the packet to travel along this path is the sum of the times required for the packet to travel along each individual wire. You are to write a program that computes the amount of time needed for a packet to travel between a given pair of distinct computers.</p>

### 입력 

 <p>The first line of the input file contains the three positive integers $N, W, P$.</p>

<p>For each wire, a line follows giving the identification numbers of the two computers connected by the wire, and an integer between $1$ and $500$ giving the time required for a packet to travel along this wire.</p>

<p>$P$ $(1 \le P \le 10\,000)$ is the number of packets which need to be sent. For each packet, a line follows giving the identification numbers of the packet's source and destination computers.</p>

### 출력 

 <p>For each packet, find the route through the network which will allow the packet to travel from the source computer to the destination computer. Output the travel time of this route on a single line.</p>


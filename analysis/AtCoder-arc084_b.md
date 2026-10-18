# Problem Analysis: AtCoder-arc084_b — D. Small Multiple

**Problem ID**: `AtCoder-arc084_b`  
**Contest**: `arc084`  
**Rating / Difficulty**: 2457  
**URL**: https://atcoder.jp/contests/arc084/tasks/arc084_b  
**VJudge Tag**: `[problem:AtCoder-arc084_b]`  
**Category File**: [`../categories/graph_theory/small_multiple_digit_sum_01_bfs.md`](../categories/graph_theory/small_multiple_digit_sum_01_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `0/1 BFS`  

---

## 1. Problem Statement & Key Idea
Find the minimum sum of digits of a positive multiple of $K$. Model as shortest path on a directed graph with $K$ vertices $0, 1, \dots, K - 1$ representing remainders modulo $K$. From remainder $u$, multiplying by 10 transitions to $(10u) \bmod K$ with edge weight 0 (digit sum unchanged); adding 1 transitions to $(u + 1) \bmod K$ with edge weight 1 (digit sum +1). The shortest path from state 1 (cost 1) to state 0 computes the answer via 0-1 BFS in $O(K)$ time.

## 2. Core Observation & Invariant
Any positive integer can be constructed starting from 1 by alternating two operations: multiplying by 10 and adding 1 (without carrying beyond 9). The transitions naturally map into modulo $K$ arithmetic where multiplying by 10 does not increase the digit sum, while incrementing adds 1. 0-1 BFS computes shortest paths in linear time without logarithmic overhead.

## 3. Step-by-Step Algorithm
1. 1. Initialize distance array `dist` of size $K$ with $\infty$, setting `dist[1] = 1`.
2. 2. Push state 1 to the front of a double-ended queue `dq`.
3. 3. While `dq` is not empty, pop the front state $u$.
4. 4. Transition 1: $v_0 = (u \times 10) \bmod K$. If `dist[u] < dist[v_0]`, update `dist[v_0] = dist[u]` and push to the front.
5. 5. Transition 2: $v_1 = (u + 1) \bmod K$. If `dist[u] + 1 < dist[v_1]`, update `dist[v_1] = dist[u] + 1` and push to the back.
6. 6. Output `dist[0]`.

## 4. Complexity Analysis
- **Time Complexity**: `O(K)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    if (!(cin >> k)) return 0;

    vector<int> dist(k, INF);
    deque<int> dq;

    // We can start with any digit 1..9, or start at state 1 with cost 1
    dist[1] = 1;
    dq.push_back(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        // Edge 1: multiply by 10 (cost 0)
        int v0 = (u * 10) % k;
        if (dist[u] < dist[v0]) {
            dist[v0] = dist[u];
            dq.push_front(v0);
        }

        // Edge 2: add 1 (cost 1)
        int v1 = (u + 1) % k;
        if (dist[u] + 1 < dist[v1]) {
            dist[v1] = dist[u] + 1;
            dq.push_back(v1);
        }
    }

    cout << dist[0] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

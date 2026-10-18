# Problem Analysis: AtCoder-agc028_c — C. Min Cost Cycle

**Problem ID**: `AtCoder-agc028_c`  
**Contest**: `agc028`  
**Rating / Difficulty**: 2463  
**URL**: https://atcoder.jp/contests/agc028/tasks/agc028_c  
**VJudge Tag**: `[problem:AtCoder-agc028_c]`  
**Category File**: [`../categories/graph_theory/min_cost_cycle_hamiltonian_extremal.md`](../categories/graph_theory/min_cost_cycle_hamiltonian_extremal.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Find a Hamiltonian cycle on a complete directed graph where edge $(u, v)$ has cost $\min(A_u, B_v)$. In any Hamiltonian cycle, each vertex $i$ has in-degree 1 and out-degree 1, selecting $N$ values from $\{A_i\} \cup \{B_i\}$. A set of $N$ chosen values can form a single connected cycle iff the set is all $A$, all $B$, or contains both $A_i$ and $B_i$ for at least one vertex $i$.

## 2. Core Observation & Invariant
If we choose all $A$ values, the cycle cost is $\sum A_i$. If all $B$, cost is $\sum B_i$. Otherwise, as long as there is at least one vertex with both $A_i$ and $B_i$ chosen, the edges can always be configured into a single Eulerian component that forms a Hamiltonian cycle. Sorting all $2N$ values allows finding the minimal cost choice in $O(N \log N)$.

## 3. Step-by-Step Algorithm
1. 1. Calculate sums $\sum A_i$ and $\sum B_i$.
2. 2. Pool all $2N$ values labeled with vertex ID and type ($A$ or $B$), and sort ascending.
3. 3. Sum the $N$ smallest values. If at least one vertex ID appears twice, this sum is valid and optimal.
4. 4. If all $N$ vertices chosen are distinct, try replacing the boundary element with the $(N+1)$-th or $(N+2)$-th element to induce a duplicate vertex ID.
5. 5. Output the minimum cost among all valid configurations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    long long val;
    int id;
    int type; // 0 for A, 1 for B
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N), B(N);
    long long sumA = 0, sumB = 0;
    vector<Item> items;
    items.reserve(2 * N);

    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> B[i];
        sumA += A[i];
        sumB += B[i];
        items.push_back({A[i], i, 0});
        items.push_back({B[i], i, 1});
    }

    sort(items.begin(), items.end(), [](const Item& x, const Item& y) {
        return x.val < y.val;
    });

    long long ans = min(sumA, sumB);

    long long cur_sum = 0;
    vector<int> cnt(N, 0);
    int both_cnt = 0;
    for (int i = 0; i < N; ++i) {
        cur_sum += items[i].val;
        cnt[items[i].id]++;
        if (cnt[items[i].id] == 2) both_cnt++;
    }

    if (both_cnt > 0) {
        ans = min(ans, cur_sum);
    } else {
        // Try replacing items[N - 1] with items[N]
        for (int i = 0; i < N; ++i) {
            long long temp = cur_sum - items[i].val + items[N].val;
            int id_out = items[i].id;
            int id_in = items[N].id;
            int b_cnt = both_cnt;
            if (cnt[id_out] == 2) b_cnt--;
            if (cnt[id_in] == 1) b_cnt++;
            if (b_cnt > 0) ans = min(ans, temp);
        }

        // Try replacing items[N - 1] or another with items[N + 1] if needed
        for (int i = 0; i < N; ++i) {
            long long temp = cur_sum - items[i].val + items[N + 1].val;
            int id_out = items[i].id;
            int id_in = items[N + 1].id;
            int b_cnt = both_cnt;
            if (cnt[id_out] == 2) b_cnt--;
            if (cnt[id_in] == 1) b_cnt++;
            if (b_cnt > 0) ans = min(ans, temp);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

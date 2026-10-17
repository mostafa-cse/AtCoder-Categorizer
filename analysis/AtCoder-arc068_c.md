# Problem Analysis: AtCoder-arc068_c — E. Snuke Line

**Problem ID**: `AtCoder-arc068_c`  
**Contest**: `arc068`  
**Rating / Difficulty**: 2307  
**URL**: https://atcoder.jp/contests/arc068/tasks/arc068_c  
**VJudge Tag**: `[problem:AtCoder-arc068_c]`  
**Category File**: [`../categories/data_structures/harmonic_query_offline_fenwick_threshold.md`](../categories/data_structures/harmonic_query_offline_fenwick_threshold.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Splitting Objects into Light and Heavy / Case Processing`  

---

## 1. Problem Statement & Key Idea
Given $N$ souvenir intervals $[l_i, r_i] \subseteq [1, M]$, for each train interval $d = 1, \dots, M$, find the number of souvenir intervals containing at least one multiple of $d$.

## 2. Core Observation & Invariant
Any interval of length $\ge d$ is guaranteed to contain at least one multiple of $d$. Intervals of length $< d$ contain at most one multiple of $d$ and can be queried via point evaluations.

## 3. Step-by-Step Algorithm
1. Sort and bucket intervals by their lengths $len_i = r_i - l_i + 1$.
2. As step size $d$ increases from $1$ to $M$, retire intervals with length $d - 1$ from the heavy count and insert them into a Fenwick tree (range add $[l_i, r_i]$).
3. Query all multiples $k \cdot d \le M$ in the Fenwick tree, yielding total complexity $O(N \log M + M \log^2 M)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log M + M \log^2 M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 2, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<pair<int, int>>> by_len(M + 2);
    for (int i = 0; i < N; ++i) {
        int l, r;
        cin >> l >> r;
        int len = r - l + 1;
        if (len <= M) {
            by_len[len].push_back({l, r});
        }
    }

    Fenwick bit(M + 1);
    int long_count = N;

    for (int d = 1; d <= M; ++d) {
        for (auto& seg : by_len[d - 1]) {
            long_count--;
            bit.add(seg.first, 1);
            bit.add(seg.second + 1, -1);
        }

        int ans = long_count;
        for (int k = d; k <= M; k += d) {
            ans += bit.query(k);
        }
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

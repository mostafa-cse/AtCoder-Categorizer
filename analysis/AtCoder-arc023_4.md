# Problem Analysis: AtCoder-arc023_4 — D - GCD区間

**Problem ID**: `AtCoder-arc023_4`  
**Contest**: `arc023`  
**Rating / Difficulty**: 2511  
**URL**: https://atcoder.jp/contests/arc023/tasks/arc023_4  
**VJudge Tag**: `[problem:AtCoder-arc023_4]`  
**Category File**: [`../categories/number_theory/gcd_intervals_distinct_values_map.md`](../categories/number_theory/gcd_intervals_distinct_values_map.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Euclidean Algorithm`  
- **Topic (Skill)**: `Euclidean Algorithm`  

---

## 1. Problem Statement & Key Idea
For $M \le 10^5$ queries $x$, count the number of subsegments $[s, t]$ with $\gcd(A_s, \dots, A_t) = x$ in an array of size $N \le 10^5$.

## 2. Core Observation & Invariant
For any fixed right endpoint $i$, the prefix GCDs $\gcd(A_j, \dots, A_i)$ as $j$ decreases from $i$ down to 1 can take at most $\log_2(\max A_i) \le 30$ distinct values because each change divides the GCD by at least 2. We maintain a compressed run-length list of pairs `(gcd_value, count)` ending at position $i$. Advancing to $i+1$ computes $\gcd(g, A_{i+1})$ for each distinct value, merges identical consecutive values, and accumulates counts into a global frequency map.

## 3. Step-by-Step Algorithm
1. 1. Maintain `cur_gcds`, a list of `(gcd_value, count)` pairs ending at the current index.
2. 2. For each element $A_i$, compute $\gcd(g, A_i)$ for all pairs in `cur_gcds`, plus $(A_i, 1)$, and merge adjacent pairs with the same GCD.
3. 3. Add `count` to `total_counts[gcd_value]` in a hash map or balanced tree.
4. 4. For each query $x$, output `total_counts[x]` in $O(1)$ or $O(\log K)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log(\max A) + M \log N)`
- **Space Complexity**: `O(N \log(\max A) + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    map<long long, long long> total_counts;
    vector<pair<long long, long long>> cur_gcds;

    for (int i = 0; i < N; ++i) {
        long long x = A[i];
        vector<pair<long long, long long>> next_gcds;
        for (auto& p : cur_gcds) {
            long long ng = gcd(p.first, x);
            if (!next_gcds.empty() && next_gcds.back().first == ng) {
                next_gcds.back().second += p.second;
            } else {
                next_gcds.push_back({ng, p.second});
            }
        }
        if (!next_gcds.empty() && next_gcds.back().first == x) {
            next_gcds.back().second += 1;
        } else {
            next_gcds.push_back({x, 1});
        }
        cur_gcds = move(next_gcds);
        for (auto& p : cur_gcds) {
            total_counts[p.first] += p.second;
        }
    }

    for (int i = 0; i < M; ++i) {
        long long q;
        cin >> q;
        auto it = total_counts.find(q);
        if (it != total_counts.end()) {
            cout << it->second << "\n";
        } else {
            cout << 0 << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

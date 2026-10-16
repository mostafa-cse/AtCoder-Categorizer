# Problem Analysis: AtCoder-typical90_ci — Chokudai's Demand

**Problem ID**: `AtCoder-typical90_ci`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 087)  
**Rating / Difficulty**: 1850 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ci  
**VJudge Tag**: `[problem:AtCoder-typical90_ci]`  
**Category File**: [`../categories/graph_theory/floyd_warshall_binary_search.md`](../categories/graph_theory/floyd_warshall_binary_search.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths & Binary Search`  
- **Topic (Skill)**: `Monotonicity of Floyd-Warshall Distance & Dual Binary Search`  

---

## 1. Problem Statement & Key Idea
Complete graph with N <= 40 vertices. Some edges have unknown weight X. Count number of integer values of X >= 1 such that exactly K pairs of vertices have shortest path distance <= P.

**Core Idea**: As X increases, all-pairs shortest path distances monotonically increase; thus the number of pairs with distance <= P monotonically DECREASES.

## 2. Core Observation & Invariant
Let f(X) be the number of pairs with distance <= P computed via Floyd-Warshall in O(N^3). Since f(X) is monotonic, use binary search to find maximum X with f(X) >= K (call it R) and maximum X with f(X) >= K + 1 (call it L). The number of valid X is R - L (or Infinity if R exceeds limit).

## 3. Step-by-Step Algorithm
1. Function count_pairs(X): run Floyd-Warshall, count pairs with dist <= P.
2. Binary search R = max X with count_pairs(X) >= K.
3. Binary search L = max X with count_pairs(X) >= K + 1.
4. If R >= INF_BOUND: output 'Infinity'; else output R - L.

## 4. Complexity Analysis
Time: O(N^3 * log(INF)), Space: O(N^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
int n, k;
long long P;
vector<vector<long long>> a;

long long count_pairs(long long X) {
    vector<vector<long long>> dist = a;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] == -1) dist[i][j] = X;
        }
    }

    for (int m = 0; m < n; ++m) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][m] + dist[m][j]);
            }
        }
    }

    long long cnt = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (dist[i][j] <= P) cnt++;
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> P >> k)) return 0;
    a.assign(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    // Binary search for max X such that count_pairs(X) >= target
    auto find_bound = [&](int target) -> long long {
        long long low = 1, high = P + 2, best = 0;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (count_pairs(mid) >= target) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return best;
    };

    long long R = find_bound(k);
    long long L = find_bound(k + 1);

    if (R > P) {
        cout << "Infinity\n";
    } else {
        cout << max(0LL, R - L) << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Dual binary search on Floyd-Warshall distance monotonicity.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Monotonicity in parametric shortest paths and dual binary search range boundary subtraction.
- **Reusable Pattern**: `Parametric Floyd-Warshall with Dual Binary Search.`

---
Back to [Monotonicity of Floyd-Warshall Distance & Dual Binary Search](../categories/graph_theory/floyd_warshall_binary_search.md) | [Categories Directory](../categories/README.md)
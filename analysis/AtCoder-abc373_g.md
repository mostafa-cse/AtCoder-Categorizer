# Problem Analysis: AtCoder-abc373_g — G. No Cross Matching

**Problem ID**: `AtCoder-abc373_g`  
**Contest**: `abc373`  
**Rating / Difficulty**: 2377  
**URL**: https://atcoder.jp/contests/abc373/tasks/abc373_g  
**VJudge Tag**: `[problem:AtCoder-abc373_g]`  
**Category File**: [`../categories/graph_theory/euclidean_minimum_matching_no_cross.md`](../categories/graph_theory/euclidean_minimum_matching_no_cross.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Given N red and N blue points with no three collinear, find a non-crossing bipartite matching. By the triangle inequality, any crossing pair of segments can be uncrossed to strictly decrease total Euclidean length; thus, the minimum Euclidean distance matching guarantees zero crossings, solved via the Hungarian algorithm in O(N^3) time.

## 2. Core Observation & Invariant
In any bipartite matching of N points to N points where no three points are collinear, if any two segments cross at an intersection point X, the triangle inequality guarantees that uncrossing their endpoints strictly decreases the total Euclidean length. Therefore, the minimum Euclidean distance matching cannot contain any crossing segments.

## 3. Step-by-Step Algorithm
1. Construct an N x N cost matrix where cost[i][j] is the Euclidean distance hypot(A_i - C_j, B_i - D_j).
2. Run the Hungarian algorithm in O(N^3) time to find the minimum-weight perfect bipartite matching.
3. Extract the assigned permutation R[p[j]] = j and output the 1-based indices.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    vector<pair<double, double>> P(n + 1), Q(n + 1);
    for (int i = 1; i <= n; ++i) cin >> P[i].first >> P[i].second;
    for (int i = 1; i <= n; ++i) cin >> Q[i].first >> Q[i].second;

    vector<vector<double>> cost(n + 1, vector<double>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cost[i][j] = hypot(P[i].first - Q[j].first, P[i].second - Q[j].second);
        }
    }

    vector<double> u(n + 1), v(n + 1);
    vector<int> p(n + 1), way(n + 1);
    for (int i = 1; i <= n; ++i) {
        p[0] = i;
        int j0 = 0;
        vector<double> minv(n + 1, 1e18);
        vector<char> used(n + 1, false);
        do {
            used[j0] = true;
            int i0 = p[j0];
            double delta = 1e18;
            int j1 = 0;
            for (int j = 1; j <= n; ++j) {
                if (!used[j]) {
                    double cur = cost[i0][j] - u[i0] - v[j];
                    if (cur < minv[j]) {
                        minv[j] = cur;
                        way[j] = j0;
                    }
                    if (minv[j] < delta) {
                        delta = minv[j];
                        j1 = j;
                    }
                }
            }
            for (int j = 0; j <= n; ++j) {
                if (used[j]) {
                    u[p[j]] += delta;
                    v[j] -= delta;
                } else {
                    minv[j] -= delta;
                }
            }
            j0 = j1;
        } while (p[j0] != 0);
        do {
            int j1 = way[j0];
            p[j0] = p[j1];
            j0 = j1;
        } while (j0);
    }

    vector<int> ans(n + 1);
    for (int j = 1; j <= n; ++j) {
        ans[p[j]] = j;
    }
    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

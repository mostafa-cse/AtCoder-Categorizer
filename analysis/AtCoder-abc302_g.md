# Problem Analysis: AtCoder-abc302_g — Sort from 1 to 4

**Problem ID**: `AtCoder-abc302_g`  
**Contest**: `abc302`  
**Rating / Difficulty**: 1891  
**URL**: https://atcoder.jp/contests/abc302/tasks/abc302_g  
**VJudge Tag**: `[problem:AtCoder-abc302_g]`  
**Category File**: [`../categories/graph_theory/directed_cycle_decomposition_array_sort.md`](../categories/graph_theory/directed_cycle_decomposition_array_sort.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cycle Decomposition`  
- **Topic (Skill)**: `Minimum Swaps to Sort Finite-Alphabet Array via Directed Cycle Decomposition`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N with values in {1, 2, 3, 4}. In one operation, swap any two elements. Find the minimum number of swaps to sort A in non-decreasing order.

**Key Insight**: Let cnt[u][v] be the number of indices where the actual array has value u but the sorted target array has value v. This forms a directed multigraph with 4 vertices. A cycle of length L fixes L elements using L - 1 swaps. To minimize swaps, maximize the number of cycles by greedily extracting 2-cycles, then 3-cycles, then 4-cycles.

## 2. Core Observation & Invariant
Greedy priority: (1) Disjoint 2-cycles u <-> v (cost 1 swap for 2 elements), (2) 3-cycles u -> v -> w -> u (cost 2 swaps for 3 elements), (3) remaining 4-cycles (cost 3 swaps for 4 elements).

## 3. Step-by-Step Algorithm
1. Compute target sorted array B.
2. Build 4x4 matrix cnt[u][v] counting pairs with A[i] = u and B[i] = v.
3. swaps = 0.
4. // Step 1: Extract 2-cycles
5. For all pairs u < v: k = min(cnt[u][v], cnt[v][u]); swaps += k; cnt[u][v] -= k; cnt[v][u] -= k.
6. // Step 2: Extract 3-cycles
7. For all triples u, v, w: k = min({cnt[u][v], cnt[v][w], cnt[w][u]}); swaps += 2*k; reduce cnt.
8. // Step 3: Extract 4-cycles
9. For all 4-tuples: k = min({cnt[u][v], cnt[v][w], cnt[w][x], cnt[x][u]}); swaps += 3*k; reduce cnt.
10. Print swaps.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + 4^4)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        b[i] = a[i];
    }

    sort(b.begin(), b.end());

    int cnt[5][5] = {};
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) {
            cnt[a[i]][b[i]]++;
        }
    }

    long long swaps = 0;

    // 2-cycles
    for (int u = 1; u <= 4; ++u) {
        for (int v = u + 1; v <= 4; ++v) {
            int k = min(cnt[u][v], cnt[v][u]);
            swaps += k;
            cnt[u][v] -= k;
            cnt[v][u] -= k;
        }
    }

    // 3-cycles
    vector<int> p3 = {1, 2, 3, 4};
    for (int u = 1; u <= 4; ++u) {
        for (int v = 1; v <= 4; ++v) {
            for (int w = 1; w <= 4; ++w) {
                if (u != v && v != w && w != u) {
                    int k = min({cnt[u][v], cnt[v][w], cnt[w][u]});
                    swaps += 2LL * k;
                    cnt[u][v] -= k;
                    cnt[v][w] -= k;
                    cnt[w][u] -= k;
                }
            }
        }
    }

    // 4-cycles
    for (int u = 1; u <= 4; ++u) {
        for (int v = 1; v <= 4; ++v) {
            for (int w = 1; w <= 4; ++w) {
                for (int x = 1; x <= 4; ++x) {
                    if (u != v && v != w && w != x && x != u && u != w && v != x) {
                        int k = min({cnt[u][v], cnt[v][w], cnt[w][x], cnt[x][u]});
                        swaps += 3LL * k;
                        cnt[u][v] -= k;
                        cnt[v][w] -= k;
                        cnt[w][x] -= k;
                        cnt[x][u] -= k;
                    }
                }
            }
        }
    }

    cout << swaps << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decomposing element displacement graphs into maximal disjoint directed cycles.
- **Reusable Pattern**: `Finite-Alphabet Swap Sort: Greedily extract 2-cycles, 3-cycles, and 4-cycles from discrepancy matrix.`

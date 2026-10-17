# Problem Analysis: AtCoder-arc200_c — Movie Theater

**Problem ID**: `AtCoder-arc200_c`  
**Contest**: `arc200`  
**Rating / Difficulty**: 2237  
**URL**: https://atcoder.jp/contests/arc200/tasks/arc200_c  
**VJudge Tag**: `[problem:AtCoder-arc200_c]`  
**Category File**: [`../categories/graph_theory/interval_containment_poset_topological_sort_movie_theater.md`](../categories/graph_theory/interval_containment_poset_topological_sort_movie_theater.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest seat permutation P minimizing the total dissatisfaction when people with staying intervals [L_i, R_i] cross seats to enter and exit.

## 2. Core Observation & Invariant
Pairwise analysis shows that for disjoint intervals, cost is 0; for overlapping non-contained intervals, cost is 1 in both orders. Only when [L_j, R_j] is strictly contained in [L_i, R_i] does order matter: P_j < P_i incurs cost 0, whereas P_i < P_j incurs cost 2. Containment defines a DAG poset where j -> i whenever interval j is contained in interval i. To find the lexicographically smallest permutation P, assign the largest seat numbers N, N-1, ..., 1 backwards to the unassigned node with the largest index having no containing unassigned ancestor.

## 3. Step-by-Step Algorithm
1. 1. For each test case, identify interval containment: person j is contained in person i if L_i < L_j < R_j < R_i.
2. 2. Greedily assign seat numbers backwards from k = N down to 1:
3.    - Among all currently unassigned people i, find those who have no unassigned person j containing them (out-degree 0 in the containment DAG).
4.    - Pick the candidate with the largest index i and assign seat P[i] = k.
5. 3. Output the resulting permutation P.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3) per testcase`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

void solve_test() {
    int n;
    if (!(cin >> n)) return;

    vector<int> l(n), r(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i] >> r[i];
    }

    vector<int> ans(n, -1);
    for (int p = n - 1; p >= 0; --p) {
        for (int i = n - 1; i >= 0; --i) {
            if (ans[i] != -1) continue;
            bool ok = true;
            for (int j = 0; j < n; ++j) {
                if (ans[j] != -1) continue;
                if (l[j] < l[i] && r[i] < r[j]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans[i] = p + 1;
                break;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

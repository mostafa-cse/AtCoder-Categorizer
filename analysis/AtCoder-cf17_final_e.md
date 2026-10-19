# Problem Analysis: AtCoder-cf17_final_e — E - Combination Lock

**Problem ID**: `AtCoder-cf17_final_e`  
**Contest**: `cf17-final`  
**Rating / Difficulty**: 2816  
**URL**: https://atcoder.jp/contests/cf17-final/tasks/cf17_final_e  
**VJudge Tag**: `[problem:AtCoder-cf17_final_e]`  
**Category File**: [`../categories/data_structures/range_increment_palindrome_difference_dsu.md`](../categories/data_structures/range_increment_palindrome_difference_dsu.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
Given string S and N cyclic range increment operations [L_i, R_i] mod 26, determine whether S can be transformed into a palindrome.

## 2. Core Observation & Invariant
Padding S with 0 at both ends gives array B = [0, S_1..S_M, 0]. The adjacent difference array D_i = (B_{i+1} - B_i) mod 26 tracks state changes: an operation [L, R] increments B_L..B_R, adding +1 to D_{L-1} and -1 to D_R. Thus, values can be transferred along edges (L-1, R). Furthermore, B is a palindrome iff D_i + D_{M-i} == 0 mod 26 for all i, equivalent to allowing transfers between i and M-i. In the resulting graph, values can be redistributed within each connected component. A palindrome is possible iff the sum of D_v mod 26 in every connected component is 0.

## 3. Step-by-Step Algorithm
1. 1. Convert S to numbers 0..25 and pad with 0: B = [0, S_1..S_M, 0].
2. 2. Compute difference array D_i = (B_{i+1} - B_i) mod 26 for i in 0..M.
3. 3. Initialize DSU on vertices 0..M.
4. 4. Union (i, M - i) for all i in 0..M (palindrome symmetry).
5. 5. Union (L - 1, R) for all N given operations.
6. 6. Sum D_i mod 26 within each connected component.
7. 7. If all component sums are 0 mod 26, output YES; else output NO.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + N * alpha(|S|))`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int n;
    if (!(cin >> n)) return 0;

    int M = (int)s.size();
    vector<int> B(M + 2, 0);
    for (int i = 0; i < M; i++) {
        B[i + 1] = s[i] - 'a';
    }

    vector<int> D(M + 1);
    for (int i = 0; i <= M; i++) {
        D[i] = (B[i + 1] - B[i]) % 26;
        if (D[i] < 0) D[i] += 26;
    }

    DSU dsu(M + 1);

    // Palindrome edges
    for (int i = 0; i <= M; i++) {
        dsu.unite(i, M - i);
    }

    // Operation edges
    for (int i = 0; i < n; i++) {
        int L, R;
        cin >> L >> R;
        dsu.unite(L - 1, R);
    }

    vector<int> comp_sum(M + 1, 0);
    for (int i = 0; i <= M; i++) {
        int r = dsu.find(i);
        comp_sum[r] = (comp_sum[r] + D[i]) % 26;
    }

    for (int i = 0; i <= M; i++) {
        if (comp_sum[i] % 26 != 0) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

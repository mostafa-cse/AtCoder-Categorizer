# Problem Analysis: AtCoder-abc366_g — G. XOR Neighbors

**Problem ID**: `AtCoder-abc366_g`  
**Contest**: `abc366`  
**Rating / Difficulty**: 2409  
**URL**: https://atcoder.jp/contests/abc366/tasks/abc366_g  
**VJudge Tag**: `[problem:AtCoder-abc366_g]`  
**Category File**: [`../categories/math/f2_nullspace_gaussian_elimination_neighborhood_xor.md`](../categories/math/f2_nullspace_gaussian_elimination_neighborhood_xor.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Gaussian Elimination Modulo 2`  

---

## 1. Problem Statement & Key Idea
Assign non-zero integers X_v in [1, 2^60 - 1] to graph vertices such that for each vertex of degree >= 1, the XOR sum of neighbors is 0. Formulate each bit independently as finding a vector in the nullspace of the adjacency matrix over F_2.

## 2. Core Observation & Invariant
The condition XOR_{u in N(v)} X_u = 0 is bitwise independent and equivalent to A x = 0 over F_2. Requiring X_v > 0 for all v means for each vertex v, there must exist a vector in ker(A) with x_v = 1. With N <= 60 and 60 bits available, solving N linear systems over F_2 guarantees each vertex receives at least one 1-bit.

## 3. Step-by-Step Algorithm
1. 1. Construct adjacency matrix over F_2 for all vertices with degree >= 1.
2. 2. For each target vertex v from 0 to N-1, append equation x_v = 1 and solve via Gaussian Elimination over F_2.
3. 3. If any vertex has an inconsistent system, output 'No'.
4. 4. Otherwise, set the v-th bit of all vertices using the solution vector and output 'Yes' with the integers.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4 / 64)`
- **Space Complexity**: `O(N^2 / 64)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<ull> adj(n, 0);
    vector<int> deg(n, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u] |= (1ULL << v);
        adj[v] |= (1ULL << u);
        deg[u]++;
        deg[v]++;
    }

    vector<ull> ans(n, 0);

    for (int target = 0; target < n; target++) {
        vector<ull> mat;
        for (int i = 0; i < n; i++) {
            if (deg[i] >= 1) {
                mat.push_back(adj[i] << 1);
            }
        }
        mat.push_back((1ULL << (target + 1)) | 1ULL);

        int row_idx = 0;
        for (int col = n; col >= 1; col--) {
            int pivot = -1;
            for (size_t r = row_idx; r < mat.size(); r++) {
                if ((mat[r] >> col) & 1ULL) {
                    pivot = r;
                    break;
                }
            }
            if (pivot != -1) {
                swap(mat[row_idx], mat[pivot]);
                for (size_t r = 0; r < mat.size(); r++) {
                    if (r != (size_t)row_idx && ((mat[r] >> col) & 1ULL)) {
                        mat[r] ^= mat[row_idx];
                    }
                }
                row_idx++;
            }
        }

        bool ok = true;
        for (size_t r = row_idx; r < mat.size(); r++) {
            if (mat[r] == 1ULL) {
                ok = false;
                break;
            }
        }

        if (!ok) {
            cout << "No\n";
            return 0;
        }

        ull sol = 0;
        for (int r = row_idx - 1; r >= 0; r--) {
            int lead_col = -1;
            for (int col = 1; col <= n; col++) {
                if ((mat[r] >> col) & 1ULL) lead_col = col;
            }
            ull rhs = mat[r] & 1ULL;
            ull other = (mat[r] >> 1) & sol;
            int parity = __builtin_popcountll(other) % 2;
            ull bit_val = rhs ^ parity;
            if (bit_val) {
                sol |= (1ULL << (lead_col - 1));
            }
        }

        for (int u = 0; u < n; u++) {
            if ((sol >> u) & 1ULL) {
                ans[u] |= (1ULL << target);
            }
        }
    }

    cout << "Yes\n";
    for (int i = 0; i < n; i++) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

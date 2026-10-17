# Problem Analysis: AtCoder-zone2021_f — F. Encounter and Farewell

**Problem ID**: `AtCoder-zone2021_f`  
**Contest**: `zone2021`  
**Rating / Difficulty**: 2197  
**URL**: https://atcoder.jp/contests/zone2021/tasks/zone2021_f  
**VJudge Tag**: `[problem:AtCoder-zone2021_f]`  
**Category File**: [`../categories/math/xor_basis_hypercube_spanning_tree.md`](../categories/math/xor_basis_hypercube_spanning_tree.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `[Technique] XOR Basis ft Reduced Row Echelon Form`  

---

## 1. Problem Statement & Key Idea
Build a spanning tree on N = 2^n vertices using edges with XOR differences not in A. The allowed difference set S = {1..N-1} \ A must span F_2^n; if not, output -1. If S spans F_2^n, extract a basis b_1..b_n in S and build a hypercube spanning tree by iteratively doubling components: (u, u ^ b_k).

## 2. Core Observation & Invariant
Starting with V = {0}, at step k connecting each u in V to u ^ b_k adds 2^{k-1} edges with allowed difference b_k in S. Because b_k is linearly independent from previous basis vectors, no cycles are formed, producing a valid tree of N - 1 edges.

## 3. Step-by-Step Algorithm
1. Mark forbidden values A in a boolean array.
2. Greedily find an XOR basis of size n from allowed values in [1, N - 1] \ A.
3. If basis size < n, output -1.
4. Start with V = {0}.
5. For each basis element b:
6.   For each u in V, add edge (u, u ^ b) and append u ^ b to V.
7. Output all N - 1 edges.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int n = 0;
    while ((1 << n) < N) n++;

    vector<bool> forbidden(N, false);
    for (int i = 0; i < M; ++i) {
        int a;
        cin >> a;
        forbidden[a] = true;
    }

    vector<int> basis(n, 0);
    vector<int> chosen_basis;

    auto insert_basis = [&](int val) -> bool {
        int orig = val;
        for (int i = n - 1; i >= 0; --i) {
            if (val & (1 << i)) {
                if (!basis[i]) {
                    basis[i] = val;
                    chosen_basis.push_back(orig);
                    return true;
                }
                val ^= basis[i];
            }
        }
        return false;
    };

    for (int x = 1; x < N; ++x) {
        if (!forbidden[x]) {
            insert_basis(x);
            if ((int)chosen_basis.size() == n) {
                break;
            }
        }
    }

    if ((int)chosen_basis.size() < n) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> V = {0};
    vector<pair<int, int>> edges;
    for (int b : chosen_basis) {
        int sz = V.size();
        for (int i = 0; i < sz; ++i) {
            int u = V[i];
            int v = u ^ b;
            edges.push_back({u, v});
            V.push_back(v);
        }
    }

    for (auto& [u, v] : edges) {
        cout << u << " " << v << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

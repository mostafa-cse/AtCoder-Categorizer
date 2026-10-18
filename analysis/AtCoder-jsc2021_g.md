# Problem Analysis: AtCoder-jsc2021_g — G - Spanning Tree

**Problem ID**: `AtCoder-jsc2021_g`  
**Contest**: `jsc2021`  
**Rating / Difficulty**: 2451  
**URL**: https://atcoder.jp/contests/jsc2021/tasks/jsc2021_g  
**VJudge Tag**: `[problem:AtCoder-jsc2021_g]`  
**Category File**: [`../categories/graph_theory/spanning_tree_kirchhoffs_matrix_tree_theorem.md`](../categories/graph_theory/spanning_tree_kirchhoffs_matrix_tree_theorem.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Kirchoffs Theorem ft Number of MSTs`  

---

## 1. Problem Statement & Key Idea
Count the number of spanning trees in a multigraph subject to forced edges (value 1), forbidden edges (value 0), and optional edges (value -1).

## 2. Core Observation & Invariant
Forced edges must not form a cycle; if they do, the answer is 0. Otherwise, contract all forced edges using Disjoint Set Union (DSU) to form $K$ components. An optional edge between original vertices translates into an edge between their corresponding contracted components. The number of spanning trees completing the contracted multigraph into a connected tree equals the cofactor determinant of its Laplacian matrix via Kirchhoff's Matrix Tree Theorem.

## 3. Step-by-Step Algorithm
1. 1. Run DSU over all pairs $(u, v)$ where $A_{u, v} = 1$. If an edge connects vertices already in the same component, report 0.
2. 2. Let $K$ be the number of components. If $K = 1$, report 1.
3. 3. Build a $K \times K$ Laplacian matrix $L$:
4.    - For every optional edge $(u, v)$ where $A_{u, v} = -1$ with $u$ and $v$ in different components $c_u \ne c_v$:
5.      $L[c_u][c_v] -= 1$, $L[c_v][c_u] -= 1$, $L[c_u][c_u] += 1$, $L[c_v][c_v] += 1$.
6. 4. Remove the last row and column of $L$ to obtain a $(K-1) \times (K-1)$ submatrix.
7. 5. Compute the determinant of the submatrix modulo $10^9+7$ using Gaussian elimination with row operations in $O(K^3)$ time.
8. 6. Output the resulting determinant.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 + K^3) = O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> A(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> A[i][j];
        }
    }

    DSU dsu(N);
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (A[i][j] == 1) {
                if (!dsu.unite(i, j)) {
                    cout << 0 << "\n";
                    return 0;
                }
            }
        }
    }

    vector<int> comp_id(N, -1);
    int num_comps = 0;
    for (int i = 0; i < N; ++i) {
        int root = dsu.find(i);
        if (comp_id[root] == -1) {
            comp_id[root] = num_comps++;
        }
        comp_id[i] = comp_id[root];
    }

    if (num_comps == 1) {
        cout << 1 << "\n";
        return 0;
    }

    vector<vector<long long>> W(num_comps, vector<long long>(num_comps, 0));
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (A[i][j] == -1) {
                int ci = comp_id[i];
                int cj = comp_id[j];
                if (ci != cj) {
                    W[ci][cj] = (W[ci][cj] + 1) % MOD;
                    W[cj][ci] = (W[cj][ci] + 1) % MOD;
                }
            }
        }
    }

    int M = num_comps - 1;
    vector<vector<long long>> L(M, vector<long long>(M, 0));
    for (int i = 0; i < M; ++i) {
        long long deg = 0;
        for (int j = 0; j < num_comps; ++j) {
            if (i != j) {
                deg = (deg + W[i][j]) % MOD;
            }
        }
        L[i][i] = deg;
        for (int j = 0; j < M; ++j) {
            if (i != j) {
                L[i][j] = (MOD - W[i][j]) % MOD;
            }
        }
    }

    long long det = 1;
    for (int i = 0; i < M; ++i) {
        int pivot = i;
        while (pivot < M && L[pivot][i] == 0) pivot++;
        if (pivot == M) {
            cout << 0 << "\n";
            return 0;
        }
        if (pivot != i) {
            swap(L[i], L[pivot]);
            det = (MOD - det) % MOD;
        }
        det = (det * L[i][i]) % MOD;
        long long inv = modInverse(L[i][i]);
        for (int j = i + 1; j < M; ++j) {
            long long factor = (L[j][i] * inv) % MOD;
            for (int k = i; k < M; ++k) {
                L[j][k] = (L[j][k] - factor * L[i][k]) % MOD;
                if (L[j][k] < 0) L[j][k] += MOD;
            }
        }
    }

    cout << det << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

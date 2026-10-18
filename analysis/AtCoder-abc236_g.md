# Problem Analysis: AtCoder-abc236_g — G. Good Vertices

**Problem ID**: `AtCoder-abc236_g`  
**Contest**: `abc236`  
**Rating / Difficulty**: 2438  
**URL**: https://atcoder.jp/contests/abc236/tasks/abc236_g  
**VJudge Tag**: `[problem:AtCoder-abc236_g]`  
**Category File**: [`../categories/math/good_vertices_min_max_matrix_exponentiation.md`](../categories/math/good_vertices_min_max_matrix_exponentiation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
In a directed graph with $N \le 100$, edges are added at times $1 \dots T$. We want to find the earliest time a walk of length exactly $L$ ($L \le 10^9$) from vertex 1 to vertex $i$ exists. This is a bottleneck shortest walk problem on the $(\min, \max)$ semiring, where matrix multiplication $(A \circ B)_{i,j} = \min_k \max(A_{i,k}, B_{k,j})$ computes the minimal edge threshold over path lengths.

## 2. Core Observation & Invariant
The min-max algebra satisfies associativity and distributivity. Matrix binary exponentiation of the adjacency matrix $M^L$ in the $(\min, \max)$ semiring computes all pair bottleneck walks of length $L$ in $O(N^3 \log L)$ time.

## 3. Step-by-Step Algorithm
1. 1. Construct adjacency matrix $M$ where $M[u][v] = t$ if edge $(u, v)$ was added at time $t$, else $\infty$.
2. 2. Define semiring matrix multiplication: $C[i][j] = \min_k \max(A[i][k], B[k][j])$.
3. 3. Initialize result matrix $res$ to the semiring identity: $res[i][i] = 0$, $res[i][j] = \infty$ for $i \ne j$.
4. 4. Compute $res = M^L$ via binary exponentiation.
5. 5. For each vertex $i \in [1, N]$, output $res[0][i-1]$ (or -1 if $\infty$).

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 log L)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int INF = 2e9;

int N, T;
long long L;

typedef vector<vector<int>> Matrix;

Matrix mat_mul(const Matrix& A, const Matrix& B) {
    Matrix C(N, vector<int>(N, INF));
    for (int i = 0; i < N; ++i) {
        for (int k = 0; k < N; ++k) {
            if (A[i][k] == INF) continue;
            for (int j = 0; j < N; ++j) {
                int val = max(A[i][k], B[k][j]);
                if (val < C[i][j]) {
                    C[i][j] = val;
                }
            }
        }
    }
    return C;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> T >> L)) return 0;

    Matrix mat(N, vector<int>(N, INF));
    for (int t = 1; t <= T; ++t) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        mat[u][v] = t;
    }

    Matrix res(N, vector<int>(N, INF));
    for (int i = 0; i < N; ++i) res[i][i] = 0;

    Matrix base = mat;
    long long p = L;
    while (p > 0) {
        if (p & 1) {
            res = mat_mul(res, base);
        }
        base = mat_mul(base, base);
        p >>= 1;
    }

    for (int i = 0; i < N; ++i) {
        int val = res[0][i];
        cout << (val == INF ? -1 : val) << (i == N - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

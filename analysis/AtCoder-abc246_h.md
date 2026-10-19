# Problem Analysis: AtCoder-abc246_h — 01? Queries

**Problem ID**: `AtCoder-abc246_h`  
**Contest**: `abc246`  
**Rating / Difficulty**: 2677  
**URL**: https://atcoder.jp/contests/abc246/tasks/abc246_h  
**VJudge Tag**: `[problem:AtCoder-abc246_h]`  
**Category File**: [`../categories/data_structures_ds/subsequence_01_matrix_segment_tree.md`](../categories/data_structures_ds/subsequence_01_matrix_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Count non-empty distinct subsequences of a ternary string S in {0, 1, ?}^N under point updates. Counting distinct subsequences is equivalent to tracking DP state vector (dp_0, dp_1, 1)^T. Each character '0', '1', '?' corresponds to a 3 x 3 transition matrix. A segment tree maintaining matrix products processes point updates and queries in O(log N) time.

## 2. Core Observation & Invariant
For '0': dp_0' = dp_0 + dp_1 + 1, dp_1' = dp_1. Matrix: [[1, 1, 1], [0, 1, 0], [0, 0, 1]]. For '1': dp_0' = dp_0, dp_1' = dp_0 + dp_1 + 1. Matrix: [[1, 0, 0], [1, 1, 1], [0, 0, 1]]. For '?': sum of both matrices. Matrix multiplication is associative, allowing a standard point-update segment tree over 3 x 3 matrices.

## 3. Step-by-Step Algorithm
1. 1. Map '0', '1', '?' to their 3 x 3 matrices.
2. 2. Build segment tree over the array of matrices of size N.
3. 3. For each query (x, c), update leaf x with the matrix for character c.
4. 4. Query root matrix product M = tree[1]. The answer is (M_{0,2} + M_{1,2}) mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const long long MOD = 998244353;

struct Matrix {
    long long m[3][3];
    Matrix() {
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < 3; ++j)
                m[i][j] = (i == j ? 1 : 0);
    }
};

Matrix multiply(const Matrix& A, const Matrix& B) {
    Matrix C;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            long long sum = 0;
            for (int k = 0; k < 3; ++k) {
                sum = (sum + A.m[i][k] * B.m[k][j]) % MOD;
            }
            C.m[i][j] = sum;
        }
    }
    return C;
}

Matrix get_matrix(char c) {
    Matrix M;
    if (c == '0') {
        M.m[0][0] = 1; M.m[0][1] = 1; M.m[0][2] = 1;
        M.m[1][0] = 0; M.m[1][1] = 1; M.m[1][2] = 0;
        M.m[2][0] = 0; M.m[2][1] = 0; M.m[2][2] = 1;
    } else if (c == '1') {
        M.m[0][0] = 1; M.m[0][1] = 0; M.m[0][2] = 0;
        M.m[1][0] = 1; M.m[1][1] = 1; M.m[1][2] = 1;
        M.m[2][0] = 0; M.m[2][1] = 0; M.m[2][2] = 1;
    } else { // '?'
        M.m[0][0] = 1; M.m[0][1] = 1; M.m[0][2] = 1;
        M.m[1][0] = 1; M.m[1][1] = 1; M.m[1][2] = 1;
        M.m[2][0] = 0; M.m[2][1] = 0; M.m[2][2] = 1;
    }
    return M;
}

int N, Q;
string S;
vector<Matrix> tree;

void build(int node, int l, int r) {
    if (l == r) {
        tree[node] = get_matrix(S[l]);
        return;
    }
    int mid = (l + r) / 2;
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
    tree[node] = multiply(tree[2 * node + 1], tree[2 * node]);
}

void update(int node, int l, int r, int idx, char c) {
    if (l == r) {
        tree[node] = get_matrix(c);
        return;
    }
    int mid = (l + r) / 2;
    if (idx <= mid) update(2 * node, l, mid, idx, c);
    else update(2 * node + 1, mid + 1, r, idx, c);
    tree[node] = multiply(tree[2 * node + 1], tree[2 * node]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> Q)) return 0;
    cin >> S;

    tree.resize(4 * N);
    build(1, 0, N - 1);

    for (int q = 0; q < Q; ++q) {
        int x;
        char c;
        cin >> x >> c;
        --x;
        update(1, 0, N - 1, x, c);
        long long ans = (tree[1].m[0][2] + tree[1].m[1][2]) % MOD;
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

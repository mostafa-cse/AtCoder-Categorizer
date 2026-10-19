# Problem Analysis: AtCoder-arc025_4 — D - コンセント

**Problem ID**: `AtCoder-arc025_4`  
**Contest**: `arc025`  
**Rating / Difficulty**: 2863  
**URL**: https://atcoder.jp/contests/arc025/tasks/arc025_4  
**VJudge Tag**: `[problem:AtCoder-arc025_4]`  
**Category File**: [`../categories/data_structures/dynamic_domino_tiling_transfer_matrix_segment_tree.md`](../categories/data_structures/dynamic_domino_tiling_transfer_matrix_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
On an H x W grid (H in {1, 2}, W <= 10^11), N <= 20000 operations dynamically toggle caps on cells. After each operation, count the number of valid matchings (placing 0 or more dominoes on uncapped cells) modulo 10^9+7.

## 2. Core Observation & Invariant
A column transition is represented by a 2^H x 2^H transfer matrix tracking which cells are covered by dominoes crossing into the next column. Since W <= 10^11 but only N <= 20000 columns are ever modified, the grid consists of K <= N modified columns interspersed with long contiguous blocks of empty columns. The matrix of an empty block of length L is M_0^L. Storing the 2K+1 matrix components in a segment tree allows O(log K * 4^3) point updates per query.

## 3. Step-by-Step Algorithm
1. 1. Coordinate compress all queried columns into sorted array col_1 < ... < col_K.
2. 2. Build a segment tree of size 2K+1 where leaves represent modified columns col_i and fixed power matrices M_0^len for empty intervals.
3. 3. Precompute M_0^L via matrix exponentiation for each gap.
4. 4. On each query, toggle the cell's cap state, update the single-column matrix in the segment tree, and output tree[1].mat[0][0].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N * 4^3 + N * 4^3 log W)`
- **Space Complexity**: `O(N * 4^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int MOD = 1000000007;

int H, dim;
long long W;
int N;

struct Matrix {
    int mat[4][4];
    Matrix() {
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                mat[i][j] = 0;
    }
    static Matrix identity() {
        Matrix res;
        for (int i = 0; i < dim; ++i) res.mat[i][i] = 1;
        return res;
    }
    Matrix operator*(const Matrix& other) const {
        Matrix res;
        for (int i = 0; i < dim; ++i) {
            for (int k = 0; k < dim; ++k) {
                if (!mat[i][k]) continue;
                for (int j = 0; j < dim; ++j) {
                    res.mat[i][j] = (res.mat[i][j] + 1LL * mat[i][k] * other.mat[k][j]) % MOD;
                }
            }
        }
        return res;
    }
};

Matrix power(Matrix base, long long exp) {
    Matrix res = Matrix::identity();
    while (exp > 0) {
        if (exp & 1) res = res * base;
        base = base * base;
        exp >>= 1;
    }
    return res;
}

Matrix get_col_matrix(int cap) {
    Matrix res;
    for (int in_mask = 0; in_mask < dim; ++in_mask) {
        if (in_mask & cap) continue;
        int occ = in_mask | cap;
        for (int vert = 0; vert <= 1; ++vert) {
            if (vert) {
                if (H != 2) continue;
                if (occ != 0) continue;
                res.mat[in_mask][0] = (res.mat[in_mask][0] + 1) % MOD;
            } else {
                vector<int> free_bits;
                for (int r = 0; r < H; ++r) {
                    if (!(occ & (1 << r))) free_bits.push_back(r);
                }
                int fb_sz = free_bits.size();
                for (int s = 0; s < (1 << fb_sz); ++s) {
                    int out_mask = 0;
                    for (int idx = 0; idx < fb_sz; ++idx) {
                        if (s & (1 << idx)) out_mask |= (1 << free_bits[idx]);
                    }
                    res.mat[in_mask][out_mask] = (res.mat[in_mask][out_mask] + 1) % MOD;
                }
            }
        }
    }
    return res;
}

struct Query {
    int r;
    long long c;
};

int num_leaves;
vector<Matrix> tree;

void update(int idx, const Matrix& val) {
    idx += num_leaves;
    tree[idx] = val;
    for (idx >>= 1; idx > 0; idx >>= 1) {
        tree[idx] = tree[idx << 1] * tree[idx << 1 | 1];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> H >> W >> N)) return 0;
    dim = 1 << H;

    vector<Query> queries(N);
    vector<long long> cols;
    for (int i = 0; i < N; ++i) {
        cin >> queries[i].r >> queries[i].c;
        queries[i].r--;
        cols.push_back(queries[i].c);
    }

    sort(cols.begin(), cols.end());
    cols.erase(unique(cols.begin(), cols.end()), cols.end());
    int K = cols.size();

    // Elements:
    // 0: prefix [1, cols[0]-1]
    // 1: cols[0]
    // 2: interval [cols[0]+1, cols[1]-1]
    // ...
    // 2K-1: cols[K-1]
    // 2K: suffix [cols[K-1]+1, W]
    int total_elems = 2 * K + 1;
    num_leaves = 1;
    while (num_leaves < total_elems) num_leaves <<= 1;
    tree.assign(2 * num_leaves, Matrix::identity());

    Matrix M0 = get_col_matrix(0);

    // Init interval 0
    tree[num_leaves + 0] = power(M0, cols[0] - 1);
    for (int i = 0; i < K; ++i) {
        // leaf 2*i + 1 is cols[i], initially cap = 0
        tree[num_leaves + 2 * i + 1] = M0;
        // leaf 2*i + 2 is interval
        long long gap = (i + 1 < K) ? (cols[i + 1] - cols[i] - 1) : (W - cols[i]);
        tree[num_leaves + 2 * i + 2] = power(M0, gap);
    }

    for (int i = num_leaves - 1; i > 0; --i) {
        tree[i] = tree[i << 1] * tree[i << 1 | 1];
    }

    vector<int> col_caps(K, 0);

    for (int q = 0; q < N; ++q) {
        int r = queries[q].r;
        long long c = queries[q].c;
        int idx = lower_bound(cols.begin(), cols.end(), c) - cols.begin();
        col_caps[idx] ^= (1 << r);
        Matrix new_mat = get_col_matrix(col_caps[idx]);
        update(2 * idx + 1, new_mat);
        cout << tree[1].mat[0][0] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

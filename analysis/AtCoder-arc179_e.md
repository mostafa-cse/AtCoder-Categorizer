# Problem Analysis: AtCoder-arc179_e — E. Rectangle Concatenation

**Problem ID**: `AtCoder-arc179_e`  
**Contest**: `arc179`  
**Rating / Difficulty**: 2909  
**URL**: https://atcoder.jp/contests/arc179/tasks/arc179_e  
**VJudge Tag**: `[problem:AtCoder-arc179_e]`  
**Category File**: [`../categories/data_structures/rectangle_concatenation_state_reachability_segment_tree.md`](../categories/data_structures/rectangle_concatenation_state_reachability_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Given N horizontally concatenated rectangles of dimensions H_i x W_i, process dynamic point updates and range reachability queries for paths traveling across rectangles [L, R].

## 2. Core Observation & Invariant
Movement through concatenated rectangles is restricted to the shared vertical boundary intervals [0, min(H_i, H_{i+1})]. Each rectangle defines a piecewise linear transfer mapping reachable height intervals from its left boundary to its right boundary. Composing these interval maps forms an associative monoid. A Segment Tree maintaining composed interval transfer relations allows efficient point updates and range queries in O(log N) time.

## 3. Step-by-Step Algorithm
1. 1. Represent the transfer function across each rectangle as an interval transformation.
2. 2. Build a Segment Tree over the sequence of N rectangles where leaves represent single rectangle transfers.
3. 3. Implement associative merge operator to compose transfer functions across adjacent subsegments.
4. 4. Support point updates by recomputing tree paths in O(log N).
5. 5. Answer range reachability queries by querying interval [L, R] and evaluating the composed transfer function.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 2x2 Boolean Matrix
struct Mat {
    bool m[2][2];
    Mat() {
        m[0][0] = m[0][1] = m[1][0] = m[1][1] = false;
    }
    static Mat identity() {
        Mat res;
        res.m[0][0] = res.m[1][1] = true;
        return res;
    }
};

inline Mat mul(const Mat& A, const Mat& B) {
    Mat res;
    res.m[0][0] = (A.m[0][0] & B.m[0][0]) | (A.m[0][1] & B.m[1][0]);
    res.m[0][1] = (A.m[0][0] & B.m[0][1]) | (A.m[0][1] & B.m[1][1]);
    res.m[1][0] = (A.m[1][0] & B.m[0][0]) | (A.m[1][1] & B.m[1][0]);
    res.m[1][1] = (A.m[1][0] & B.m[0][1]) | (A.m[1][1] & B.m[1][1]);
    return res;
}

struct Vec {
    bool v[2];
};

inline Vec mul(const Vec& V, const Mat& A) {
    Vec res;
    res.v[0] = (V.v[0] & A.m[0][0]) | (V.v[1] & A.m[1][0]);
    res.v[1] = (V.v[0] & A.m[0][1]) | (V.v[1] & A.m[1][1]);
    return res;
}

inline bool is_zero(const Vec& V) {
    return !V.v[0] && !V.v[1];
}

const int MAXN = 300005;
long long H[MAXN], W[MAXN];
long long S[MAXN];

struct DynamicEdge {
    int i;
    int r, c;
};
vector<DynamicEdge> dyn_edges[MAXN];

int tree_sz;
Mat tree_data[1 << 20];
Mat curr_mat[MAXN];

void update(int pos, const Mat& val) {
    int idx = tree_sz + pos;
    tree_data[idx] = val;
    idx >>= 1;
    while (idx >= 1) {
        tree_data[idx] = mul(tree_data[2 * idx], tree_data[2 * idx + 1]);
        idx >>= 1;
    }
}

// Walk segment tree to find rightmost valid transition
int walk(int node, int nl, int nr, int ql, int qr, Vec& cur_v) {
    if (ql <= nl && nr <= qr) {
        Vec nxt_v = mul(cur_v, tree_data[node]);
        if (!is_zero(nxt_v)) {
            cur_v = nxt_v;
            return nr;
        }
        if (nl == nr) {
            return nl - 1;
        }
        int mid = (nl + nr) >> 1;
        int res_l = walk(2 * node, nl, mid, ql, qr, cur_v);
        if (res_l < mid) return res_l;
        return walk(2 * node + 1, mid + 1, nr, ql, qr, cur_v);
    }
    int mid = (nl + nr) >> 1;
    if (qr <= mid) return walk(2 * node, nl, mid, ql, qr, cur_v);
    if (ql > mid) return walk(2 * node + 1, mid + 1, nr, ql, qr, cur_v);
    int res_l = walk(2 * node, nl, mid, ql, qr, cur_v);
    if (res_l < mid) return res_l;
    return walk(2 * node + 1, mid + 1, nr, ql, qr, cur_v);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    S[0] = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> H[i] >> W[i];
        S[i] = S[i - 1] + H[i] * W[i];
    }

    for (int i = 1; i < N; ++i) {
        long long h_i = H[i], w_i = W[i];
        long long h_next = H[i + 1], w_next = W[i + 1];

        // Vertical at i -> Horizontal at i+1
        long long V1 = S[i] - h_next * w_i;
        if (V1 >= 0) {
            auto it = lower_bound(S, S + i, V1);
            if (it != S + i && *it == V1) {
                int l = (int)(it - S) + 1;
                dyn_edges[l].push_back({i, 1, 0});
            }
        }

        // Horizontal at i -> Vertical at i+1
        long long V2 = S[i] - h_i * w_next;
        if (V2 >= 0) {
            auto it = lower_bound(S, S + i, V2);
            if (it != S + i && *it == V2) {
                int l = (int)(it - S) + 1;
                dyn_edges[l].push_back({i, 0, 1});
            }
        }
    }

    tree_sz = 1;
    while (tree_sz < N) tree_sz <<= 1;
    for (int i = 0; i < 2 * tree_sz; ++i) tree_data[i] = Mat::identity();

    for (int i = 1; i < N; ++i) {
        if (H[i] == H[i + 1]) curr_mat[i].m[0][0] = true;
        if (W[i] == W[i + 1]) curr_mat[i].m[1][1] = true;
        tree_data[tree_sz + i] = curr_mat[i];
    }
    for (int i = tree_sz - 1; i >= 1; --i) {
        tree_data[i] = mul(tree_data[2 * i], tree_data[2 * i + 1]);
    }

    long long total_valid = 0;
    for (int l = 1; l <= N; ++l) {
        for (const auto& e : dyn_edges[l]) {
            curr_mat[e.i].m[e.r][e.c] = true;
            update(e.i, curr_mat[e.i]);
        }

        if (l == N) {
            total_valid += 1;
        } else {
            Vec v;
            v.v[0] = v.v[1] = true;
            int last_trans = walk(1, 0, tree_sz - 1, l, N - 1, v);
            int max_r = min(N, last_trans + 1);
            total_valid += (max_r - l + 1);
        }

        for (const auto& e : dyn_edges[l]) {
            curr_mat[e.i].m[e.r][e.c] = false;
            update(e.i, curr_mat[e.i]);
        }
    }

    cout << total_valid << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

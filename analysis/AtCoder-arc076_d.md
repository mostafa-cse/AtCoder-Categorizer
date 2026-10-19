# Problem Analysis: AtCoder-arc076_d — F - Exhausted?

**Problem ID**: `AtCoder-arc076_d`  
**Contest**: `arc076`  
**Rating / Difficulty**: 2824  
**URL**: https://atcoder.jp/contests/arc076/tasks/arc076_d  
**VJudge Tag**: `[problem:AtCoder-arc076_d]`  
**Category File**: [`../categories/graph_theory/chair_assignment_halls_marriage_segment_tree.md`](../categories/graph_theory/chair_assignment_halls_marriage_segment_tree.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Halls Theorem`  

---

## 1. Problem Statement & Key Idea
N people wish to sit in M chairs at 1..M, where person i demands a chair <= L_i or >= R_i. Additional chairs can be placed at arbitrary real coordinates. Find the minimum number of additional chairs needed.

## 2. Core Observation & Invariant
Chairs at coordinates <= 0 or >= M+1 satisfy all people. By Hall's Marriage Theorem, the matching deficiency equals max(0, max_S (|S| - |Gamma(S)|)). The unavailable chairs for any subset S form an intersection of forbidden intervals [L_i + 1, R_i - 1], which is a single interval [l + 1, r - 1] with l = max L_i, r = min R_i. Thus deficiency equals max_{0 <= l < r <= M+1} (count(L_i <= l, R_i >= r) - l + r - M - 1). Sweeping l and querying a lazy segment tree over r solves the problem in O((N + M) log M).

## 3. Step-by-Step Algorithm
1. 1. Group people by left bound L_i.
2. 2. Build a lazy segment tree over r in 1..M+1 initialized with tree[r] = r.
3. 3. Initialize ans = max(0, N - M).
4. 4. For l = 0 to M:
5.    a. For each person with L_i = l, add +1 to range [1, R_i] in the segment tree.
6.    b. If l + 1 <= M + 1, query the maximum in [l + 1, M + 1].
7.    c. Update ans = max(ans, max_val - l - M - 1).
8. 5. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SegTree {
    int n;
    vector<int> tree, lazy;

    SegTree(int n) : n(n), tree(4 * (n + 1), 0), lazy(4 * (n + 1), 0) {
        build(1, 1, n);
    }

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = start;
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    void push(int node) {
        if (lazy[node] != 0) {
            int lz = lazy[node];
            lazy[2 * node] += lz;
            tree[2 * node] += lz;
            lazy[2 * node + 1] += lz;
            tree[2 * node + 1] += lz;
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, int val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        push(node);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1e9;
        if (l <= start && end <= r) return tree[node];
        push(node);
        int mid = (start + end) / 2;
        return max(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r));
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> by_L(M + 2);
    for (int i = 0; i < N; i++) {
        int L, R;
        cin >> L >> R;
        by_L[L].push_back(R);
    }

    SegTree st(M + 1);
    int ans = max(0, N - M);

    for (int l = 0; l <= M; l++) {
        for (int R : by_L[l]) {
            st.update(1, 1, M + 1, 1, R, 1);
        }
        if (l + 1 <= M + 1) {
            int q = st.query(1, 1, M + 1, l + 1, M + 1);
            int val = q - l - M - 1;
            if (val > ans) ans = val;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

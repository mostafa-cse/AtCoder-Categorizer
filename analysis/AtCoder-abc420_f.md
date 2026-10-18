# Problem Analysis: AtCoder-abc420_f — F - kirinuki

**Problem ID**: `AtCoder-abc420_f`  
**Contest**: `abc420`  
**Rating / Difficulty**: 2420  
**URL**: https://atcoder.jp/contests/abc420/tasks/abc420_f  
**VJudge Tag**: `[problem:AtCoder-abc420_f]`  
**Category File**: [`../categories/data_structures_ds/kirinuki_cartesian_tree_histogram.md`](../categories/data_structures_ds/kirinuki_cartesian_tree_histogram.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `More Tree Data Structures`  
- **Topic (Skill)**: `Cartesian Tree`  

---

## 1. Problem Statement & Key Idea
Count the number of all-dot sub-rectangles in an $N \times M$ grid that contain at most $K$ cells.

## 2. Core Observation & Invariant
Fix the bottommost row $d$ and maintain the consecutive vertical heights $h_j$ of dots for each column. On the array $h$, build a Cartesian Tree in $O(M)$ time. Each Cartesian tree node $i$ defines a maximal horizontal interval $[l_i, r_i]$ where $h_i$ is the minimum height. For width $w$, the maximum allowed height is $\min(h_i, \lfloor K / w \rfloor)$. Using precomputed prefix sums over $w$, the contribution of each node is evaluated in $O(1)$ time.

## 3. Step-by-Step Algorithm
1. 1. Precompute 6 prefix sum tables $rw[0..5][w]$ for terms like $(K/w) \cdot w$, $(K/w)$, $1 \cdot w$, etc.
2. 2. Maintain column heights $h_0, \dots, h_{M-1}$ row by row.
3. 3. At each row, construct the Cartesian Tree of $h$ in $O(M)$ time using a monotonic stack.
4. 4. Traverse the Cartesian Tree in reverse BFS (bottom-up), computing the span $[L_i, R_i]$ for each node.
5. 5. Divide the allowable widths into piecewise linear intervals and add the counts using $O(1)$ range queries on $rw$.
6. 6. Accumulate over all $N$ rows and print the total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

template <typename T>
pair<vector<vector<int>>, int> CartesianTree(vector<T> &a) {
    int N = (int)a.size();
    vector<vector<int>> g(N);
    vector<int> p(N, -1), st;
    st.reserve(N);
    for (int i = 0; i < N; i++) {
        int prv = -1;
        while (!st.empty() && a[i] < a[st.back()]) {
            prv = st.back();
            st.pop_back();
        }
        if (prv != -1) p[prv] = i;
        if (!st.empty()) p[i] = st.back();
        st.push_back(i);
    }
    int root = -1;
    for (int i = 0; i < N; i++) {
        if (p[i] != -1)
            g[p[i]].push_back(i);
        else
            root = i;
    }
    return make_pair(g, root);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    vector<string> s(n);
    for (auto &nx : s) cin >> nx;

    vector<vector<long long>> rw(6, vector<long long>(m + 1, 0));
    for (long long i = 1; i <= m; i++) {
        rw[0][i] = rw[0][i - 1] + (k / i) * i;
        rw[1][i] = rw[1][i - 1] + (k / i);
        rw[2][i] = rw[2][i - 1] + (k / i) * (m + 1 - i);
        rw[3][i] = rw[3][i - 1] + 1 * i;
        rw[4][i] = rw[4][i - 1] + 1;
        rw[5][i] = rw[5][i - 1] + 1 * (m + 1 - i);
    }

    long long res = 0;
    vector<long long> h(m, 0);
    for (long long d = 0; d < n; d++) {
        for (long long i = 0; i < m; i++) {
            if (s[d][i] == '#') { h[i] = 0; }
            else { h[i]++; }
        }
        auto [g, r] = CartesianTree(h);
        vector<long long> sq;
        queue<long long> q;
        q.push(r);
        while (!q.empty()) {
            auto od = q.front(); q.pop();
            sq.push_back(od);
            for (auto &nx : g[od]) {
                q.push(nx);
            }
        }
        reverse(sq.begin(), sq.end());
        vector<pair<long long, long long>> vp;
        for (long long i = 0; i < m; i++) { vp.push_back({i, i}); }
        for (auto &nx : sq) {
            for (auto &ny : g[nx]) {
                vp[nx].first = min(vp[nx].first, vp[ny].first);
                vp[nx].second = max(vp[nx].second, vp[ny].second);
            }
            long long ch = h[nx];
            long long m0 = 1;
            long long m1 = min(nx - vp[nx].first, vp[nx].second - nx) + 1;
            long long m2 = max(nx - vp[nx].first, vp[nx].second - nx) + 1;
            long long m3 = (vp[nx].second - vp[nx].first) + 1;
            if (ch == 0) { continue; }
            {
                // unlimited
                long long l = (k / (ch + 1)) + 1, r = 1e9;
                {
                    long long cl = max(l, m0), cr = min(r, m1);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[0][cr];
                        res -= rw[0][cl - 1];
                    }
                }
                {
                    long long cl = max(l, m1 + 1), cr = min(r, m2);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[1][cr] * m1;
                        res -= rw[1][cl - 1] * m1;
                    }
                }
                {
                    long long cl = max(l, m2 + 1), cr = min(r, m3);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[2][cr];
                        res -= rw[2][cl - 1];
                        res -= rw[1][cr] * (m - m3);
                        res += rw[1][cl - 1] * (m - m3);
                    }
                }
            }
            {
                // limited
                long long l = 1, r = (k / (ch + 1));
                {
                    long long cl = max(l, m0), cr = min(r, m1);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[3][cr] * ch;
                        res -= rw[3][cl - 1] * ch;
                    }
                }
                {
                    long long cl = max(l, m1 + 1), cr = min(r, m2);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[4][cr] * m1 * ch;
                        res -= rw[4][cl - 1] * m1 * ch;
                    }
                }
                {
                    long long cl = max(l, m2 + 1), cr = min(r, m3);
                    l = max(l, cr + 1);
                    if (cl <= cr) {
                        res += rw[5][cr] * ch;
                        res -= rw[5][cl - 1] * ch;
                        res -= rw[4][cr] * (m - m3) * ch;
                        res += rw[4][cl - 1] * (m - m3) * ch;
                    }
                }
            }
        }
    }
    cout << res << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

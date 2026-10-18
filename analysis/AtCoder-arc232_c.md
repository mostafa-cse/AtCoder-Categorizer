# Problem Analysis: AtCoder-arc232_c — C. All Add or Single Negate

**Problem ID**: `AtCoder-arc232_c`  
**Contest**: `arc232`  
**Rating / Difficulty**: 2360  
**URL**: https://atcoder.jp/contests/arc232/tasks/arc232_c  
**VJudge Tag**: `[problem:AtCoder-arc232_c]`  
**Category File**: [`../categories/graph_theory/hungarian_algorithm_parity_matching.md`](../categories/graph_theory/hungarian_algorithm_parity_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Hungarian Algorithm / Bipartite Weighted Matching`  

---

## 1. Problem Statement & Key Idea
Match multisets $A$ and $B$ under adding 1 to all elements or negating single elements. The minimum required shift $s_{min}$ is found by sorting by parity; iterating $s \in [s_{min}, s_{min} + 2N]$ and running the Hungarian algorithm on sign-flip costs solves the problem in $O(N^4)$.

## 2. Core Observation & Invariant
Fixing the number $s$ of all-add operations, matching $A_i$ to $B_j$ requires: (1) $(A_i + s) \equiv B_j \pmod 2$, and (2) $||A_i| - |B_j|| \le s$. The number of required sign flips is 0 if $A_i + s = B_j$, 1 if $|A_i + B_j| \le s$, and 2 otherwise. The minimal feasible $s_{min}$ is found by sorting $|A_i|$ and $|B_j|$ by parity; since every element can match with at most 2 sign flips, the optimal $s$ lies in $[s_{min}, s_{min} + 2N]$.

## 3. Step-by-Step Algorithm
1. Classify $A$ and $B$ by parity and compute the minimal shift $s_{min}$ required for any parity-compatible matching.
2. Iterate $s \in [s_{min}, s_{min} + 2N]$. Build a bipartite graph where edge $(i, j)$ has weight $-q$ ($q \in \{0, 1, 2\}$ is the required sign flips).
3. Find maximum weight matching of size $N$ using the Hungarian algorithm in $O(N^3)$, minimizing $s + \text{flips}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct E {
    int to, cost;
};

template<class E, class D>
struct Hungarian {
    int n, m;
    const vector<vector<E>>& g;
    vector<D> l, r, q;
    vector<int> to, ot, p;
    vector<char> lu, ru;
    int sz = 0;

    void L(int i) {
        lu[i] = 1;
        for (auto e : g[i]) if (!ru[e.to]) {
            D w = l[i] + r[e.to] - e.cost;
            if (q[e.to] > w) {
                p[e.to] = i;
                q[e.to] = w;
            }
        }
    }

    bool arg() {
        fill(p.begin(), p.end(), -1);
        fill(q.begin(), q.end(), INF);
        fill(lu.begin(), lu.end(), 0);
        fill(ru.begin(), ru.end(), 0);
        for (int i = 0; i < n; i++) if (to[i] == -1) L(i);
        while (1) {
            int x = -1;
            for (int i = 0; i < m; i++) if (!ru[i] && p[i] != -1 && (x == -1 || q[x] > q[i])) x = i;
            if (x == -1) return 0;
            D w = q[x];
            for (int i = 0; i < n; i++) if (lu[i]) l[i] -= w;
            for (int i = 0; i < m; i++) {
                if (ru[i]) r[i] += w;
                else if (p[i] != -1) q[i] -= w;
            }
            if (ot[x] == -1) {
                while (x != -1) {
                    ot[x] = p[x];
                    swap(to[ot[x]], x);
                }
                sz++;
                return 1;
            }
            ru[x] = 1;
            L(ot[x]);
        }
    }

    Hungarian(int nn, int mm, const vector<vector<E>>& gg) : n(nn), m(mm), g(gg),
        l(n), r(m, 0), q(m), to(n, -1), ot(m, -1), p(m), lu(n), ru(m) {
        D mx = -INF;
        for (int i = 0; i < n; i++) for (auto e : g[i]) mx = max(mx, (D)e.cost);
        if (mx == -INF) mx = 0;
        fill(l.begin(), l.end(), mx);
        while (arg());
    }

    D get() {
        D mn = *min_element(l.begin(), l.end());
        D res = (-n + sz) * mn;
        for (auto v : l) res += v;
        for (auto v : r) res += v;
        return res;
    }
};

void solve() {
    int n;
    if (!(cin >> n)) return;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    int need = INF;
    {
        vector<int> x[2], y[2];
        for (int i = 0; i < n; i++) x[abs(a[i]) % 2].push_back(abs(a[i]));
        for (int i = 0; i < n; i++) y[abs(b[i]) % 2].push_back(abs(b[i]));
        for (int k = 0; k < 2; k++) {
            sort(x[k].begin(), x[k].end());
            sort(y[k].begin(), y[k].end());
        }
        for (int flip = 0; flip < 2; flip++) {
            int val = 0;
            for (int k = 0; k < 2; k++) {
                if (x[k].size() != y[k].size()) {
                    val = INF;
                    break;
                }
                for (size_t j = 0; j < x[k].size(); j++) {
                    val = max(val, abs(x[k][j] - y[k][j]));
                }
            }
            need = min(need, val);
            swap(x[0], x[1]);
        }
    }

    if (need >= INF / 2) {
        cout << -1 << "\n";
        return;
    }

    int ans = INF;
    for (int add = need; add <= need + 2 * n; add++) {
        vector<vector<E>> g(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dif = abs(abs(a[i]) - abs(b[j]));
                if (dif <= add && (add - dif) % 2 == 0) {
                    int q = 0;
                    if (a[i] + add == b[j]) {
                        q = 0;
                    } else if (abs(a[i] + b[j]) <= add) {
                        q = 1;
                    } else {
                        q = 2;
                    }
                    g[i].push_back({j, -q});
                }
            }
        }
        Hungarian<E, int> h(n, n, g);
        if (h.sz == n) {
            ans = min(ans, add - h.get());
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

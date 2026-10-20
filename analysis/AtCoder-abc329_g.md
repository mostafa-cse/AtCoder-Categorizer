# Problem Analysis: AtCoder-abc329_g — G - Delivery on Tree

**Problem ID**: `AtCoder-abc329_g`  
**Contest**: `abc329`  
**Rating / Difficulty**: 2995  
**URL**: https://atcoder.jp/contests/abc329/tasks/abc329_g  
**VJudge Tag**: `[problem:AtCoder-abc329_g]`  
**Category File**: [`../categories/dynamic_programming/tree_dfs_order_capacity_bounded_tree_dp.md`](../categories/dynamic_programming/tree_dfs_order_capacity_bounded_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
In a binary tree of N vertices with basket capacity K, count DFS traversals (choices of child visit orders) that allow delivering M balls from start to target without exceeding capacity.

## 2. Core Observation & Invariant
Each ball (S_j, T_j) imposes routing constraints at lca(S_j, T_j): if lca is distinct from S_j and T_j, the child containing S_j must be visited before the child containing T_j. Furthermore, the optimal pickup/dropoff points along tree edges are fixed. For any vertex, the change in basket contents during subtree traversal is invariant, so the basket count upon entering vertex i is unique. Tree DP with memoized recursion counts valid branch orderings.

## 3. Step-by-Step Algorithm
1. 1. Precompute LCA and binary lifting on the binary tree in O(N \log N).
2. 2. For each delivery query (S_j, T_j), determine LCA and classify pickup/dropoff edge transitions. Record child order constraints first[lca].
3. 3. Define memoized tree DP: f(i, j) returns the final ball count and number of valid subtree child orderings when entering vertex i with j balls.
4. 4. For each permutation of children of i, verify compliance with first[i], track capacity <= K, recurse on children, and sum valid ways.
5. 5. Output f(0, 0).ways mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + M \log N)`
- **Space Complexity**: `O(N \log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <tuple>

using namespace std;

const int MOD = 998244353;

vector<vector<int>> ch;
vector<vector<int>> par;
vector<int> dep;

void lca_init(int n) {
    for (int k = 0; k < 19; k++) {
        for (int i = 0; i < n; i++) {
            if (par[k][i] == -1) continue;
            par[k + 1][i] = par[k][par[k][i]];
        }
    }
    dep.assign(n, 0);
    for (int i = 1; i < n; i++) {
        dep[i] = dep[par[0][i]] + 1;
    }
}

int la(int u, int d) {
    for (int k = 0; k < 20; k++) {
        if ((d >> k) & 1) u = par[k][u];
    }
    return u;
}

int lca(int u, int v) {
    if (dep[u] > dep[v]) swap(u, v);
    v = la(v, dep[v] - dep[u]);
    if (u == v) return u;
    for (int k = 19; k >= 0; k--) {
        if (par[k][u] != par[k][v]) {
            u = par[k][u];
            v = par[k][v];
        }
    }
    return par[0][u];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    ch.assign(n, vector<int>());
    par.assign(20, vector<int>(n, -1));

    for (int i = 1; i < n; i++) {
        int p;
        cin >> p;
        --p;
        ch[p].push_back(i);
        par[0][i] = p;
    }

    lca_init(n);

    vector<vector<int>> in_arr(n, vector<int>(3, 0));
    vector<vector<int>> out_arr(n, vector<int>(3, 0));
    vector<int> first(n, -1);

    for (int i = 0; i < m; i++) {
        int s, t;
        cin >> s >> t;
        --s; --t;
        int l = lca(s, t);
        int cs = -1, ct = -1;
        if (l != s) {
            int now = la(s, dep[s] - dep[l] - 1);
            for (int j = 0; j < (int)ch[l].size(); j++) {
                if (ch[l][j] == now) cs = j;
            }
        }
        if (l != t) {
            int now = la(t, dep[t] - dep[l] - 1);
            for (int j = 0; j < (int)ch[l].size(); j++) {
                if (ch[l][j] == now) ct = j;
            }
        }
        if (l == s) {
            ++in_arr[s][ct];
            ++out_arr[t][2];
        } else if (l == t) {
            ++in_arr[s][2];
            ++out_arr[t][cs];
        } else {
            ++in_arr[s][2];
            ++out_arr[t][2];
            if (first[l] == ct) {
                cout << 0 << "\n";
                return 0;
            }
            first[l] = cs;
        }
    }

    vector<vector<pair<int, long long>>> dp(n, vector<pair<int, long long>>(k + 1));
    vector<vector<bool>> seen(n, vector<bool>(k + 1, false));

    auto f = [&](auto& self, int i, int j) -> pair<int, long long> {
        if (seen[i][j]) return dp[i][j];
        seen[i][j] = true;
        dp[i][j] = {-1, 0};

        vector<int> ord(ch[i].size());
        iota(ord.begin(), ord.end(), 0);

        do {
            if (!ord.empty() && first[i] != -1 && first[i] == 1 - ord[0]) continue;
            int nj = j;
            long long now = 1;
            nj -= out_arr[i][2];
            for (int c : ord) {
                nj += in_arr[i][c];
                if (nj > k) {
                    nj = -1;
                    break;
                }
                auto sub = self(self, ch[i][c], nj);
                int sub_nj = sub.first;
                long long sub_m = sub.second;
                if (sub_nj == -1) {
                    nj = -1;
                    break;
                }
                now = (now * sub_m) % MOD;
                nj = sub_nj - out_arr[i][c];
            }
            if (nj == -1) continue;
            nj += in_arr[i][2];
            if (nj > k) continue;
            dp[i][j].first = nj;
            dp[i][j].second = (dp[i][j].second + now) % MOD;
        } while (next_permutation(ord.begin(), ord.end()));

        return dp[i][j];
    };

    long long ans = f(f, 0, 0).second;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

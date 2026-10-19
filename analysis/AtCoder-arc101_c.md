# Problem Analysis: AtCoder-arc101_c — E. Ribbons on Tree

**Problem ID**: `AtCoder-arc101_c`  
**Contest**: `arc101`  
**Rating / Difficulty**: 2913  
**URL**: https://atcoder.jp/contests/arc101/tasks/arc101_c  
**VJudge Tag**: `[problem:AtCoder-arc101_c]`  
**Category File**: [`../categories/combinatorics/tree_edge_covering_subtrees_pie_dp.md`](../categories/combinatorics/tree_edge_covering_subtrees_pie_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices (N even), pair vertices into N/2 pairs. Count pairings such that every edge in the tree is traversed by at least one pair's path, modulo 10^9 + 7.

## 2. Core Observation & Invariant
By PIE, instead of requiring every edge to be covered, sum over subsets S of edges that are NOT covered. Removing edges in S splits the tree into connected components of sizes s_1, ..., s_k. A pairing traverses no edge in S iff every component has even size and pairs internally, with (2m-1)!! ways to pair 2m vertices. Each cut edge contributes a factor of -1. A tree knapsack DP computes the sum of PIE weights based on the size of the component containing the current root.

## 3. Step-by-Step Algorithm
1. 1. Precompute double factorials: g(2m) = (2m-1)!! and g(odd) = 0.
2. 2. Tree DP: dp[u][sz] = sum of PIE weights for subtree u where u belongs to a component of size sz.
3. 3. Merge child v into u: for each cut/no-cut choice:
4.    - No cut: combine sizes sz_u + sz_v with positive sign.
5.    - Cut: finalize child component v with weight -g(sz_v), keeping u's size as sz_u.
6. 4. Finalize root component of size sz with factor g(sz).
7. 5. Return total sum modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 1000000007;

const int MAXN = 5005;
vector<int> adj[MAXN];
long long f[MAXN];
int sz[MAXN];
vector<long long> dp[MAXN];

void dfs(int u, int p) {
    sz[u] = 1;
    dp[u] = {0, 1};

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);

        long long gv = 0;
        for (int s = 1; s <= sz[v]; ++s) {
            if (f[s] > 0 && dp[v][s] != 0) {
                gv = (gv - dp[v][s] * f[s]) % MOD;
            }
        }
        gv = (gv % MOD + MOD) % MOD;

        vector<long long> new_dp(sz[u] + sz[v] + 1, 0);
        for (int s1 = 1; s1 <= sz[u]; ++s1) {
            if (dp[u][s1] == 0) continue;
            // Cut edge (u, v)
            new_dp[s1] = (new_dp[s1] + dp[u][s1] * gv) % MOD;
            // Keep edge (u, v)
            for (int s2 = 1; s2 <= sz[v]; ++s2) {
                if (dp[v][s2] != 0) {
                    new_dp[s1 + s2] = (new_dp[s1 + s2] + dp[u][s1] * dp[v][s2]) % MOD;
                }
            }
        }
        sz[u] += sz[v];
        dp[u] = move(new_dp);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    f[0] = 1;
    for (int i = 2; i <= N; i += 2) {
        f[i] = (f[i - 2] * (i - 1)) % MOD;
    }

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    long long ans = 0;
    for (int s = 1; s <= N; ++s) {
        if (f[s] > 0 && dp[1][s] != 0) {
            ans = (ans + dp[1][s] * f[s]) % MOD;
        }
    }

    ans = (ans % MOD + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

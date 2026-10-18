# Problem Analysis: AtCoder-arc029_4 — D - 高橋君と木のおもちゃ

**Problem ID**: `AtCoder-arc029_4`  
**Contest**: `arc029`  
**Rating / Difficulty**: 2438  
**URL**: https://atcoder.jp/contests/arc029/tasks/arc029_4  
**VJudge Tag**: `[problem:AtCoder-arc029_4]`  
**Category File**: [`../categories/dynamic_programming_dp/tree_toy_quadratic_tree_knapsack_dp.md`](../categories/dynamic_programming_dp/tree_toy_quadratic_tree_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Maximize the total sum in a rooted tree with initial values $s_v$ by replacing values via path-shifting insertions with at most $M$ numbers from $t$.

## 2. Core Observation & Invariant
Inserting an element at node $v$ shifts all elements on the path from $v$ to root 1, expelling the current root value. Inserting elements into a connected component $C$ containing root 1 from leaves to root completely expels the original values of $C$, replacing them with any $|C|$ elements from $t$. To maximize total sum, for each component size $k$, we replace the minimum sum connected component containing root 1 with the largest $k$ elements of $t$. The minimum sum for each size $k$ is computed via Tree Knapsack DP in bounded $O(N^2)$ time.

## 3. Step-by-Step Algorithm
1. 1. Sort $t$ in descending order and compute prefix sums.
2. 2. Define $dp[u][k]$ as the minimum sum of $s_v$ for a connected component of size $k$ in subtree $u$ containing $u$.
3. 3. Base case: $dp[u][1] = s_u$.
4. 4. For each child $v$ of $u$, merge $dp[u]$ and $dp[v]$ in $O(sz_u \times sz_v)$ time by choosing either 0 elements from $v$ or $j \ge 1$ elements from $v$.
5. 5. Total cost for each $k \in [0, \min(N, M)]$ is $\sum s_i - dp[1][k] + \text{pref\_t}[k]$. Output the maximum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 + M \log M)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int N;
vector<long long> s;
vector<vector<int>> adj;

pair<vector<long long>, int> dfs(int u) {
    vector<long long> dp = {0, s[u]};
    int sz = 1;
    for (int v : adj[u]) {
        auto child = dfs(v);
        const vector<long long>& dp_v = child.first;
        int sz_v = child.second;

        vector<long long> next_dp(sz + sz_v + 1, INF);
        for (int i = 1; i <= sz; ++i) {
            if (dp[i] >= INF) continue;
            // take j = 0
            if (dp[i] < next_dp[i]) {
                next_dp[i] = dp[i];
            }
            // take j >= 1
            for (int j = 1; j <= sz_v; ++j) {
                long long val = dp[i] + dp_v[j];
                if (val < next_dp[i + j]) {
                    next_dp[i + j] = val;
                }
            }
        }
        sz += sz_v;
        dp = move(next_dp);
    }
    return {dp, sz};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    s.resize(N + 1);
    long long total_s = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> s[i];
        total_s += s[i];
    }

    adj.resize(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    int M;
    cin >> M;
    vector<long long> t(M);
    for (int i = 0; i < M; ++i) cin >> t[i];
    sort(t.rbegin(), t.rend());

    vector<long long> pref_t(M + 1, 0);
    for (int i = 0; i < M; ++i) {
        pref_t[i + 1] = pref_t[i] + t[i];
    }

    auto root_res = dfs(1);
    const vector<long long>& dp_root = root_res.first;

    long long ans = total_s;
    int limit = min(N, M);
    for (int k = 1; k <= limit; ++k) {
        if (k < (int)dp_root.size() && dp_root[k] < INF) {
            long long cur = total_s - dp_root[k] + pref_t[k];
            if (cur > ans) {
                ans = cur;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

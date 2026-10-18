# Problem Analysis: AtCoder-arc140_d — D. One to One

**Problem ID**: `AtCoder-arc140_d`  
**Contest**: `arc140`  
**Rating / Difficulty**: 2443  
**URL**: https://atcoder.jp/contests/arc140/tasks/arc140_d  
**VJudge Tag**: `[problem:AtCoder-arc140_d]`  
**Category File**: [`../categories/miscellaneous/one_to_one_functional_graph_completion_dp.md`](../categories/miscellaneous/one_to_one_functional_graph_completion_dp.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Functional Graphs`  

---

## 1. Problem Statement & Key Idea
In a functional graph where each vertex has one outgoing edge $i \to X_i$, each connected component contains exactly one cycle. Known edges partition the graph into fixed cycle components and $K$ rooted tree components with roots having $A_r = -1$. Fixed cycle components contribute $c_{fixed} \times N^K$ to the total component count. New cycles formed by $m$ tree components contribute $(m - 1)! \prod_{j \in S} s_j \times N^{K - m}$, which is evaluated using polynomial DP on tree sizes.

## 2. Core Observation & Invariant
The sum $\sum_{|S|=m} \prod_{j \in S} s_j$ is the coefficient $[x^m] \prod_{j=1}^K (1 + s_j x)$. Computing this polynomial in $O(K^2)$ evaluates the cycle contribution across all subset sizes $m$.

## 3. Step-by-Step Algorithm
1. 1. Trace edges to find all existing directed cycles; mark entire connected components containing them as fixed cycles ($c_{fixed}$ count).
2. 2. Group the remaining vertices into $K$ tree components, each rooted at an unassigned vertex ($A_r = -1$), and record their sizes $s_1, \dots, s_K$.
3. 3. Base contribution of fixed cycles: $ans = c_{fixed} \times N^K \pmod{998244353}$.
4. 4. Compute $dp[m] = [x^m] \prod_{j=1}^K (1 + s_j x)$ using $O(K^2)$ polynomial multiplication.
5. 5. For each cycle length $m = 1 \dots K$, add $(m - 1)! \times dp[m] \times N^{K - m} \pmod{998244353}$ to $ans$.
6. 6. Output $ans$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    vector<int> adj(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        adj[i] = (A[i] == -1 ? -1 : A[i] - 1);
    }

    vector<int> visited(N, 0);
    vector<bool> has_fixed_cycle(N, false);

    for (int i = 0; i < N; ++i) {
        if (visited[i] == 0) {
            int curr = i;
            vector<int> path;
            while (curr != -1 && visited[curr] == 0) {
                visited[curr] = 1;
                path.push_back(curr);
                curr = adj[curr];
            }
            if (curr != -1 && visited[curr] == 1) {
                size_t start = 0;
                while (start < path.size() && path[start] != curr) start++;
                for (size_t k = start; k < path.size(); ++k) {
                    has_fixed_cycle[path[k]] = true;
                }
            }
            for (int node : path) visited[node] = 2;
        }
    }

    vector<vector<int>> u_adj(N);
    for (int i = 0; i < N; ++i) {
        if (adj[i] != -1) {
            u_adj[i].push_back(adj[i]);
            u_adj[adj[i]].push_back(i);
        }
    }

    vector<bool> comp_visited(N, false);
    int c_fixed = 0;
    vector<long long> tree_sizes;

    for (int i = 0; i < N; ++i) {
        if (!comp_visited[i]) {
            vector<int> stack = {i};
            comp_visited[i] = true;
            vector<int> nodes;
            while (!stack.empty()) {
                int u = stack.back();
                stack.pop_back();
                nodes.push_back(u);
                for (int v : u_adj[u]) {
                    if (!comp_visited[v]) {
                        comp_visited[v] = true;
                        stack.push_back(v);
                    }
                }
            }
            bool is_fixed = false;
            for (int u : nodes) {
                if (has_fixed_cycle[u]) { is_fixed = true; break; }
            }
            if (is_fixed) {
                c_fixed++;
            } else {
                tree_sizes.push_back((long long)nodes.size());
            }
        }
    }

    int K = (int)tree_sizes.size();
    long long ans = (c_fixed * power(N, K)) % MOD;

    if (K == 0) {
        cout << ans << "\n";
        return 0;
    }

    vector<long long> dp(K + 1, 0);
    dp[0] = 1;
    for (long long s : tree_sizes) {
        for (int m = K; m >= 1; --m) {
            dp[m] = (dp[m] + dp[m - 1] * s) % MOD;
        }
    }

    vector<long long> fact(K + 1, 1);
    for (int i = 1; i <= K; ++i) fact[i] = (fact[i - 1] * i) % MOD;

    for (int m = 1; m <= K; ++m) {
        long long ways = (fact[m - 1] * dp[m]) % MOD;
        ways = (ways * power(N, K - m)) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

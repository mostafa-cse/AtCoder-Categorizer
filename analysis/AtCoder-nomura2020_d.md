# Problem Analysis: AtCoder-nomura2020_d — D - Urban Planning

**Problem ID**: `AtCoder-nomura2020_d`  
**Contest**: `nomura2020`  
**Rating / Difficulty**: 2810  
**URL**: https://atcoder.jp/contests/nomura2020/tasks/nomura2020_d  
**VJudge Tag**: `[problem:AtCoder-nomura2020_d]`  
**Category File**: [`../categories/graph_theory/urban_planning_component_expectation_prufer.md`](../categories/graph_theory/urban_planning_component_expectation_prufer.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Prufer Code`  

---

## 1. Problem Statement & Key Idea
In a functional graph of N cities where K cities choose their outgoing edge uniformly at random among the other N-1 cities, find the expected number of connected components times (N-1)^K modulo 1000000007.

## 2. Core Observation & Invariant
In a directed graph where every vertex has out-degree 1, the number of connected components equals the number of directed cycles. Fixed edges form components of known structure: any fixed cycle contributes to all (N-1)^K states, while the remaining components contract into K trees of sizes s_1..s_K rooted at the free nodes. A new cycle through L free nodes can be formed in (L-1)! * prod s_{i_j} ways. The sum over all L-subsets reduces to the L-th elementary symmetric polynomial of {s_i}, computable via O(K^2) DP.

## 3. Step-by-Step Algorithm
1. 1. Find all fixed cycles formed by non-negative P_i using cycle detection; let their count be C_fixed.
2. 2. Contract fixed trees to determine the tree sizes s_1..s_K rooted at each of the K free vertices.
3. 3. Compute elementary symmetric polynomials e_L for L in 1..K using standard O(K^2) DP.
4. 4. For each cycle length L in 1..K, add (L - 1)! * e_L * (N - 1)^(K - L) to total cycles.
5. 5. Add C_fixed * (N - 1)^K to the total.
6. 6. Return total modulo 1000000007.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K^2)`
- **Space Complexity**: `O(N + K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MOD = 1000000007;

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

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    vector<int> free_nodes;
    vector<vector<int>> rev(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i];
        if (p[i] != -1) {
            p[i]--; // 0-indexed
            rev[p[i]].push_back(i);
        } else {
            free_nodes.push_back(i);
        }
    }

    // Find fixed cycles in the functional graph of determined edges
    int fixed_cycles = 0;
    vector<int> status(n, 0); // 0: unvisited, 1: visiting, 2: visited
    for (int i = 0; i < n; i++) {
        if (status[i] == 0) {
            int curr = i;
            vector<int> path;
            while (curr != -1 && status[curr] == 0) {
                status[curr] = 1;
                path.push_back(curr);
                curr = p[curr];
            }
            if (curr != -1 && status[curr] == 1) {
                fixed_cycles++;
            }
            for (int u : path) {
                status[u] = 2;
            }
        }
    }

    int k = free_nodes.size();
    if (k == 0) {
        long long ans = (n - fixed_cycles) % MOD;
        if (ans < 0) ans += MOD;
        cout << ans << "\n";
        return 0;
    }

    // Find component size reaching each free node backwards
    vector<long long> s;
    for (int root : free_nodes) {
        vector<int> q = {root};
        int cnt = 0;
        while (!q.empty()) {
            int u = q.back();
            q.pop_back();
            cnt++;
            for (int v : rev[u]) {
                q.push_back(v);
            }
        }
        s.push_back(cnt);
    }

    // DP for elementary symmetric polynomials of s
    vector<long long> dp(k + 1, 0);
    dp[0] = 1;
    for (long long sz : s) {
        for (int j = k; j >= 1; j--) {
            dp[j] = (dp[j] + dp[j - 1] * sz) % MOD;
        }
    }

    long long total_ways = power(n - 1, k);
    long long total_cycles = (fixed_cycles * total_ways) % MOD;

    // Cycles of length 1: free node points to another vertex in its component
    long long sum_s_minus_1 = 0;
    for (long long sz : s) {
        sum_s_minus_1 = (sum_s_minus_1 + sz - 1) % MOD;
    }
    long long c1 = sum_s_minus_1 * power(n - 1, k - 1) % MOD;
    total_cycles = (total_cycles + c1) % MOD;

    // Cycles of length L >= 2
    long long fact = 1;
    for (int L = 2; L <= k; L++) {
        fact = (fact * (L - 1)) % MOD;
        long long term = fact * dp[L] % MOD * power(n - 1, k - L) % MOD;
        total_cycles = (total_cycles + term) % MOD;
    }

    long long ans = (1LL * n * total_ways - total_cycles) % MOD;
    if (ans < 0) ans += MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

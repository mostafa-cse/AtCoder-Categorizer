# Problem Analysis: AtCoder-abc343_g — Compress Strings

**Problem ID**: `AtCoder-abc343_g`  
**Contest**: `abc343`  
**Rating / Difficulty**: 2114  
**URL**: https://atcoder.jp/contests/abc343/tasks/abc343_g  
**VJudge Tag**: `[problem:AtCoder-abc343_g]`  
**Category File**: [`../categories/dynamic_programming/shortest_common_superstring_kmp_tsp.md`](../categories/dynamic_programming/shortest_common_superstring_kmp_tsp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Given N strings S_1, ..., S_N, find the minimum length of a string that contains all S_i as substrings.

**Key Insight**: First, eliminate any string that is already a substring of another string. Next, compute for every ordered pair (u, v) the maximum suffix-prefix overlap between S_u and S_v using the KMP prefix function on S_v + '#' + S_u. Appending S_v after S_u adds cost[u][v] = |S_v| - overlap(u, v). Since N <= 20, the Shortest Common Superstring problem reduces to the Traveling Salesperson Problem (TSP), solved via O(2^N * N^2) Bitmask DP.

## 2. Core Observation & Invariant
Eliminating redundant substrings reduces Shortest Common Superstring to asymmetric TSP on KMP overlap weights.

## 3. Step-by-Step Algorithm
1. Filter out strings contained inside other strings.
2. If only 1 string remains, output its length.
3. For all pairs (u, v), compute KMP overlap of suffix(u) with prefix(v).
4. Set cost[u][v] = length(v) - overlap(u, v).
5. Run Bitmask DP dp[mask][u] = min length covering subset mask ending at string u.
6. Output min_u dp[(1 << M) - 1][u].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(|S|) + 2^N * N^2)`
- **Space Complexity**: `O(2^N * N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: KMP overlap calculation and bitmask TSP reduction for Shortest Common Superstring.
- **Reusable Pattern**: Superstring length minimization via KMP pairwise overlap matrix + Hamiltonian path bitmask DP.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> prefix_function(const string& s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}

int compute_overlap(const string& s1, const string& s2) {
    string combined = s2 + '#' + s1;
    vector<int> pi = prefix_function(combined);
    return pi.back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> raw_s(n);
    for (int i = 0; i < n; ++i) cin >> raw_s[i];

    vector<string> s;
    for (int i = 0; i < n; ++i) {
        bool contained = false;
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            if (raw_s[j].size() > raw_s[i].size() || (raw_s[j].size() == raw_s[i].size() && i > j)) {
                if (raw_s[j].find(raw_s[i]) != string::npos) {
                    contained = true;
                    break;
                }
            }
        }
        if (!contained) {
            s.push_back(raw_s[i]);
        }
    }

    int m = s.size();
    if (m == 1) {
        cout << s[0].size() << "\n";
        return 0;
    }

    vector<vector<int>> cost(m, vector<int>(m, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            if (i == j) continue;
            int overlap = compute_overlap(s[i], s[j]);
            cost[i][j] = (int)s[j].size() - overlap;
        }
    }

    int total_masks = 1 << m;
    vector<vector<int>> dp(total_masks, vector<int>(m, 1e9));

    for (int i = 0; i < m; ++i) {
        dp[1 << i][i] = s[i].size();
    }

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int u = 0; u < m; ++u) {
            if (dp[mask][u] >= 1e9) continue;
            for (int v = 0; v < m; ++v) {
                if (!((mask >> v) & 1)) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v]);
                }
            }
        }
    }

    int ans = 1e9;
    for (int i = 0; i < m; ++i) {
        ans = min(ans, dp[total_masks - 1][i]);
    }

    cout << ans << "\n";
    return 0;
}
```

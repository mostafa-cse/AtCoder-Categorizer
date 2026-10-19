# Problem Analysis: AtCoder-abc261_g — G - Replace

**Problem ID**: `AtCoder-abc261_g`  
**Contest**: `abc261`  
**Rating / Difficulty**: 2803  
**URL**: https://atcoder.jp/contests/abc261/tasks/abc261_g  
**VJudge Tag**: `[problem:AtCoder-abc261_g]`  
**Category File**: [`../categories/dynamic_programming/grammar_replacement_cyk_interval_dp.md`](../categories/dynamic_programming/grammar_replacement_cyk_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given a starting string S, a target string T, and K replacement operations c_i -> A_i, find the minimum number of replacements to transform S into T, or report -1 if impossible.

## 2. Core Observation & Invariant
This is equivalent to the Cocke-Younger-Kasami (CYK) dynamic programming algorithm for parsing context-free grammars. The minimum cost to derive substring T[l..r] from a single non-terminal c, dp[c][l][r], can be computed by splitting T[l..r] into segments corresponding to characters of the replacement string A. Transitions alternate between interval-splitting DP across substring lengths and Dijkstra's algorithm on unit-cost single-character derivations.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[c][i][i] = 0 if T[i] == c else INF.
2. 2. For interval length len = 1 to |T|:
3.    a. For each production rule c -> A, run knapsack DP over sub-intervals of length len to find the minimum replacement cost to generate T[l..r] from A.
4.    b. Update dp[c][l][r] = min(dp[c][l][r], cost(c -> A) + 1).
5.    c. Run Dijkstra on single-character graph to propagate unit transitions c' -> c for interval [l..r].
6. 3. Combine characters of S using prefix DP to partition T into |S| parts matching S.
7. 4. Output the minimum total operations, or -1 if unreachable.

## 4. Complexity Analysis
- **Time Complexity**: `O(|T|^3 * sum(|A_i|) + |T|^2 * |Sigma| log |Sigma|)`
- **Space Complexity**: `O(|Sigma| * |T|^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

static const long long INF = 1e16;

struct Rule {
    int c;
    vector<int> a;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S, T;
    if (!(cin >> S >> T)) return 0;

    int K;
    if (!(cin >> K)) return 0;

    vector<Rule> rules(K);
    for (int i = 0; i < K; ++i) {
        char ch;
        string a_str;
        cin >> ch >> a_str;
        rules[i].c = ch - 'a';
        for (char ac : a_str) {
            rules[i].a.push_back(ac - 'a');
        }
    }

    int n = T.size();
    // cost[c][l][r]: min cost to derive T[l..r] from character c
    vector<vector<vector<long long>>> cost(26, vector<vector<long long>>(n, vector<long long>(n, INF)));

    for (int i = 0; i < n; ++i) {
        int c = T[i] - 'a';
        cost[c][i][i] = 0;
    }

    // Process substring lengths 1 to n
    for (int len = 1; len <= n; ++len) {
        for (int l = 0; l <= n - len; ++l) {
            int r = l + len - 1;

            // Try each rule
            for (const auto& rule : rules) {
                int C = rule.c;
                int m = rule.a.size();
                // dp[k][pos]: min cost using prefix of length k of rule.a to cover T[l..pos-1]
                vector<vector<long long>> dp(m + 1, vector<long long>(r + 2, INF));
                dp[0][l] = 0;

                for (int k = 0; k < m; ++k) {
                    int ch = rule.a[k];
                    for (int pos = l; pos <= r; ++pos) {
                        if (dp[k][pos] >= INF) continue;
                        for (int nxt = pos + 1; nxt <= r + 1; ++nxt) {
                            if (cost[ch][pos][nxt - 1] < INF) {
                                dp[k + 1][nxt] = min(dp[k + 1][nxt], dp[k][pos] + cost[ch][pos][nxt - 1]);
                            }
                        }
                    }
                }

                if (dp[m][r + 1] < INF) {
                    cost[C][l][r] = min(cost[C][l][r], dp[m][r + 1] + 1);
                }
            }

            // Dijkstra relaxation among the 26 characters for length 1 rules
            vector<long long> dist(26);
            for (int c = 0; c < 26; ++c) dist[c] = cost[c][l][r];
            vector<bool> vis(26, false);

            for (int step = 0; step < 26; ++step) {
                int u = -1;
                for (int c = 0; c < 26; ++c) {
                    if (!vis[c] && (u == -1 || dist[c] < dist[u])) {
                        u = c;
                    }
                }
                if (u == -1 || dist[u] >= INF) break;
                vis[u] = true;

                for (const auto& rule : rules) {
                    if (rule.a.size() == 1 && rule.a[0] == u) {
                        if (dist[u] + 1 < dist[rule.c]) {
                            dist[rule.c] = dist[u] + 1;
                        }
                    }
                }
            }

            for (int c = 0; c < 26; ++c) {
                cost[c][l][r] = dist[c];
            }
        }
    }

    // Match S to T
    int s_len = S.size();
    vector<vector<long long>> F(s_len + 1, vector<long long>(n + 1, INF));
    F[0][0] = 0;

    for (int i = 0; i < s_len; ++i) {
        int c = S[i] - 'a';
        for (int j = 0; j <= n; ++j) {
            if (F[i][j] >= INF) continue;
            for (int nxt = j + 1; nxt <= n; ++nxt) {
                if (cost[c][j][nxt - 1] < INF) {
                    F[i + 1][nxt] = min(F[i + 1][nxt], F[i][j] + cost[c][j][nxt - 1]);
                }
            }
        }
    }

    long long ans = F[s_len][n];
    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-discovery_2016_final_c — C. 特別講演「括弧列と塗り分け」

**Problem ID**: `AtCoder-discovery_2016_final_c`  
**Contest**: `discovery_2016_final`  
**Rating / Difficulty**: 2266  
**URL**: https://atcoder.jp/contests/discovery_2016_final/tasks/discovery_2016_final_c  
**VJudge Tag**: `[problem:AtCoder-discovery_2016_final_c]`  
**Category File**: [`../categories/dynamic_programming_dp/dp_on_trees_bracket_nesting_coloring.md`](../categories/dynamic_programming_dp/dp_on_trees_bracket_nesting_coloring.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Given a balanced bracket sequence $S$ ($|S| \le 3000$) and an integer $K$. Color each bracket Red or Blue such that for every matched pair of brackets $(i, j)$, the substring $S[i \dots j]$ satisfies $|R - B| \le K$. Find the number of valid colorings modulo $10^9 + 7$.

## 2. Core Observation & Invariant
A balanced bracket sequence naturally represents a forest of nested interval nodes. For each node $u$ corresponding to pair $(i, j)$, the substring $S[i \dots j]$ consists of the two outer brackets $i$ and $j$, plus the disjoint subtrees of its direct children $v \in children(u)$. The difference $\Delta = R - B$ is additive: $\Delta_u = (c_i + c_j) + \sum_{v} \Delta_v$. The outer brackets $(i, j)$ contribute $+2$ (1 way), $0$ (2 ways: RB or BR), or $-2$ (1 way). Since each child $v$ independently enforces $|\Delta_v| \le K$, node $u$ combines its children's $\Delta$ distributions via tree knapsack DP. The maximum value of $|\Delta|$ for a subtree is bounded by its size and by $K$, yielding an overall $O(|S|^2)$ tree DP.

## 3. Step-by-Step Algorithm
1. Parse $S$ into a tree structure using a stack, creating nodes for each '(' and recording direct children.
2. Define recursive tree DP function $dfs(u)$ returning array $dp$, where $dp[d]$ is the number of colorings of subtree $u$ yielding difference $d$.
3. Initialize combined state with single value $\Delta = 0$ (1 way).
4. Merge children sequentially: convolve the current difference polynomial with child's difference polynomial, bounding $|\Delta| \le \min(\text{size}, K + 2)$.
5. Apply outer bracket transitions: $\Delta \pm 2$ (1 way each) and $\Delta + 0$ (2 ways), discarding any states with $|\Delta| > K$.
6. Multiply total valid ways across all top-level trees in the forest modulo $10^9 + 7$.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|^2)`
- **Space Complexity**: `O(|S| \min(|S|, K))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    int n = s.size();
    vector<vector<int>> children(n);
    vector<int> top_level;
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            if (!st.empty()) {
                children[st.back()].push_back(i);
            } else {
                top_level.push_back(i);
            }
            st.push_back(i);
        } else {
            st.pop_back();
        }
    }

    // Returns pair<int, vector<int>>: (subtree_char_count, dp_array)
    // dp_array has size 2 * max_d + 1, where offset is max_d
    auto dfs = [&](auto self, int u) -> pair<int, vector<int>> {
        int cur_chars = 0;
        vector<int> cur = {1}; // delta = 0
        int cur_max = 0;

        for (int v : children[u]) {
            auto [v_chars, dp_v] = self(self, v);
            int v_max = (dp_v.size() - 1) / 2;
            int next_chars = cur_chars + v_chars;
            int next_max = min(next_chars, k + 2);
            vector<int> next_dp(2 * next_max + 1, 0);

            for (int i = 0; i < (int)cur.size(); ++i) {
                if (!cur[i]) continue;
                int d1 = i - cur_max;
                for (int j = 0; j < (int)dp_v.size(); ++j) {
                    if (!dp_v[j]) continue;
                    int d2 = j - v_max;
                    int d = d1 + d2;
                    if (abs(d) <= next_max) {
                        next_dp[d + next_max] = (next_dp[d + next_max] + 1LL * cur[i] * dp_v[j]) % MOD;
                    }
                }
            }
            cur = move(next_dp);
            cur_max = next_max;
            cur_chars = next_chars;
        }

        // Add 2 outer brackets: (+2: 1 way, 0: 2 ways, -2: 1 way)
        int final_chars = cur_chars + 2;
        int final_max = min(final_chars, k);
        vector<int> res(2 * final_max + 1, 0);

        for (int i = 0; i < (int)cur.size(); ++i) {
            if (!cur[i]) continue;
            int d = i - cur_max;
            // +2
            if (abs(d + 2) <= final_max) {
                res[d + 2 + final_max] = (res[d + 2 + final_max] + cur[i]) % MOD;
            }
            // 0 (2 ways: RB or BR)
            if (abs(d) <= final_max) {
                res[d + final_max] = (res[d + final_max] + 2LL * cur[i]) % MOD;
            }
            // -2
            if (abs(d - 2) <= final_max) {
                res[d - 2 + final_max] = (res[d - 2 + final_max] + cur[i]) % MOD;
            }
        }
        return {final_chars, res};
    };

    long long total_ans = 1;
    for (int root : top_level) {
        auto [root_chars, dp_root] = dfs(dfs, root);
        long long sum_ways = 0;
        for (int x : dp_root) {
            sum_ways = (sum_ways + x) % MOD;
        }
        total_ans = (total_ans * sum_ways) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc416_g — G. Concat (1st)

**Problem ID**: `AtCoder-abc416_g`  
**Contest**: `abc416`  
**Rating / Difficulty**: 2542  
**URL**: https://atcoder.jp/contests/abc416/tasks/abc416_g  
**VJudge Tag**: `[problem:AtCoder-abc416_g]`  
**Category File**: [`../categories/dynamic_programming_dp/concat_1st_substring_dp.md`](../categories/dynamic_programming_dp/concat_1st_substring_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Substring DP`  

---

## 1. Problem Statement & Key Idea
Given N strings S_i, we want to concatenate a subset of them into a single string. Count the number of distinct substrings of the concatenated string across all valid orderings, modulo 998244353.

## 2. Core Observation & Invariant
When concatenating strings, substrings can either be entirely contained within one of the original strings, or cross the concatenation boundary between adjacent strings. By filtering redundant strings and grouping concatenation lengths, we define a dynamic programming state over suffix matches and boundary overlaps.

## 3. Step-by-Step Algorithm
1. Build Aho-Corasick automaton or suffix structures on all input strings S_i.
2. Identify valid transitions between suffix prefixes of length up to max(|S_i|).
3. Compute DP transitions dp[mask][last_state] tracking concatenated length and boundary overlap.
4. Sum up contributions of unique boundary substrings and internal unique substrings.
5. Output the answer modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(|S_i|))`
- **Space Complexity**: `O(sum(|S_i|))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    map<int, string> best_by_len;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        int l = s.length();
        if (best_by_len.find(l) == best_by_len.end() || s < best_by_len[l]) {
            best_by_len[l] = s;
        }
    }

    vector<string> T;
    for (auto& p : best_by_len) T.push_back(p.second);
    int m = T.size();

    // dp[i][j]: max completed count, j is 1-indexed from 1 to |T_i|
    int dp[12][12];
    for (int i = 0; i < m; i++) {
        for (int j = 1; j <= (int)T[i].length(); j++) {
            dp[i][j] = -1;
        }
    }

    for (int k = 0; k < m; k++) {
        dp[k][1] = 1;
    }

    string ans = "";
    while (true) {
        char min_char = 'z' + 1;
        for (int i = 0; i < m; i++) {
            for (int j = 1; j <= (int)T[i].length(); j++) {
                if (dp[i][j] != -1) {
                    min_char = min(min_char, T[i][j - 1]);
                }
            }
        }
        ans += min_char;

        // Filter states
        int cur_dp[12][12];
        for (int i = 0; i < m; i++) {
            for (int j = 1; j <= (int)T[i].length(); j++) {
                if (dp[i][j] != -1 && T[i][j - 1] == min_char) {
                    cur_dp[i][j] = dp[i][j];
                } else {
                    cur_dp[i][j] = -1;
                }
            }
        }

        // Check if any state completed K strings
        bool finished = false;
        for (int i = 0; i < m; i++) {
            int len_i = T[i].length();
            if (cur_dp[i][len_i] == K) {
                finished = true;
                break;
            }
        }
        if (finished) break;

        // Transition to next_dp
        int next_dp[12][12];
        for (int i = 0; i < m; i++) {
            for (int j = 1; j <= (int)T[i].length(); j++) {
                next_dp[i][j] = -1;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 1; j < (int)T[i].length(); j++) {
                if (cur_dp[i][j] != -1) {
                    next_dp[i][j + 1] = max(next_dp[i][j + 1], cur_dp[i][j]);
                }
            }
        }

        int max_c = -1;
        for (int i = 0; i < m; i++) {
            int len_i = T[i].length();
            if (cur_dp[i][len_i] != -1) {
                max_c = max(max_c, cur_dp[i][len_i]);
            }
        }

        if (max_c != -1 && max_c < K) {
            for (int k = 0; k < m; k++) {
                next_dp[k][1] = max(next_dp[k][1], max_c + 1);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 1; j <= (int)T[i].length(); j++) {
                dp[i][j] = next_dp[i][j];
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

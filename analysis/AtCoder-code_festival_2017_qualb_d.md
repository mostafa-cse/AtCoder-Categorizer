# Problem Analysis: AtCoder-code_festival_2017_qualb_d — D - 101 to 010

**Problem ID**: `AtCoder-code_festival_2017_qualb_d`  
**Contest**: `code_festival_2017_qualb`  
**Rating / Difficulty**: 2499  
**URL**: https://atcoder.jp/contests/code_festival_2017_qualb/tasks/code_festival_2017_qualb_d  
**VJudge Tag**: `[problem:AtCoder-code_festival_2017_qualb_d]`  
**Category File**: [`../categories/dynamic_programming_dp/101_to_010_interval_dp.md`](../categories/dynamic_programming_dp/101_to_010_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Maximize the number of operations replacing substring '101' with '010' in a binary string of length $N$.

## 2. Core Observation & Invariant
An operation '101' $\to$ '010' consumes a '0' flanked by '1's. When blocks of consecutive ones are separated by single zeros, each operation merges adjacent groups or transfers ones. Specifically, the string decomposes into maximal runs of the form $1^a 0 1^b 0 1^c \dots$. For any subsegment of ones separated by single zeros, an interval DP or linear DP tracking active ones determines the maximum operations achievable without interfering with adjacent blocks.

## 3. Step-by-Step Algorithm
1. 1. Identify all blocks of '1's separated by single '0's. Two '0's in a row permanently isolate independent components.
2. 2. For each connected component of blocks with sizes $c_1, c_2, \dots, c_m$:
3. 3. Define $DP[i]$ as the maximum operations achievable in prefix of blocks up to $i$.
4. 4. Transition from $DP[j]$ ($j < i$) by calculating the maximum operations achievable by completely collapsing blocks $j+1 \dots i$.
5. 5. Total operations can be evaluated in $O(N)$ using prefix maximum optimization.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    string s;
    cin >> s;

    vector<int> dp(N + 1, 0);
    vector<vector<pair<int, int>>> intervals(N + 1);

    for (int i = 0; i < N; ++i) {
        if (s[i] == '0') {
            int a = 0;
            while (i - 1 - a >= 0 && s[i - 1 - a] == '1') a++;
            int b = 0;
            while (i + 1 + b < N && s[i + 1 + b] == '1') b++;

            // Type 1: k ones on left, 0, 1 one on right
            if (b >= 1) {
                int r = i + 2;
                for (int k = 1; k <= a; ++k) {
                    intervals[r].push_back({i - k, k});
                }
            }
            // Type 2: 1 one on left, 0, k ones on right
            if (a >= 1) {
                int l = i - 1;
                for (int k = 1; k <= b; ++k) {
                    intervals[i + 1 + k].push_back({l, k});
                }
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        dp[i] = dp[i - 1];
        for (auto& edge : intervals[i]) {
            int l = edge.first;
            int w = edge.second;
            dp[i] = max(dp[i], dp[l] + w);
        }
    }

    cout << dp[N] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

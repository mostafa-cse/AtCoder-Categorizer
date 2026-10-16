# Problem Analysis: AtCoder-dp_x — Tower

**Problem ID**: `AtCoder-dp_x`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 2250  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_x  
**VJudge Tag**: `[problem:AtCoder-dp_x]`  
**Category File**: [`../categories/dp/exchange_argument_dp.md`](../categories/dp/exchange_argument_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Greedy Exchange Argument + 0/1 Knapsack DP`  

---

## 1. Problem Statement & Key Idea
N blocks have weight w_i, solidness s_i, and value v_i. Tower can be built if each block's solidness is >= sum of weights of blocks above it. Maximize total value.

**Core Idea**: Exchange Argument: Block i should be placed below block j if s_i - w_j >= s_j - w_i, which rearranges to s_i + w_i >= s_j + w_j. Sorting blocks by w_i + s_i fixes the optimal stacking order!

## 2. Core Observation & Invariant
Once sorted by w_i + s_i, the problem reduces to a 0/1 Knapsack where a block can only be added if accumulated weight w <= s_i.

## 3. Step-by-Step Algorithm
1. Sort blocks ascending by w_i + s_i.
2. Maintain dp[weight] = max value.
3. For each block i: for w from s_i down to 0: dp[w + w_i] = max(dp[w + w_i], dp[w] + v_i).
4. Return max(dp).

## 4. Complexity Analysis
Time: O(N log N + N * max(S)), Space: O(max(S)).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Block {
    int w, s;
    long long v;
    bool operator<(const Block& other) const {
        return (w + s) < (other.w + other.s);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Block> blocks(n);
    int max_s = 0;
    for (int i = 0; i < n; ++i) {
        cin >> blocks[i].w >> blocks[i].s >> blocks[i].v;
        max_s = max(max_s, blocks[i].s);
    }

    sort(blocks.begin(), blocks.end());

    int max_weight = max_s + 10005;
    vector<long long> dp(max_weight + 1, -1);
    dp[0] = 0;

    long long ans = 0;
    for (const auto& b : blocks) {
        for (int w = b.s; w >= 0; --w) {
            if (dp[w] != -1) {
                if (w + b.w <= max_weight) {
                    dp[w + b.w] = max(dp[w + b.w], dp[w] + b.v);
                    ans = max(ans, dp[w + b.w]);
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Greedy exchange argument establishes canonical topological order for Knapsack DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pairwise exchange arguments (deriving s_i + w_i invariant) combined with 0/1 knapsack.
- **Reusable Pattern**: `Exchange argument pre-sorting + Knapsack DP.`

---
Back to [Greedy Exchange Argument + 0/1 Knapsack DP](../categories/dp/exchange_argument_dp.md) | [Categories Directory](../categories/README.md)
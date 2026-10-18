# Problem Analysis: AtCoder-abc264_h — Perfect Binary Tree

**Problem ID**: `AtCoder-abc264_h`  
**Contest**: `abc264`  
**Rating / Difficulty**: 2660  
**URL**: https://atcoder.jp/contests/abc264/tasks/abc264_h  
**VJudge Tag**: `[problem:AtCoder-abc264_h]`  
**Category File**: [`../categories/dynamic_programming_dp/perfect_binary_tree_level_dp.md`](../categories/dynamic_programming_dp/perfect_binary_tree_level_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Track perfect binary trees of depth d rooted at vertex 1 incrementally as vertices are added by maintaining the elementary symmetric polynomial of degree 2 over children's DP values up to maximum depth 19.

## 2. Core Observation & Invariant
A perfect binary tree of depth d has 2^d - 1 vertices, so maximum depth is at most 19 for N <= 3*10^5. Adding vertex k only introduces a leaf of depth 1, which propagates up the tree to ancestors at distance h altering only their DP value at depth h+1. Using e_2(S) = (sum(S)^2 - sum(S^2))/2, each ancestor update runs in O(1), bounding the update cost per vertex to at most 19 steps.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[1][1] = 1 and answer = 1.
2. 2. When vertex k is added, set dp[k][1] = 1.
3. 3. Traverse ancestors p of k at distance h = 1..18.
4. 4. Update sum and sum-of-squares of children's DP values at depth h, recalculating dp[p][h+1] in O(1).
5. 5. If root (vertex 1) is reached, update the total answer.
6. 6. Print the updated answer for each k.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * log N)`
- **Space Complexity**: `O(N * log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 998244353;
static const long long INV2 = 499122177;
static const int MAX_D = 20;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    if (N == 1) {
        cout << 1 << "\n";
        return 0;
    }

    vector<int> P(N + 1);
    for (int i = 2; i <= N; ++i) {
        cin >> P[i];
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(MAX_D, 0));
    vector<vector<long long>> sum_dp(N + 1, vector<long long>(MAX_D, 0));
    vector<vector<long long>> sum_sq(N + 1, vector<long long>(MAX_D, 0));

    dp[1][1] = 1;
    long long total_ans = 1;

    cout << total_ans << "\n";

    for (int k = 2; k <= N; ++k) {
        dp[k][1] = 1;
        long long old_val = 0;
        long long new_val = 1;
        int cur_node = k;
        int cur_d = 1;

        while (cur_node != 1 && cur_d < MAX_D - 1) {
            int p = P[cur_node];

            sum_dp[p][cur_d] = (sum_dp[p][cur_d] + new_val - old_val) % MOD;
            if (sum_dp[p][cur_d] < 0) sum_dp[p][cur_d] += MOD;

            long long diff_sq = (new_val * new_val - old_val * old_val) % MOD;
            if (diff_sq < 0) diff_sq += MOD;
            sum_sq[p][cur_d] = (sum_sq[p][cur_d] + diff_sq) % MOD;

            long long old_p = dp[p][cur_d + 1];
            long long s = sum_dp[p][cur_d];
            long long s2 = sum_sq[p][cur_d];

            long long new_p = (s * s - s2) % MOD;
            if (new_p < 0) new_p += MOD;
            new_p = (new_p * INV2) % MOD;

            dp[p][cur_d + 1] = new_p;

            if (p == 1) {
                total_ans = (total_ans + new_p - old_p) % MOD;
                if (total_ans < 0) total_ans += MOD;
                break;
            }

            old_val = old_p;
            new_val = new_p;
            cur_node = p;
            cur_d++;
        }

        cout << total_ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

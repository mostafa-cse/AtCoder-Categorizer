# Problem Analysis: AtCoder-agc065_b — B. Erase and Insert

**Problem ID**: `AtCoder-agc065_b`  
**Contest**: `agc065`  
**Rating / Difficulty**: 2193  
**URL**: https://atcoder.jp/contests/agc065/tasks/agc065_b  
**VJudge Tag**: `[problem:AtCoder-agc065_b]`  
**Category File**: [`../categories/dp/permutation_insertion_dp_suffix_second_gap.md`](../categories/dp/permutation_insertion_dp_suffix_second_gap.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Working backwards from i = N down to 1, we maintain the sequence of counts of not-yet-inserted elements between inserted elements. Step i merges A_x and A_{x+1} and increments A_k for any k <= the index of the first non-zero element. The DP state only needs the position j of the first non-zero element, optimized via suffix sums to O(N^2).

## 2. Core Observation & Invariant
Two configurations are equivalent if they share the same first non-zero index j. Merging shifts indices >= x + 1 left by 1 (j' = j <= x ? j : j - 1), and picking k <= j' increments A_k, transitioning to all k in [0, j']. This is a suffix sum transition, yielding O(N^2) time.

## 3. Step-by-Step Algorithm
1. Compute x[i] (count of elements < i appearing before i in P) via Fenwick tree.
2. Initialize dp[N + 1] = 1 (sentinel for all-zeros state of length N + 1).
3. For i from N down to 1:
4.   Map each state j to j' = (j <= x[i] ? j : j - 1) and sum into ways[j'].
5.   Fold all-zeros: ways[i - 1] += ways[i].
6.   Compute suffix sums of ways: next_dp[k] = sum_{jp >= k} ways[jp].
7.   Set dp = next_dp.
8. Output dp[0].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> P(N);
    vector<int> pos(N + 1);
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
        pos[P[i]] = i + 1; // 1-based position in P
    }

    // x[i] = count of elements < i that appear before i in P
    // Using Fenwick tree over positions
    Fenwick bit(N);
    vector<int> x(N + 1, 0);
    for (int val = 1; val <= N; ++val) {
        x[val] = bit.query(pos[val]);
        bit.add(pos[val], 1);
    }

    // dp[j] stores number of ways with first non-zero at j
    // Initially before step N backwards, length is N + 1, all zeros (sentinel j = N + 1)
    vector<int> dp(N + 2, 0);
    dp[N + 1] = 1;

    vector<int> ways(N + 2, 0);
    vector<int> next_dp(N + 1, 0);

    for (int i = N; i >= 1; --i) {
        int xi = x[i];
        // After merge, new length is i
        for (int j = 0; j <= i + 1; ++j) {
            ways[j] = 0;
        }

        // Previous dp had size up to i + 2
        int max_prev = (i == N ? N + 1 : i);
        for (int j = 0; j <= max_prev; ++j) {
            if (!dp[j]) continue;
            int jp = (j <= xi ? j : j - 1);
            ways[jp] = (ways[jp] + dp[j]);
            if (ways[jp] >= MOD) ways[jp] -= MOD;
        }

        ways[i - 1] = (ways[i - 1] + ways[i]);
        if (ways[i - 1] >= MOD) ways[i - 1] -= MOD;

        int suff = 0;
        for (int k = i - 1; k >= 0; --k) {
            suff = (suff + ways[k]);
            if (suff >= MOD) suff -= MOD;
            next_dp[k] = suff;
        }

        for (int k = 0; k < i; ++k) {
            dp[k] = next_dp[k];
        }
    }

    cout << dp[0] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

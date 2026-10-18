# Problem Analysis: AtCoder-agc009_c — C. Division into Two

**Problem ID**: `AtCoder-agc009_c`  
**Contest**: `agc009`  
**Rating / Difficulty**: 2437  
**URL**: https://atcoder.jp/contests/agc009/tasks/agc009_c  
**VJudge Tag**: `[problem:AtCoder-agc009_c]`  
**Category File**: [`../categories/dynamic_programming/division_into_two_fenwick_dp.md`](../categories/dynamic_programming/division_into_two_fenwick_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
Partition a sorted set $S_1 < S_2 < \dots < S_N$ into sets $X$ and $Y$ with minimum differences $A$ and $B$. In a prefix $1 \dots k$, if $S_k \in X$, the last element in $Y$ was $S_j$ ($j < k$), and all intervening elements were in $X$. Transitioning $S_{k+1}$ into $Y$ requires $S_{k+1} - S_j \ge B$, which is a prefix sum of valid $j$'s on $dpX$. Adjacent violations ($S_{k+1} - S_k < A$) wipe out all states in $dpX$, which is efficiently maintained using Fenwick trees.

## 2. Core Observation & Invariant
Only the position of the last element in the other set matters. Valid transitions from $dpX$ to $dpY$ require $S_j \le S_{k+1} - B$, corresponding to a binary search prefix on the Fenwick tree. Clearing the DP data structure takes $O(1)$ amortized or reset.

## 3. Step-by-Step Algorithm
1. 1. Verify feasibility: if $S_{i+2} - S_i < A$ and $S_{i+2} - S_i < B$ for any $i$, output 0.
2. 2. Maintain two Fenwick trees for $dpX$ and $dpY$ indexed by the last element's position.
3. 3. Initialize $dpX[0] = 1, dpY[0] = 1$ representing the virtual $-\infty$ initial elements.
4. 4. For each $k = 1 \dots N - 1$:
5.    - Query prefix sum of $dpX$ up to index where $S_j \le S_k - B$ to get $sum_X$.
6.    - Query prefix sum of $dpY$ up to index where $S_i \le S_k - A$ to get $sum_Y$.
7.    - If $S_k - S_{k-1} < A$, clear $dpX$; insert $sum_Y$ at position $k$ in $dpX$.
8.    - If $S_k - S_{k-1} < B$, clear $dpY$; insert $sum_X$ at position $k$ in $dpY$.
9. 5. Output total remaining ways in both Fenwick trees modulo $10^9 + 7$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

struct Fenwick {
    int n;
    vector<long long> tree;
    int base_clear;

    Fenwick(int n) : n(n), tree(n + 2, 0), base_clear(0) {}

    void add(int i, long long val) {
        i++;
        while (i <= n + 1) {
            tree[i] = (tree[i] + val) % MOD;
            i += i & (-i);
        }
    }

    long long query(int i) {
        if (i < 0) return 0;
        i = min(i, n) + 1;
        long long s = 0;
        while (i > 0) {
            s = (s + tree[i]) % MOD;
            i -= i & (-i);
        }
        return s;
    }

    void clear_all() {
        fill(tree.begin(), tree.end(), 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long A, B;
    if (!(cin >> N >> A >> B)) return 0;

    vector<long long> S(N);
    for (int i = 0; i < N; ++i) cin >> S[i];

    // Check consecutive violations:
    for (int i = 0; i < N - 2; ++i) {
        if (S[i + 2] - S[i] < A && S[i + 2] - S[i] < B) {
            cout << 0 << "\n";
            return 0;
        }
    }

    Fenwick bitX(N), bitY(N);
    bitX.add(0, 1);
    bitY.add(0, 1);

    for (int k = 1; k < N; ++k) {
        long long prev_val = S[k - 1];
        long long cur_val = S[k];

        // S[k] - S[j] >= B => S[j] <= cur_val - B
        // find max j such that S[j-1] <= cur_val - B
        long long target_B = cur_val - B;
        int max_j = upper_bound(S.begin(), S.begin() + k, target_B) - S.begin();
        long long sum_X = bitX.query(max_j);

        long long target_A = cur_val - A;
        int max_i = upper_bound(S.begin(), S.begin() + k, target_A) - S.begin();
        long long sum_Y = bitY.query(max_i);

        if (cur_val - prev_val < A) {
            bitX.clear_all();
        }
        if (sum_Y > 0) {
            bitX.add(k, sum_Y);
        }

        if (cur_val - prev_val < B) {
            bitY.clear_all();
        }
        if (sum_X > 0) {
            bitY.add(k, sum_X);
        }
    }

    long long ans = (bitX.query(N) + bitY.query(N)) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

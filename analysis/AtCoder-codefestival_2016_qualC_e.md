# Problem Analysis: AtCoder-codefestival_2016_qualC_e — E. Encyclopedia of Permutations

**Problem ID**: `AtCoder-codefestival_2016_qualC_e`  
**Contest**: `code-festival-2016-qualc`  
**Rating / Difficulty**: 2885  
**URL**: https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_e  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_qualC_e]`  
**Category File**: [`../categories/basics/partial_permutation_lexicographical_rank_sum.md`](../categories/basics/partial_permutation_lexicographical_rank_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Permutations, Combinations and Basic Counting Problems`  

---

## 1. Problem Statement & Key Idea
Given a partial permutation of length N with some known values and some missing values, find the sum of lexicographical ranks over all valid completions modulo 10^9+7.

## 2. Core Observation & Invariant
The lexicographical rank of permutation P is 1 + sum_{i=1}^N c_i (N - i)!, where c_i is the count of j > i with P_j < P_i. By linearity of expectation, sum c_i over completions by partitioning pairs (i, j) into four types: fixed-fixed, fixed-free, free-fixed, and free-free. Using a Fenwick tree and prefix sums of unused numbers, each type can be counted in O(N log N) time.

## 3. Step-by-Step Algorithm
1. 1. Identify fixed positions and remaining unused values.
2. 2. Use Fenwick tree to count inversions between pairs of fixed elements.
3. 3. Compute cross-inversion contributions between fixed and free elements using Fenwick prefix queries.
4. 4. Free-free element pairs invert with probability 1/2.
5. 5. Accumulate weighted contributions with (N - i)! * (# free completions) modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 1000000007;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int idx, int val) {
        for (; idx <= n; idx += idx & (-idx)) {
            tree[idx] += val;
        }
    }

    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & (-idx)) {
            sum += tree[idx];
        }
        return sum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    vector<bool> present(n + 1, false);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        if (p[i] != 0) {
            present[p[i]] = true;
        }
    }

    int max_fact = n + 5;
    vector<long long> fact(max_fact, 1);
    for (int i = 1; i < max_fact; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    long long inv2 = (MOD + 1) / 2;

    vector<int> u_prefix(n + 1, 0);
    for (int v = 1; v <= n; ++v) {
        u_prefix[v] = u_prefix[v - 1] + (present[v] ? 0 : 1);
    }
    int k = u_prefix[n];

    vector<int> zeros_after(n, 0);
    int cnt_z = 0;
    for (int i = n - 1; i >= 0; --i) {
        zeros_after[i] = cnt_z;
        if (p[i] == 0) {
            cnt_z++;
        }
    }

    vector<long long> suffix_u_greater(n + 1, 0);
    long long cur_sum = 0;
    for (int i = n - 1; i >= 0; --i) {
        suffix_u_greater[i] = cur_sum;
        if (p[i] != 0) {
            cur_sum = (cur_sum + (k - u_prefix[p[i]])) % MOD;
        }
    }

    Fenwick fenw(n + 2);
    long long total_ans = fact[k]; // 1-based page rank base

    for (int i = n - 1; i >= 0; --i) {
        long long weight = fact[n - 1 - i];
        long long contrib = 0;

        if (p[i] != 0) {
            long long smaller_fixed = fenw.query(p[i] - 1);
            long long t1 = fact[k] * smaller_fixed % MOD;
            long long t2 = 0;
            if (k >= 1) {
                t2 = (long long)zeros_after[i] * fact[k - 1] % MOD * u_prefix[p[i]] % MOD;
            }
            contrib = (t1 + t2) % MOD;
            fenw.add(p[i], 1);
        } else {
            long long t3 = 0;
            if (k >= 1) {
                t3 = fact[k - 1] * suffix_u_greater[i] % MOD;
            }
            long long t4 = 0;
            if (k >= 2) {
                t4 = (long long)zeros_after[i] * fact[k] % MOD * inv2 % MOD;
            }
            contrib = (t3 + t4) % MOD;
        }

        total_ans = (total_ans + contrib * weight) % MOD;
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

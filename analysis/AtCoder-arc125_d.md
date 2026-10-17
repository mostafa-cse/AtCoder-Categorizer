# Problem Analysis: AtCoder-arc125_d — D. Unique Subsequence

**Problem ID**: `AtCoder-arc125_d`  
**Contest**: `arc125`  
**Rating / Difficulty**: 2187  
**URL**: https://atcoder.jp/contests/arc125/tasks/arc125_d  
**VJudge Tag**: `[problem:AtCoder-arc125_d]`  
**Category File**: [`../categories/data_structures/fenwick_tree_last_occurrence_unique_subsequences.md`](../categories/data_structures/fenwick_tree_last_occurrence_unique_subsequences.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Count non-empty subsequences s of A that can be extracted in exactly one unique way as an index sequence modulo 998244353. A subsequence index sequence is unique iff between any two consecutive chosen indices x_i and x_{i+1}, neither A_{x_i} nor A_{x_{i+1}} appears.

## 2. Core Observation & Invariant
Define dummy boundary values A_0 = 0 and A_{N+1} = N+1. Transition from index i to j requires prev[A_j] <= i < j and next[A_i] > j. At any step j, only the most recent occurrence of each value satisfies next[i] >= j. Maintaining these active DP values in a Fenwick tree allows querying dp[j] = query(prev[A_j], j - 1), removing prev[A_j] from the BIT, and inserting j.

## 3. Step-by-Step Algorithm
1. Set A_0 = 0, A_{N+1} = N+1. Initialize Fenwick tree over indices 0..N+1.
2. Initialize dp[0] = 1, insert dp[0] at index 0 in the BIT.
3. Maintain an array last_pos[val] tracking the most recent index of each value.
4. For j = 1 to N+1: let p = last_pos[A_j]. Compute dp[j] = query_range(p, j - 1). If p > 0, remove dp[p] from the BIT at index p. Add dp[j] at index j in the BIT. Update last_pos[A_j] = j.
5. Output (dp[N + 1] - 1 + MOD) mod MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, long long delta) {
        delta = (delta % MOD + MOD) % MOD;
        for (++i; i <= n; i += i & -i) {
            tree[i] = (tree[i] + delta) % MOD;
        }
    }

    long long query(int i) { // sum in [0, i]
        if (i < 0) return 0;
        long long sum = 0;
        for (++i; i > 0; i -= i & -i) {
            sum = (sum + tree[i]) % MOD;
        }
        return sum;
    }

    long long query_range(int l, int r) {
        if (l > r) return 0;
        return (query(r) - query(l - 1) + MOD) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 2);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }
    A[0] = 0;
    A[N + 1] = N + 1;

    Fenwick bit(N + 2);
    vector<long long> dp(N + 2, 0);
    vector<int> last_pos(N + 2, 0);

    dp[0] = 1;
    bit.add(0, 1);

    for (int j = 1; j <= N + 1; ++j) {
        int val = A[j];
        int p = last_pos[val];

        dp[j] = bit.query_range(p, j - 1);

        if (p > 0) {
            bit.add(p, -dp[p]);
        }
        bit.add(j, dp[j]);
        last_pos[val] = j;
    }

    long long ans = (dp[N + 1] - 1 + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc174_e — E. Existence Counting

**Problem ID**: `AtCoder-arc174_e`  
**Contest**: `arc174`  
**Rating / Difficulty**: 2336  
**URL**: https://atcoder.jp/contests/arc174/tasks/arc174_e  
**VJudge Tag**: `[problem:AtCoder-arc174_e]`  
**Category File**: [`../categories/combinatorics/lexicographical_divergence_fenwick_existence_counting.md`](../categories/combinatorics/lexicographical_divergence_fenwick_existence_counting.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
For each $t \in [1, N]$, count permutations $b \le P$ of length $K$ containing $t$. Decomposing by the first diverging position and counting occurrences of $t$ via an offline Fenwick tree sweep solves in $O(N \log N)$.

## 2. Core Observation & Invariant
A sequence $b \le P$ diverges from $P$ at the earliest index $i$ where $b[i] < P[i]$. For each diverging index $i$, any element $t \in P[0 \dots i-1]$ is included with probability 1, while any $t \notin P[0 \dots i-1]$ is included if $b[i] = t$ (possible when $t < P[i]$) or if $t$ is chosen in the remaining $K - 1 - i$ positions.

## 3. Step-by-Step Algorithm
1. Factor out the universal base count $\sum c_i V_i$ for all $t \in [1, N]$.
2. For each $t = P[i]$, add suffix sums of $c_j (W_j - V_j)$ for all steps $j > i$ where $t$ is already fixed in the prefix.
3. For steps before $pos[t]$ where $P[j] > t$, add $(W_j - V_j)$ using an offline sweep line over a Fenwick tree in $O(N \log N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        delta = (delta % MOD + MOD) % MOD;
        for (; i <= n; i += i & (-i)) {
            tree[i] = (tree[i] + delta) % MOD;
        }
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & (-i)) {
            sum = (sum + tree[i]) % MOD;
        }
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> p(k);
    for (int i = 0; i < k; ++i) {
        cin >> p[i];
    }

    vector<long long> fact(n + 1, 1), inv(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto P_perm = [&](int total, int take) -> long long {
        if (take < 0 || take > total) return 0;
        return (fact[total] * inv[total - take]) % MOD;
    };

    Fenwick bit1(n);
    vector<long long> c(k), W(k), V(k), diff(k);
    vector<int> pos(n + 1, -1);

    for (int i = 0; i < k; ++i) {
        pos[p[i]] = i;
        long long less = bit1.query(p[i]);
        c[i] = (p[i] - 1 - less) % MOD;
        bit1.add(p[i], 1);

        int rem = k - 1 - i;
        W[i] = P_perm(n - 1 - i, rem);
        V[i] = (rem > 0) ? (rem * P_perm(n - 2 - i, rem - 1)) % MOD : 0;
        diff[i] = (W[i] - V[i] + MOD) % MOD;
    }

    long long total_V = 0;
    for (int i = 0; i < k; ++i) {
        total_V = (total_V + c[i] * V[i]) % MOD;
    }

    vector<long long> suff_c_diff(k + 1, 0);
    for (int i = k - 1; i >= 0; --i) {
        suff_c_diff[i] = (suff_c_diff[i + 1] + c[i] * diff[i]) % MOD;
    }

    Fenwick bit2(n);
    vector<long long> ans(n + 1, 0);

    for (int i = 0; i < k; ++i) {
        int t = p[i];
        long long greater_sum = (bit2.query(n) - bit2.query(t) + MOD) % MOD;
        long long cur = (total_V + 1 + suff_c_diff[i + 1] + greater_sum) % MOD;
        ans[t] = cur;
        bit2.add(p[i], diff[i]);
    }

    for (int t = 1; t <= n; ++t) {
        if (pos[t] == -1) {
            long long greater_sum = (bit2.query(n) - bit2.query(t) + MOD) % MOD;
            ans[t] = (total_V + greater_sum) % MOD;
        }
    }

    for (int t = 1; t <= n; ++t) {
        cout << ans[t] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

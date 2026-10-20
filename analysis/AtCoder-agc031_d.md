# Problem Analysis: AtCoder-agc031_d — D - A Sequence of Permutations

**Problem ID**: `AtCoder-agc031_d`  
**Contest**: `agc031`  
**Rating / Difficulty**: 2953  
**URL**: https://atcoder.jp/contests/agc031/tasks/agc031_d  
**VJudge Tag**: `[problem:AtCoder-agc031_d]`  
**Category File**: [`../categories/miscellaneous/permutation_commutator_six_periodicity_cycle_power.md`](../categories/miscellaneous/permutation_commutator_six_periodicity_cycle_power.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Permutations and Permutation Cycles`  

---

## 1. Problem Statement & Key Idea
Compute the K-th permutation in the sequence defined by a_1 = p, a_2 = q, and a_{n+1} = a_n a_{n-1}^{-1} for n >= 2, where K <= 10^18 and N <= 10^5.

## 2. Core Observation & Invariant
Expanding the sequence terms shows a_1 = p, a_2 = q, a_3 = q p^{-1}, a_4 = q p^{-1} q^{-1}, a_5 = q p^{-1} q^{-1} p q^{-1}, a_6 = q p^{-1} q^{-1} p q p^{-1} q^{-1}. Then a_7 = (q p^{-1} q^{-1} p) p (q p^{-1} q^{-1} p)^{-1}. Letting C = q p^{-1} q^{-1} p be the group commutator, we have a_{n+6} = C a_n C^{-1} for all n >= 1. By induction, a_{6m + r} = C^m a_r C^{-m}. Because permutation conjugation preserves cycle structure, C^m is computed in O(N) via cycle decomposition.

## 3. Step-by-Step Algorithm
1. 1. Compute permutation inverse, composition, and commutator C = q o p^{-1} o q^{-1} o p.
2. 2. Generate base terms a_1, a_2, ..., a_6 using the recurrence a_{i+1} = a_i o a_{i-1}^{-1}.
3. 3. For given K, compute m = (K - 1) // 6 and r = (K - 1) % 6 + 1.
4. 4. Compute C^m in O(N) by decomposing C into disjoint cycles and advancing each cycle by m mod length.
5. 5. Compute a_K = C^m o a_r o (C^m)^{-1}.
6. 6. Output the resulting 1-indexed permutation.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> inv(const vector<int>& p) {
    int n = p.size();
    vector<int> res(n);
    for (int i = 0; i < n; ++i) {
        res[p[i] - 1] = i + 1;
    }
    return res;
}

vector<int> comp(const vector<int>& p, const vector<int>& q) {
    int n = p.size();
    vector<int> res(n);
    for (int i = 0; i < n; ++i) {
        res[i] = p[q[i] - 1];
    }
    return res;
}

vector<int> f(const vector<int>& p, const vector<int>& q) {
    return comp(q, inv(p));
}

vector<int> perm_pow(const vector<int>& p, long long k) {
    int n = p.size();
    vector<int> res(n);
    for (int i = 0; i < n; ++i) res[i] = i + 1;
    vector<bool> vis(n, false);
    for (int i = 0; i < n; ++i) {
        if (!vis[i]) {
            vector<int> cycle;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                cycle.push_back(cur);
                cur = p[cur] - 1;
            }
            int L = cycle.size();
            int step = k % L;
            for (int j = 0; j < L; ++j) {
                res[cycle[j]] = cycle[(j + step) % L] + 1;
            }
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<int> p(N), q(N);
    for (int i = 0; i < N; ++i) cin >> p[i];
    for (int i = 0; i < N; ++i) cin >> q[i];

    vector<vector<int>> a(7);
    a[1] = p;
    a[2] = q;
    for (int i = 3; i <= 6; ++i) {
        a[i] = f(a[i - 2], a[i - 1]);
    }

    int r = (K - 1) % 6 + 1;
    long long t = (K - r) / 6;

    vector<int> c = comp(comp(comp(q, inv(p)), inv(q)), p);
    vector<int> ct = perm_pow(c, t);
    vector<int> inv_ct = inv(ct);

    vector<int> ans = comp(comp(ct, a[r]), inv_ct);

    for (int i = 0; i < N; ++i) {
        cout << ans[i] << (i == N - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

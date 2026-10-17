# Problem Analysis: AtCoder-abc464_f — Random Vault Heist

**Problem ID**: `AtCoder-abc464_f`  
**Contest**: `abc464`  
**Rating / Difficulty**: 2225  
**URL**: https://atcoder.jp/contests/abc464/tasks/abc464_f  
**VJudge Tag**: `[problem:AtCoder-abc464_f]`  
**Category File**: [`../categories/miscellaneous/meet_in_the_middle_random_vault_heist_prefix_expectation.md`](../categories/miscellaneous/meet_in_the_middle_random_vault_heist_prefix_expectation.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Meet in the Middle`  

---

## 1. Problem Statement & Key Idea
Find the expected total amount stolen from N <= 40 safes opened in uniform random order until the total amount stolen reaches at least X.

## 2. Core Observation & Invariant
By linearity of expectation, the expected value equals the sum over all subsets S with sum(S) < X of the probability of reaching state S times the expected money stolen next: sum_{S: sum(S)<X} [1 / (C(N, |S|) * (N - |S|))] * (A_all - sum(S)). Grouping by subset size k = |S|, we only need the count of subsets of size k with sum < X and the sum of their sums. Because N <= 40, we split the elements into halves of size 20 and apply Meet-in-the-Middle with binary search.

## 3. Step-by-Step Algorithm
1. 1. Split the N elements into left half (l = N/2) and right half (r = N - l).
2. 2. In the right half, enumerate all 2^r subsets, group sums by subset size kr in [0, r], sort each group, and precompute prefix sums.
3. 3. In the left half, iterate over all 2^l subsets (sum sl, size kl). For each right subset size kr, binary search in sums_r[kr] for elements < X - sl, accumulating the count and sum of sums for total size k = kl + kr.
4. 4. Combine contributions over each size k in [0, N-1] with modular inverse of C(N, k) * (N - k).

## 4. Complexity Analysis
- **Time Complexity**: `O(r * 2^r + 2^l * r * log(C(r, r/2)))`
- **Space Complexity**: `O(2^r)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long X;
    if (!(cin >> n >> X)) return 0;

    vector<long long> a(n);
    long long A_all = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        A_all += a[i];
    }

    int l = n / 2;
    int r = n - l;

    vector<long long> al(a.begin(), a.begin() + l);
    vector<long long> ar(a.begin() + l, a.end());

    // Right half
    vector<vector<long long>> sums_r(r + 1);
    auto gen_r = [&](auto& self, int idx, long long cur_sum, int cur_cnt) -> void {
        if (idx == r) {
            sums_r[cur_cnt].push_back(cur_sum);
            return;
        }
        self(self, idx + 1, cur_sum, cur_cnt);
        self(self, idx + 1, cur_sum + ar[idx], cur_cnt + 1);
    };
    gen_r(gen_r, 0, 0, 0);

    vector<vector<long long>> pref_r(r + 1);
    for (int kr = 0; kr <= r; ++kr) {
        sort(sums_r[kr].begin(), sums_r[kr].end());
        pref_r[kr].resize(sums_r[kr].size() + 1, 0);
        for (size_t i = 0; i < sums_r[kr].size(); ++i) {
            pref_r[kr][i + 1] = (pref_r[kr][i] + sums_r[kr][i]) % MOD;
        }
    }

    // Left half
    vector<long long> count(n + 1, 0);
    vector<long long> sum_sums(n + 1, 0);

    auto gen_l = [&](auto& self, int idx, long long cur_sum, int cur_cnt) -> void {
        if (idx == l) {
            for (int kr = 0; kr <= r; ++kr) {
                long long target = X - cur_sum;
                int idx_r = lower_bound(sums_r[kr].begin(), sums_r[kr].end(), target) - sums_r[kr].begin();
                int k = cur_cnt + kr;
                count[k] = (count[k] + idx_r) % MOD;
                long long cur_sum_mod = cur_sum % MOD;
                long long term = ((long long)idx_r * cur_sum_mod + pref_r[kr][idx_r]) % MOD;
                sum_sums[k] = (sum_sums[k] + term) % MOD;
            }
            return;
        }
        self(self, idx + 1, cur_sum, cur_cnt);
        self(self, idx + 1, cur_sum + al[idx], cur_cnt + 1);
    };
    gen_l(gen_l, 0, 0, 0);

    // Factorials
    vector<long long> fact(n + 1, 1), inv_fact(n + 1, 1);
    for (int i = 1; i <= n; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv_fact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 0; --i) inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n_val, int r_val) -> long long {
        if (r_val < 0 || r_val > n_val) return 0;
        return fact[n_val] * inv_fact[r_val] % MOD * inv_fact[n_val - r_val] % MOD;
    };

    long long ans = 0;
    long long A_all_mod = A_all % MOD;
    for (int k = 0; k < n; ++k) {
        long long denom = nCr(n, k) * (n - k) % MOD;
        long long inv_denom = modInverse(denom);
        long long val = (A_all_mod * count[k] - sum_sums[k] % MOD + MOD) % MOD;
        ans = (ans + val * inv_denom) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

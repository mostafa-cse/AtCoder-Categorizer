# Problem Analysis: AtCoder-arc231_e — E. Odd Inversion

**Problem ID**: `AtCoder-arc231_e`  
**Contest**: `arc231`  
**Rating / Difficulty**: 2393  
**URL**: https://atcoder.jp/contests/arc231/tasks/arc231_e  
**VJudge Tag**: `[problem:AtCoder-arc231_e]`  
**Category File**: [`../categories/miscellaneous/odd_inversion_adjacent_sign_reversal_involution_dp.md`](../categories/miscellaneous/odd_inversion_adjacent_sign_reversal_involution_dp.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Inversions`  

---

## 1. Problem Statement & Key Idea
The difference between even and odd inversion sequences satisfies X_i = (A_i - A_{i-1}) X_{i-1} + A_{i-1} X_{i-2} by adjacent element swapping involution. Solving this linear recurrence yields the exact odd count in O(N) time.

## 2. Core Observation & Invariant
Let C and D be counts of sequences with even and odd inversions. Then C + D = prod A_i, while C - D = X_N under sign-reversing involution: swapping adjacent elements B_{i-1} != B_i within [1, A_{i-1}] cancels out opposite parities, leaving only B_{i-1} = B_i (contributing A_{i-1} X_{i-2}) and B_i > A_{i-1} (contributing (A_i - A_{i-1}) X_{i-1}).

## 3. Step-by-Step Algorithm
1. Initialize base cases X_0 = 1, X_1 = A_1.
2. For i = 2 to N, compute X_i = (A_i - A_{i-1}) X_{i-1} + A_{i-1} X_{i-2} mod 998244353.
3. Compute total sequences prod = prod_{i=1}^N A_i mod 998244353.
4. Number of odd inversion sequences is (prod - X_N) / 2 mod 998244353 in O(N) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;
const ll INV2 = (MOD + 1) / 2;

void solve() {
    int N;
    if (!(cin >> N)) return;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    if (N == 1) {
        cout << 0 << "\n";
        return;
    }

    vector<ll> X(N + 1, 0);
    X[0] = 1;
    X[1] = A[0] % MOD;
    for (int i = 2; i <= N; i++) {
        ll diff = (A[i - 1] - A[i - 2]) % MOD;
        if (diff < 0) diff += MOD;
        ll prev_A = A[i - 2] % MOD;
        X[i] = (diff * X[i - 1] % MOD + prev_A * X[i - 2] % MOD) % MOD;
    }

    ll prod = 1;
    for (int i = 0; i < N; i++) {
        prod = (prod * (A[i] % MOD)) % MOD;
    }

    ll ans = (prod - X[N] + MOD) % MOD * INV2 % MOD;
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

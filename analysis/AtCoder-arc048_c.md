# Problem Analysis: AtCoder-arc048_c — C. 足の多い高橋君

**Problem ID**: `AtCoder-arc048_c`  
**Contest**: `arc048`  
**Rating / Difficulty**: 2390  
**URL**: https://atcoder.jp/contests/arc048/tasks/arc048_c  
**VJudge Tag**: `[problem:AtCoder-arc048_c]`  
**Category File**: [`../categories/basics/palindrome_leg_path_gcd_difference_components.md`](../categories/basics/palindrome_leg_path_gcd_difference_components.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Permutations, Combinations and Basic Counting Problems`  

---

## 1. Problem Statement & Key Idea
Paths between leg tips form palindromes iff identical-depth bones match and differences between leg lengths form periodic palindromic suffixes with period g = gcd of differences. The number of independent bone components is L_min + floor((g+1)/2), evaluated in O(N + log M) time.

## 2. Core Observation & Invariant
For any two legs A and B of lengths L_A <= L_B, the path outer(A) -> body -> outer(B) being a palindrome forces bones at distance k <= L_A from the tip to share identical characters across all legs, while the remaining suffix of length L_B - L_A on leg B must be a palindrome. For multiple leg lengths, these palindromic suffix constraints equate characters with period g = gcd of adjacent length differences, giving exactly L_min + floor((g + 1) / 2) independent components.

## 3. Step-by-Step Algorithm
1. Collect and sort unique leg lengths L_1 < L_2 < ... < L_k.
2. If k == 1, all legs are identical length L_1, yielding 2^{L_1} mod (10^9+7).
3. If k > 1, compute g = gcd(L_2 - L_1, ..., L_k - L_{k-1}).
4. Total independent bone components is comps = L_1 + (g + 1) // 2.
5. Output 2^{comps} mod (10^9+7) via modular exponentiation in O(N + log(10^9+7)) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + \log(\max L_i))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 1e9 + 7;

ll power(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

ll gcd_val(ll a, ll b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<ll> L(N);
    for (int i = 0; i < N; i++) cin >> L[i];
    sort(L.begin(), L.end());
    L.erase(unique(L.begin(), L.end()), L.end());

    ll comps = 0;
    if (L.size() == 1) {
        comps = L[0];
    } else {
        ll L_min = L[0];
        ll g = 0;
        for (size_t i = 1; i < L.size(); i++) {
            g = gcd_val(g, L[i] - L[i - 1]);
        }
        comps = L_min + (g + 1) / 2;
    }

    cout << power(2, comps) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

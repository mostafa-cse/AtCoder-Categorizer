# Problem Analysis: AtCoder-abc167_e — Colorful Blocks

**Problem ID**: `AtCoder-abc167_e`  
**Contest**: `abc167`  
**Rating / Difficulty**: 1442  
**URL**: https://atcoder.jp/contests/abc167/tasks/abc167_e  
**VJudge Tag**: `[problem:AtCoder-abc167_e]`  
**Category File**: [`../categories/combinatorics/adjacent_matching_stars_and_bars.md`](../categories/combinatorics/adjacent_matching_stars_and_bars.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stars and Bars`  
- **Topic (Skill)**: `Adjacent Matching Constraints Combinatorics`  

---

## 1. Problem Statement & Key Idea
N blocks placed in a row are colored using M colors. Find the number of ways to color the blocks such that AT MOST K adjacent pairs of blocks share the same color, modulo 998244353.

**Key Insight**: Iterate over the exact number of matching adjacent pairs j (0 <= j <= K). Choose which j positions match, color the first block with M choices, and each subsequent block with either 1 choice (if matching) or M - 1 choices (if different).

## 2. Core Observation & Invariant
For exact j adjacent matches: C(N - 1, j) ways to choose the matching positions. First block has M choices. The j matching blocks have 1 choice. The remaining N - 1 - j blocks must differ from their predecessor (M - 1 choices). Thus: C(N - 1, j) * M * (M - 1)^(N - 1 - j).

## 3. Step-by-Step Algorithm
1. Precompute factorials and modular inverse factorials up to N.
2. Iterate j from 0 to K:
3.   ways = C(N - 1, j) * M % MOD * power(M - 1, N - 1 - j) % MOD.
4.   total_sum = (total_sum + ways) % MOD.
5. Print total_sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

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

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    long long ans = 0;
    for (int j = 0; j <= k; ++j) {
        long long ways = nCr(n - 1, j) * m % MOD;
        ways = (ways * power(m - 1, n - 1 - j)) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exact-match parameterization and independent choice multiplication for sequential colorings.
- **Reusable Pattern**: `Adjacent Matching Sum: sum_{j=0}^K C(N-1, j) * M * (M-1)^(N-1-j).`

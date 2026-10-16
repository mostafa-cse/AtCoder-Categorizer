# Problem Analysis: AtCoder-abc156_e — Roaming

**Problem ID**: `AtCoder-abc156_e`  
**Contest**: `abc156`  
**Rating / Difficulty**: 1514  
**URL**: https://atcoder.jp/contests/abc156/tasks/abc156_e  
**VJudge Tag**: `[problem:AtCoder-abc156_e]`  
**Category File**: [`../categories/combinatorics/stars_and_bars_empty_boxes.md`](../categories/combinatorics/stars_and_bars_empty_boxes.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stars and Bars`  
- **Topic (Skill)**: `Stars and Bars Empty Boxes Combinatorics`  

---

## 1. Problem Statement & Key Idea
There are N rooms, each initially containing 1 person. In each move, one person moves to a different room. Find the number of possible configurations of people in rooms after at most K moves, modulo 10^9 + 7.

**Key Insight**: Each move can create at most one empty room. Thus, after at most K moves, the number of empty rooms z satisfies 0 <= z <= min(N - 1, K).

## 2. Core Observation & Invariant
For a fixed number of empty rooms z: choose which z rooms are empty in C(N, z) ways. The remaining N - z rooms must each contain at least 1 person. Distributing N people into N - z positive integer bins gives C(N - 1, (N - z) - 1) = C(N - 1, N - z - 1) ways.

## 3. Step-by-Step Algorithm
1. Precompute factorials and modular inverse factorials up to N.
2. ans = 0.
3. For z from 0 to min((long long)N - 1, K):
4.   ways = C(N, z) * C(N - 1, N - z - 1) % MOD.
5.   ans = (ans + ways) % MOD.
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;
const int MAX = 400005;

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

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    long long max_z = min((long long)n - 1, k);
    long long ans = 0;

    for (int z = 0; z <= max_z; ++z) {
        long long ways = nCr(n, z) * nCr(n - 1, n - z - 1) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Characterizing reachable states by invariant empty-box count and applying Stars and Bars.
- **Reusable Pattern**: `Empty Room Configurations: sum_{z=0}^{min(N-1, K)} C(N, z) * C(N-1, N-z-1).`

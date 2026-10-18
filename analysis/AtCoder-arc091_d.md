# Problem Analysis: AtCoder-arc091_d — F. Strange Nim

**Problem ID**: `AtCoder-arc091_d`  
**Contest**: `arc091`  
**Rating / Difficulty**: 2395  
**URL**: https://atcoder.jp/contests/arc091/tasks/arc091_d  
**VJudge Tag**: `[problem:AtCoder-arc091_d]`  
**Category File**: [`../categories/game_theory/strange_nim_floor_subtraction_division_jumps.md`](../categories/game_theory/strange_nim_floor_subtraction_division_jumps.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
The Sprague-Grundy theorem reduces the game to Nim with Grundy values G(X, K) = X/K (if K | X) and G(X - floor(X/K) - 1, K) otherwise. Division jumps accelerate the recursion to O(sqrt(A/K)) per pile, total O(N sqrt(max A)) time.

## 2. Core Observation & Invariant
The Grundy function for a pile of X stones with divisor K satisfies G(X, K) = X / K when X % K == 0, and G(X, K) = G(X - (floor(X/K) + 1), K) otherwise. Because d = floor(X/K) remains constant across contiguous ranges of length d+1, division jumps of size (X % K) // (d + 1) compress long subtraction chains into O(sqrt(A/K)) steps.

## 3. Step-by-Step Algorithm
1. Define get_G(X, K): while X % K != 0, let d = X // K, r = X % K, step = d + 1.
2. If r >= step, jump X -= (r // step) * step; else jump X -= step.
3. When X is a multiple of K, return X // K.
4. XOR all pile Grundy values: Takahashi wins iff the XOR sum is non-zero, otherwise Aoki wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sqrt{\max A_i})`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll get_G(ll X, ll K) {
    while (X % K != 0) {
        ll d = X / K;
        ll r = X % K;
        ll step = d + 1;
        ll num_jumps = r / step;
        if (num_jumps > 0) {
            X -= num_jumps * step;
        } else {
            X -= step;
        }
    }
    return X / K;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;

    ll xor_sum = 0;
    for (int i = 0; i < N; i++) {
        ll A, K;
        cin >> A >> K;
        xor_sum ^= get_G(A, K);
    }

    if (xor_sum != 0) cout << "Takahashi\n";
    else cout << "Aoki\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

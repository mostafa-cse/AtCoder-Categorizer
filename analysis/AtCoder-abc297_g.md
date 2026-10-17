# Problem Analysis: AtCoder-abc297_g — Constrained Nim 2

**Problem ID**: `AtCoder-abc297_g`  
**Contest**: `abc297`  
**Rating / Difficulty**: 1834  
**URL**: https://atcoder.jp/contests/abc297/tasks/abc297_g  
**VJudge Tag**: `[problem:AtCoder-abc297_g]`  
**Category File**: [`../categories/game_theory/sprague_grundy_bounded_move_nim.md`](../categories/game_theory/sprague_grundy_bounded_move_nim.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Sprague-Grundy`  
- **Topic (Skill)**: `Sprague-Grundy Closed Form for Bounded-Move Nim: (X mod (L+R)) / L`  

---

## 1. Problem Statement & Key Idea
N piles of stones. In a turn, a player removes between L and R stones (1 <= L <= R) from a single pile. A player who cannot move loses. Determine who wins under optimal play.

**Key Insight**: The Sprague-Grundy theorem applies. For a single pile of size X with allowed moves in [L, R], the Grundy value satisfies a periodic step-function pattern: g(X) = floor((X % (L + R)) / L).

## 2. Core Observation & Invariant
First player wins iff the XOR sum of g(A_i) over all piles is non-zero.

## 3. Step-by-Step Algorithm
1. Read N, L, R.
2. xor_sum = 0.
3. For each pile A_i:
4.   g_val = (A_i % (L + R)) / L.
5.   xor_sum ^= g_val.
6. Print 'First' if xor_sum != 0 else 'Second'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long l, r;
    if (!(cin >> n >> l >> r)) return 0;

    long long xor_sum = 0;
    long long period = l + r;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        long long g = (a % period) / l;
        xor_sum ^= g;
    }

    if (xor_sum != 0) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Deriving exact periodic Sprague-Grundy closed-form values for bounded range subtraction games.
- **Reusable Pattern**: `Interval Subtraction Grundy Function: g(X) = (X % (L + R)) / L.`

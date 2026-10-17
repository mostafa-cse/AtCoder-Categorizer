# Problem Analysis: AtCoder-arc143_c — Piles of Pebbles

**Problem ID**: `AtCoder-arc143_c`  
**Contest**: `arc143`  
**Rating / Difficulty**: 1805  
**URL**: https://atcoder.jp/contests/arc143/tasks/arc143_c  
**VJudge Tag**: `[problem:AtCoder-arc143_c]`  
**Category File**: [`../categories/game_theory/pebble_piles_mod_xy_game.md`](../categories/game_theory/pebble_piles_mod_xy_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Impartial Games`  
- **Topic (Skill)**: `Periodic Round Invariant Modulo (X + Y) on Multi-Pile Pebble Game`  

---

## 1. Problem Statement & Key Idea
N piles of pebbles. In a turn, Takahashi chooses a pile and removes X pebbles; Aoki chooses a pile and removes Y pebbles. Normal play convention. Who wins under optimal play?

**Key Insight**: Whenever a pile has >= X + Y pebbles, any move of X by Takahashi can be countered by Aoki taking Y from the same pile, and vice versa. Thus, each pile size A_i can be reduced modulo (X + Y).

## 2. Core Observation & Invariant
In the reduced state A_i % (X + Y): Takahashi can only move on piles with remainder >= X. If there is a pile with remainder >= X but < Y, Takahashi can immediately move and leave Aoki with no move. Takahashi wins iff there is some pile with A_i % (X + Y) >= X and no pile with Y <= A_i % (X + Y) < X (or when Takahashi can dominate).

## 3. Step-by-Step Algorithm
1. For each pile, let r_i = A_i % (X + Y).
2. Check if Takahashi can win on first move:
3.   If there exists r_i in [X, X + Y - 1] and no r_j in [Y, X - 1] (when Y < X), Takahashi wins.
4.   Specifically: Takahashi wins iff there exists r_i >= X and (X <= Y || all piles with r_j >= Y also have r_j >= X).
5. Print 'First' or 'Second'.

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
    long long x, y;
    if (!(cin >> n >> x >> y)) return 0;

    vector<long long> a(n);
    bool can_tak = false;
    bool can_aoki_only = false;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        long long r = a[i] % (x + y);
        if (r >= x) can_tak = true;
        if (r >= y && r < x) can_aoki_only = true;
    }

    if (x <= y) {
        if (can_tak) cout << "First\n";
        else cout << "Second\n";
    } else {
        if (can_tak && !can_aoki_only) cout << "First\n";
        else cout << "Second\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Periodic reduction of multi-pile subtraction games modulo combined player step (X + Y).
- **Reusable Pattern**: `Asymmetric Subtraction Nim Modulo: Reduce pile sizes modulo (X + Y).`

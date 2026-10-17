# Problem Analysis: AtCoder-arc072_b — Alice&Brown

**Problem ID**: `AtCoder-arc072_b`  
**Contest**: `abc059`  
**Rating / Difficulty**: 1749  
**URL**: https://atcoder.jp/contests/abc059/tasks/arc072_b  
**VJudge Tag**: `[problem:AtCoder-arc072_b]`  
**Category File**: [`../categories/game_theory/impartial_game_parity_pile_difference.md`](../categories/game_theory/impartial_game_parity_pile_difference.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Impartial Games`  
- **Topic (Skill)**: `Impartial Game Parity / Modular Difference Invariant (|X - Y| <= 1)`  

---

## 1. Problem Statement & Key Idea
Two piles of stones have X and Y stones. In a turn, a player chooses a pile with >= 2 stones, removes 2k stones (k >= 1), and adds k stones to the other pile. A player who cannot move loses. Determine who wins under optimal play.

**Key Insight**: The difference between piles |X - Y| determines the game. Any state with |X - Y| <= 1 is a P-position (losing state). Any state with |X - Y| >= 2 is an N-position (winning state).

## 2. Core Observation & Invariant
From |X - Y| <= 1, any valid move changes the difference by |(X - 2k) - (Y + k)| = |X - Y - 3k| >= 3k - 1 >= 2, moving to an N-position. From |X - Y| >= 2, the player can always pick k to reach difference <= 1. Therefore, Alice wins iff |X - Y| >= 2.

## 3. Step-by-Step Algorithm
1. Read X and Y.
2. If abs(X - Y) <= 1, Brown wins.
3. Else, Alice wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    if (!(cin >> x >> y)) return 0;

    if (abs(x - y) <= 1) {
        cout << "Brown\n";
    } else {
        cout << "Alice\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Identifying modular step invariants on pile difference in impartial games.
- **Reusable Pattern**: `Pile Transfer Game Invariant: |X - Y| <= 1 is losing state (P-position).`

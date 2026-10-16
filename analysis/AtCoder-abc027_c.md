# Problem Analysis: AtCoder-abc027_c — Doubling Game

**Problem ID**: `AtCoder-abc027_c`  
**Contest**: `abc027`  
**Rating / Difficulty**: 1539  
**URL**: https://atcoder.jp/contests/abc027/tasks/abc027_c  
**VJudge Tag**: `[problem:AtCoder-abc027_c]`  
**Category File**: [`../categories/game_theory/minimax_depth_parity_doubling.md`](../categories/game_theory/minimax_depth_parity_doubling.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax`  
- **Topic (Skill)**: `Binary Tree Game Theory Minimax Depth Parity`  

---

## 1. Problem Statement & Key Idea
Starting with x = 1, Takahashi and Aoki alternate turns. On their turn, a player replaces x with either 2x or 2x + 1. The first player to make x > N loses. Determine the winner under optimal play.

**Key Insight**: The game takes place on a complete binary tree where leaves exceed N. The player who wants to win should force the game to a depth where the opponent is compelled to exceed N.

## 2. Core Observation & Invariant
Let depth D = floor(log2(N)) + 1. If D is odd, Takahashi wants the game to end at depth D (odd depth, Aoki's turn to exceed). Thus Takahashi chooses the right child (2x+1) to maximize x, while Aoki chooses the left child (2x) to delay. If D is even, roles reverse.

## 3. Step-by-Step Algorithm
1. Compute depth D = floor(log2(N)) + 1.
2. Simulate from x = 1, tracking whose turn it is.
3. If D is even:
4.   Takahashi picks 2x + 1; Aoki picks 2x.
5. If D is odd:
6.   Takahashi picks 2x; Aoki picks 2x + 1.
7. Continue until x > N. The player whose turn it was when x exceeded N loses; the other player wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int depth = 0;
    for (long long temp = n; temp > 0; temp /= 2) {
        depth++;
    }

    long long x = 1;
    bool takahashi_turn = true;

    while (x <= n) {
        if (depth % 2 == 1) {
            // Takahashi minimizes, Aoki maximizes
            if (takahashi_turn) x = 2 * x + 1;
            else x = 2 * x;
        } else {
            // Takahashi maximizes, Aoki minimizes
            if (takahashi_turn) x = 2 * x;
            else x = 2 * x + 1;
        }
        takahashi_turn = !takahashi_turn;
    }

    // The player whose turn it is now won, because the previous player exceeded N
    if (takahashi_turn) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Game tree depth parity analysis for binary expansion pursuit-evasion games.
- **Reusable Pattern**: `Doubling Game Parity: compare depth parity, winner forces max expansion on own turn and min on opponent's.`

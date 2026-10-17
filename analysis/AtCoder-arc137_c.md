# Problem Analysis: AtCoder-arc137_c — Distinct Numbers

**Problem ID**: `AtCoder-arc137_c`  
**Contest**: `arc137`  
**Rating / Difficulty**: 2043  
**URL**: https://atcoder.jp/contests/arc137/tasks/arc137_c  
**VJudge Tag**: `[problem:AtCoder-arc137_c]`  
**Category File**: [`../categories/game_theory/strategy_stealing_extreme_gap_parity_game.md`](../categories/game_theory/strategy_stealing_extreme_gap_parity_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Combinatorial Games`  
- **Topic (Skill)**: `Strategy-Stealing and Extreme Gap Parity Invariant in Subtraction Game`  

---

## 1. Problem Statement & Key Idea
Given a sorted sequence A_1 < A_2 < ... < A_N of positive integers. Two players take turns replacing an element with a smaller non-negative integer not currently in A. The player who cannot move loses. Determine if Alice (first) wins.

**Key Idea**: Analyze the top two elements A_N and A_{N-1}. If A_N - A_{N-1} > 1, Alice can move A_N to A_{N-1} + 1. If that resulting state is losing for the recipient, Bob loses. If it were winning for the recipient, Alice could have chosen that very winning transition directly (strategy stealing / option dominance). Thus Alice always wins if A_N - A_{N-1} > 1. If A_N - A_{N-1} == 1, neither player can leapfrog without losing, so moves strictly decrement available empty slots one by one. The total number of available slots is A_N - (N - 1), so Alice wins iff (A_N - N) is even.

## 2. Core Observation & Invariant
A gap > 1 at the top allows strategy-stealing dominance; a gap of 1 forces full linear descent determined purely by gap parity.

## 3. Step-by-Step Algorithm
1. If A_N - A_{N-1} > 1: Alice wins.
2. If A_N - A_{N-1} == 1:
3.   Empty slots = A_N - N.
4.   If (A_N - N) % 2 != 0: Bob wins.
5.   Else: Alice wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Core Algorithmic Skill & Learning Takeaway
Strategy stealing dominance and forced game length parity invariants.

**Reusable Pattern**: Top Gap Strategy Stealing: If gap > 1, first player steals the winning strategy; if gap == 1, outcome is parity of remaining empty slots.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (a[n - 1] - a[n - 2] > 1) {
        cout << "Alice\n";
    } else {
        if ((a[n - 1] - n) % 2 != 0) {
            cout << "Bob\n";
        } else {
            cout << "Alice\n";
        }
    }

    return 0;
}
```

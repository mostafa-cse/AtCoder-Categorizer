# Problem Analysis: AtCoder-arc064_b — An Ordinary Game

**Problem ID**: `AtCoder-arc064_b`  
**Contest**: `abc048`  
**Rating / Difficulty**: 1814  
**URL**: https://atcoder.jp/contests/abc048/tasks/arc064_b  
**VJudge Tag**: `[problem:AtCoder-arc064_b]`  
**Category File**: [`../categories/game_theory/boundary_endpoints_game_parity.md`](../categories/game_theory/boundary_endpoints_game_parity.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Impartial Games`  
- **Topic (Skill)**: `Combinatorial Game Parity Determined by Boundary Endpoints`  

---

## 1. Problem Statement & Key Idea
Given string S of length >= 3 with no adjacent identical characters. In a turn, a player deletes an interior character such that no two adjacent characters become equal. A player who cannot move loses. Determine who wins.

**Key Insight**: The endpoints S[0] and S[N - 1] can never be deleted. The game must end in an alternating string c_1 c_2 c_1 c_2... If S[0] == S[N - 1], the final string must have odd length; if S[0] != S[N - 1], the final string must have even length.

## 2. Core Observation & Invariant
Since each turn removes exactly 1 character, the total turns played is N - (final_length), whose parity is completely determined by (S[0] == S[N - 1]) and N.

## 3. Step-by-Step Algorithm
1. Read string S. Let N = |S|.
2. If S[0] == S[N - 1]: final length is odd. Number of moves has parity (N - odd) = N % 2 == 0 ? odd : even.
3. If S[0] != S[N - 1]: final length is even. Number of moves has parity (N - even) = N % 2 == 0 ? even : odd.
4. First wins if total turns is odd, else Second wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    bool same_ends = (s.front() == s.back());

    // If same_ends, final length is odd
    // If !same_ends, final length is even
    int moves_parity = same_ends ? (n % 2 == 0 ? 1 : 0) : (n % 2 == 1 ? 1 : 0);

    if (moves_parity == 1) {
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
- **Core Skill**: Deriving exact invariant game duration parity from terminal boundary conditions.
- **Reusable Pattern**: `Terminal Endpoint Parity Invariant: Final length parity is fixed by endpoint equality.`

# Problem Analysis: AtCoder-arc151_c — 01 Game

**Problem ID**: `AtCoder-arc151_c`  
**Contest**: `arc151`  
**Rating / Difficulty**: 1940  
**URL**: https://atcoder.jp/contests/arc151/tasks/arc151_c  
**VJudge Tag**: `[problem:AtCoder-arc151_c]`  
**Category File**: [`../categories/game_theory/interval_grundy_alternating_boundary.md`](../categories/game_theory/interval_grundy_alternating_boundary.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Sprague-Grundy Theorem`  
- **Topic (Skill)**: `Interval Grundy Decomposition under Alternating Parity Boundary Constraints`  

---

## 1. Problem Statement & Key Idea
N squares in a row. M squares initially have 0 or 1. Players alternate placing 0 or 1 into an empty square such that no adjacent squares share the same number. Last player to move wins. Determine winner.

The board decomposes into independent intervals of empty cells. By Sprague-Grundy theorem, the total game is the XOR sum of segment Grundy values. For an open end of length L, G(L) = L. For an internal segment of length L between matching values (0...0 or 1...1), G(L) = 1 if L is odd, 0 if L is even (i.e. 1 for odd, 0 for even). Between opposite values (0...1 or 1...0), G(L) = 0 for all L! If M = 0, G = N mod 2.

## 2. Core Observation & Invariant
Opposite boundary values neutralize the entire interval (G = 0); matching values give parity 1; open ends give length L.

## 3. Step-by-Step Algorithm
1. If M == 0: Takahashi wins iff N % 2 == 1.
2. Sort clues by position.
3. xor_sum = (pos[0] - 1) ^ (N - pos[M - 1]).
4. For each adjacent clue pair: if val[i] == val[i + 1], xor_sum ^= 1.
5. If xor_sum != 0, print Takahashi; else print Aoki.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Clue {
    long long pos;
    int val;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    if (m == 0) {
        cout << (n % 2 == 1 ? "Takahashi" : "Aoki") << "\n";
        return 0;
    }

    vector<Clue> clues(m);
    for (int i = 0; i < m; ++i) {
        cin >> clues[i].pos >> clues[i].val;
    }

    sort(clues.begin(), clues.end(), [](const Clue& a, const Clue& b) {
        return a.pos < b.pos;
    });

    long long xor_sum = 0;

    xor_sum ^= (clues[0].pos - 1);

    for (int i = 0; i < m - 1; ++i) {
        if (clues[i].val == clues[i + 1].val) {
            xor_sum ^= 1;
        } else {
            xor_sum ^= 0;
        }
    }

    xor_sum ^= (n - clues[m - 1].pos);

    cout << (xor_sum != 0 ? "Takahashi" : "Aoki") << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sprague-Grundy game decomposition with local boundary-constrained state transitions.
- **Reusable Pattern**: `Boundary-Constrained Grundy: Open ends give G = L; identical boundaries give G = 1; opposite give G = 0.`

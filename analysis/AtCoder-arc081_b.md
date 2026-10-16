# Problem Analysis: AtCoder-arc081_b — Coloring Dominoes

**Problem ID**: `AtCoder-arc081_b`  
**Contest**: `abc071`  
**Rating / Difficulty**: 1165  
**URL**: https://atcoder.jp/contests/abc071/tasks/arc081_b  
**VJudge Tag**: `[problem:AtCoder-arc081_b]`  
**Category File**: [`../categories/dp/domino_tiling_chromatic_dp.md`](../categories/dp/domino_tiling_chromatic_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `State Machine DP`  
- **Topic (Skill)**: `Domino Tiling Chromatic Transition DP`  

---

## 1. Problem Statement & Key Idea
A 2 x N grid is tiled with dominoes (each 1x2 or 2x1). Color the dominoes using 3 colors such that adjacent dominoes have different colors. Output count modulo 10^9 + 7.

**Key Idea**: Each position in the 2 x N grid is occupied either by a single vertical domino (1x2) or two stacked horizontal dominoes (2x1).

## 2. Core Observation & Invariant
Transitions depend strictly on the type of current domino and previous domino: (1) First block: vertical -> 3 ways; horizontal -> 3 * 2 = 6 ways. (2) vert -> vert: 2 ways. (3) vert -> horiz: 2 ways. (4) horiz -> vert: 1 way. (5) horiz -> horiz: 3 ways. Scan left-to-right multiplying factors.

## 3. Step-by-Step Algorithm
1. Parse grid into domino blocks: 'V' for vertical (1 col), 'H' for horizontal pair (2 cols).
2. Initialize ways: if blocks[0] == 'V' ways = 3, else ways = 6.
3. For i from 1 to blocks.size() - 1: if prev == 'V' and cur == 'V': ways *= 2; if prev == 'V' and cur == 'H': ways *= 2; if prev == 'H' and cur == 'V': ways *= 1; if prev == 'H' and cur == 'H': ways *= 3; ways %= MOD.
4. Output ways.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s1, s2;
    if (!(cin >> n >> s1 >> s2)) return 0;

    vector<char> blocks;
    for (int i = 0; i < n; ) {
        if (s1[i] == s2[i]) {
            blocks.push_back('V');
            i += 1;
        } else {
            blocks.push_back('H');
            i += 2;
        }
    }

    long long ways = (blocks[0] == 'V' ? 3 : 6);

    for (size_t i = 1; i < blocks.size(); ++i) {
        char prev = blocks[i - 1];
        char cur = blocks[i];

        if (prev == 'V' && cur == 'V') ways = (ways * 2) % MOD;
        else if (prev == 'V' && cur == 'H') ways = (ways * 2) % MOD;
        else if (prev == 'H' && cur == 'V') ways = (ways * 1) % MOD;
        else if (prev == 'H' && cur == 'H') ways = (ways * 3) % MOD;
    }

    cout << ways << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: State-machine chromatic polynomial transitions on 2D strips.
- **Reusable Pattern**: `Domino coloring: V->V: *2, V->H: *2, H->V: *1, H->H: *3.`

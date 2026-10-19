# Problem Analysis: AtCoder-agc002_e — E. Candy Piles

**Problem ID**: `AtCoder-agc002_e`  
**Contest**: `agc002`  
**Rating / Difficulty**: 2889  
**URL**: https://atcoder.jp/contests/agc002/tasks/agc002_e  
**VJudge Tag**: `[problem:AtCoder-agc002_e]`  
**Category File**: [`../categories/game_theory/young_diagram_grid_walk_game.md`](../categories/game_theory/young_diagram_grid_walk_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
N piles of candies are given. In each turn, a player either removes the largest pile or removes 1 candy from every positive pile. The player who takes the last candy wins. Determine First or Second win.

## 2. Core Observation & Invariant
Sort piles in descending order to form a Young diagram. Removing the largest pile shifts origin right (x -> x+1); decrementing all piles shifts origin up (y -> y+1). The game is an impartial grid walk starting at (0, 0) where leaving the diagram loses. Along any diagonal x + y = c, winning/losing outcomes alternate. Find the largest diagonal cell (k, k) inside the diagram. The outcome of (k, k) depends on the parity of the distance to the right boundary vs top boundary.

## 3. Step-by-Step Algorithm
1. 1. Sort pile sizes a_1 >= a_2 >= ... >= a_N.
2. 2. Find maximum index k (0-indexed) such that a_{k+1} >= k + 1.
3. 3. Compute horizontal distance from (k, k) to right boundary: R = a_{k+1} - 1 - k.
4. 4. Compute vertical distance from (k, k) to top boundary: U = count of i with a_i > k.
5. 5. If R % 2 == 1 or (U - 1 - k) % 2 == 1, First wins; otherwise Second wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.rbegin(), a.rend());

    int k = 0;
    while (k < n && a[k] > k) {
        k++;
    }
    k--; // maximal k where a[k] > k

    long long U = a[k] - 1 - k;
    int r = k;
    while (r < n && a[r] > k) {
        r++;
    }
    long long R = (r - 1) - k;

    if (U % 2 == 1 || R % 2 == 1) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

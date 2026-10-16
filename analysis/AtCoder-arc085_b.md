# Problem Analysis: AtCoder-arc085_b — ABS

**Problem ID**: `AtCoder-arc085_b`  
**Contest**: `abc078`  
**Rating / Difficulty**: 1550  
**URL**: https://atcoder.jp/contests/abc078/tasks/arc085_b  
**VJudge Tag**: `[problem:AtCoder-arc085_b]`  
**Category File**: [`../categories/game_theory/game_theory_card_draw_minimax.md`](../categories/game_theory/game_theory_card_draw_minimax.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax`  
- **Topic (Skill)**: `Game Theory Minimax 1-Step Lookahead / Card Draw Reduction`  

---

## 1. Problem Statement & Key Idea
N cards with values A_1, ..., A_N. X starts with card Z and Y starts with card W. X draws some number of cards (leaving at least 1 for Y). Y draws some cards. Final score is |X's card - Y's card|. X maximizes, Y minimizes. Determine the game outcome under optimal play.

**Key Insight**: By backward induction, Y will always choose to take all remaining cards up to N to achieve |X's chosen card - A_N|. Knowing this, X only needs to choose between taking all cards up to N (score |A_N - W|) or taking all cards up to N - 1 (score |A_{N-1} - A_N|).

## 2. Core Observation & Invariant
Any other choice gives Y an option to achieve an even smaller difference. Thus X's optimal move is simply max(|A_N - W|, |A_{N-1} - A_N|) when N >= 2.

## 3. Step-by-Step Algorithm
1. If N == 1, answer is |A_0 - W|.
2. If N >= 2, answer is max(|A[N-1] - W|, |A[N-2] - A[N-1]|).
3. Print answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long z, w;
    if (!(cin >> n >> z >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << abs(a[0] - w) << "\n";
    } else {
        long long ans = max(abs(a[n - 1] - w), abs(a[n - 2] - a[n - 1]));
        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Minimax analysis identifying dominant end-game strategies.
- **Reusable Pattern**: `Sequential Card Draw Minimax: simplifies to max(|last - W|, |second_last - last|).`

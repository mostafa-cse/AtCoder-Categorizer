# Problem Analysis: AtCoder-arc105_d — Let's Play Nim

**Problem ID**: `AtCoder-arc105_d`  
**Contest**: `arc105`  
**Rating / Difficulty**: 1871  
**URL**: https://atcoder.jp/contests/arc105/tasks/arc105_d  
**VJudge Tag**: `[problem:AtCoder-arc105_d]`  
**Category File**: [`../categories/game_theory/phase_shifted_nim_parity_inversion.md`](../categories/game_theory/phase_shifted_nim_parity_inversion.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Combinatorial Games`  
- **Topic (Skill)**: `Phase-Shifted Combinatorial Game with Nim Parity Inversion`  

---

## 1. Problem Statement & Key Idea
N coins are on a table in piles A_1..A_N. In Phase 1, players take turns placing piles into bags. In Phase 2, players play normal Nim on the bags. Who wins under optimal play?

**Key Insight**: Phase 2 is normal Nim: second player wins iff XOR sum of bags is 0. If N is odd, Player 1 makes the final bag placement, so Player 2 plays first in Nim; Player 2 can always ensure non-zero XOR sum, winning Nim (First player overall wins). If N is even, Player 2 makes the final placement; Player 2 can mirror Player 1 and make all bags pairwise identical iff every coin count has even frequency.

## 2. Core Observation & Invariant
When N is odd: Second player wins Nim, meaning First player in overall game loses Phase 2 -> Second player wins! When N is even: Second player wins overall iff all pile sizes appear an even number of times.

## 3. Step-by-Step Algorithm
1. If N % 2 == 1: print 'Second'.
2. If N % 2 == 0:
3.   Sort A. Count occurrences of each value.
4.   If every value appears an even number of times: print 'Second'.
5.   Else: print 'First'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

void solve() {
    int n;
    cin >> n;

    map<long long, int> freq;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        freq[a]++;
    }

    if (n % 2 == 1) {
        cout << "Second\n";
    } else {
        bool all_even = true;
        for (auto& [val, count] : freq) {
            if (count % 2 != 0) {
                all_even = false;
                break;
            }
        }
        if (all_even) cout << "Second\n";
        else cout << "First\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Tracing strategic control over terminal Nim states across a two-phase game structure.
- **Reusable Pattern**: `Two-Phase Nim Analysis: Odd N reverses first/second role; Even N reduces to even multiplicity matching.`

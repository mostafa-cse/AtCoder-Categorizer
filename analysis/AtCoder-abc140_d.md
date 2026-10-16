# Problem Analysis: AtCoder-abc140_d — Face Produces Unhappiness

**Problem ID**: `AtCoder-abc140_d`  
**Contest**: `abc140`  
**Rating / Difficulty**: 1074  
**URL**: https://atcoder.jp/contests/abc140/tasks/abc140_d  
**VJudge Tag**: `[problem:AtCoder-abc140_d]`  
**Category File**: [`../categories/basics/run_length_inversion_boundary_reduction.md`](../categories/basics/run_length_inversion_boundary_reduction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy / Invariants`  
- **Topic (Skill)**: `Run-Length Inversion / Boundary Reduction Greedy`  

---

## 1. Problem Statement & Key Idea
N people standing in line facing 'L' or 'R'. A person at i is happy if they face someone facing the same way (person facing R has i+1 facing R; person facing L has i-1 facing L). You can reverse a contiguous subarray of people and flip their directions up to K times. Maximize happy people.

**Key Idea**: The total number of happy people is N minus the number of contiguous blocks of same-facing people (run-length blocks).

## 2. Core Observation & Invariant
Reversing an internal contiguous segment flips directions and merges at most 2 boundaries between different blocks, reducing block count by at most 2 per operation. Thus, each operation increases happiness by at most 2, capped at N - 1.

## 3. Step-by-Step Algorithm
1. Calculate initial happiness: count i where S[i] == S[i+1].
2. Each operation can increase happiness by 2.
3. Result is min(N - 1, initial_happiness + 2 * K).
4. Output result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    string s;
    if (!(cin >> n >> k >> s)) return 0;

    int initial_happy = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i + 1]) {
            initial_happy++;
        }
    }

    int ans = min(n - 1, initial_happy + 2 * k);
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Boundary reduction and invariant analysis under range reversal operations.
- **Reusable Pattern**: `Range reversal boundary reduction: happiness increases by min(N - 1, initial + 2 * K).`

# Problem Analysis: AtCoder-abc085_d — Katana Thrower

**Problem ID**: `AtCoder-abc085_d`  
**Contest**: `abc085`  
**Rating / Difficulty**: 954  
**URL**: https://atcoder.jp/contests/abc085/tasks/abc085_d  
**VJudge Tag**: `[problem:AtCoder-abc085_d]`  
**Category File**: [`../categories/basics/threshold_bounded_greedy.md`](../categories/basics/threshold_bounded_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Threshold-Bounded Greedy Consumption`  

---

## 1. Problem Statement & Key Idea
An enemy has H health. You have N katanas. Katana i can slash for a_i damage (unlimited uses) or be thrown for b_i damage (single use). Minimize attacks to defeat the enemy.

**Key Idea**: Slashing should only ever be done using the single katana with maximum slash damage max_a = max(a_i).

## 2. Core Observation & Invariant
Throwing katana j is superior to slashing if and only if b_j > max_a. Sort throwing damages in descending order and throw all katanas with b_j > max_a as long as H > 0. If health remains, finish with ceil(H / max_a) slashes.

## 3. Step-by-Step Algorithm
1. Find max_a = max(a_i).
2. Filter and sort all throwing damages b_i in descending order.
3. Initialize attacks = 0.
4. For each b in descending throws: if b > max_a and H > 0: H -= b, attacks++.
5. If H > 0: attacks += (H + max_a - 1) / max_a.
6. Print attacks.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long h;
    if (!(cin >> n >> h)) return 0;

    long long max_a = 0;
    vector<long long> b(n);

    for (int i = 0; i < n; ++i) {
        long long ai;
        cin >> ai >> b[i];
        max_a = max(max_a, ai);
    }

    sort(b.rbegin(), b.rend());

    long long attacks = 0;
    for (int i = 0; i < n; ++i) {
        if (b[i] > max_a && h > 0) {
            h -= b[i];
            attacks++;
        } else {
            break;
        }
    }

    if (h > 0) {
        attacks += (h + max_a - 1) / max_a;
    }

    cout << attacks << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy thresholding against a reusable maximum baseline.
- **Reusable Pattern**: `Use one-time bonuses with value > reusable_max first, then divide remainder by reusable_max.`

# Problem Analysis: AtCoder-arc075_b — Widespread

**Problem ID**: `AtCoder-arc075_b`  
**Contest**: `abc063`  
**Rating / Difficulty**: 1544  
**URL**: https://atcoder.jp/contests/abc063/tasks/arc075_b  
**VJudge Tag**: `[problem:AtCoder-arc075_b]`  
**Category File**: [`../categories/basics/binary_search_splash_damage.md`](../categories/basics/binary_search_splash_damage.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `Binary Search on Answer / Splash Damage Allocation`  

---

## 1. Problem Statement & Key Idea
N monsters with health H_i. An explosion deals A damage to a chosen center monster and B damage to all other monsters (A > B). Find the minimum explosions to defeat all monsters.

**Key Insight**: Binary search on the total explosions K. In K explosions, every monster automatically receives K * B splash damage. Additional center blasts on monster i add A - B damage each.

## 2. Core Observation & Invariant
For a fixed K, monster i has remaining health rem = max(0LL, H_i - K * B). The number of center hits needed on monster i is ceil(rem / (A - B)). All monsters are defeated iff the sum of needed center hits <= K.

## 3. Step-by-Step Algorithm
1. Binary search on explosions K in [1, 10^9].
2. Define check(K):
3.   centers_needed = 0.
4.   For each H_i:
5.     rem = H_i - K * B.
6.     If rem > 0: centers_needed += (rem + (A - B) - 1) / (A - B).
7.   Return centers_needed <= K.
8. Output the minimum K satisfying check(K).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max H))`
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
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }

    long long diff = a - b;
    long long low = 1, high = 1e9;
    long long ans = high;

    auto check = [&](long long k) -> bool {
        long long centers = 0;
        for (int i = 0; i < n; ++i) {
            long long rem = h[i] - k * b;
            if (rem > 0) {
                centers += (rem + diff - 1) / diff;
                if (centers > k) return false;
            }
        }
        return centers <= k;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Binary search feasibility check by isolating uniform baseline splash damage from targeted focal damage.
- **Reusable Pattern**: `Area-of-Effect Splash Damage: baseline K*B damage + ceil(rem / (A-B)) center allocations.`

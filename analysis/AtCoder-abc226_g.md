# Problem Analysis: AtCoder-abc226_g — G. The baggage

**Problem ID**: `AtCoder-abc226_g`  
**Contest**: `abc226`  
**Rating / Difficulty**: 2373  
**URL**: https://atcoder.jp/contests/abc226/tasks/abc226_g  
**VJudge Tag**: `[problem:AtCoder-abc226_g]`  
**Category File**: [`../categories/basics/greedy_bounded_knapsack_capacities.md`](../categories/basics/greedy_bounded_knapsack_capacities.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Determine if baggages of weights $1..5$ can be carried by people of capacities $1..5$. Strict greedy allocation matches items from weight 5 down to 1 to the tightest fitting available containers in $O(1)$ per testcase.

## 2. Core Observation & Invariant
Baggage weights and person capacities are integers in $[1, 5]$. Larger weights have strictly fewer container choices. Assigning weights from 5 down to 1 greedily to the tightest fitting available containers maximizes flexibility for smaller weights, with weight 1 items simply requiring total remaining capacity $\ge A_1$.

## 3. Step-by-Step Algorithm
1. Weight 5: must use $B_5$. If $A_5 > B_5$, return No. $B_5 \gets B_5 - A_5$.
2. Weight 4: use $B_4$ first, then $B_5$ (leaving 1 leftover capacity each). If $A_4 > 0$, return No.
3. Weight 3: use $B_3$ first, then $B_5$ (leaving 2 capacity each), then $B_4$ (leaving 1 capacity each). If $A_3 > 0$, return No.
4. Weight 2: use 2-capacity leftovers, then $B_2$, then $B_4$ (takes two 2s), then $B_5$ (takes two 2s, leaving 1). If $A_2 > 0$, return No.
5. Weight 1: check if total remaining capacity across all containers is $\ge A_1$ in $O(1)$ per testcase.

## 4. Complexity Analysis
- **Time Complexity**: `O(T)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long a[6], b[6];
    for (int i = 1; i <= 5; i++) cin >> a[i];
    for (int i = 1; i <= 5; i++) cin >> b[i];

    // 1. Items of weight 5
    if (a[5] > b[5]) {
        cout << "No\n";
        return;
    }
    b[5] -= a[5];

    // 2. Items of weight 4
    long long u4 = min(a[4], b[4]);
    a[4] -= u4;
    b[4] -= u4;
    if (a[4] > b[5]) {
        cout << "No\n";
        return;
    }
    b[5] -= a[4];
    long long rem1 = a[4]; // each gave 1 capacity leftover

    // 3. Items of weight 3
    long long u3 = min(a[3], b[3]);
    a[3] -= u3;
    b[3] -= u3;

    long long rem2 = 0;
    long long u3_from_5 = min(a[3], b[5]);
    a[3] -= u3_from_5;
    b[5] -= u3_from_5;
    rem2 += u3_from_5; // each left 2 capacity

    long long u3_from_4 = min(a[3], b[4]);
    a[3] -= u3_from_4;
    b[4] -= u3_from_4;
    rem1 += u3_from_4; // each left 1 capacity

    if (a[3] > 0) {
        cout << "No\n";
        return;
    }

    // 4. Items of weight 2
    // Use rem2 first
    long long u2_rem2 = min(a[2], rem2);
    a[2] -= u2_rem2;
    rem2 -= u2_rem2;

    // Use b[2]
    long long u2_b2 = min(a[2], b[2]);
    a[2] -= u2_b2;
    b[2] -= u2_b2;

    // Use b[4] (each can take 2 items of weight 2)
    long long take_from_b4 = min(a[2] / 2, b[4]);
    a[2] -= take_from_b4 * 2;
    b[4] -= take_from_b4;
    if (a[2] > 0 && b[4] > 0) {
        a[2]--;
        b[4]--;
        rem2++; // left 2 capacity
    }

    // Use b[5] (each can take 2 items of weight 2, leaves 1)
    long long take_from_b5 = min(a[2] / 2, b[5]);
    a[2] -= take_from_b5 * 2;
    b[5] -= take_from_b5;
    rem1 += take_from_b5;
    if (a[2] > 0 && b[5] > 0) {
        a[2]--;
        b[5]--;
        rem1++;
        rem2++; // took 2 out of 5, leaves 3 = 1 + 2
    }

    if (a[2] > 0) {
        cout << "No\n";
        return;
    }

    // 5. Items of weight 1
    long long total_cap1 = b[1] + rem1 + rem2 * 2 + b[2] * 2 + b[3] * 3 + b[4] * 4 + b[5] * 5;
    if (total_cap1 >= a[1]) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
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

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

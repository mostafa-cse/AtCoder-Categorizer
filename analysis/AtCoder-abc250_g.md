# Problem Analysis: AtCoder-abc250_g — Stonks

**Problem ID**: `AtCoder-abc250_g`  
**Contest**: `abc250`  
**Rating / Difficulty**: 2219  
**URL**: https://atcoder.jp/contests/abc250/tasks/abc250_g  
**VJudge Tag**: `[problem:AtCoder-abc250_g]`  
**Category File**: [`../categories/dynamic_programming/stonks_buy_low_sell_high_priority_queue_slope_trick.md`](../categories/dynamic_programming/stonks_buy_low_sell_high_priority_queue_slope_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Slope Trick`  

---

## 1. Problem Statement & Key Idea
Given daily stock prices P_1, ..., P_N, maximize total profit by choosing to buy 1 share, sell 1 share, or do nothing each day with unlimited holding capacity.

## 2. Core Observation & Invariant
Classic Slope Trick / Buy Low Sell High with priority queue replacement. When price P_i exceeds the minimum available price in the min-heap, we greedily pair it with the lowest price, adding P_i - top to profit. We push P_i twice: once representing an option to upgrade the selling price to a future higher price, and once as a buy option.

## 3. Step-by-Step Algorithm
1. 1. Maintain a min-priority queue of purchase opportunities.
2. 2. For each day i with price P_i: if pq is not empty and pq.top() < P_i, add P_i - pq.top() to total profit, pop top, and push P_i into pq.
3. 3. Push P_i into pq as a standard buy opportunity.
4. 4. Output total profit accumulated.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long ans = 0;

    for (int i = 0; i < n; i++) {
        long long p;
        cin >> p;
        if (!pq.empty() && pq.top() < p) {
            ans += p - pq.top();
            pq.pop();
            pq.push(p);
        }
        pq.push(p);
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

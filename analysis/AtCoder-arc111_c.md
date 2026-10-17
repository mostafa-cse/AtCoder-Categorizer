# Problem Analysis: AtCoder-arc111_c — Too Heavy

**Problem ID**: `AtCoder-arc111_c`  
**Contest**: `arc111`  
**Rating / Difficulty**: 1750  
**URL**: https://atcoder.jp/contests/arc111/tasks/arc111_c  
**VJudge Tag**: `[problem:AtCoder-arc111_c]`  
**Category File**: [`../categories/basics/permutation_cycle_catalyst_swap.md`](../categories/basics/permutation_cycle_catalyst_swap.md)  

- **Tag (Domain)**: `Greedy`  
- **Subtopic**: `Permutations / Cycles`  
- **Topic (Skill)**: `Permutation Cycle Decomposition with Minimum-Capacity Catalyst Sorting`  

---

## 1. Problem Statement & Key Idea
N people and N pieces of luggage. Person i has weight A_i, luggage j has weight B_j. Person i currently has luggage P_i, but wants luggage i. A person can only hold luggage if strictly heavier than it (A_i > B_cur). Two people can swap luggage if both can lift what they receive. Find min swaps or output -1.

**Key Insight**: The permutation P decomposes into independent cycles. For any cycle of length >= 2, each person who does not have their own luggage must satisfy A_i > B_{P_i} initially. If this holds, the person with the smallest target luggage weight B_u can safely take their own luggage first and act as a catalyst.

## 2. Core Observation & Invariant
Sorting people in a cycle by target luggage weight B_i allows sequential swaps: swap catalyst with whoever currently holds luggage i, resolving luggage i without ever violating weight capacity.

## 3. Step-by-Step Algorithm
1. If P[i] != i and A[i] <= B[P[i]]: output -1 (cannot even hold current luggage).
2. Decompose P into cycles.
3. For each cycle of size > 1:
4.   Find person u with minimum B[u]. If A[u] <= B[u], output -1.
5.   Sort other vertices in cycle by B[v] ascending and swap with catalyst.
6. Print total swaps and swap pairs.

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
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1), b(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int i = 1; i <= n; ++i) cin >> b[i];

    vector<int> p(n + 1), pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
        pos[p[i]] = i;
    }

    for (int i = 1; i <= n; ++i) {
        if (p[i] != i && a[i] <= b[p[i]]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    vector<int> order(n);
    for (int i = 0; i < n; ++i) order[i] = i + 1;
    sort(order.begin(), order.end(), [&](int x, int y) {
        return b[x] < b[y];
    });

    vector<pair<int, int>> swaps;
    for (int x : order) {
        if (p[x] == x) continue;
        int holder = pos[x];
        swaps.push_back({x, holder});

        // Swap luggage between x and holder
        int lug_x = p[x];
        int lug_h = p[holder]; // which is x

        p[x] = lug_h;
        p[holder] = lug_x;

        pos[lug_h] = x;
        pos[lug_x] = holder;
    }

    cout << swaps.size() << "\n";
    for (auto& s : swaps) {
        cout << s.first << " " << s.second << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Permutation cycle resolution under weight capacity constraints via catalyst ordering.
- **Reusable Pattern**: `Permutation Cycle Catalyst Swap: Pick element with min target weight B to resolve cycle.`

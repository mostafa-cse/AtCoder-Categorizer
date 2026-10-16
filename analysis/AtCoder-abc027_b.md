# Problem Analysis: AtCoder-abc027_b — Island Bridges

**Problem ID**: `AtCoder-abc027_b`  
**Contest**: `abc027`  
**Rating / Difficulty**: 855  
**URL**: https://atcoder.jp/contests/abc027/tasks/abc027_b  
**VJudge Tag**: `[problem:AtCoder-abc027_b]`  
**Category File**: [`../categories/math/prefix_imbalance_minimum_cuts.md`](../categories/math/prefix_imbalance_minimum_cuts.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Prefix Invariants`  
- **Topic (Skill)**: `Prefix Imbalance Minimum Cuts`  

---

## 1. Problem Statement & Key Idea
N islands in a line have populations a_1, ..., a_N. You can build bridges between adjacent islands (i, i+1). Find the minimum number of bridges needed so that all connected islands can redistribute people equally.

**Key Idea**: If total population S is not divisible by N, redistribution is impossible (-1). The target population for each island is avg = S / N.

## 2. Core Observation & Invariant
Consider the cut between island i and i+1. The first i islands currently have sum_{j=1}^i a_j people, but need i * avg people. If sum_{j=1}^i a_j != i * avg, people must cross between i and i+1, so a bridge is mandatory! Conversely, if sum_{j=1}^i a_j == i * avg, no people need to cross, so no bridge is needed.

## 3. Step-by-Step Algorithm
1. Compute total sum S. If S % N != 0, output -1.
2. Let avg = S / N.
3. Initialize bridges = 0, running_sum = 0.
4. For i = 1 to N - 1: running_sum += a[i]. If running_sum != i * avg, bridges++.
5. Print bridges.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % n != 0) {
        cout << -1 << "\n";
        return 0;
    }

    int avg = total / n;
    int bridges = 0;
    int pref = 0;

    for (int i = 0; i < n - 1; ++i) {
        pref += a[i];
        if (pref != (i + 1) * avg) {
            bridges++;
        }
    }

    cout << bridges << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Determining minimum cut bridges via prefix mass balance conservation.
- **Reusable Pattern**: `Mandatory boundary edge test: prefix_sum != prefix_length * average.`

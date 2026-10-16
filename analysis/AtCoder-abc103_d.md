# Problem Analysis: AtCoder-abc103_d — Islands War

**Problem ID**: `AtCoder-abc103_d`  
**Contest**: `abc103`  
**Rating / Difficulty**: 1278  
**URL**: https://atcoder.jp/contests/abc103/tasks/abc103_d  
**VJudge Tag**: `[problem:AtCoder-abc103_d]`  
**Category File**: [`../categories/basics/interval_scheduling_right_endpoint_cuts.md`](../categories/basics/interval_scheduling_right_endpoint_cuts.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Interval Scheduling / Right-Endpoint Greedy Cuts`  

---

## 1. Problem Statement & Key Idea
N islands in a row with N - 1 bridges between adjacent islands. M disputes: dispute i requires island a_i and b_i to NOT be connected. Find the minimum bridges to remove.

**Key Idea**: Each dispute requires cutting at least one bridge in the interval [a_i, b_i - 1]. This is equivalent to finding the minimum stabbing set for a set of intervals.

## 2. Core Observation & Invariant
Sort disputes by their right endpoint b_i in ascending order. Greedily cut the rightmost bridge in the interval: bridge b_i - 1. Cutting as far right as possible maximizes the number of subsequent disputes that are also severed by the same cut!

## 3. Step-by-Step Algorithm
1. Read M intervals (a_i, b_i).
2. Sort intervals by right endpoint b_i ascending.
3. Initialize cuts = 0, last_cut = -1.
4. For each interval (a, b): if a > last_cut, we must make a new cut: cuts++, last_cut = b - 1.
5. Print cuts.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Dispute {
    int a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Dispute> d(m);
    for (int i = 0; i < m; ++i) {
        cin >> d[i].a >> d[i].b;
    }

    sort(d.begin(), d.end(), [](const Dispute& x, const Dispute& y) {
        return x.b < y.b;
    });

    int cuts = 0;
    int last_cut = -1;

    for (const auto& disp : d) {
        if (disp.a > last_cut) {
            cuts++;
            last_cut = disp.b - 1;
        }
    }

    cout << cuts << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy interval stabbing / hitting set using rightmost endpoint sorting.
- **Reusable Pattern**: `Interval stabbing: sort by end ascending, cut at end - 1 if start > last_cut.`

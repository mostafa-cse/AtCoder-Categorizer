# Problem Analysis: AtCoder-abc160_d — Line++

**Problem ID**: `AtCoder-abc160_d`  
**Contest**: `abc160`  
**Rating / Difficulty**: 879  
**URL**: https://atcoder.jp/contests/abc160/tasks/abc160_d  
**VJudge Tag**: `[problem:AtCoder-abc160_d]`  
**Category File**: [`../categories/graph_theory/shortcut_distance_enumeration.md`](../categories/graph_theory/shortcut_distance_enumeration.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Shortcut Distance Closed Form Enumeration`  

---

## 1. Problem Statement & Key Idea
A graph has N vertices along a line with edges (i, i+1) for 1 <= i < N, plus an additional shortcut edge (X, Y) with X < Y. For each k in 1..N-1, count the number of pairs (i, j) with i < j whose shortest path distance is exactly k.

**Key Idea**: For any pair of vertices (i, j) with i < j, the shortest path can either stay entirely on the line or take the shortcut (X, Y).

## 2. Core Observation & Invariant
Distance is min(j - i, |i - X| + 1 + |j - Y|). Since N <= 2000, we can evaluate all O(N^2) pairs in O(1) each and accumulate counts into a frequency array.

## 3. Step-by-Step Algorithm
1. Initialize count array ans[1..N-1] to 0.
2. Iterate i from 1 to N - 1 and j from i + 1 to N.
3. Compute dist = min(j - i, abs(i - X) + 1 + abs(j - Y)).
4. Increment ans[dist].
5. Print ans[k] for each k from 1 to N - 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
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

    int n, x, y;
    if (!(cin >> n >> x >> y)) return 0;

    vector<int> ans(n, 0);

    for (int i = 1; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            int direct = j - i;
            int via_bridge = abs(i - x) + 1 + abs(j - y);
            int dist = min(direct, via_bridge);
            ans[dist]++;
        }
    }

    for (int k = 1; k < n; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Closed-form metric formulation with graph shortcuts.
- **Reusable Pattern**: `Shortest path on line with bridge (X, Y): min(j - i, |i - X| + 1 + |j - Y|).`

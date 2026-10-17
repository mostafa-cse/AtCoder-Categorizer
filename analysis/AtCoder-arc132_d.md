# Problem Analysis: AtCoder-arc132_d — Between Two Binary Strings

**Problem ID**: `AtCoder-arc132_d`  
**Contest**: `arc132`  
**Rating / Difficulty**: 2221  
**URL**: https://atcoder.jp/contests/arc132/tasks/arc132_d  
**VJudge Tag**: `[problem:AtCoder-arc132_d]`  
**Category File**: [`../categories/basics/greedy_binary_strings_envelope_ray_tracing.md`](../categories/basics/greedy_binary_strings_envelope_ray_tracing.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Maximize the beauty (number of adjacent identical characters) of a binary string lying on the shortest swap path between two given binary strings S and T.

## 2. Core Observation & Invariant
A string lies on a shortest swap path between S and T iff the cumulative count of ones at every prefix p is bounded within [low[p], high[p]] = [min(pref_S[p], pref_T[p]), max(pref_S[p], pref_T[p])]. Maximizing beauty (n + m - 1 - transitions) is equivalent to minimizing the number of alternating runs of 0s and 1s. This maps to finding a path with minimum turns in a 2D corridor from (0,0) to (n,m). Greedily ray-shooting horizontally and vertically as far as possible from the current position achieves the theoretical minimum turns.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix sums of 1s in S and T to determine lower and upper bounds low[p] and high[p] for all prefix lengths p in [0, n+m].
2. 2. If n == 0 or m == 0, output max(0, n + m - 1).
3. 3. Simulate greedy ray-shooting starting with a horizontal move (run of 0s):
4.    - Move horizontally (increasing x, constant y) as far as valid: low[x+y] <= y <= high[x+y].
5.    - Move vertically (increasing y, constant x) as far as valid: low[x+y] <= y <= high[x+y].
6.    - Repeat until (n, m) is reached, counting the number of segments.
7. 4. Simulate greedy ray-shooting starting with a vertical move (run of 1s).
8. 5. The minimum segments across both options yields max beauty = (n + m - 1) - (min_segs - 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    string s, t;
    cin >> s >> t;

    int L = n + m;
    if (n == 0 || m == 0) {
        cout << max(0, L - 1) << "\n";
        return 0;
    }

    vector<int> ps(L + 1, 0), pt(L + 1, 0);
    for (int i = 0; i < L; ++i) {
        ps[i + 1] = ps[i] + (s[i] == '1' ? 1 : 0);
        pt[i + 1] = pt[i] + (t[i] == '1' ? 1 : 0);
    }

    vector<int> low(L + 1), high(L + 1);
    for (int i = 0; i <= L; ++i) {
        low[i] = min(ps[i], pt[i]);
        high[i] = max(ps[i], pt[i]);
    }

    auto simulate = [&](int first_dir) -> int {
        int x = 0, y = 0;
        int segs = 0;
        int cur_dir = first_dir;
        while (x < n || y < m) {
            segs++;
            if (cur_dir == 0) {
                int nx = x;
                while (nx + 1 <= n && low[nx + 1 + y] <= y && y <= high[nx + 1 + y]) {
                    nx++;
                }
                if (nx == x && (x < n || y < m)) return 1e9;
                x = nx;
                cur_dir = 1;
            } else {
                int ny = y;
                while (ny + 1 <= m && low[x + ny + 1] <= ny + 1 && ny + 1 <= high[x + ny + 1]) {
                    ny++;
                }
                if (ny == y && (x < n || y < m)) return 1e9;
                y = ny;
                cur_dir = 0;
            }
        }
        return segs;
    };

    int s0 = simulate(0);
    int s1 = simulate(1);
    int min_segs = min(s0, s1);

    cout << (L - 1) - (min_segs - 1) << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

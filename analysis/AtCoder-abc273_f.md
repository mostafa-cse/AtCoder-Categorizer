# Problem Analysis: AtCoder-abc273_f — F. Hammer 2

**Problem ID**: `AtCoder-abc273_f`  
**Contest**: `abc273`  
**Rating / Difficulty**: 2277  
**URL**: https://atcoder.jp/contests/abc273/tasks/abc273_f  
**VJudge Tag**: `[problem:AtCoder-abc273_f]`  
**Category File**: [`../categories/dynamic_programming_dp/interval_dp_1d_coordinate_hammer_wall_reachability.md`](../categories/dynamic_programming_dp/interval_dp_1d_coordinate_hammer_wall_reachability.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given a coordinate line with start at 0, target at $X$, $N$ walls, and $N$ hammers required to break corresponding walls, find the minimum total travel distance to reach $X$, or -1 if unreachable.

## 2. Core Observation & Invariant
On a 1D line starting at 0, the set of visited coordinates always forms a contiguous interval $[l, r]$ containing 0, with the player situated at either $l$ or $r$. Expanding to $l - 1$ or $r + 1$ is valid if and only if any wall encountered has its associated hammer located within $[l, r]$.

## 3. Step-by-Step Algorithm
1. 1. Collect all critical points: start 0, goal $X$, wall locations $Y_i$, and hammer locations $Z_i$ ($2N + 2 \le 3002$ points). Compress coordinates into a sorted array of unique values.\n2. Define interval DP state: $dp[l][r][0]$ is the minimum distance to have visited the compressed range $[l, r]$ ending at left endpoint $l$; $dp[l][r][1]$ is the minimum distance ending at right endpoint $r$.\n3. Transitions from state $(l, r, \text{side})$ expand by 1 step: moving left to $l - 1$ is allowed if $l - 1$ is not a wall or if its required hammer index lies in $[l, r]$; moving right to $r + 1$ is similarly conditioned.\n4. Once an interval $[l, r]$ covers the goal coordinate $X$, update the global answer $\text{ans} = \min(\text{ans}, dp[l][r][0], dp[l][r][1])$. Total complexity is $O(M^2)$ where $M \le 3000$, executing in under 0.1s.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 1e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> y(n), z(n);
    vector<long long> coords;
    coords.push_back(0);
    coords.push_back(x);

    for (int i = 0; i < n; i++) {
        cin >> y[i];
        coords.push_back(y[i]);
    }
    for (int i = 0; i < n; i++) {
        cin >> z[i];
        coords.push_back(z[i]);
    }

    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    int m = coords.size();
    int s = lower_bound(coords.begin(), coords.end(), 0) - coords.begin();
    int g = lower_bound(coords.begin(), coords.end(), x) - coords.begin();

    vector<int> req(m, -1);
    for (int i = 0; i < n; i++) {
        int wall_idx = lower_bound(coords.begin(), coords.end(), y[i]) - coords.begin();
        int hammer_idx = lower_bound(coords.begin(), coords.end(), z[i]) - coords.begin();
        req[wall_idx] = hammer_idx;
    }

    vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(m, vector<long long>(2, INF)));
    dp[s][s][0] = 0;
    dp[s][s][1] = 0;

    long long ans = INF;

    for (int len = 1; len <= m; len++) {
        for (int l = 0; l + len - 1 < m; l++) {
            int r = l + len - 1;

            if (l <= g && g <= r) {
                ans = min({ans, dp[l][r][0], dp[l][r][1]});
                continue;
            }

            for (int side = 0; side < 2; side++) {
                long long cur_dist = dp[l][r][side];
                if (cur_dist >= INF) continue;

                long long cur_pos = (side == 0 ? coords[l] : coords[r]);

                if (l > 0) {
                    int nxt = l - 1;
                    int needed_hammer = req[nxt];
                    if (needed_hammer == -1 || (needed_hammer >= l && needed_hammer <= r)) {
                        long long d = cur_dist + abs(coords[nxt] - cur_pos);
                        dp[nxt][r][0] = min(dp[nxt][r][0], d);
                    }
                }

                if (r + 1 < m) {
                    int nxt = r + 1;
                    int needed_hammer = req[nxt];
                    if (needed_hammer == -1 || (needed_hammer >= l && needed_hammer <= r)) {
                        long long d = cur_dist + abs(coords[nxt] - cur_pos);
                        dp[l][nxt][1] = min(dp[l][nxt][1], d);
                    }
                }
            }
        }
    }

    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

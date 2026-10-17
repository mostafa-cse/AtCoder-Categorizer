# Problem Analysis: AtCoder-abc076_d — AtCoder Express

**Problem ID**: `AtCoder-abc076_d`  
**Contest**: `abc076`  
**Rating / Difficulty**: 1884  
**URL**: https://atcoder.jp/contests/abc076/tasks/abc076_d  
**VJudge Tag**: `[problem:AtCoder-abc076_d]`  
**Category File**: [`../categories/basics/velocity_profile_envelope_bidirectional_relaxation.md`](../categories/basics/velocity_profile_envelope_bidirectional_relaxation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Continuous Optimization`  
- **Topic (Skill)**: `Velocity Profile Chmin Envelope via Bidirectional Relaxation on Doubled Grid`  

---

## 1. Problem Statement & Key Idea
A train travels through N sections. Section i has duration t_i and speed limit v_i. Acceleration and deceleration are at most 1 m/s^2. Start and end at speed 0. Find the maximum distance traveled.

**Key Insight**: Discretize time into 0.5-second steps by doubling all times and speeds (t -> 2t, v -> 2v). The velocity profile v(t) must satisfy: (1) section speed limits, (2) start and end at 0, (3) v(t + 1) <= v(t) + 1, (4) v(t) <= v(t + 1) + 1. Initialize max allowable speed at each grid point and apply forward and backward chmin relaxation.

## 2. Core Observation & Invariant
Integrating the resulting upper bound velocity envelope using the trapezoidal rule gives the exact maximum distance.

## 3. Step-by-Step Algorithm
1. Total time T = sum(t_i). Double time steps to 2 * T.
2. Initialize upper bound limit[2 * T + 1] from section speed limits.
3. limit[0] = 0, limit[2 * T] = 0.
4. Forward relaxation: limit[t] = min(limit[t], limit[t - 1] + 0.5).
5. Backward relaxation: limit[t] = min(limit[t], limit[t + 1] + 0.5).
6. Integrate trapezoids: sum_{t=0}^{2T - 1} (limit[t] + limit[t + 1]) * 0.5 * 0.5.
7. Print total distance.

## 4. Complexity Analysis
- **Time Complexity**: `O(sum t_i)`
- **Space Complexity**: `O(sum t_i)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> t(n), v(n);
    int total_t = 0;
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        total_t += t[i];
    }
    for (int i = 0; i < n; ++i) cin >> v[i];

    int steps = 2 * total_t;
    vector<double> max_v(steps + 1, 1e9);

    int cur_time = 0;
    for (int i = 0; i < n; ++i) {
        for (int step = cur_time; step <= cur_time + 2 * t[i]; ++step) {
            max_v[step] = min(max_v[step], (double)v[i]);
        }
        cur_time += 2 * t[i];
    }

    max_v[0] = 0;
    max_v[steps] = 0;

    // Forward pass
    for (int step = 1; step <= steps; ++step) {
        max_v[step] = min(max_v[step], max_v[step - 1] + 0.5);
    }

    // Backward pass
    for (int step = steps - 1; step >= 0; --step) {
        max_v[step] = min(max_v[step], max_v[step + 1] + 0.5);
    }

    double distance = 0;
    for (int step = 0; step < steps; ++step) {
        distance += (max_v[step] + max_v[step + 1]) * 0.5 * 0.5;
    }

    cout << fixed << setprecision(12) << distance << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Continuous kinematic profile bounding through discrete grid bidirectional chmin relaxation.
- **Reusable Pattern**: `Velocity Envelope Chmin: Forward & backward propagation of slope constraints on doubled grid.`

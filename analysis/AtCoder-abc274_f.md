# Problem Analysis: AtCoder-abc274_f — Fishing

**Problem ID**: `AtCoder-abc274_f`  
**Contest**: `abc274`  
**Rating / Difficulty**: 2212  
**URL**: https://atcoder.jp/contests/abc274/tasks/abc274_f  
**VJudge Tag**: `[problem:AtCoder-abc274_f]`  
**Category File**: [`../categories/geometry/fishing_moving_points_interval_sweep_line.md`](../categories/geometry/fishing_moving_points_interval_sweep_line.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Sweep Line`  
- **Topic (Skill)**: `Sweep Line Algorithm and Radial Sweep`  

---

## 1. Problem Statement & Key Idea
1D event sweep line over time intervals of fish containment with respect to reference fish coordinate.

## 2. Core Observation & Invariant
Without loss of generality, at the optimal moment, some fish i lies exactly at the left boundary of the net: x = X_i + t V_i. For a fixed reference fish i, any other fish j is inside the net [x, x + A] iff 0 <= (X_j - X_i) + t(V_j - V_i) <= A, which defines a closed time interval [L_{i,j}, R_{i,j}] cap [0, infty).

## 3. Step-by-Step Algorithm
1. 1. For each fish i in 1..N:
2.    - Set base weight W_i.
3.    - For every other fish j, solve the linear inequalities for t >= 0 to get valid interval [L, R]. If delta V == 0 and delta X in [0, A], add W_j to base weight.
4.    - Create event +W_j at time L and -W_j at time R.
5.    - Sort events (process enters before leaves at identical times) and sweep to find maximum weight for reference fish i.
6. 2. Output the global maximum over all reference fish.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Event {
    double t;
    int type; // +1: enter, -1: leave
    int weight;

    bool operator<(const Event& other) const {
        if (abs(t - other.t) > 1e-11) {
            return t < other.t;
        }
        return type > other.type; // enter (+1) before leave (-1)
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    double A;
    if (!(cin >> N >> A)) return 0;

    struct Fish {
        int w;
        double x, v;
    };

    vector<Fish> fishes(N);
    for (int i = 0; i < N; ++i) {
        cin >> fishes[i].w >> fishes[i].x >> fishes[i].v;
    }

    int global_max = 0;

    for (int i = 0; i < N; ++i) {
        int base_weight = fishes[i].w;
        vector<Event> events;

        for (int j = 0; j < N; ++j) {
            if (i == j) continue;

            double dx = fishes[j].x - fishes[i].x;
            double dv = fishes[j].v - fishes[i].v;

            if (abs(dv) < 1e-11) {
                if (dx >= -1e-11 && dx <= A + 1e-11) {
                    base_weight += fishes[j].w;
                }
            } else if (dv > 0) {
                double l = -dx / dv;
                double r = (A - dx) / dv;
                l = max(0.0, l);
                if (l <= r + 1e-11) {
                    events.push_back({l, 1, fishes[j].w});
                    events.push_back({r, -1, fishes[j].w});
                }
            } else {
                double l = (A - dx) / dv;
                double r = -dx / dv;
                l = max(0.0, l);
                if (l <= r + 1e-11) {
                    events.push_back({l, 1, fishes[j].w});
                    events.push_back({r, -1, fishes[j].w});
                }
            }
        }

        sort(events.begin(), events.end());

        int cur_weight = base_weight;
        global_max = max(global_max, cur_weight);

        for (const auto& ev : events) {
            if (ev.type == 1) {
                cur_weight += ev.weight;
            } else {
                cur_weight -= ev.weight;
            }
            global_max = max(global_max, cur_weight);
        }
    }

    cout << global_max << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

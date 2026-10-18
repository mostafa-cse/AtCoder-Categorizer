# Problem Analysis: AtCoder-arc072_c — Alice in linear land

**Problem ID**: `AtCoder-arc072_c`  
**Contest**: `arc072`  
**Rating / Difficulty**: 2655  
**URL**: https://atcoder.jp/contests/arc072/tasks/arc072_c  
**VJudge Tag**: `[problem:AtCoder-arc072_c]`  
**Category File**: [`../categories/basics/linear_land_backward_reachable_intervals.md`](../categories/basics/linear_land_backward_reachable_intervals.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Determining whether rewriting the q-th step in a vehicle's sequence of greedy moves can prevent reaching distance 0 decomposes into forward position tracking and backward threshold reachability DP.

## 2. Core Observation & Invariant
The vehicle moves towards the destination if distance decreases: x -> |x - d| if d < 2x, else x stays unchanged. Rewriting d_q allows the witch to set the distance entering step q+1 to any integer y in [0, X_{q-1}]. By backward simulation, let req[i] be the minimum distance before step i that avoids reaching 0 after steps i..N: req[N+1] = 1, and req[i] = req[i+1] if d_i >= 2*req[i+1] else req[i+1] + d_i. The witch succeeds iff X_{q-1} >= req[q+1].

## 3. Step-by-Step Algorithm
1. 1. Run forward simulation from D: X_0 = D, X_i = step(X_{i-1}, d_i).
2. 2. Run backward recurrence from N down to 1: req[N+1] = 1, req[i] = req[i+1] if d_i >= 2*req[i+1] else req[i+1] + d_i.
3. 3. For each query q, output 'YES' if X_{q-1} >= req[q+1], otherwise 'NO'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

long long step_dist(long long x, long long d) {
    if (d < 2 * x) {
        return abs(x - d);
    }
    return x;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long D;
    if (!(cin >> N >> D)) return 0;

    vector<long long> d(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> d[i];
    }

    int Q;
    if (!(cin >> Q)) return 0;
    vector<int> q(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> q[i];
    }

    // Forward simulation
    vector<long long> X(N + 1);
    X[0] = D;
    for (int i = 1; i <= N; ++i) {
        X[i] = step_dist(X[i - 1], d[i]);
    }

    // Backward simulation
    // req[i] = minimum distance needed before step i to prevent reaching 0 after steps i..N
    vector<long long> req(N + 2);
    req[N + 1] = 1;
    for (int i = N; i >= 1; --i) {
        long long nxt = req[i + 1];
        if (d[i] >= 2 * nxt) {
            req[i] = nxt;
        } else {
            req[i] = nxt + d[i];
        }
    }

    for (int i = 0; i < Q; ++i) {
        int idx = q[i];
        if (X[idx - 1] >= req[idx + 1]) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

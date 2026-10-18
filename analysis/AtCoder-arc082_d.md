# Problem Analysis: AtCoder-arc082_d — Sandglass

**Problem ID**: `AtCoder-arc082_d`  
**Contest**: `arc082`  
**Rating / Difficulty**: 2429  
**URL**: https://atcoder.jp/contests/arc082/tasks/arc082_d  
**VJudge Tag**: `[problem:AtCoder-arc082_d]`  
**Category File**: [`../categories/basics/sandglass_piecewise_clamped_linear_binary_search.md`](../categories/basics/sandglass_piecewise_clamped_linear_binary_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Maintain the sandglass state transformation as a piecewise-linear clamped function f(a) = min(B, max(A, a + D)) across flip events, and answer queries in O(log K) via binary search on flip times.

## 2. Core Observation & Invariant
Both draining and filling operations compose with clamping to preserve the functional invariant f(a) = clamp(a + D, A, B). Because the function is monotonic, the state at any time t can be evaluated in O(1) from the latest preceding flip event.

## 3. Step-by-Step Algorithm
1. 1. Precompute states (t, D, A, B) at time 0 and each flip time r_i in O(K) time.
2. 2. For each query (t_q, a_q), binary search the latest precomputed event time <= t_q.
3. 3. Advance the state by dt = t_q - base.t with appropriate flow direction sgn.
4. 4. Evaluate min(B_q, max(A_q, a_q + D_q)) in O(1) and output the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(K + Q log K)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll X;
    int K;
    if (!(cin >> X >> K)) return 0;

    vector<ll> r(K);
    for (int i = 0; i < K; i++) cin >> r[i];

    struct State {
        ll t, D, A, B;
    };
    vector<State> states;
    states.push_back({0, 0, 0, X});

    ll cur_t = 0, cur_D = 0, cur_A = 0, cur_B = X;
    for (int i = 0; i < K; i++) {
        ll next_t = r[i];
        ll dt = next_t - cur_t;
        ll sgn = (i % 2 == 0 ? -1 : 1);
        cur_D += sgn * dt;
        cur_A = max(0LL, min(X, cur_A + sgn * dt));
        cur_B = max(0LL, min(X, cur_B + sgn * dt));
        cur_t = next_t;
        states.push_back({cur_t, cur_D, cur_A, cur_B});
    }

    int Q;
    cin >> Q;
    while (Q--) {
        ll t_q, a_q;
        cin >> t_q >> a_q;

        // Binary search for latest event <= t_q
        int low = 0, high = (int)states.size() - 1, best = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (states[mid].t <= t_q) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        auto& base = states[best];
        ll dt = t_q - base.t;
        ll sgn = (best % 2 == 0 ? -1 : 1);
        ll D_q = base.D + sgn * dt;
        ll A_q = max(0LL, min(X, base.A + sgn * dt));
        ll B_q = max(0LL, min(X, base.B + sgn * dt));

        ll ans = min(B_q, max(A_q, a_q + D_q));
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

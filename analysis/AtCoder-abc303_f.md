# Problem Analysis: AtCoder-abc303_f — F. Damage over Time

**Problem ID**: `AtCoder-abc303_f`  
**Contest**: `abc303`  
**Rating / Difficulty**: 2381  
**URL**: https://atcoder.jp/contests/abc303/tasks/abc303_f  
**VJudge Tag**: `[problem:AtCoder-abc303_f]`  
**Category File**: [`../categories/basics/damage_over_time_binary_search_convex.md`](../categories/basics/damage_over_time_binary_search_convex.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Find the earliest turn T to defeat a monster of health H given N spells dealing d_i damage for t_i turns. Binary searching on T allows greedy damage evaluation at each remaining turn k as max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i); summing over piecewise linear segments in O(N) per test evaluates in O(N log(H)) time.

## 2. Core Observation & Invariant
When evaluating whether a monster of health H can be defeated in T turns, casting spell i when k turns remain contributes min(t_i, k) * d_i damage. Since each turn's contribution is independent, the optimal strategy greedily maximizes F(k) = max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i) at each remaining turn k.

## 3. Step-by-Step Algorithm
1. Binary search on turn count T in [1, 2 * 10^18].
2. Precompute unique values of t_i, prefix maximum of t_i * d_i, and suffix maximum of d_i.
3. Between adjacent distinct values of t, F(k) = max(C_1, k * C_2) is piecewise linear, summed in O(1) using arithmetic progressions.
4. Sum across at most N intervals in O(N) using __int128 to test if total damage >= H.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log(H))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef __int128_t int128;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long H_in;
    if (!(cin >> n >> H_in)) return 0;
    int128 H = H_in;

    map<long long, long long> by_t;
    for (int i = 0; i < n; ++i) {
        long long t, d;
        cin >> t >> d;
        by_t[t] = max(by_t[t], d);
    }

    vector<long long> unique_t;
    vector<long long> val_d;
    for (auto& p : by_t) {
        unique_t.push_back(p.first);
        val_d.push_back(p.second);
    }
    int m = unique_t.size();

    vector<int128> max_td(m);
    int128 cur = 0;
    for (int i = 0; i < m; ++i) {
        cur = max(cur, (int128)unique_t[i] * val_d[i]);
        max_td[i] = cur;
    }

    vector<int128> max_d(m);
    cur = 0;
    for (int i = m - 1; i >= 0; --i) {
        cur = max(cur, (int128)val_d[i]);
        max_d[i] = cur;
    }

    auto sum_interval = [](int128 L, int128 R, int128 C1, int128 C2) -> int128 {
        if (L > R) return 0;
        if (C2 == 0) return C1 * (R - L + 1);
        int128 k_cross = (C1 + C2 - 1) / C2;
        int128 total = 0;
        if (L <= k_cross - 1) {
            int128 r1 = min(R, k_cross - 1);
            total += C1 * (r1 - L + 1);
        }
        if (max(L, k_cross) <= R) {
            int128 l2 = max(L, k_cross);
            int128 cnt = R - l2 + 1;
            int128 sum_k = (l2 + R) * cnt / 2;
            total += sum_k * C2;
        }
        return total;
    };

    auto total_damage = [&](int128 T) -> int128 {
        int128 total = 0;
        int128 prev = 0;
        for (int i = 0; i < m; ++i) {
            int128 t_curr = unique_t[i];
            if (prev + 1 > T) break;
            int128 L = prev + 1;
            int128 R = min(T, t_curr);
            int128 C1 = (i > 0 ? max_td[i - 1] : 0);
            int128 C2 = max_d[i];
            total += sum_interval(L, R, C1, C2);
            prev = t_curr;
            if (prev >= T) break;
        }
        if (T > prev) {
            total += (T - prev) * max_td[m - 1];
        }
        return total;
    };

    long long low = 1, high = 2000000000000000000LL;
    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (total_damage(mid) >= H) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

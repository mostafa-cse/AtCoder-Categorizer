# Problem Analysis: AtCoder-cf_2015_morning_hard_b — D - 立方体とペンキ

**Problem ID**: `AtCoder-cf_2015_morning_hard_b`  
**Contest**: `cf_2015_morning_hard`  
**Rating / Difficulty**: 2456  
**URL**: https://atcoder.jp/contests/cf_2015_morning_hard/tasks/cf_2015_morning_hard_b  
**VJudge Tag**: `[problem:AtCoder-cf_2015_morning_hard_b]`  
**Category File**: [`../categories/data_structures_ds/cubes_paint_monotonic_stack_peak_shaving.md`](../categories/data_structures_ds/cubes_paint_monotonic_stack_peak_shaving.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Remove at most $K$ unit cubes from a 2D histogram of heights $A_i$ (keeping all $A_i \ge 1$) to minimize the total painted surface area.

## 2. Core Observation & Invariant
Every removed cube strictly decreases the front and back painted area by 2, contributing $-2K$ to the total area change. Side area decreases by 2 only when a complete horizontal row across a contiguous peak between higher boundaries is shaved. A monotonic stack decomposes the histogram into peak blocks $(W_i, \Delta H_i)$, where width $W_i$ represents the number of cubes per shaved horizontal layer, giving an additional $-2$ area reduction per unit layer. Greedy allocation of $K$ to the narrowest widths $W_i$ first minimizes the final surface area.

## 3. Step-by-Step Algorithm
1. 1. Pad array $A$ with 1 at both ends to bound peaks.
2. 2. Use a monotonic stack to identify all local peak rectangular blocks $(W_i, \Delta H_i)$ where $W_i$ is width and $\Delta H_i$ is height.
3. 3. Sort blocks by width $W_i$ ascending.
4. 4. Initialize answer to the original surface area $- 2K$.
5. 5. Greedily shave layers: take $\min(\Delta H_i, \lfloor K / W_i \rfloor)$ layers, subtract $2 \times \text{take}$ from the surface area, and decrement $K$ by $\text{take} \times W_i$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<long long> A(N);
    long long tot_A = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        tot_A += A[i];
    }

    long long top = N;
    long long front_back = 2 * tot_A;
    long long sides = A[0] + A[N - 1];
    for (int i = 0; i < N - 1; ++i) {
        sides += abs(A[i] - A[i + 1]);
    }
    long long init_area = top + front_back + sides;

    vector<long long> padded;
    padded.push_back(1);
    for (auto x : A) padded.push_back(x);
    padded.push_back(1);

    vector<pair<long long, long long>> st; // {height, width}
    vector<pair<long long, long long>> V;  // {width, diff}

    for (long long h : padded) {
        long long w = 0;
        while (!st.empty() && st.back().first > h) {
            auto top_elem = st.back();
            st.pop_back();
            w += top_elem.second;
            long long lower = max(h, st.empty() ? 1LL : st.back().first);
            long long diff = top_elem.first - lower;
            if (diff > 0 && w > 0) {
                V.push_back({w, diff});
            }
        }
        if (!st.empty() && st.back().first == h) {
            st.back().second += w + 1;
        } else {
            st.push_back({h, w + 1});
        }
    }

    sort(V.begin(), V.end());

    long long ret = init_area - 2 * K;
    long long rem_K = K;

    for (auto& p : V) {
        long long w = p.first;
        long long diff = p.second;
        long long take = min(diff, rem_K / w);
        ret -= 2 * take;
        rem_K -= take * w;
    }

    cout << ret << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc106_e — E - Medals

**Problem ID**: `AtCoder-arc106_e`  
**Contest**: `arc106`  
**Rating / Difficulty**: 2825  
**URL**: https://atcoder.jp/contests/arc106/tasks/arc106_e  
**VJudge Tag**: `[problem:AtCoder-arc106_e]`  
**Category File**: [`../categories/dynamic_programming/employee_schedule_halls_marriage_sos_dp.md`](../categories/dynamic_programming/employee_schedule_halls_marriage_sos_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Sum Over Subsets DP (SOS DP)`  

---

## 1. Problem Statement & Key Idea
N employees (N <= 18) cycle between working A_i days and resting A_i days. Each day, 1 working employee can receive a medal. Find the minimum days D so that every employee receives at least K medals.

## 2. Core Observation & Invariant
This is bipartite matching between N employees (demand K each) and days 1..D (capacity 1). By Hall's Marriage Theorem, a valid matching exists iff for every subset S of employees, the number of days where at least one employee in S works is at least |S| * K. Equivalently, the number of days where the working mask W(d) is a subset of S^c must be at most D - |S| * K. Since D <= 2NK <= 3.6 * 10^6, binary search on D with Fast Walsh-Hadamard / SOS DP on 2^18 masks checks Hall's condition in O(N * 2^N) per step.

## 3. Step-by-Step Algorithm
1. 1. Precompute day_mask[d] for each day d in 1..2NK indicating which employees work on day d.
2. 2. Binary search D in [1, 2NK].
3. 3. For a candidate D, populate frequency array cnt[mask] for d in 1..D.
4. 4. Compute SOS DP over all 2^N masks: sos[mask] = sum_{sub in mask} cnt[sub] in O(N 2^N) time.
5. 5. For every mask T, verify sos[T] <= D - (N - popcount(T)) * K.
6. 6. Return the minimal valid D.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K + log(NK) * N * 2^N)`
- **Space Complexity**: `O(NK + 2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_d = 2 * n * k;
    vector<int> day_mask(max_d + 1, 0);
    for (int i = 0; i < n; ++i) {
        int period = 2 * a[i];
        int work_len = a[i];
        for (int d = 1; d <= max_d; ++d) {
            if ((d - 1) % period < work_len) {
                day_mask[d] |= (1 << i);
            }
        }
    }

    int num_masks = 1 << n;
    vector<int> pop(num_masks, 0);
    for (int mask = 0; mask < num_masks; ++mask) {
        pop[mask] = __builtin_popcount(mask);
    }

    vector<int> sos(num_masks, 0);

    auto check = [&](int D) -> bool {
        fill(sos.begin(), sos.end(), 0);
        for (int d = 1; d <= D; ++d) {
            sos[day_mask[d]]++;
        }

        for (int i = 0; i < n; ++i) {
            int bit = 1 << i;
            for (int mask = 0; mask < num_masks; ++mask) {
                if (mask & bit) {
                    sos[mask] += sos[mask ^ bit];
                }
            }
        }

        for (int mask = 0; mask < num_masks; ++mask) {
            int subset_size = n - pop[mask];
            if (sos[mask] > D - 1LL * subset_size * k) {
                return false;
            }
        }
        return true;
    };

    int low = 1, high = max_d;
    int ans = high;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
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

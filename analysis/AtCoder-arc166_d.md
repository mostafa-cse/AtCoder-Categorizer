# Problem Analysis: AtCoder-arc166_d — D. Interval Counts

**Problem ID**: `AtCoder-arc166_d`  
**Contest**: `arc166`  
**Rating / Difficulty**: 2192  
**URL**: https://atcoder.jp/contests/arc166/tasks/arc166_d  
**VJudge Tag**: `[problem:AtCoder-arc166_d]`  
**Category File**: [`../categories/basics/interval_counts_difference_fifo_matching.md`](../categories/basics/interval_counts_difference_fifo_matching.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given point coverage requirements y_i at coordinates x_i, positive differences y_i - y_{i-1} start intervals at x_{i-1} + 1, and negative differences y_{i-1} - y_i end intervals at x_i - 1. Maximizing min(R_j - L_j) is solved by FIFO queue matching between starts and ends.

## 2. Core Observation & Invariant
For any two intervals with L_1 < L_2 and R_1 < R_2, FIFO pairing (L_1, R_1) and (L_2, R_2) yields min(R_1 - L_1, R_2 - L_2) >= min(R_1 - L_2, R_2 - L_1). Thus FIFO matching dominates all other matchings. Intervals starting at -inf or ending at +inf have infinite length and are ignored.

## 3. Step-by-Step Algorithm
1. Set x_0 = -INF, y_0 = 0, x_{N+1} = INF, y_{N+1} = 0.
2. Maintain a queue of pairs (L, count) of open interval starts.
3. For i from 1 to N + 1:
4.   If y_i > y_{i-1}, push (x_{i-1} + 1, y_i - y_{i-1}) to queue (L = -INF for i = 1).
5.   If y_i < y_{i-1}, pop y_{i-1} - y_i intervals from queue front, setting R = x_i - 1 (R = INF for i = N+1). If both L and R are finite, update min_len = min(min_len, R - L).
6. Output min_len if finite, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> x(N + 2);
    vector<long long> y(N + 2, 0);

    for (int i = 1; i <= N; ++i) {
        cin >> x[i];
    }
    for (int i = 1; i <= N; ++i) {
        cin >> y[i];
    }

    // Queue stores pairs: {L, count}
    // L = -INF means start at -infinity
    deque<pair<long long, long long>> q;
    long long min_len = INF;

    for (int i = 1; i <= N + 1; ++i) {
        if (y[i] > y[i - 1]) {
            long long diff = y[i] - y[i - 1];
            long long L = (i == 1 ? -INF : x[i - 1] + 1);
            q.push_back({L, diff});
        } else if (y[i] < y[i - 1]) {
            long long need = y[i - 1] - y[i];
            long long R = (i == N + 1 ? INF : x[i] - 1);
            while (need > 0) {
                auto& [L, cnt] = q.front();
                long long take = min(cnt, need);
                if (L != -INF && R != INF) {
                    min_len = min(min_len, R - L);
                }
                cnt -= take;
                need -= take;
                if (cnt == 0) {
                    q.pop_front();
                }
            }
        }
    }

    if (min_len == INF) {
        cout << -1 << "\n";
    } else {
        cout << min_len << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc228_f — I. Stamp Game

**Problem ID**: `AtCoder-abc228_f`  
**Contest**: `abc228`  
**Rating / Difficulty**: 2179  
**URL**: https://atcoder.jp/contests/abc228/tasks/abc228_f  
**VJudge Tag**: `[problem:AtCoder-abc228_f]`  
**Category File**: [`../categories/data_structures/monotonic_queue_2d_sliding_window_max.md`](../categories/data_structures/monotonic_queue_2d_sliding_window_max.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Queue 2D`  

---

## 1. Problem Statement & Key Idea
Takahashi selects an h1 x w1 subgrid on an H x W board to paint black, after which Aoki places an h2 x w2 white stamp entirely inside Takahashi subgrid (effectively size min(h1, h2) x min(w1, w2)) to erase black cells. Takahashi maximizes the remaining sum of black cells. This reduces to computing for every Takahashi placement (r, c) the maximum sub-rectangle sum available to Aoki inside that window via 2D sliding window maximum.

## 2. Core Observation & Invariant
Let ah = min(h1, h2) and aw = min(w1, w2). For Takahashi placement at (r, c), Aoki can choose any top-left (r', c') with r <= r' <= r + h1 - ah and c <= c' <= c + w1 - aw. Precomputing all ah x aw sums S[r'][c'] via 2D prefix sums, Aoki choice is the maximum of S in a 2D window of size (h1 - ah + 1) x (w1 - aw + 1). Applying 1D monotonic deque maximum row-by-row followed by 1D monotonic deque column-by-column computes all 2D window maximums in optimal O(HW) time and memory.

## 3. Step-by-Step Algorithm
1. Compute 2D prefix sums pref[r][c] of grid A to answer rectangle sum queries in O(1).
2. Compute S[i][j] = get_sum(i, j, i + ah - 1, j + aw - 1) for all 1 <= i <= H - ah + 1 and 1 <= j <= W - aw + 1, where ah = min(h1, h2) and aw = min(w1, w2).
3. For each row i, compute 1D sliding window maximum of length len_c = w1 - aw + 1 across columns using a monotonic deque: M1[i][j] = max_{k=j}^{j+len_c-1} S[i][k].
4. For each column j, compute 1D sliding window maximum of length len_r = h1 - ah + 1 across rows using a monotonic deque: M2[i][j] = max_{k=i}^{i+len_r-1} M1[k][j].
5. Iterate over all valid Takahashi placements (i, j) with 1 <= i <= H - h1 + 1 and 1 <= j <= W - w1 + 1. Takahashi score is get_sum(i, j, i + h1 - 1, j + w1 - 1) - M2[i][j]. Output the maximum over all (i, j).

## 4. Complexity Analysis
- **Time Complexity**: `O(HW)`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, h1, w1, h2, w2;
    if (!(cin >> H >> W >> h1 >> w1 >> h2 >> w2)) return 0;

    vector<vector<long long>> A(H + 1, vector<long long>(W + 1, 0));
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            cin >> A[i][j];
        }
    }

    vector<vector<long long>> pref(H + 1, vector<long long>(W + 1, 0));
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            pref[i][j] = A[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    auto get_sum = [&](int r1, int c1, int r2, int c2) {
        return pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
    };

    int ah = min(h1, h2);
    int aw = min(w1, w2);

    int max_r = H - ah + 1;
    int max_c = W - aw + 1;
    vector<vector<long long>> S(max_r + 1, vector<long long>(max_c + 1, 0));
    for (int i = 1; i <= max_r; ++i) {
        for (int j = 1; j <= max_c; ++j) {
            S[i][j] = get_sum(i, j, i + ah - 1, j + aw - 1);
        }
    }

    int len_r = h1 - ah + 1;
    int len_c = w1 - aw + 1;

    // Row sliding window max of length len_c
    int res_c = max_c - len_c + 1;
    vector<vector<long long>> M1(max_r + 1, vector<long long>(res_c + 1, 0));
    for (int i = 1; i <= max_r; ++i) {
        deque<int> dq;
        for (int j = 1; j <= max_c; ++j) {
            while (!dq.empty() && dq.front() <= j - len_c) dq.pop_front();
            while (!dq.empty() && S[i][dq.back()] <= S[i][j]) dq.pop_back();
            dq.push_back(j);
            if (j >= len_c) {
                M1[i][j - len_c + 1] = S[i][dq.front()];
            }
        }
    }

    // Col sliding window max of length len_r
    int res_r = max_r - len_r + 1;
    vector<vector<long long>> M2(res_r + 1, vector<long long>(res_c + 1, 0));
    for (int j = 1; j <= res_c; ++j) {
        deque<int> dq;
        for (int i = 1; i <= max_r; ++i) {
            while (!dq.empty() && dq.front() <= i - len_r) dq.pop_front();
            while (!dq.empty() && M1[dq.back()][j] <= M1[i][j]) dq.pop_back();
            dq.push_back(i);
            if (i >= len_r) {
                M2[i - len_r + 1][j] = M1[dq.front()][j];
            }
        }
    }

    long long ans = 0;
    for (int i = 1; i <= H - h1 + 1; ++i) {
        for (int j = 1; j <= W - w1 + 1; ++j) {
            long long takahashi = get_sum(i, j, i + h1 - 1, j + w1 - 1);
            long long aoki = M2[i][j];
            ans = max(ans, takahashi - aoki);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

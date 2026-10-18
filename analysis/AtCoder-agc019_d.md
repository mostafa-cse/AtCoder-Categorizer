# Problem Analysis: AtCoder-agc019_d — D. Shift and Flip

**Problem ID**: `AtCoder-agc019_d`  
**Contest**: `agc019`  
**Rating / Difficulty**: 2601  
**URL**: https://atcoder.jp/contests/agc019/tasks/agc019_d  
**VJudge Tag**: `[problem:AtCoder-agc019_d]`  
**Category File**: [`../categories/basics/shift_and_flip_two_pointers.md`](../categories/basics/shift_and_flip_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
Given two binary strings A and B of length N, we can shift A circularly left or right, and flip any bit of A if the aligned bit of B is 1. Find the minimum total number of shifts and flips to make A equal to B.

## 2. Core Observation & Invariant
Fix the net shift s in [-(N-1), N-1]. The shift path starting at 0 and ending at s visiting an interval [-L, R] takes minimum distance 2L + 2R - |s|. Each mismatch bit i must visit some 1 in B, requiring L >= l_i or R >= r_i where l_i, r_i are the distances to the nearest 1 of B. For a fixed s, grouping these constraints and taking suffix maximums of r_i allows computing the optimal R for each L in O(N) time.

## 3. Step-by-Step Algorithm
1. Precompute distance to nearest 1 of B to left and right for all indices.
2. For each net shift s in [-(N-1), N-1]: identify all mismatch positions i. If l_i > min_L and r_i > min_R, record requirement. Suffix maximum array computes max r_i for each L. Find min(2L + 2R - |s| + flips). Output global minimum over all s.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string A, B;
    if (!(cin >> A >> B)) return 0;

    int n = (int)A.size();
    bool has_one = false;
    for (char c : B) {
        if (c == '1') {
            has_one = true;
            break;
        }
    }

    if (!has_one) {
        if (A == B) cout << 0 << "\n";
        else cout << -1 << "\n";
        return 0;
    }

    vector<int> ones;
    for (int i = 0; i < n; ++i) {
        if (B[i] == '1') ones.push_back(i);
    }

    vector<int> next_right(n), next_left(n);
    for (int i = 0; i < n; ++i) {
        int r_dist = n, l_dist = n;
        for (int o : ones) {
            r_dist = min(r_dist, (o - i + n) % n);
            l_dist = min(l_dist, (i - o + n) % n);
        }
        next_right[i] = r_dist;
        next_left[i] = l_dist;
    }

    int ans = 1e9;

    for (int s = -(n - 1); s < n; ++s) {
        int flips = 0;
        vector<pair<int, int>> pairs;
        for (int i = 0; i < n; ++i) {
            int b_idx = (i + s) % n;
            if (b_idx < 0) b_idx += n;
            if (A[i] != B[b_idx]) {
                flips++;
                pairs.push_back({next_left[i], next_right[i]});
            }
        }

        int min_L = max(0, -s);
        int min_R = max(0, s);

        vector<int> max_r(n + 1, 0);
        for (auto& p : pairs) {
            if (p.first > min_L && p.second > min_R) {
                max_r[p.first - 1] = max(max_r[p.first - 1], p.second);
            }
        }

        for (int l = n - 1; l >= 0; --l) {
            max_r[l] = max(max_r[l], max_r[l + 1]);
        }

        int best_shift = 1e9;
        for (int L = min_L; L < n; ++L) {
            int R = max(min_R, max_r[L]);
            best_shift = min(best_shift, 2 * L + 2 * R - abs(s));
        }

        ans = min(ans, best_shift + flips);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

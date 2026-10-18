# Problem Analysis: AtCoder-abc337_f — F. Usual Color Ball Problems

**Problem ID**: `AtCoder-abc337_f`  
**Contest**: `abc337`  
**Rating / Difficulty**: 2386  
**URL**: https://atcoder.jp/contests/abc337/tasks/abc337_f  
**VJudge Tag**: `[problem:AtCoder-abc337_f]`  
**Category File**: [`../categories/basics/cyclic_box_allocation_two_pointers.md`](../categories/basics/cyclic_box_allocation_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
For all N cyclic rotations of balls into M boxes of capacity K, find total stored balls. A box is allocated when a color reaches 1, K+1, 2K+1, ... balls in the active prefix until M boxes are full, accepting min(total_count[c], b_c * K) balls per color. A two-pointer sliding window maintaining allocated boxes evaluates all shifts in O(N) amortized time.

## 2. Core Observation & Invariant
When balls arrive, an empty box is allocated to color c on its 1st, (K+1)-th, (2K+1)-th ball until M boxes are full. Once b_c boxes are allocated to color c, exactly min(total_count[c], b_c * K) balls of color c are accepted. The set of balls allocating boxes forms a sliding window [L, R) on the doubled array, maintained via two pointers in O(N) amortized time.

## 3. Step-by-Step Algorithm
1. Duplicate C to length 2N to handle cyclic shifts seamlessly.
2. Maintain active counts in_win[c] and allocated boxes b[c] for each color in the current window [L, R).
3. Advance R while total_boxes < M; incrementing b[c] dynamically updates the accepted balls sum min(total_count[c], b[c] * K).
4. Slide L from 0 to N-1: record the answer, remove ball C[L] (reclaiming a box if in_win[c] % K == 0), and expand R forward to reallocate.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    vector<int> C(n);
    vector<int> total_cnt(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> C[i];
        total_cnt[C[i]]++;
    }

    vector<int> A(2 * n);
    for (int i = 0; i < n; ++i) {
        A[i] = A[i + n] = C[i];
    }

    vector<int> b(n + 1, 0);
    vector<int> in_win(n + 1, 0);
    int total_boxes = 0;
    long long ans_balls = 0;

    auto add_color = [&](int c) -> bool {
        bool need_box = (in_win[c] % k == 0);
        if (need_box) {
            if (total_boxes == m) return false;
            total_boxes++;
            long long old_cap = min((long long)total_cnt[c], 1LL * b[c] * k);
            b[c]++;
            long long new_cap = min((long long)total_cnt[c], 1LL * b[c] * k);
            ans_balls += (new_cap - old_cap);
        }
        in_win[c]++;
        return true;
    };

    auto remove_color = [&](int c) {
        in_win[c]--;
        if (in_win[c] % k == 0) {
            total_boxes--;
            long long old_cap = min((long long)total_cnt[c], 1LL * b[c] * k);
            b[c]--;
            long long new_cap = min((long long)total_cnt[c], 1LL * b[c] * k);
            ans_balls += (new_cap - old_cap);
        }
    };

    int R = 0;
    while (R < n) {
        if (!add_color(A[R])) break;
        R++;
    }

    for (int L = 0; L < n; ++L) {
        cout << ans_balls << "\n";
        if (R == L) {
            R++;
        } else {
            remove_color(A[L]);
        }
        while (R < L + n) {
            if (!add_color(A[R])) break;
            R++;
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

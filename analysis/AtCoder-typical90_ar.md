# Problem Analysis: AtCoder-typical90_ar — Shift and Swapping

**Problem ID**: `AtCoder-typical90_ar`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 044)  
**Rating / Difficulty**: 800 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ar  
**VJudge Tag**: `[problem:AtCoder-typical90_ar]`  
**Category File**: [`../categories/basics/circular_shift_offset.md`](../categories/basics/circular_shift_offset.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Array Transformations`  
- **Topic (Skill)**: `Virtual Circular Array Shift via Modulo Pointer Offset`  

---

## 1. Problem Statement & Key Idea
Array of length N, Q queries: (1) swap A_x and A_y; (2) shift array right circularly A = (A_N, A_1, ..., A_{N-1}); (3) print A_x.

**Core Idea**: Moving elements physically on shift takes O(N). Instead, maintain a global shift offset pointer in O(1).

## 2. Core Observation & Invariant
A right shift moves the virtual start position back by 1: shift = (shift - 1 + N) % N. Array index x maps to real index (x + shift) % N in O(1).

## 3. Step-by-Step Algorithm
1. shift = 0.
2. Query 1: swap A[(x + shift) % N] and A[(y + shift) % N].
3. Query 2: shift = (shift - 1 + N) % N.
4. Query 3: print A[(x + shift) % N].

## 4. Complexity Analysis
Time: O(Q), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int shift = 0;

    while (q--) {
        int t, x, y;
        cin >> t >> x >> y;
        --x; --y;
        if (t == 1) {
            int idx1 = (x + shift) % n;
            int idx2 = (y + shift) % n;
            swap(a[idx1], a[idx2]);
        } else if (t == 2) {
            shift = (shift - 1 + n) % n;
        } else {
            int idx = (x + shift) % n;
            cout << a[idx] << "\n";
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Pointer offset virtualization for O(1) circular array shift.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Virtual array rotation using modulo index mapping without moving data.
- **Reusable Pattern**: `Virtual Circular Pointer Offset.`

---
Back to [Virtual Circular Array Shift via Modulo Pointer Offset](../categories/basics/circular_shift_offset.md) | [Categories Directory](../categories/README.md)
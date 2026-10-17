# Problem Analysis: AtCoder-abc038_d — プレゼント

**Problem ID**: `AtCoder-abc038_d`  
**Contest**: `abc038`  
**Rating / Difficulty**: 1804  
**URL**: https://atcoder.jp/contests/abc038/tasks/abc038_d  
**VJudge Tag**: `[problem:AtCoder-abc038_d]`  
**Category File**: [`../categories/dp/2d_partially_ordered_lis_asymmetric_sort.md`](../categories/dp/2d_partially_ordered_lis_asymmetric_sort.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `LIS / Fenwick Tree`  
- **Topic (Skill)**: `2D Partially-Ordered LIS via Asymmetric Sorting (w ascending, h descending)`  

---

## 1. Problem Statement & Key Idea
Given N boxes with width w_i and height h_i. Box i can nest inside box j iff w_i < w_j and h_i < h_j. Find the maximum number of nested boxes.

**Key Insight**: Sort boxes by width w ascending, and by height h DESCENDING for ties. Then the problem reduces to finding the standard 1D strictly increasing Longest Increasing Subsequence on h.

## 2. Core Observation & Invariant
Because h is sorted descending for identical w, two boxes with the same width can never be chosen in the increasing subsequence of h, automatically enforcing w_i < w_j.

## 3. Step-by-Step Algorithm
1. Read N pairs (w_i, h_i).
2. Sort with comparator: if w_a != w_b, w_a < w_b; else h_a > h_b.
3. Run standard Patience Sorting (or Fenwick tree) LIS on heights h.
4. Print length of LIS.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Box {
    int w, h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Box> boxes(n);
    for (int i = 0; i < n; ++i) {
        cin >> boxes[i].w >> boxes[i].h;
    }

    sort(boxes.begin(), boxes.end(), [](const Box& a, const Box& b) {
        if (a.w != b.w) return a.w < b.w;
        return a.h > b.h;
    });

    vector<int> lis;
    for (int i = 0; i < n; ++i) {
        int val = boxes[i].h;
        auto it = lower_bound(lis.begin(), lis.end(), val);
        if (it == lis.end()) {
            lis.push_back(val);
        } else {
            *it = val;
        }
    }

    cout << lis.size() << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reducing 2D strict partial order nesting to 1D LIS via tie-breaking opposite sort order.
- **Reusable Pattern**: `2D Box Nesting LIS: Sort (x ASC, y DESC) then compute 1D LIS on y.`

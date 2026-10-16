# Problem Analysis: AtCoder-arc084_a — Snuke Festival

**Problem ID**: `AtCoder-arc084_a`  
**Contest**: `abc077`  
**Rating / Difficulty**: 1096  
**URL**: https://atcoder.jp/contests/abc077/tasks/arc084_a  
**VJudge Tag**: `[problem:AtCoder-arc084_a]`  
**Category File**: [`../categories/basics/dual_binary_search_triplets.md`](../categories/basics/dual_binary_search_triplets.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Dual Binary Search on Middle Anchor / Triplet Counting`  

---

## 1. Problem Statement & Key Idea
You have three parts of altars: top parts A, middle parts B, bottom parts C (each size N). An altar consists of a < b < c (a in A, b in B, c in C). Count valid altars.

**Key Idea**: Anchor on the middle element b in B. For each b, choices of a in A and c in C are independent.

## 2. Core Observation & Invariant
Sort A and C. For a fixed b, valid a are those with a < b (count is std::lower_bound(A) - A.begin()). Valid c are those with c > b (count is C.end() - std::upper_bound(C)). Total altars for this b is count_A * count_C.

## 3. Step-by-Step Algorithm
1. Sort array A and array C in ascending order.
2. Initialize total = 0.
3. For each b in B: count_a = lower_bound(A.begin(), A.end(), b) - A.begin(); count_c = C.end() - upper_bound(C.begin(), C.end(), b); total += (long long)count_a * count_c.
4. Print total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n), c(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];

    sort(a.begin(), a.end());
    sort(c.begin(), c.end());

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long val_b = b[i];
        long long cnt_a = lower_bound(a.begin(), a.end(), val_b) - a.begin();
        long long cnt_c = c.end() - upper_bound(c.begin(), c.end(), val_b);
        total += cnt_a * cnt_c;
    }

    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting independent combinations by anchoring on the middle variable via binary search.
- **Reusable Pattern**: `Triplet count a < b < c: iterate middle b, multiply binary search counts in A and C.`

# Problem Analysis: AtCoder-arc064_a — Boxes and Candies

**Problem ID**: `AtCoder-arc064_a`  
**Contest**: `abc048`  
**Rating / Difficulty**: 1164  
**URL**: https://atcoder.jp/contests/abc048/tasks/arc064_a  
**VJudge Tag**: `[problem:AtCoder-arc064_a]`  
**Category File**: [`../categories/basics/adjacent_overlap_forward_greedy.md`](../categories/basics/adjacent_overlap_forward_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Adjacent Pair Overlap Forward Greedy Reduction`  

---

## 1. Problem Statement & Key Idea
Given array a_1..a_n. In one operation, eat a candy from box i. Make every adjacent pair sum a_i + a_{i+1} <= x. Minimize candies eaten.

**Key Idea**: Process adjacent pairs from left to right. When a_i + a_{i+1} > x, reduce candies from the right box a_{i+1} as much as possible.

## 2. Core Observation & Invariant
Reducing candies from a_{i+1} fixes the current pair (a_i, a_{i+1}) AND simultaneously helps the next pair (a_{i+1}, a_{i+2})! If a_i itself exceeds x, first reduce a_i to x.

## 3. Step-by-Step Algorithm
1. Initialize eaten = 0.
2. If a[0] > x: eaten += a[0] - x, a[0] = x.
3. For i from 0 to n - 2: sum = a[i] + a[i+1]; if sum > x: excess = sum - x, eaten += excess, a[i+1] -= excess.
4. Output eaten.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long eaten = 0;
    if (a[0] > x) {
        eaten += a[0] - x;
        a[0] = x;
    }

    for (int i = 0; i < n - 1; ++i) {
        long long sum = a[i] + a[i + 1];
        if (sum > x) {
            long long excess = sum - x;
            eaten += excess;
            a[i + 1] -= excess;
        }
    }

    cout << eaten << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy overlap optimization prioritizing future constraint satisfaction.
- **Reusable Pattern**: `Adjacent sum reduction: greedily reduce the right element of the pair.`

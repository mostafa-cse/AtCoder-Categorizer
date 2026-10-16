# Problem Analysis: AtCoder-abc251_d — At Most 3

**Problem ID**: `AtCoder-abc251_d`  
**Contest**: `abc251`  
**Rating / Difficulty**: 1463  
**URL**: https://atcoder.jp/contests/abc251/tasks/abc251_d  
**VJudge Tag**: `[problem:AtCoder-abc251_d]`  
**Category File**: [`../categories/basics/base100_additive_basis.md`](../categories/basics/base100_additive_basis.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Constructive Base-100 Representation for Additive Basis`  

---

## 1. Problem Statement & Key Idea
Given W <= 10^6, construct a set of at most 300 integers such that every integer between 1 and W can be represented as the sum of AT MOST 3 distinct elements from the set.

**Key Insight**: Decompose numbers in base 100. Any number <= 10^6 can be written as a + b * 100 + c * 10000 with 0 <= a, b, c <= 99.

## 2. Core Observation & Invariant
By including {1, 2, ..., 99}, {100, 200, ..., 9900}, and {10000, 20000, ..., 990000}, we use exactly 99 * 3 = 297 numbers <= 300. Every number in [1, 999999] can be uniquely written as a sum of at most 3 numbers (at most one from each set).

## 3. Step-by-Step Algorithm
1. Generate set: {1 * i | 1 <= i <= 99}.
2. Generate set: {100 * i | 1 <= i <= 99}.
3. Generate set: {10000 * i | 1 <= i <= 99}.
4. Total elements = 297.
5. Print 297, followed by all 297 elements.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    if (!(cin >> w)) return 0;

    vector<int> ans;
    for (int i = 1; i <= 99; ++i) ans.push_back(i);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 100);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 10000);

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "\n" : " ");
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Positional base decomposition to construct minimal additive bases.
- **Reusable Pattern**: `Additive 3-Sum Basis: {1..B-1}, {B*(1..B-1)}, {B^2*(1..B-1)} covering B^3 values.`

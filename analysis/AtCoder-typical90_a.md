# Problem Analysis: AtCoder-typical90_a — Yokan Party

**Problem ID**: `AtCoder-typical90_a`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 001)  
**Rating / Difficulty**: 1200 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_a  
**VJudge Tag**: `[problem:AtCoder-typical90_a]`  
**Category File**: [`../categories/basics/binary_search_on_answer.md`](../categories/basics/binary_search_on_answer.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on Answer / Greedy Feasibility`  

---

## 1. Problem Statement & Key Idea
A Yokan of length L has N cut points A_1, A_2, ..., A_N. Choose exactly K cut points to divide it into K+1 pieces such that the length of the shortest piece is maximized.

**Core Idea**: The feasibility condition 'Can we cut into K+1 pieces each of length >= M?' is monotonic in M. Binary search on M in [1, L].

## 2. Core Observation & Invariant
Because all piece lengths are positive, greedy left-to-right interval accumulation is optimal: cut as soon as the current piece length reaches at least M.

## 3. Step-by-Step Algorithm
1. Set low = 1, high = L, ans = 1.
2. In binary search: mid = low + (high - low) / 2.
3. Greedily cut: iterate cut points; if current piece >= mid and remaining suffix >= mid, make cut and count++.
4. If count >= K: low = mid + 1, ans = mid; else high = mid - 1.

## 4. Complexity Analysis
Time: O(N log L), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

bool check(long long m, int k, long long l, const vector<long long>& a) {
    int cnt = 0;
    long long prev = 0;
    for (long long x : a) {
        if (x - prev >= m && l - x >= m) {
            cnt++;
            prev = x;
        }
    }
    return cnt >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    long long l;
    if (!(cin >> n >> l >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long low = 1, high = l, ans = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, k, l, a)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Standard monotonic predicate binary search with greedy interval counting.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: The fundamental 'maximize the minimum' binary search on answer template and greedy feasibility checks.
- **Reusable Pattern**: `Binary search on monotonic answer with greedy verification.`

---
Back to [Binary Search on Answer / Greedy Feasibility](../categories/basics/binary_search_on_answer.md) | [Categories Directory](../categories/README.md)
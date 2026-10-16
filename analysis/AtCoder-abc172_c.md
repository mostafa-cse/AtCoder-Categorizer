# Problem Analysis: AtCoder-abc172_c — Tsundoku

**Problem ID**: `AtCoder-abc172_c`  
**Contest**: `abc172`  
**Rating / Difficulty**: 930  
**URL**: https://atcoder.jp/contests/abc172/tasks/abc172_c  
**VJudge Tag**: `[problem:AtCoder-abc172_c]`  
**Category File**: [`../categories/basics/dual_monotonic_prefix_sum.md`](../categories/basics/dual_monotonic_prefix_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Two Pointers`  
- **Topic (Skill)**: `Dual Monotonic Prefix Sum Optimization`  

---

## 1. Problem Statement & Key Idea
Two desks have N books (times A_1..A_N) and M books (times B_1..B_M). Find the maximum number of books you can read from the tops of desks in total time <= K.

**Key Idea**: If we take i books from desk A, the time spent is prefA[i]. The remaining time for desk B is K - prefA[i].

## 2. Core Observation & Invariant
Because reading times are positive, prefA and prefB are strictly increasing. As i increases, the maximum valid number of books j taken from desk B is monotonically non-increasing. We can maintain j using two pointers in O(N + M).

## 3. Step-by-Step Algorithm
1. Compute prefix sums prefA of size N + 1 and prefB of size M + 1.
2. Start with i = 0 and j = M.
3. Find largest j such that prefA[0] + prefB[j] <= K.
4. Iterate i from 0 to N: if prefA[i] > K, break; while j > 0 and prefA[i] + prefB[j] > K, j--; ans = max(ans, i + j).
5. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    vector<long long> pa(n + 1, 0), pb(m + 1, 0);
    for (int i = 0; i < n; ++i) pa[i + 1] = pa[i] + a[i];
    for (int i = 0; i < m; ++i) pb[i + 1] = pb[i] + b[i];

    int max_books = 0;
    int j = m;

    for (int i = 0; i <= n; ++i) {
        if (pa[i] > k) break;
        while (j >= 0 && pa[i] + pb[j] > k) {
            j--;
        }
        if (j >= 0) {
            max_books = max(max_books, i + j);
        }
    }

    cout << max_books << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two pointers synchronization on opposing monotonic prefix sums.
- **Reusable Pattern**: `Two pointers prefix balance: as i increases, pointer j decreases.`

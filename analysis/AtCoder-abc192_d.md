# Problem Analysis: AtCoder-abc192_d — Base n

**Problem ID**: `AtCoder-abc192_d`  
**Contest**: `abc192`  
**Rating / Difficulty**: 1425  
**URL**: https://atcoder.jp/contests/abc192/tasks/abc192_d  
**VJudge Tag**: `[problem:AtCoder-abc192_d]`  
**Category File**: [`../categories/math/binary_search_base_overflow_guard.md`](../categories/math/binary_search_base_overflow_guard.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `Binary Search on Positional Notation Base with Overflow Guard`  

---

## 1. Problem Statement & Key Idea
Given a number string X and an integer M (1 <= M <= 10^18). Let d be the maximum digit in X. For how many integers n > d is the value of X when interpreted in base n at most M?

**Key Insight**: If |X| == 1, the value does not depend on base n; if int(X) <= M, answer is 1, else 0. If |X| >= 2, the value is strictly monotonically increasing with base n. Binary search for the maximum valid base n with 128-bit integer overflow protection.

## 2. Core Observation & Invariant
Because |X| >= 2, base n can grow up to M + 1. The monotonic property guarantees that binary search in [d + 1, M + 1] finds the exact upper bound base.

## 3. Step-by-Step Algorithm
1. Find maximum digit d in string X.
2. If |X| == 1: value is (X[0] - '0'). Output (value <= M ? 1 : 0).
3. Define evaluate(X, base, M) using __int128:
4.   val = 0; for digit c in X: val = val * base + (c - '0'); if val > M return false. Return true.
5. Binary search on base in range [d + 1, M + 1]:
6.   mid = low + (high - low) / 2.
7.   If evaluate(X, mid, M) is true, valid_base = mid, low = mid + 1.
8.   Else high = mid - 1.
9. Output max(0LL, valid_base - d).

## 4. Complexity Analysis
- **Time Complexity**: `O(|X| * log M)`
- **Space Complexity**: `O(|X|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool evaluate(const string& x, long long base, long long M) {
    __int128 val = 0;
    for (char c : x) {
        val = val * base + (c - '0');
        if (val > M) return false;
    }
    return val <= M;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string x;
    long long m;
    if (!(cin >> x >> m)) return 0;

    int d = 0;
    for (char c : x) {
        d = max(d, c - '0');
    }

    if (x.size() == 1) {
        cout << (d <= m ? 1 : 0) << "\n";
        return 0;
    }

    long long low = d + 1, high = m + 1;
    long long best_base = d;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (evaluate(x, mid, m)) {
            best_base = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << max(0LL, best_base - d) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Positional polynomial evaluation with monotonic binary search and __int128 overflow prevention.
- **Reusable Pattern**: `Base Evaluation Binary Search: evaluate with __int128 clamp to M.`

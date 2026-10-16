# Problem Analysis: AtCoder-abc152_d — Handstand 2

**Problem ID**: `AtCoder-abc152_d`  
**Contest**: `abc152`  
**Rating / Difficulty**: 1045  
**URL**: https://atcoder.jp/contests/abc152/tasks/abc152_d  
**VJudge Tag**: `[problem:AtCoder-abc152_d]`  
**Category File**: [`../categories/math/digit_pair_frequency_matrix.md`](../categories/math/digit_pair_frequency_matrix.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Counting & Matrices`  
- **Topic (Skill)**: `First-Last Digit Pair Frequency Matrix Double Counting`  

---

## 1. Problem Statement & Key Idea
Count pairs of integers (A, B) such that 1 <= A, B <= N and the first digit of A equals the last digit of B, and the last digit of A equals the first digit of B (N <= 2 * 10^5).

**Key Idea**: The condition on (A, B) depends solely on the first and last digits of each number.

## 2. Core Observation & Invariant
Let cnt[f][l] be the count of integers in 1..N whose first digit is f and last digit is l. If a number A has first digit f and last digit l, any valid B must have first digit l and last digit f. Therefore, the number of pairs formed by this class is cnt[f][l] * cnt[l][f]! Total answer is sum_{f=1}^9 sum_{l=1}^9 cnt[f][l] * cnt[l][f].

## 3. Step-by-Step Algorithm
1. Initialize 10 x 10 matrix cnt to 0.
2. For each i from 1 to N: extract first digit f and last digit l = i % 10; if l > 0, cnt[f][l]++.
3. Initialize ans = 0.
4. For f in 1..9, for l in 1..9: ans += cnt[f][l] * cnt[l][f].
5. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> cnt(10, vector<long long>(10, 0));

    for (int i = 1; i <= n; ++i) {
        string s = to_string(i);
        int f = s.front() - '0';
        int l = s.back() - '0';
        cnt[f][l]++;
    }

    long long ans = 0;
    for (int f = 1; f <= 9; ++f) {
        for (int l = 1; l <= 9; ++l) {
            ans += cnt[f][l] * cnt[l][f];
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Independence of paired properties via 2D feature frequency matrix.
- **Reusable Pattern**: `Pair matching on independent attributes: build frequency matrix cnt[A][B], ans = sum cnt[A][B] * cnt[B][A].`

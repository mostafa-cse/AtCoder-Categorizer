# Problem Analysis: AtCoder-abc133_d — Rain Flows into Dams

**Problem ID**: `AtCoder-abc133_d`  
**Contest**: `abc133`  
**Rating / Difficulty**: 938  
**URL**: https://atcoder.jp/contests/abc133/tasks/abc133_d  
**VJudge Tag**: `[problem:AtCoder-abc133_d]`  
**Category File**: [`../categories/math/odd_cycle_alternating_sum.md`](../categories/math/odd_cycle_alternating_sum.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Systems`  
- **Topic (Skill)**: `Odd Cycle Telescoping Alternating Sum`  

---

## 1. Problem Statement & Key Idea
N mountains and N dams in a circle (N is odd). Dam i receives half the rain from mountain i and mountain i+1 (dam N between N and 1). Given dam water amounts A_1..A_N, find rain on each mountain X_1..X_N.

**Key Idea**: The system of equations is X_i + X_{i+1} = 2 * A_i. Because N is odd, taking the alternating sum isolates X_1 directly.

## 2. Core Observation & Invariant
Notice X_1 = sum_{i=1}^N A_i - 2 * (A_2 + A_4 + ... + A_{N-1}). Once X_1 is known, every subsequent variable is determined in O(1) via X_{i+1} = 2 * A_i - X_i.

## 3. Step-by-Step Algorithm
1. Compute total_A = sum_{i=1}^N A_i.
2. Compute even_A = sum of A_i for even indices i = 2, 4, ..., N - 1.
3. Set X_1 = total_A - 2 * even_A.
4. For i = 1 to N - 1: X_{i+1} = 2 * A_i - X_i.
5. Print X_1..X_N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    long long total_a = 0;
    long long even_a = 0;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        total_a += a[i];
        if (i % 2 == 0) {
            even_a += a[i];
        }
    }

    vector<long long> x(n + 1);
    x[1] = total_a - 2 * even_a;

    for (int i = 1; i < n; ++i) {
        x[i + 1] = 2 * a[i] - x[i];
    }

    for (int i = 1; i <= n; ++i) {
        cout << x[i] << (i == n ? '\n' : ' ');
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Inverting cyclic tridiagonal linear systems on odd cycles via alternating sums.
- **Reusable Pattern**: `Odd cyclic sum: X_1 = sum(A) - 2 * sum(even_A).`

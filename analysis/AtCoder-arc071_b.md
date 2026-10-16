# Problem Analysis: AtCoder-arc071_b — ###

**Problem ID**: `AtCoder-arc071_b`  
**Contest**: `abc058`  
**Rating / Difficulty**: 1641  
**URL**: https://atcoder.jp/contests/abc058/tasks/arc071_b  
**VJudge Tag**: `[problem:AtCoder-arc071_b]`  
**Category File**: [`../categories/math/rectilinear_area_1d_decomposition.md`](../categories/math/rectilinear_area_1d_decomposition.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Combinatorics`  
- **Topic (Skill)**: `2D Rectilinear Area Decomposition into 1D Coordinate Gaps`  

---

## 1. Problem Statement & Key Idea
N vertical lines x_1 < ... < x_N and M horizontal lines y_1 < ... < y_M. Find the sum of areas of all possible rectangles formed by pairs of lines, modulo 10^9 + 7.

**Key Insight**: The area of a rectangle formed by (x_i, x_j) and (y_k, y_l) is (x_j - x_i) * (y_l - y_k). The sum over all pairs decomposes into (sum_{i < j} (x_j - x_i)) * (sum_{k < l} (y_l - y_k)).

## 2. Core Observation & Invariant
Each interval gap delta_i = x_{i+1} - x_i is included in exactly i * (N - i) pairs of lines! Thus sum_{i < j} (x_j - x_i) = sum_{i=1}^{N-1} (x_{i+1} - x_i) * i * (N - i) mod MOD. Same applies independently to y.

## 3. Step-by-Step Algorithm
1. Compute sum_X = sum_{i=1}^{N-1} (x[i+1] - x[i]) * i * (N - i) % MOD.
2. Compute sum_Y = sum_{j=1}^{M-1} (y[j+1] - y[j]) * j * (M - j) % MOD.
3. Total sum = (sum_X * sum_Y) % MOD.
4. Print total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> x(n), y(m);
    for (int i = 0; i < n; ++i) cin >> x[i];
    for (int j = 0; j < m; ++j) cin >> y[j];

    long long sum_x = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long delta = (x[i + 1] - x[i]) % MOD;
        long long count = 1LL * (i + 1) * (n - 1 - i) % MOD;
        sum_x = (sum_x + delta * count) % MOD;
    }

    long long sum_y = 0;
    for (int j = 0; j < m - 1; ++j) {
        long long delta = (y[j + 1] - y[j]) % MOD;
        long long count = 1LL * (j + 1) * (m - 1 - j) % MOD;
        sum_y = (sum_y + delta * count) % MOD;
    }

    long long total = (sum_x * sum_y) % MOD;
    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decoupling 2D geometric quantities into independent 1D interval frequency sums.
- **Reusable Pattern**: `Rectilinear Pair Sum: sum (x_j - x_i) = sum (x_{i+1} - x_i) * i * (N - i).`

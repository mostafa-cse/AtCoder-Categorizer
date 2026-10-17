# Problem Analysis: AtCoder-abc204_f — Hanjo 2

**Problem ID**: `AtCoder-abc204_f`  
**Contest**: `abc204`  
**Rating / Difficulty**: 2044  
**URL**: https://atcoder.jp/contests/abc204/tasks/abc204_f  
**VJudge Tag**: `[problem:AtCoder-abc204_f]`  
**Category File**: [`../categories/dynamic_programming/profile_dp_matrix_exponentiation_tiling.md`](../categories/dynamic_programming/profile_dp_matrix_exponentiation_tiling.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Profile DP with Matrix Exponentiation for Domino and Monomino Tiling`  

---

## 1. Problem Statement & Key Idea
Find the number of ways to tile an H x W grid (H <= 6, W <= 10^12) with 1x1 and 1x2 tiles modulo 998244353.

**Key Idea**: Since H <= 6 and W <= 10^12, we use Broken Profile / Column Transition DP with Matrix Exponentiation. A column profile is represented by a bitmask of size 2^H (64 states), where bit r is 1 if a horizontal 1x2 tile protrudes into row r of the current column. Transition matrix T[u][v] counts the number of ways to tile the current column given incoming mask u and leaving outgoing mask v. Using a small recursive DFS for a single column, we build the 64x64 matrix T, and compute T^W * [mask 0] via Matrix Exponentiation in O(64^3 log W).

## 2. Core Observation & Invariant
Small width H <= 6 allows complete transition matrix enumeration over 2^H profile bitmasks accelerated by matrix exponentiation.

## 3. Step-by-Step Algorithm
1. Let states = 1 << H (at most 64).
2. Build transition matrix T of size 64 x 64:
3.   Define dfs(row, in_mask, out_mask):
4.     if row == H: T[in_mask][out_mask]++; return;
5.     if in_mask has bit row set (already covered): dfs(row + 1, in_mask, out_mask);
6.     else:
7.       // 1. Place 1x1 tile
8.       dfs(row + 1, in_mask, out_mask);
9.       // 2. Place horizontal 1x2 tile (protrudes into out_mask)
10.       dfs(row + 1, in_mask, out_mask | (1 << row));
11.       // 3. Place vertical 2x1 tile (covers row and row + 1)
12.       if (row + 1 < H && !(in_mask & (1 << (row + 1)))):
13.         dfs(row + 2, in_mask, out_mask);
14. Compute T^W using binary matrix exponentiation.
15. Answer is (T^W)[0][0] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O((2^H)^3 log W)`
- **Space Complexity**: `O((2^H)^2)`

## 5. Core Algorithmic Skill & Learning Takeaway
Profile DP state compression and binary matrix exponentiation.

**Reusable Pattern**: Broken Profile Matrix Exponentiation: Enumerate intra-column tiling configurations to form 2^H x 2^H transition matrix T, then compute T^W.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power(Matrix A, long long exp) {
    int n = A.size();
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (exp > 0) {
        if (exp % 2 == 1) res = multiply(res, A);
        A = multiply(A, A);
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h;
    long long w;
    if (!(cin >> h >> w)) return 0;

    int num_states = (1 << h);
    Matrix T(num_states, vector<long long>(num_states, 0));

    auto dfs = [&](auto& self, int row, int in_mask, int out_mask, int orig_in) -> void {
        if (row == h) {
            T[orig_in][out_mask]++;
            return;
        }

        if (in_mask & (1 << row)) {
            // Already covered by incoming horizontal tile
            self(self, row + 1, in_mask, out_mask, orig_in);
        } else {
            // Option 1: 1x1 tile
            self(self, row + 1, in_mask, out_mask, orig_in);
            // Option 2: 1x2 horizontal tile (protrudes to next col)
            self(self, row + 1, in_mask, out_mask | (1 << row), orig_in);
            // Option 3: 2x1 vertical tile
            if (row + 1 < h && !(in_mask & (1 << (row + 1)))) {
                self(self, row + 2, in_mask, out_mask, orig_in);
            }
        }
    };

    for (int mask = 0; mask < num_states; ++mask) {
        dfs(dfs, 0, mask, 0, mask);
    }

    Matrix Tw = power(T, w);
    cout << Tw[0][0] << "\n";

    return 0;
}
```

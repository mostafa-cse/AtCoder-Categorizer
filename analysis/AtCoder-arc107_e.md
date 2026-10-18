# Problem Analysis: AtCoder-arc107_e — E. Mex Mat

**Problem ID**: `AtCoder-arc107_e`  
**Contest**: `arc107`  
**Rating / Difficulty**: 2604  
**URL**: https://atcoder.jp/contests/arc107/tasks/arc107_e  
**VJudge Tag**: `[problem:AtCoder-arc107_e]`  
**Category File**: [`../categories/miscellaneous/mex_mat_diagonal_periodicity.md`](../categories/miscellaneous/mex_mat_diagonal_periodicity.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Invariants and Monovariants`  

---

## 1. Problem Statement & Key Idea
An N x N matrix has entries in {0, 1, 2}. The first row and column are given. Remaining entries satisfy a_{i,j} = mex(a_{i-1,j}, a_{i,j-1}). Count the total occurrences of 0, 1, and 2 in the entire matrix for N <= 5 * 10^5.

## 2. Core Observation & Invariant
For all i, j >= 4 (1-indexed), the values along each diagonal are invariant: a_{i,j} = a_{i-1,j-1}. Thus the matrix values stabilize into constant diagonals after the 4th row and 4th column.

## 3. Step-by-Step Algorithm
1. Explicitly compute the first 4 rows and 4 columns in O(N) time.
2. Count values in the first 3 rows and first 3 columns directly.
3. For each diagonal starting at (4, c) for c in 4 ... N, add (N - c + 1) * 1 to the count of value a_{4, c}.
4. For each diagonal starting at (r, 4) for r in 5 ... N, add (N - r + 1) * 1 to the count of value a_{r, 4}. Output counts.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int mex_tbl[3][3] = {
    {1, 2, 1},
    {2, 0, 0},
    {1, 0, 0}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> row1(N);
    for (int j = 0; j < N; ++j) {
        cin >> row1[j];
    }

    vector<int> col1(N);
    col1[0] = row1[0];
    for (int i = 1; i < N; ++i) {
        cin >> col1[i];
    }

    long long cnt[3] = {0, 0, 0};

    if (N <= 4) {
        vector<vector<int>> A(N, vector<int>(N, 0));
        for (int j = 0; j < N; ++j) A[0][j] = row1[j];
        for (int i = 1; i < N; ++i) A[i][0] = col1[i];

        for (int i = 1; i < N; ++i) {
            for (int j = 1; j < N; ++j) {
                A[i][j] = mex_tbl[A[i - 1][j]][A[i][j - 1]];
            }
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cnt[A[i][j]]++;
            }
        }
        cout << cnt[0] << " " << cnt[1] << " " << cnt[2] << "\n";
        return 0;
    }

    // N > 4
    vector<vector<int>> A(4, vector<int>(N, 0));
    for (int j = 0; j < N; ++j) A[0][j] = row1[j];
    for (int i = 1; i < 4; ++i) A[i][0] = col1[i];

    for (int i = 1; i < 4; ++i) {
        for (int j = 1; j < N; ++j) {
            A[i][j] = mex_tbl[A[i - 1][j]][A[i][j - 1]];
        }
    }

    vector<vector<int>> C(N, vector<int>(4, 0));
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            C[i][j] = A[i][j];
        }
    }
    for (int i = 4; i < N; ++i) {
        C[i][0] = col1[i];
        for (int j = 1; j < 4; ++j) {
            C[i][j] = mex_tbl[C[i - 1][j]][C[i][j - 1]];
        }
    }

    // Count top 3 rows: A[0], A[1], A[2]
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < N; ++j) {
            cnt[A[i][j]]++;
        }
    }

    // Count first 3 columns for i >= 3: C[i][0], C[i][1], C[i][2]
    for (int i = 3; i < N; ++i) {
        for (int j = 0; j < 3; ++j) {
            cnt[C[i][j]]++;
        }
    }

    // Diagonals starting at row 3 (c in 3 ... N-1)
    for (int c = 3; c < N; ++c) {
        int val = A[3][c];
        int len = N - c;
        cnt[val] += len;
    }

    // Diagonals starting at col 3 (r in 4 ... N-1)
    for (int r = 4; r < N; ++r) {
        int val = C[r][3];
        int len = N - r;
        cnt[val] += len;
    }

    cout << cnt[0] << " " << cnt[1] << " " << cnt[2] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

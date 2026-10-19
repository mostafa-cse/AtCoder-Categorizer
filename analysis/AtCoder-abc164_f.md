# Problem Analysis: AtCoder-abc164_f — I hate Matrix Construction

**Problem ID**: `AtCoder-abc164_f`  
**Contest**: `abc164`  
**Rating / Difficulty**: 2683  
**URL**: https://atcoder.jp/contests/abc164/tasks/abc164_f  
**VJudge Tag**: `[problem:AtCoder-abc164_f]`  
**Category File**: [`../categories/graph_theory/matrix_bitwise_and_or_2sat.md`](../categories/graph_theory/matrix_bitwise_and_or_2sat.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Satisfiability`  
- **Topic (Skill)**: `2 SAT`  

---

## 1. Problem Statement & Key Idea
Construct an N x N matrix A where row i has bitwise AND/OR equal to U_i and column j has bitwise AND/OR equal to V_j. Because bitwise operations are completely decoupled across bit positions, we solve the problem independently for each bit b in [0, 63] as a binary 2-SAT / constraint satisfaction problem.

## 2. Core Observation & Invariant
For each bit b in [0, 63], rows and columns impose conditions: (a) all 0, (b) contains 0, (c) all 1, (d) contains 1. Forced rows and columns determine cell values. Conflicts between forced rows and forced columns determine unsatisfiability. Remaining unforced cells are filled to satisfy existence conditions, and final verification validates the 64-bit matrix.

## 3. Step-by-Step Algorithm
1. 1. For each bit k = 0..63, extract target bits u_i and v_j.
2. 2. Solve the single-bit 0/1 matrix problem using deterministic constraint propagation.
3. 3. Combine the 64 binary matrices into a single 64-bit unsigned integer matrix A.
4. 4. Verify matrix A against all row and column AND/OR requirements. If valid, print A; otherwise output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(64 * N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

vector<vector<uint64_t>> solve_bit(int N, const vector<uint64_t>& S, const vector<uint64_t>& T, const vector<uint64_t>& U, const vector<uint64_t>& V) {
    vector<vector<uint64_t>> A(N, vector<uint64_t>(N, 0));
    if (N == 1) {
        A[0][0] = U[0];
        return A;
    }
    vector<bool> all_one_row(N, false), all_zero_row(N, false);
    bool r0 = false, r1 = false;
    for (int i = 0; i < N; i++) {
        if (S[i] == 0 && U[i] == 1) { all_one_row[i] = true; r1 = true; }
        if (S[i] == 1 && U[i] == 0) { all_zero_row[i] = true; r0 = true; }
    }
    vector<bool> all_one_col(N, false), all_zero_col(N, false);
    bool c0 = false, c1 = false;
    for (int j = 0; j < N; j++) {
        if (T[j] == 0 && V[j] == 1) { all_one_col[j] = true; c1 = true; }
        if (T[j] == 1 && V[j] == 0) { all_zero_col[j] = true; c0 = true; }
    }

    if ((c0 || c1) && !(r0 || r1)) {
        vector<vector<uint64_t>> res = solve_bit(N, T, S, V, U);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                A[i][j] = res[j][i];
        return A;
    }

    if (!r0 && !r1) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if ((i + j) % 2 == 1) A[i][j] = 1;
            }
        }
        return A;
    }

    if (r0 && r1) {
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                A[i][j] = U[i];
        return A;
    }

    if (r0) {
        if (c1) return A;
        if (c0) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    A[i][j] = (all_zero_row[i] || all_zero_col[j]) ? 0 : 1;
                }
            }
            return A;
        }
        bool any_u1 = false;
        for (int i = 0; i < N; i++) if (U[i] == 1) any_u1 = true;
        if (any_u1) {
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    A[i][j] = U[i];
            return A;
        }
        bool any_v0 = false;
        for (int j = 0; j < N; j++) if (V[j] == 0) any_v0 = true;
        if (any_v0) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    A[i][j] = all_zero_row[i] ? 0 : V[j];
                }
            }
            return A;
        }
        int cnt_zero_row = 0;
        vector<int> not_zero_rows;
        for (int i = 0; i < N; i++) {
            if (all_zero_row[i]) cnt_zero_row++;
            else not_zero_rows.push_back(i);
        }
        if (N - 1 <= cnt_zero_row) return A;
        A[not_zero_rows.front()][0] = 1;
        for (int j = 1; j < N; j++) A[not_zero_rows.back()][j] = 1;
        return A;
    }

    if (r1) {
        if (c0) return A;
        if (c1) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    A[i][j] = (all_one_row[i] || all_one_col[j]) ? 1 : 0;
                }
            }
            return A;
        }
        bool any_u0 = false;
        for (int i = 0; i < N; i++) if (U[i] == 0) any_u0 = true;
        if (any_u0) {
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    A[i][j] = U[i];
            return A;
        }
        bool any_v1 = false;
        for (int j = 0; j < N; j++) if (V[j] == 1) any_v1 = true;
        if (any_v1) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    A[i][j] = all_one_row[i] ? 1 : V[j];
                }
            }
            return A;
        }
        int cnt_one_row = 0;
        vector<int> not_one_rows;
        for (int i = 0; i < N; i++) {
            if (all_one_row[i]) cnt_one_row++;
            else not_one_rows.push_back(i);
        }
        if (N - 1 <= cnt_one_row) return A;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                A[i][j] = 1;
        A[not_one_rows.front()][0] = 0;
        for (int j = 1; j < N; j++) A[not_one_rows.back()][j] = 0;
        return A;
    }
    return A;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<uint64_t> S(N), T(N), U(N), V(N);
    for (int i = 0; i < N; i++) cin >> S[i];
    for (int i = 0; i < N; i++) cin >> T[i];
    for (int i = 0; i < N; i++) cin >> U[i];
    for (int i = 0; i < N; i++) cin >> V[i];

    vector<vector<uint64_t>> A(N, vector<uint64_t>(N, 0));
    vector<uint64_t> cur_U(N), cur_V(N);

    for (int k = 0; k < 64; k++) {
        for (int i = 0; i < N; i++) cur_U[i] = (U[i] >> k) & 1ULL;
        for (int j = 0; j < N; j++) cur_V[j] = (V[j] >> k) & 1ULL;

        vector<vector<uint64_t>> bit_mat = solve_bit(N, S, T, cur_U, cur_V);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] ^= (bit_mat[i][j] << k);
            }
        }
    }

    // Verify matrix A against S, T, U, V
    bool ok = true;
    for (int i = 0; i < N; i++) {
        uint64_t r_and = ~0ULL, r_or = 0ULL;
        for (int j = 0; j < N; j++) {
            r_and &= A[i][j];
            r_or |= A[i][j];
        }
        if (S[i] == 0 && r_and != U[i]) ok = false;
        if (S[i] == 1 && r_or != U[i]) ok = false;
    }
    for (int j = 0; j < N; j++) {
        uint64_t c_and = ~0ULL, c_or = 0ULL;
        for (int i = 0; i < N; i++) {
            c_and &= A[i][j];
            c_or |= A[i][j];
        }
        if (T[j] == 0 && c_and != V[j]) ok = false;
        if (T[j] == 1 && c_or != V[j]) ok = false;
    }

    if (!ok) {
        cout << -1 << "\n";
    } else {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << A[i][j] << (j + 1 == N ? "" : " ");
            }
            cout << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc347_f — I. Non-overlapping Squares

**Problem ID**: `AtCoder-abc347_f`  
**Contest**: `abc347`  
**Rating / Difficulty**: 2179  
**URL**: https://atcoder.jp/contests/abc347/tasks/abc347_f  
**VJudge Tag**: `[problem:AtCoder-abc347_f]`  
**Category File**: [`../categories/basics/2d_prefix_sum_geometric_cut_decomposition.md`](../categories/basics/2d_prefix_sum_geometric_cut_decomposition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Select three pairwise disjoint M x M squares in an N x N grid to maximize their total element sum. By geometric separating lines, any three non-overlapping squares can be separated by either two parallel cuts (3 horizontal or 3 vertical slabs) or one primary cut and one secondary perpendicular cut (T-splits in 4 orientations: left, right, top, bottom).

## 2. Core Observation & Invariant
Computing 2D prefix sums allows evaluating the sum of any M x M square S[i][j] in O(1). Precomputing the 4 corner 2D prefix/suffix maximums (TL, TR, BL, BR) and 1D horizontal/vertical slab maximums enables evaluating all 6 separation topologies in O(N^2) total time.

## 3. Step-by-Step Algorithm
1. Compute 2D prefix sums of grid A to answer square sums S[i][j] of size M x M in O(1).
2. Precompute 4 corner 2D prefix/suffix maximums: TL[r][c] (top-left), TR[r][c] (top-right), BL[r][c] (bottom-left), BR[r][c] (bottom-right).
3. Precompute 1D row prefix/suffix maximums (PrefRow, SuffRow) and 1D column prefix/suffix maximums (PrefCol, SuffCol).
4. Evaluate 3 horizontal slabs: fix middle row i and combine PrefRow[i - M] + Row[i] + SuffRow[i + M].
5. Evaluate 3 vertical slabs: fix middle col j and combine PrefCol[j - M] + Col[j] + SuffCol[j + M].
6. Evaluate 4 T-shape topologies: for each vertical cut c and horizontal cut r, evaluate (TL + BL + SuffCol) and (PrefCol + TR + BR); for each horizontal cut r and vertical cut c, evaluate (TL + TR + SuffRow) and (PrefRow + BL + BR).
7. Output the global maximum across all 6 topologies.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<long long>> A(N + 1, vector<long long>(N + 1, 0));
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            cin >> A[i][j];
        }
    }

    vector<vector<long long>> pref(N + 1, vector<long long>(N + 1, 0));
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            pref[i][j] = A[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    auto get_sum = [&](int r1, int c1, int r2, int c2) {
        return pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
    };

    int L = N - M + 1;
    vector<vector<long long>> S(L + 2, vector<long long>(L + 2, 0));
    for (int i = 1; i <= L; ++i) {
        for (int j = 1; j <= L; ++j) {
            S[i][j] = get_sum(i, j, i + M - 1, j + M - 1);
        }
    }

    // 4 Corner 2D Prefix/Suffix Extremums:
    // TL[r][c]: max S[i][j] with i <= r, j <= c
    vector<vector<long long>> TL(L + 2, vector<long long>(L + 2, 0));
    for (int i = 1; i <= L; ++i) {
        for (int j = 1; j <= L; ++j) {
            TL[i][j] = max({S[i][j], TL[i - 1][j], TL[i][j - 1]});
        }
    }

    // TR[r][c]: max S[i][j] with i <= r, j >= c
    vector<vector<long long>> TR(L + 2, vector<long long>(L + 2, 0));
    for (int i = 1; i <= L; ++i) {
        for (int j = L; j >= 1; --j) {
            TR[i][j] = max({S[i][j], TR[i - 1][j], TR[i][j + 1]});
        }
    }

    // BL[r][c]: max S[i][j] with i >= r, j <= c
    vector<vector<long long>> BL(L + 2, vector<long long>(L + 2, 0));
    for (int i = L; i >= 1; --i) {
        for (int j = 1; j <= L; ++j) {
            BL[i][j] = max({S[i][j], BL[i + 1][j], BL[i][j - 1]});
        }
    }

    // BR[r][c]: max S[i][j] with i >= r, j >= c
    vector<vector<long long>> BR(L + 2, vector<long long>(L + 2, 0));
    for (int i = L; i >= 1; --i) {
        for (int j = L; j >= 1; --j) {
            BR[i][j] = max({S[i][j], BR[i + 1][j], BR[i][j + 1]});
        }
    }

    // Row maxes: Row[i] = max_{j} S[i][j]
    vector<long long> Row(L + 2, 0), PrefRow(L + 2, 0), SuffRow(L + 2, 0);
    for (int i = 1; i <= L; ++i) {
        for (int j = 1; j <= L; ++j) Row[i] = max(Row[i], S[i][j]);
    }
    for (int i = 1; i <= L; ++i) PrefRow[i] = max(PrefRow[i - 1], Row[i]);
    for (int i = L; i >= 1; --i) SuffRow[i] = max(SuffRow[i + 1], Row[i]);

    // Col maxes: Col[j] = max_{i} S[i][j]
    vector<long long> Col(L + 2, 0), PrefCol(L + 2, 0), SuffCol(L + 2, 0);
    for (int j = 1; j <= L; ++j) {
        for (int i = 1; i <= L; ++i) Col[j] = max(Col[j], S[i][j]);
    }
    for (int j = 1; j <= L; ++j) PrefCol[j] = max(PrefCol[j - 1], Col[j]);
    for (int j = L; j >= 1; --j) SuffCol[j] = max(SuffCol[j + 1], Col[j]);

    long long ans = 0;

    // 1. Three horizontal stripes:
    // Middle square at row i: i in [M+1, L - M]
    for (int i = M + 1; i <= L - M; ++i) {
        ans = max(ans, PrefRow[i - M] + Row[i] + SuffRow[i + M]);
    }

    // 2. Three vertical stripes:
    // Middle square at col j: j in [M+1, L - M]
    for (int j = M + 1; j <= L - M; ++j) {
        ans = max(ans, PrefCol[j - M] + Col[j] + SuffCol[j + M]);
    }

    // Note: Two squares on one side of a cut at coordinate k:
    // In terms of S indices, if cut is between row r and r+1 (1-based on grid):
    // Top squares must have row <= r - M + 1
    // Bottom squares must have row >= r + 1.
    // So let cut row be r in [M, N - M]:
    // top squares are at row <= r - M + 1
    // bottom squares are at row >= r + 1.
    // Let cut col be c in [M, N - M]:
    // left squares are at col <= c - M + 1
    // right squares are at col >= c + 1.

    // 3. Vertical cut at col c, Horizontal cut on Left at row r:
    // Left: TL[r - M + 1][c - M + 1] + BL[r + 1][c - M + 1]
    // Right: SuffCol[c + 1]
    for (int c = M; c <= N - M; ++c) {
        int sc_left = c - M + 1;
        int sc_right = c + 1;
        long long right_val = SuffCol[sc_right];
        for (int r = M; r <= N - M; ++r) {
            int sr_top = r - M + 1;
            int sr_bot = r + 1;
            ans = max(ans, TL[sr_top][sc_left] + BL[sr_bot][sc_left] + right_val);
        }
    }

    // 4. Vertical cut at col c, Horizontal cut on Right at row r:
    // Left: PrefCol[c - M + 1]
    // Right: TR[r - M + 1][c + 1] + BR[r + 1][c + 1]
    for (int c = M; c <= N - M; ++c) {
        int sc_left = c - M + 1;
        int sc_right = c + 1;
        long long left_val = PrefCol[sc_left];
        for (int r = M; r <= N - M; ++r) {
            int sr_top = r - M + 1;
            int sr_bot = r + 1;
            ans = max(ans, left_val + TR[sr_top][sc_right] + BR[sr_bot][sc_right]);
        }
    }

    // 5. Horizontal cut at row r, Vertical cut on Top at col c:
    // Top: TL[r - M + 1][c - M + 1] + TR[r - M + 1][c + 1]
    // Bottom: SuffRow[r + 1]
    for (int r = M; r <= N - M; ++r) {
        int sr_top = r - M + 1;
        int sr_bot = r + 1;
        long long bot_val = SuffRow[sr_bot];
        for (int c = M; c <= N - M; ++c) {
            int sc_left = c - M + 1;
            int sc_right = c + 1;
            ans = max(ans, TL[sr_top][sc_left] + TR[sr_top][sc_right] + bot_val);
        }
    }

    // 6. Horizontal cut at row r, Vertical cut on Bottom at col c:
    // Top: PrefRow[r - M + 1]
    // Bottom: BL[r + 1][c - M + 1] + BR[r + 1][c + 1]
    for (int r = M; r <= N - M; ++r) {
        int sr_top = r - M + 1;
        int sr_bot = r + 1;
        long long top_val = PrefRow[sr_top];
        for (int c = M; c <= N - M; ++c) {
            int sc_left = c - M + 1;
            int sc_right = c + 1;
            ans = max(ans, top_val + BL[sr_bot][sc_left] + BR[sr_bot][sc_right]);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

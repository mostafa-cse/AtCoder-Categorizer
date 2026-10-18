# Problem Analysis: AtCoder-arc158_e — E - All-Pair Shortest Paths

**Problem ID**: `AtCoder-arc158_e`  
**Contest**: `arc158`  
**Rating / Difficulty**: 2641  
**URL**: https://atcoder.jp/contests/arc158/tasks/arc158_e  
**VJudge Tag**: `[problem:AtCoder-arc158_e]`  
**Category File**: [`../categories/basics/grid_all_pairs_shortest_paths_dnc.md`](../categories/basics/grid_all_pairs_shortest_paths_dnc.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Divide and Conquer`  
- **Topic (Skill)**: `Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
In a 2 x N grid with positive vertex weights, find the sum of shortest path weights over all pairs of squares (X, Y) modulo 998244353.

## 2. Core Observation & Invariant
Shortest paths never leave the bounding column range [c_1, c_2]. Divide and conquer on columns [L, R] with midpoint M: any path from X in [L, M] to Y in [M+1, R] crosses from M to M+1 exactly once, using either top edge (1, M)-(1, M+1) or bottom edge (2, M)-(2, M+1). The shortest distance is min(d_top(X) + d_top(Y), d_bot(X) + d_bot(Y)). The condition d_top(X) - d_bot(X) <= d_bot(Y) - d_top(Y) separates which boundary edge is optimal, solved by binary search on sorted right differences.

## 3. Step-by-Step Algorithm
1. Recursive function DNC(L, R):
2. If L == R, add internal column pairs.
3. Set M = (L + R) / 2, recurse on [L, M] and [M+1, R].
4. Compute shortest distances from (0, M) and (1, M) moving left to L.
5. Compute shortest distances from (0, M+1) and (1, M+1) moving right to R.
6. Sort right nodes by d_bot(Y) - d_top(Y) and precompute prefix sums.
7. For each left node, binary search the threshold and add cross-distances.
8. Return total sum modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int N;
vector<long long> grid[2];
long long total_ans = 0;

struct RightNode {
    long long c_val; // d_top
    long long d_val; // d_bot
    long long diff;  // d_bot - d_top
};

void dnc(int L, int R) {
    if (L == R) {
        long long d = grid[0][L] + grid[1][L];
        total_ans = (total_ans + 2 * (d % MOD)) % MOD;
        return;
    }
    int M = (L + R) / 2;
    dnc(L, M);
    dnc(M + 1, R);

    // Compute d_top_L and d_bot_L from M down to L
    // d_top_L: source is (0, M)
    vector<long long> topL_0(M - L + 1), topL_1(M - L + 1);
    topL_0[M - L] = grid[0][M];
    topL_1[M - L] = grid[0][M] + grid[1][M];
    for (int c = M - 1; c >= L; --c) {
        int idx = c - L;
        long long p0 = topL_0[idx + 1], p1 = topL_1[idx + 1];
        topL_0[idx] = min(p0 + grid[0][c], p1 + grid[1][c] + grid[0][c]);
        topL_1[idx] = min(p1 + grid[1][c], p0 + grid[0][c] + grid[1][c]);
    }

    // d_bot_L: source is (1, M)
    vector<long long> botL_0(M - L + 1), botL_1(M - L + 1);
    botL_1[M - L] = grid[1][M];
    botL_0[M - L] = grid[1][M] + grid[0][M];
    for (int c = M - 1; c >= L; --c) {
        int idx = c - L;
        long long p0 = botL_0[idx + 1], p1 = botL_1[idx + 1];
        botL_0[idx] = min(p0 + grid[0][c], p1 + grid[1][c] + grid[0][c]);
        botL_1[idx] = min(p1 + grid[1][c], p0 + grid[0][c] + grid[1][c]);
    }

    // Compute d_top_R and d_bot_R from M + 1 up to R
    // d_top_R: source is (0, M + 1)
    vector<long long> topR_0(R - M), topR_1(R - M);
    topR_0[0] = grid[0][M + 1];
    topR_1[0] = grid[0][M + 1] + grid[1][M + 1];
    for (int c = M + 2; c <= R; ++c) {
        int idx = c - (M + 1);
        long long p0 = topR_0[idx - 1], p1 = topR_1[idx - 1];
        topR_0[idx] = min(p0 + grid[0][c], p1 + grid[1][c] + grid[0][c]);
        topR_1[idx] = min(p1 + grid[1][c], p0 + grid[0][c] + grid[1][c]);
    }

    // d_bot_R: source is (1, M + 1)
    vector<long long> botR_0(R - M), botR_1(R - M);
    botR_1[0] = grid[1][M + 1];
    botR_0[0] = grid[1][M + 1] + grid[0][M + 1];
    for (int c = M + 2; c <= R; ++c) {
        int idx = c - (M + 1);
        long long p0 = botR_0[idx - 1], p1 = botR_1[idx - 1];
        botR_0[idx] = min(p0 + grid[0][c], p1 + grid[1][c] + grid[0][c]);
        botR_1[idx] = min(p1 + grid[1][c], p0 + grid[0][c] + grid[1][c]);
    }

    // Build right elements
    int right_sz = 2 * (R - M);
    vector<RightNode> right_nodes;
    right_nodes.reserve(right_sz);
    for (int c = M + 1; c <= R; ++c) {
        int idx = c - (M + 1);
        // (0, c)
        right_nodes.push_back({topR_0[idx], botR_0[idx], botR_0[idx] - topR_0[idx]});
        // (1, c)
        right_nodes.push_back({topR_1[idx], botR_1[idx], botR_1[idx] - topR_1[idx]});
    }

    sort(right_nodes.begin(), right_nodes.end(), [](const RightNode& a, const RightNode& b) {
        return a.diff < b.diff;
    });

    vector<long long> pref_c(right_sz + 1, 0), pref_d(right_sz + 1, 0);
    for (int i = 0; i < right_sz; ++i) {
        pref_c[i + 1] = (pref_c[i] + (right_nodes[i].c_val % MOD)) % MOD;
        pref_d[i + 1] = (pref_d[i] + (right_nodes[i].d_val % MOD)) % MOD;
    }

    // For each left node
    long long cross_sum = 0;
    for (int c = L; c <= M; ++c) {
        int idx = c - L;
        for (int r = 0; r < 2; ++r) {
            long long a = (r == 0 ? topL_0[idx] : topL_1[idx]);
            long long b = (r == 0 ? botL_0[idx] : botL_1[idx]);
            long long k = a - b;

            // find first right_node with diff >= k
            int low = 0, high = right_sz - 1, p = right_sz;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (right_nodes[mid].diff >= k) {
                    p = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }

            // For i in [0, p): diff < k, so min is b + d
            if (p > 0) {
                long long part_b = (b % MOD) * p % MOD;
                long long part_d = pref_d[p];
                cross_sum = (cross_sum + part_b + part_d) % MOD;
            }
            // For i in [p, right_sz): diff >= k, so min is a + c
            if (p < right_sz) {
                int cnt = right_sz - p;
                long long part_a = (a % MOD) * cnt % MOD;
                long long part_c = (pref_c[right_sz] - pref_c[p] + MOD) % MOD;
                cross_sum = (cross_sum + part_a + part_c) % MOD;
            }
        }
    }

    total_ans = (total_ans + 2 * cross_sum) % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    grid[0].resize(N);
    grid[1].resize(N);

    for (int i = 0; i < N; ++i) cin >> grid[0][i];
    for (int i = 0; i < N; ++i) cin >> grid[1][i];

    // Single vertex paths
    for (int r = 0; r < 2; ++r) {
        for (int c = 0; c < N; ++c) {
            total_ans = (total_ans + grid[r][c] % MOD) % MOD;
        }
    }

    dnc(0, N - 1);

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

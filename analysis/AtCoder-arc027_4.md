# Problem Analysis: AtCoder-arc027_4 — D - ぴょんぴょんトレーニング

**Problem ID**: `AtCoder-arc027_4`  
**Contest**: `arc027`  
**Rating / Difficulty**: 2474  
**URL**: https://atcoder.jp/contests/arc027/tasks/arc027_4  
**VJudge Tag**: `[problem:AtCoder-arc027_4]`  
**Category File**: [`../categories/data_structures_ds/pyon_training_sqrt_matrix_decomposition.md`](../categories/data_structures_ds/pyon_training_sqrt_matrix_decomposition.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Basic SQRT Decomposition`  

---

## 1. Problem Statement & Key Idea
Count the number of jump paths from stone $s$ to $t$ modulo 1000000007 across $D \le 5000$ queries on stones with jump limit $h_i \le 10$.

## 2. Core Observation & Invariant
Because $h_i \le 10$, each stone $x$ can only be reached from stones in $[x - 10, x - 1]$. The transitions form a linear recurrence of order 10 represented by a $10 \times 10$ transition matrix. With $N \le 300,000$, we partition stones into blocks of size $B = 500$. For each block, we precompute the cumulative $10 \times 10$ transition matrix in $O(100 B)$ time. For each query $(s, t)$, multiplying a $1 \times 10$ state vector across full blocks takes only $10 \times 10 = 100$ operations per block, and partial boundaries take scalar DP, answering each query in $O(B + (N/B) \times 100)$ time.

## 3. Step-by-Step Algorithm
1. 1. Divide $1 \dots N$ into blocks of size $B = 500$.
2. 2. For each block, simulate transitions of basis vectors $e_0, \dots, e_9$ across the block to obtain the $10 \times 10$ block transition matrix.
3. 3. For each query $(s, t)$, if $s$ and $t$ lie in the same block, execute standard scalar DP.
4. 4. Otherwise, compute scalar DP up to the end of block of $s$ to form a 10-element vector, multiply across intermediate full blocks, and finish with scalar DP in the block of $t$.
5. 5. Print $dp[t]$ modulo 1000000007.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \cdot 100 + D \cdot (B + \frac{N}{B} \cdot 100))`
- **Space Complexity**: `O(N + \frac{N}{B} \cdot 100)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int N;
vector<int> H;
int D;

// Matrix 10x10
struct Matrix {
    int mat[10][10];
    Matrix() {
        for (int i = 0; i < 10; ++i)
            for (int j = 0; j < 10; ++j)
                mat[i][j] = (i == j ? 1 : 0);
    }
};

const int BLOCK_SIZE = 500;
int num_blocks;
vector<Matrix> block_mat;

void precompute() {
    num_blocks = (N + BLOCK_SIZE - 1) / BLOCK_SIZE;
    block_mat.resize(num_blocks);

    for (int b = 0; b < num_blocks; ++b) {
        int L = b * BLOCK_SIZE + 1;
        int R = min(N, (b + 1) * BLOCK_SIZE);

        // Precompute transitions across [L, R]
        // To build the matrix that maps state before L to state at R:
        // We can push basis vectors e_0..e_9
        Matrix M;
        for (int start_row = 0; start_row < 10; ++start_row) {
            // dp table for positions L..R
            // vector size up to R - L + 15
            int len = R - L + 15;
            vector<int> dp(len, 0);
            // basis entry at L - 1 - start_row
            // We simulate transitions into [L, R]
            int base_pos = L - 1 - start_row;
            if (base_pos >= 1 && base_pos <= N) {
                int h_base = H[base_pos];
                for (int step = 1; step <= h_base; ++step) {
                    int target = base_pos + step;
                    if (target >= L && target <= R) {
                        dp[target - L] = (dp[target - L] + 1) % MOD;
                    }
                }
            }

            for (int i = L; i <= R; ++i) {
                int cur = dp[i - L];
                if (!cur) continue;
                int hi = H[i];
                for (int step = 1; step <= hi; ++step) {
                    int target = i + step;
                    if (target >= L && target <= R) {
                        dp[target - L] = (dp[target - L] + cur) % MOD;
                    }
                }
            }

            for (int c = 0; c < 10; ++c) {
                int pos = R - c;
                if (pos >= L) {
                    M.mat[start_row][c] = dp[pos - L];
                } else if (pos == base_pos) {
                    M.mat[start_row][c] = 1;
                } else {
                    M.mat[start_row][c] = 0;
                }
            }
        }
        block_mat[b] = M;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    H.resize(N + 1);
    for (int i = 1; i <= N; ++i) cin >> H[i];

    cin >> D;
    vector<pair<int, int>> queries(D);
    for (int i = 0; i < D; ++i) {
        cin >> queries[i].first >> queries[i].second;
    }

    // Since D <= 5000, let's see if simple bounded DP per query runs fast, or if we use Block DP
    // For D <= 5000 and max gap up to 300000:
    // With N <= 300,000, pure scalar DP for all queries could take 5000 * 300,000 / 2 operations if gap is large.
    // So block DP is essential.
    precompute();

    for (int q = 0; q < D; ++q) {
        int s = queries[q].first;
        int t = queries[q].second;

        int b_s = (s - 1) / BLOCK_SIZE;
        int b_t = (t - 1) / BLOCK_SIZE;

        if (b_s == b_t) {
            // direct scalar DP within block
            int len = t - s + 1;
            vector<int> dp(len, 0);
            dp[0] = 1;
            for (int i = s; i < t; ++i) {
                int cur = dp[i - s];
                if (!cur) continue;
                int hi = min(H[i], t - i);
                for (int j = 1; j <= hi; ++j) {
                    dp[i + j - s] = (dp[i + j - s] + cur) % MOD;
                }
            }
            cout << dp[t - s] << "\n";
        } else {
            // Step 1: scalar DP in block b_s up to end of block R_s
            int R_s = (b_s + 1) * BLOCK_SIZE;
            int len_s = R_s - s + 1;
            vector<int> dp_s(len_s, 0);
            dp_s[0] = 1;
            for (int i = s; i <= R_s; ++i) {
                int cur = dp_s[i - s];
                if (!cur) continue;
                int hi = min(H[i], R_s - i);
                for (int j = 1; j <= hi; ++j) {
                    dp_s[i + j - s] = (dp_s[i + j - s] + cur) % MOD;
                }
            }

            // state vector at R_s: vec[c] = dp at R_s - c
            vector<long long> V(10, 0);
            for (int c = 0; c < 10; ++c) {
                int pos = R_s - c;
                if (pos >= s) V[c] = dp_s[pos - s];
            }

            // Step 2: multiply across full blocks from b_s + 1 to b_t - 1
            for (int b = b_s + 1; b < b_t; ++b) {
                vector<long long> next_V(10, 0);
                for (int i = 0; i < 10; ++i) {
                    if (!V[i]) continue;
                    for (int j = 0; j < 10; ++j) {
                        next_V[j] = (next_V[j] + V[i] * block_mat[b].mat[i][j]) % MOD;
                    }
                }
                V = move(next_V);
            }

            // Step 3: scalar DP in block b_t from L_t to t
            int L_t = b_t * BLOCK_SIZE + 1;
            int len_t = t - (L_t - 10) + 1;
            vector<int> dp_t(len_t, 0);
            for (int c = 0; c < 10; ++c) {
                int pos = L_t - 1 - c;
                dp_t[pos - (L_t - 10)] = V[c];
            }

            for (int i = L_t - 10; i < t; ++i) {
                int cur = dp_t[i - (L_t - 10)];
                if (!cur || i < 1) continue;
                int hi = min(H[i], t - i);
                for (int j = 1; j <= hi; ++j) {
                    dp_t[i + j - (L_t - 10)] = (dp_t[i + j - (L_t - 10)] + cur) % MOD;
                }
            }
            cout << dp_t[t - (L_t - 10)] << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

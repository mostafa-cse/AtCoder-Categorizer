# Problem Analysis: AtCoder-abc221_g — G. Jumping sequence

**Problem ID**: `AtCoder-abc221_g`  
**Contest**: `abc221`  
**Rating / Difficulty**: 2914  
**URL**: https://atcoder.jp/contests/abc221/tasks/abc221_g  
**VJudge Tag**: `[problem:AtCoder-abc221_g]`  
**Category File**: [`../categories/dynamic_programming/manhattan_chebyshev_rotation_independent_subset_sum.md`](../categories/dynamic_programming/manhattan_chebyshev_rotation_independent_subset_sum.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Starting at (0, 0), make N jumps of lengths D_1, ..., D_N in directions (U, D, L, R). Determine if (A, B) is reachable, and reconstruct the path if possible.

## 2. Core Observation & Invariant
Rotate coordinates by 45 degrees: let u = x + y and v = x - y. Each step of length D changes (u, v) by (+/-D, +/-D) where the signs for u and v are completely independent! The 2D reachability problem decouples into two independent 1D subset sum problems: choose signs for u to reach A + B, and signs for v to reach A - B. Subset sum with bitset optimization determines reachability and enables exact path reconstruction.

## 3. Step-by-Step Algorithm
1. 1. Compute U = A + B and V = A - B.
2. 2. Check parity and bound conditions: sum(D) >= |U|, sum(D) >= |V|, and sum(D) = U = V (mod 2). If invalid, return No.
3. 3. Target subset sums are Su = (sum(D) + U) / 2 and Sv = (sum(D) + V) / 2.
4. 4. Solve subset sum for Su and Sv using bitset-accelerated knapsack.
5. 5. Backtrack to recover chosen sign vectors for u and v.
6. 6. Map sign pairs back to original directions: (+,+) -> U, (-,-) -> D, (-,+) -> L, (+,-) -> R.
7. 7. Print Yes and the reconstructed movement string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(D) / 64)`
- **Space Complexity**: `O(N * sum(D) / 64)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <numeric>
#include <cstdint>

using namespace std;

const int MAX_VAL = 3600005;
const int N_WORDS = (MAX_VAL / 64) + 5;

uint64_t bs[N_WORDS];
int step_arr[MAX_VAL];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long A, B;
    if (!(cin >> N >> A >> B)) return 0;

    vector<int> D(N);
    long long S = 0;
    for (int i = 0; i < N; ++i) {
        cin >> D[i];
        S += D[i];
    }

    if ((A + B + S) % 2 != 0 || (A - B + S) % 2 != 0) {
        cout << "No\n";
        return 0;
    }

    long long Tu = (A + B + S) / 2;
    long long Tv = (A - B + S) / 2;

    if (Tu < 0 || Tu > S || Tv < 0 || Tv > S) {
        cout << "No\n";
        return 0;
    }

    memset(step_arr, -1, sizeof(step_arr));
    step_arr[0] = -2; // 0 is initially reached

    bs[0] = 1ULL; // bit 0 is set
    int max_word = 1;

    for (int i = 0; i < N; ++i) {
        int d = D[i];
        int word_shift = d >> 6;
        int bit_shift = d & 63;
        int new_max_word = min(N_WORDS - 1, max_word + word_shift + 2);

        if (bit_shift == 0) {
            for (int j = new_max_word; j >= word_shift; --j) {
                uint64_t shifted = bs[j - word_shift];
                uint64_t diff = shifted & (~bs[j]);
                if (diff) {
                    bs[j] |= diff;
                    while (diff) {
                        int b = __builtin_ctzll(diff);
                        int val = (j << 6) | b;
                        if (val <= S && step_arr[val] == -1) {
                            step_arr[val] = i;
                        }
                        diff &= diff - 1;
                    }
                }
            }
        } else {
            for (int j = new_max_word; j >= word_shift; --j) {
                uint64_t low = bs[j - word_shift] << bit_shift;
                uint64_t high = (j - word_shift - 1 >= 0) ? (bs[j - word_shift - 1] >> (64 - bit_shift)) : 0ULL;
                uint64_t shifted = low | high;
                uint64_t diff = shifted & (~bs[j]);
                if (diff) {
                    bs[j] |= diff;
                    while (diff) {
                        int b = __builtin_ctzll(diff);
                        int val = (j << 6) | b;
                        if (val <= S && step_arr[val] == -1) {
                            step_arr[val] = i;
                        }
                        diff &= diff - 1;
                    }
                }
            }
        }
        max_word = new_max_word;
    }

    if (step_arr[Tu] == -1 || step_arr[Tv] == -1) {
        cout << "No\n";
        return 0;
    }

    vector<bool> used_u(N, false);
    long long cur = Tu;
    while (cur > 0) {
        int idx = step_arr[cur];
        used_u[idx] = true;
        cur -= D[idx];
    }

    vector<bool> used_v(N, false);
    cur = Tv;
    while (cur > 0) {
        int idx = step_arr[cur];
        used_v[idx] = true;
        cur -= D[idx];
    }

    string moves = "";
    moves.reserve(N);
    for (int i = 0; i < N; ++i) {
        bool su = used_u[i];
        bool sv = used_v[i];
        if (su && sv) moves.push_back('R');
        else if (!su && !sv) moves.push_back('L');
        else if (su && !sv) moves.push_back('U');
        else moves.push_back('D');
    }

    cout << "Yes\n" << moves << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

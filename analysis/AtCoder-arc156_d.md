# Problem Analysis: AtCoder-arc156_d — D. Xor Sum 5

**Problem ID**: `AtCoder-arc156_d`  
**Contest**: `arc156`  
**Rating / Difficulty**: 2568  
**URL**: https://atcoder.jp/contests/arc156/tasks/arc156_d  
**VJudge Tag**: `[problem:AtCoder-arc156_d]`  
**Category File**: [`../categories/combinatorics/xor_sum_5_lucas_theorem_bitwise_dp.md`](../categories/combinatorics/xor_sum_5_lucas_theorem_bitwise_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Lucas Theorem`  

---

## 1. Problem Statement & Key Idea
Find the bitwise XOR sum of all $\sum_{i=1}^K A_{X_i}$ over all $N^K$ index sequences $X$.

## 2. Core Observation & Invariant
By Lucas' Theorem / Freshman's Dream in $\mathbb{F}_2[x]$, the multinomial coefficient $\binom{K}{c_1, \dots, c_N}$ is odd iff the base-2 expansions of $c_i$ partition the bits of $K$. Thus, the XOR sum reduces to $\bigoplus_{(i_b)} \sum_{b \in \text{bits}(K)} 2^b A_{i_b}$. Each bit of the sum is determined by the carry, where carry never exceeds $\max(A) \le 1000$.

## 3. Step-by-Step Algorithm
1. 1. Extract the bit positions of $K$.
2. 2. Maintain bitwise carry DP $DP[c]$ modulo 2 from step $j = 0$ up to $\max(\text{bits}(K)) + 30$.
3. 3. If $j \in \text{bits}(K)$, convolve $DP$ with $A$ in $\mathbb{F}_2$; else propagate carry $\lfloor c / 2 \rfloor$.
4. 4. For each bit $j$, the parity of transitions with $s \pmod 2 == 1$ multiplied by $N^{\text{remaining bits}} \pmod 2$ determines bit $j$ of the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \max(A) \log(K \max(A)))`
- **Space Complexity**: `O(\max(A))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<int> A(N);
    int max_A = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        max_A = max(max_A, A[i]);
    }

    vector<int> bits;
    for (int b = 0; b < 60; ++b) {
        if ((K >> b) & 1) bits.push_back(b);
    }

    int max_step = (bits.empty() ? 0 : bits.back() + 30);
    vector<int> dp(max_A + 1, 0);
    dp[0] = 1;

    long long ans = 0;

    for (int j = 0; j <= max_step; ++j) {
        int rem = 0;
        for (int b : bits) {
            if (b > j) rem++;
        }
        int rem_mult = 1;
        if (rem > 0 && N % 2 == 0) rem_mult = 0;

        int odd_count = 0;
        vector<int> next_dp(max_A + 1, 0);

        if ((K >> j) & 1) {
            for (int c = 0; c <= max_A; ++c) {
                if (dp[c]) {
                    for (int a : A) {
                        int s = c + a;
                        if (s % 2 == 1) odd_count ^= 1;
                        int c_next = s / 2;
                        if (c_next <= max_A) {
                            next_dp[c_next] ^= 1;
                        }
                    }
                }
            }
        } else {
            for (int c = 0; c <= max_A; ++c) {
                if (dp[c]) {
                    int s = c;
                    if (s % 2 == 1) odd_count ^= 1;
                    int c_next = s / 2;
                    if (c_next <= max_A) {
                        next_dp[c_next] ^= 1;
                    }
                }
            }
        }

        int bit_val = (odd_count * rem_mult) % 2;
        if (bit_val) {
            ans |= (1LL << j);
        }

        dp = move(next_dp);

        bool any_dp = false;
        for (int c = 0; c <= max_A; ++c) {
            if (dp[c]) {
                any_dp = true;
                break;
            }
        }
        if (!any_dp && (bits.empty() || j > bits.back())) break;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

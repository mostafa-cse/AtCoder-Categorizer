# Problem Analysis: AtCoder-arc075_d — F. Mirrored

**Problem ID**: `AtCoder-arc075_d`  
**Contest**: `arc075`  
**Rating / Difficulty**: 2549  
**URL**: https://atcoder.jp/contests/arc075/tasks/arc075_d  
**VJudge Tag**: `[problem:AtCoder-arc075_d]`  
**Category File**: [`../categories/dynamic_programming_dp/mirrored_digit_differences_dfs.md`](../categories/dynamic_programming_dp/mirrored_digit_differences_dfs.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Count positive integers $N$ such that $\text{rev}(N) - N = D$ for $1 \le D < 10^9$. For a fixed length $L$, expanding the decimal expansion expresses $\text{rev}(N) - N = \sum_{i=0}^{\lfloor (L-1)/2 \rfloor} x_i (10^{L-1-i} - 10^i) = D$, where $x_i = d_{L-1-i} - d_i \in [-9, 9]$. Working from the outside layer inward, at each step $x_i$ is uniquely constrained modulo 10: $x_i \equiv -D \pmod{10}$.

## 2. Core Observation & Invariant
Since $x_i \in [-9, 9]$, there are at most two candidate values for $x_i$ satisfying $x_i \equiv -D \pmod{10}$. Once $x_i$ is chosen, $(D - x_i (10^{r - l} - 1))$ is divisible by 10, so dividing by 10 advances the problem to the next inner digit layer. The number of digit pairs $(d_l, d_r)$ achieving difference $x_i$ is easily counted. With at most 2 choices per layer and depth $\le 10$, the recursion visits $\le 1024$ states per length $L \in [2, 18]$.

## 3. Step-by-Step Algorithm
1. 1. Iterate length $L$ from 2 to 18.
2. 2. In DFS function `dfs(rem_D, l, r, ways)`:
3.    a. If $l > r$: if $rem\_D == 0$, add $ways$ to total.
4.    b. If $l == r$: if $rem\_D == 0$, add $ways \times 10$ to total.
5.    c. Find $target = (-rem\_D) \bmod 10$. Test $x \in [-9, 9]$ with $x \equiv target \pmod{10}$.
6.    d. Count valid digit pairs with difference $x$ (handling no leading zero for $l = 0$).
7.    e. Let $p = 10^{r - l} - 1$. If $(rem\_D - x \cdot p) \bmod 10 == 0$, recurse on $(rem\_D - x \cdot p) / 10$ with $l + 1, r - 1$.
8. 3. Sum results across all lengths.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^{L/2})`
- **Space Complexity**: `O(L)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long long ans_count = 0;

// DFS over digit differences from outer layers to inner layers
void dfs(long long D, int l, int r, long long ways) {
    if (ways == 0) return;
    if (l > r) {
        if (D == 0) ans_count += ways;
        return;
    }
    if (l == r) {
        // middle digit contributes 0 to D
        if (D == 0) {
            ans_count += ways * 10;
        }
        return;
    }

    // Outer digits l and r
    // Contributes x * (10^r - 10^l)
    // At current mod 10: x * (0 - 1) = -x mod 10, so x = -D mod 10
    int target = (-D % 10 + 10) % 10;

    for (int x = -9; x <= 9; ++x) {
        if ((x % 10 + 10) % 10 == target) {
            // Count number of pairs (d_l, d_r) with d_r - d_l = x
            // Note: N has no leading zero, so if l == 0, d_l in [1, 9] and d_r in [1, 9]
            long long pair_ways = 0;
            if (l == 0) {
                // d_l in [1, 9], d_r = d_l + x in [1, 9]
                int min_dl = max(1, 1 - x);
                int max_dl = min(9, 9 - x);
                pair_ways = max(0, max_dl - min_dl + 1);
            } else {
                // d_l in [0, 9], d_r = d_l + x in [0, 9]
                int min_dl = max(0, -x);
                int max_dl = min(9, 9 - x);
                pair_ways = max(0, max_dl - min_dl + 1);
            }

            if (pair_ways > 0) {
                long long p = 1;
                for (int k = 0; k < r - l; ++k) p *= 10;
                p -= 1;

                long long nxt_D = D - x * p;
                if (nxt_D % 10 == 0) {
                    dfs(nxt_D / 10, l + 1, r - 1, ways * pair_ways);
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long D;
    if (!(cin >> D)) return 0;

    ans_count = 0;
    // Length of N can be from 2 to 18
    for (int len = 2; len <= 18; ++len) {
        dfs(D, 0, len - 1, 1);
    }

    cout << ans_count << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-nikkei2019_2_qual_e — E. Non-triangular Triplets

**Problem ID**: `AtCoder-nikkei2019_2_qual_e`  
**Contest**: `nikkei2019_2_qual`  
**Rating / Difficulty**: 2257  
**URL**: https://atcoder.jp/contests/nikkei2019_2_qual/tasks/nikkei2019_2_qual_e  
**VJudge Tag**: `[problem:AtCoder-nikkei2019_2_qual_e]`  
**Category File**: [`../categories/basics/constructive_triplets_parity_interleaving.md`](../categories/basics/constructive_triplets_parity_interleaving.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Determine if the $3N$ integers $K, K+1, \dots, K+3N-1$ can be partitioned into $N$ triplets $(a_i, b_i, c_i)$ such that $a_i + b_i \le c_i$ for all $i$. If possible, construct the partition; otherwise output -1.

## 2. Core Observation & Invariant
Comparing the minimum sum of $2N$ smallest elements with the maximum sum of $N$ largest elements yields the necessary condition $K \le \lfloor (N+1)/2 \rfloor$. This condition is also sufficient: partition the numbers into $A = [K, K+N-1]$, $B = [K+N, K+2N-1]$, $C = [K+2N, K+3N-1]$. Splitting $A$ and $B$ into sizes $L_1 = \lfloor(N+1)/2\rfloor$ and $L_2 = N - L_1$ and interleaving parity pairs generates every target in $C$ with $a_i + b_i \le c_i$.

## 3. Step-by-Step Algorithm
1. If $K > (N + 1) / 2$, output -1.
2. Set $L_1 = (N + 1) / 2$ and $L_2 = N - L_1$.
3. For $i = 0 \dots L_1 - 1$, pair $a = K + i, b = K + N + L_2 + i, c = K + 2N + 2i$.
4. For $i = 0 \dots L_2 - 1$, pair $a = K + L_1 + i, b = K + N + i, c = K + 2N + 2i + 1$.
5. Output all $N$ triplets.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, K;
    if (!(cin >> N >> K)) return 0;

    if (K > (N + 1) / 2) {
        cout << -1 << "\n";
        return 0;
    }

    int L1 = (N + 1) / 2;
    int L2 = N - L1;

    for (int i = 0; i < L1; ++i) {
        long long a = K + i;
        long long b = K + N + L2 + i;
        long long c = K + 2 * N + 2LL * i;
        cout << a << " " << b << " " << c << "\n";
    }

    for (int i = 0; i < L2; ++i) {
        long long a = K + L1 + i;
        long long b = K + N + i;
        long long c = K + 2 * N + 2LL * i + 1;
        cout << a << " " << b << " " << c << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

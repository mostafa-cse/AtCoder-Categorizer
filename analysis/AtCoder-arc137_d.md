# Problem Analysis: AtCoder-arc137_d — D. Prefix XORs

**Problem ID**: `AtCoder-arc137_d`  
**Contest**: `arc137`  
**Rating / Difficulty**: 2191  
**URL**: https://atcoder.jp/contests/arc137/tasks/arc137_d  
**VJudge Tag**: `[problem:AtCoder-arc137_d]`  
**Category File**: [`../categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md`](../categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Sum Over Subsets DP (SOS DP)`  

---

## 1. Problem Statement & Key Idea
After k prefix XOR operations, A_i contributes to A_N with coefficient C(N - i + k - 1, k - 1) mod 2. By Lucas' theorem, C(a + b, b) = 1 mod 2 iff a AND b = 0, which means (N - i) is a submask of ~ (k - 1). The answer for all k in [1, M] is computed via SOS DP over B bits in O(B * 2^B) time.

## 2. Core Observation & Invariant
No carries in binary addition of a and b is equivalent to a AND b = 0, which is a is a submask of ~b. Thus A_N^(k) is precisely the submask XOR sum of A_{N-a} for all a subset of (~(k-1)), which is the standard SOS DP zeta transform over XOR.

## 3. Step-by-Step Algorithm
1. Find bit width B such that 2^B > max(N, M), size = 2^B, U = size - 1.
2. Initialize dp of size 2^B with dp[N - i] = A[i] for 1 <= i <= N.
3. For each bit b from 0 to B - 1:
4.   For each mask with bit b set: dp[mask] ^= dp[mask ^ (1 << b)].
5. For each k from 1 to M, output dp[U ^ (k - 1)].

## 4. Complexity Analysis
- **Time Complexity**: `O(B * 2^B)`
- **Space Complexity**: `O(2^B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int B = 0;
    while ((1 << B) < max(N, M)) {
        B++;
    }
    // Need at least 1 bit
    B = max(B, 1);
    int size = 1 << B;
    int U = size - 1;

    vector<int> dp(size, 0);
    for (int i = 1; i <= N; ++i) {
        int a;
        cin >> a;
        int x = N - i;
        dp[x] = a;
    }

    for (int b = 0; b < B; ++b) {
        for (int mask = 0; mask < size; ++mask) {
            if (mask & (1 << b)) {
                dp[mask] ^= dp[mask ^ (1 << b)];
            }
        }
    }

    for (int k = 1; k <= M; ++k) {
        int K = k - 1;
        int target_mask = U ^ K;
        cout << dp[target_mask] << (k == M ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

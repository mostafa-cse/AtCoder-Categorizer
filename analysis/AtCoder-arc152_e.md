# Problem Analysis: AtCoder-arc152_e — E - Xor Annihilation

**Problem ID**: `AtCoder-arc152_e`  
**Contest**: `arc152`  
**Rating / Difficulty**: 2990  
**URL**: https://atcoder.jp/contests/arc152/tasks/arc152_e  
**VJudge Tag**: `[problem:AtCoder-arc152_e]`  
**Category File**: [`../categories/basics/prefix_xor_annihilation_msb_independence_trick.md`](../categories/basics/prefix_xor_annihilation_msb_independence_trick.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bit Manipulation`  
- **Topic (Skill)**: `The XOR Trick`  

---

## 1. Problem Statement & Key Idea
Balls with weights w_1, ..., w_{2^N-1} on a line move toward the larger adjacent prefix XOR sum, merging upon collision. Determine how many boundary weights Z <= 2^N-1 ensure all balls come to rest within finite time.

## 2. Core Observation & Invariant
Cumulative XOR sums p_i represent the potentials driving ball movement. Merging balls eliminates local peaks. The balls stabilize if and only if no prefix XOR sum satisfies Z XOR p_i < Z. The XOR trick establishes that Z XOR p_i < Z iff the most significant bit (MSB) of p_i is 1 in Z. Thus, Z must have 0 at every bit position that appears as the MSB of any p_i, while all other bit positions can be freely 0 or 1.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix XOR array p_i of weights w_1, ..., w_{2^N-1}.
2. 2. For each non-zero p_i, find its most significant bit (MSB) using __builtin_clz.
3. 3. Track all unique MSB bit positions in a boolean array seen_msb.
4. 4. Count the number of unused bit positions k among 0, ..., N-1.
5. 5. Output 2^k.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    int total_elements = (1 << N) - 1;
    vector<bool> seen_msb(N, false);

    int cur_xor = 0;
    for (int i = 0; i < total_elements; ++i) {
        int w;
        cin >> w;
        cur_xor ^= w;
        if (cur_xor > 0) {
            int msb = 31 - __builtin_clz(cur_xor);
            if (msb < N) {
                seen_msb[msb] = true;
            }
        }
    }

    int unused_bits = 0;
    for (int b = 0; b < N; ++b) {
        if (!seen_msb[b]) {
            unused_bits++;
        }
    }

    long long ans = 1LL << unused_bits;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-typical90_ch — Snuke's Favorite Arrays

**Problem ID**: `AtCoder-typical90_ch`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 086)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ch  
**VJudge Tag**: `[problem:AtCoder-typical90_ch]`  
**Category File**: [`../categories/basics/bitwise_independence.md`](../categories/basics/bitwise_independence.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitwise Independence`  
- **Topic (Skill)**: `Bitwise Independence & Bit-by-Bit Brute Force Verification`  

---

## 1. Problem Statement & Key Idea
N items (N <= 12). Q conditions: A_{x} | A_{y} | A_{z} = w. Count arrays satisfying all conditions modulo 998244353 where elements are 60-bit integers.

**Core Idea**: Bitwise OR operates completely independently on each of the 60 bit positions.

## 2. Core Observation & Invariant
For each bit b in [0, 59], test all 2^N = 2^12 = 4096 boolean configurations. Verify if (bit_x | bit_y | bit_z) == bit_b(w) for all Q conditions. Multiply valid configuration counts across all 60 bits.

## 3. Step-by-Step Algorithm
1. ans = 1.
2. For bit from 0 to 59:
   - valid_count = 0
   - for mask from 0 to (1<<N) - 1:
     - check if mask satisfies (mask[x] | mask[y] | mask[z]) == ((w >> bit) & 1) for all Q.
     - if valid: valid_count++
   - ans = (ans * valid_count) % MOD.
3. Output ans.

## 4. Complexity Analysis
Time: O(60 * Q * 2^N) ≈ 60 * 50 * 4096 ≈ 1.2 * 10^7 ops (< 0.05s), Space: O(Q).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct Condition {
    int x, y, z;
    unsigned long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Condition> conds(q);
    for (int i = 0; i < q; ++i) {
        cin >> conds[i].x >> conds[i].y >> conds[i].z >> conds[i].w;
        --conds[i].x; --conds[i].y; --conds[i].z;
    }

    long long total_ways = 1;
    int total_masks = 1 << n;

    for (int bit = 0; bit < 60; ++bit) {
        int valid_for_bit = 0;
        for (int mask = 0; mask < total_masks; ++mask) {
            bool ok = true;
            for (const auto& c : conds) {
                int bx = (mask >> c.x) & 1;
                int by = (mask >> c.y) & 1;
                int bz = (mask >> c.z) & 1;
                int target = (c.w >> bit) & 1ULL;
                if ((bx | by | bz) != target) {
                    ok = false;
                    break;
                }
            }
            if (ok) valid_for_bit++;
        }
        total_ways = (total_ways * valid_for_bit) % MOD;
    }

    cout << total_ways << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Bitwise independence reducing 60-bit integer problem to 60 independent boolean satisfiability evaluations.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitwise independence principle, bit-by-bit problem decomposition, and product-rule combination.
- **Reusable Pattern**: `Bitwise Independence & Bit-by-Bit Verification.`

---
Back to [Bitwise Independence & Bit-by-Bit Brute Force Verification](../categories/basics/bitwise_independence.md) | [Categories Directory](../categories/README.md)
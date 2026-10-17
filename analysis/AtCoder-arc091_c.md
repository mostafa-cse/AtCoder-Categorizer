# Problem Analysis: AtCoder-arc091_c — LISDL

**Problem ID**: `AtCoder-arc091_c`  
**Contest**: `arc091`  
**Rating / Difficulty**: 1889  
**URL**: https://atcoder.jp/contests/arc091/tasks/arc091_c  
**VJudge Tag**: `[problem:AtCoder-arc091_c]`  
**Category File**: [`../categories/basics/erdos_szekeres_lis_lds_construction.md`](../categories/basics/erdos_szekeres_lis_lds_construction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive`  
- **Topic (Skill)**: `Erdős–Szekeres Extremal Permutation Construction (LIS = A, LDS = B)`  

---

## 1. Problem Statement & Key Idea
Given N, A, B. Construct a permutation of 1..N with LIS length exactly A and LDS length exactly B, or determine impossible.

**Key Insight**: By the Erdős–Szekeres theorem, a valid permutation exists iff A + B <= N + 1 and A * B >= N. If valid, decompose N into A blocks of sizes s_1..s_A where 1 <= s_i <= B and sum s_i = N. Within each block, write numbers in descending order; arrange blocks in ascending order.

## 2. Core Observation & Invariant
Start with s_1 = B, and distribute the remaining N - B elements across the remaining A - 1 blocks with sizes between 1 and B.

## 3. Step-by-Step Algorithm
1. If A + B > N + 1 or (long long)A * B < N: print -1, return.
2. Initialize block sizes: sizes of A blocks.
3. Set first block size to B, remaining A - 1 blocks to 1.
4. Distribute remaining N - (B + A - 1) elements to blocks 2..A up to max size B.
5. Generate permutation: for each block of size s, assign next s numbers and reverse them.
6. Print permutation.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    if (a + b > n + 1 || a * b < n) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> block_sizes(a, 1);
    block_sizes[0] = b;
    long long rem = n - (b + a - 1);

    for (int i = 1; i < a && rem > 0; ++i) {
        int add = min(rem, b - 1);
        block_sizes[i] += add;
        rem -= add;
    }

    vector<int> ans;
    int cur_val = 1;

    for (int sz : block_sizes) {
        vector<int> blk;
        for (int i = 0; i < sz; ++i) {
            blk.push_back(cur_val++);
        }
        reverse(blk.begin(), blk.end());
        for (int x : blk) ans.push_back(x);
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Constructing extremal permutations matching exact Dilworth / Erdős–Szekeres bounds.
- **Reusable Pattern**: `LIS/LDS Dual Extremal Construction: Reverse elements inside A blocks of size <= B.`

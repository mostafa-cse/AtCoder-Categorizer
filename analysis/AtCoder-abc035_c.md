# Problem Analysis: AtCoder-abc035_c — Othello

**Problem ID**: `AtCoder-abc035_c`  
**Contest**: `abc035`  
**Rating / Difficulty**: 1096  
**URL**: https://atcoder.jp/contests/abc035/tasks/abc035_c  
**VJudge Tag**: `[problem:AtCoder-abc035_c]`  
**Category File**: [`../categories/data_structures/parity_difference_array_imos.md`](../categories/data_structures/parity_difference_array_imos.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Difference Arrays`  
- **Topic (Skill)**: `1D Parity Difference Array (Imos Mod 2)`  

---

## 1. Problem Statement & Key Idea
An array of N pieces initially all white (0). Q queries flip the pieces in range [l, r] between white and black. Output the final board state.

**Key Idea**: Flipping an interval [l, r] toggles parity of all elements in [l, r]. This is a range XOR difference update.

## 2. Core Observation & Invariant
Apply difference array modulo 2: diff[l] ^= 1 and diff[r + 1] ^= 1. Then compute prefix XORs running_xor ^= diff[i] to determine the final state of each piece in O(N + Q).

## 3. Step-by-Step Algorithm
1. Initialize diff array of size N + 2 to 0.
2. For each query (l, r): diff[l] ^= 1, diff[r + 1] ^= 1.
3. Compute prefix sums: running_xor ^= diff[i].
4. Print running_xor for each i in 1..N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> diff(n + 2, 0);
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        diff[l] ^= 1;
        diff[r + 1] ^= 1;
    }

    int cur = 0;
    for (int i = 1; i <= n; ++i) {
        cur ^= diff[i];
        cout << cur;
    }
    cout << "\n";

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Range toggling / parity flips via difference array.
- **Reusable Pattern**: `Range parity toggle: diff[l] ^= 1, diff[r+1] ^= 1, prefix XOR sweep.`

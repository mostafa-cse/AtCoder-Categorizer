# Problem Analysis: AtCoder-abc246_f — typewriter

**Problem ID**: `AtCoder-abc246_f`  
**Contest**: `abc246`  
**Rating / Difficulty**: 1677  
**URL**: https://atcoder.jp/contests/abc246/tasks/abc246_f  
**VJudge Tag**: `[problem:AtCoder-abc246_f]`  
**Category File**: [`../categories/combinatorics/pie_keyboard_key_sets.md`](../categories/combinatorics/pie_keyboard_key_sets.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion-Exclusion (PIE) on Keyboard Key Sets`  

---

## 1. Problem Statement & Key Idea
A typewriter has N rows of keys. Row i contains a set of lowercase letters S_i. A string of length L can be typed if there is AT LEAST ONE row containing all its letters. Find the number of typeable strings of length L, modulo 998244353.

**Key Insight**: Principle of Inclusion-Exclusion (PIE) over the N rows of keys! A string is typeable using row i if all its letters belong to S_i (which gives |S_i|^L strings).

## 2. Core Observation & Invariant
For any non-empty subset of rows mask, a string can be typed using ALL rows in mask iff its letters belong to the INTERSECTION of key sets of rows in mask: (intersection_count)^L. Apply PIE with signs determined by popcount(mask).

## 3. Step-by-Step Algorithm
1. Convert each row S_i to a 26-bit bitmask.
2. total_ans = 0.
3. For mask from 1 to (1 << N) - 1:
4.   intersection_keys = (1 << 26) - 1.
5.   For i from 0 to N - 1:
6.     if (mask & (1 << i)): intersection_keys &= row_mask[i].
7.   common_chars = popcount(intersection_keys).
8.   ways = power(common_chars, L, MOD).
9.   if popcount(mask) % 2 == 1: total_ans = (total_ans + ways) % MOD.
10.   else: total_ans = (total_ans - ways + MOD) % MOD.
11. Print total_ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<int> row_mask(n, 0);
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (char c : s) {
            row_mask[i] |= (1 << (c - 'a'));
        }
    }

    int total_masks = 1 << n;
    long long ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        int common_keys = (1 << 26) - 1;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                common_keys &= row_mask[i];
            }
        }
        int cnt = __builtin_popcount(common_keys);
        long long ways = power(cnt, L);

        if (__builtin_popcount(mask) % 2 == 1) {
            ans = (ans + ways) % MOD;
        } else {
            ans = (ans - ways + MOD) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Principle of Inclusion-Exclusion on character set intersections.
- **Reusable Pattern**: `PIE Union of Powers: sum (-1)^{|S|+1} * |intersection(S)|^L.`

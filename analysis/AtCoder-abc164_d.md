# Problem Analysis: AtCoder-abc164_d — Multiple of 2019

**Problem ID**: `AtCoder-abc164_d`  
**Contest**: `abc164`  
**Rating / Difficulty**: 1232  
**URL**: https://atcoder.jp/contests/abc164/tasks/abc164_d  
**VJudge Tag**: `[problem:AtCoder-abc164_d]`  
**Category File**: [`../categories/math/suffix_modulo_coprime_base.md`](../categories/math/suffix_modulo_coprime_base.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Number Theory`  
- **Topic (Skill)**: `Suffix Modulo 2019 Prefix Arithmetic (Coprime Base)`  

---

## 1. Problem Statement & Key Idea
Given a string S of digits. Count contiguous substrings that represent a multiple of 2019 when viewed as an integer.

**Key Idea**: A substring S[l..r] is a multiple of 2019 if and only if (suffix[l] - suffix[r + 1]) / 10^(|S|-1-r) = 0 (mod 2019).

## 2. Core Observation & Invariant
Because gcd(10, 2019) = 1 (10 is coprime to 2019 = 3 * 673), dividing by powers of 10 modulo 2019 does not change divisibility! Thus, S[l..r] = 0 (mod 2019) if and only if suffix[l] == suffix[r + 1] (mod 2019). Two matching suffix remainders define a valid multiple of 2019.

## 3. Step-by-Step Algorithm
1. Compute suffix remainders scanning S from right to left.
2. Maintain running_rem = (running_rem + digit * power_of_10) % 2019.
3. Record frequencies of each remainder in cnt array (with cnt[0] initialized to 1).
4. For each remainder r: ans += cnt[r] * (cnt[r] - 1) / 2.
5. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(MOD)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 2019;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> cnt(MOD, 0);
    cnt[0] = 1;

    int cur_rem = 0;
    int p10 = 1;
    long long ans = 0;

    for (int i = (int)s.size() - 1; i >= 0; --i) {
        int d = s[i] - '0';
        cur_rem = (cur_rem + d * p10) % MOD;
        p10 = (p10 * 10) % MOD;
        ans += cnt[cur_rem];
        cnt[cur_rem]++;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Subarray modular divisibility via suffix remainders with coprime radix.
- **Reusable Pattern**: `Divisibility by coprime M: suffix[i] == suffix[j] implies substring i..j-1 divisible by M.`

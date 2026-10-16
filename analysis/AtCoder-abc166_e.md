# Problem Analysis: AtCoder-abc166_e — This Message Will Self-Destruct in 5s

**Problem ID**: `AtCoder-abc166_e`  
**Contest**: `abc166`  
**Rating / Difficulty**: 1062  
**URL**: https://atcoder.jp/contests/abc166/tasks/abc166_e  
**VJudge Tag**: `[problem:AtCoder-abc166_e]`  
**Category File**: [`../categories/basics/algebraic_rearrangement_hash.md`](../categories/basics/algebraic_rearrangement_hash.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Hashing / Rearrangement`  
- **Topic (Skill)**: `Algebraic Rearrangement Hash Frequency Match`  

---

## 1. Problem Statement & Key Idea
Given N people with heights A_1, ..., A_N standing in line at positions 1..N. Count pairs (i, j) with i < j such that j - i = A_i + A_j.

**Key Idea**: The condition j - i = A_i + A_j couples indices i and j. Algebraic rearrangement decouples i and j: j - A_j = i + A_i.

## 2. Core Observation & Invariant
Let left_key(i) = i + A_i and right_key(j) = j - A_j. As we iterate through j from 1 to N, the number of valid pairs with j is the count of previous indices i < j such that left_key(i) == right_key(j). Maintain frequencies in a hash map.

## 3. Step-by-Step Algorithm
1. Initialize frequency map cnt.
2. Initialize pair_count = 0.
3. For j from 1 to N: read A_j; pair_count += cnt[j - A_j]; cnt[j + A_j]++.
4. Output pair_count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<long long, int> cnt;
    long long ans = 0;

    for (int j = 1; j <= n; ++j) {
        long long a;
        cin >> a;
        long long target = j - a;
        if (cnt.count(target)) {
            ans += cnt[target];
        }
        cnt[j + a]++;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Separating coupled variable equations into decoupled single-variable keys.
- **Reusable Pattern**: `Equation decoupling: j - i = A_i + A_j -> match (i + A_i) with (j - A_j) via map.`

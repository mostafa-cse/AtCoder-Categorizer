# Problem Analysis: AtCoder-agc037_b — RGB Balls

**Problem ID**: `AtCoder-agc037_b`  
**Contest**: `agc037`  
**Rating / Difficulty**: 2202  
**URL**: https://atcoder.jp/contests/agc037/tasks/agc037_b  
**VJudge Tag**: `[problem:AtCoder-agc037_b]`  
**Category File**: [`../categories/basics/rgb_balls_3color_prefix_greedy_matching.md`](../categories/basics/rgb_balls_3color_prefix_greedy_matching.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Greedy prefix matching of 3-color balls minimizing span sum sum(c_j - a_j) with exact state multiplicity counting.

## 2. Core Observation & Invariant
To minimize sum(c_j - a_j), each arriving ball should be matched as early as possible. If it can complete an existing 2-ball pair missing its color, it MUST do so. If not, it should be paired with an existing 1-ball single of a different color. If neither is available, it must start a new single.

## 3. Step-by-Step Algorithm
1. 1. Maintain counts c1[col] of 1-ball singles of each color, and c2[col] of 2-ball pairs missing color col.
2. 2. When ball of color col arrives:
3.    - If c2[col] > 0: multiply answer by c2[col] and decrement c2[col].
4.    - Else if any c1[other] > 0: multiply answer by (c1[o1] + c1[o2]) and transition one single into a pair missing the remaining color.
5.    - Else: increment c1[col].
6. 3. Multiply total ways by N! to account for assigning the N completed triples to N distinct persons.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    // c1[col]: number of 1-ball groups of color col
    // c2[col]: number of 2-ball groups missing color col
    vector<ll> c1(3, 0), c2(3, 0);

    auto get_col = [](char c) {
        if (c == 'R') return 0;
        if (c == 'G') return 1;
        return 2;
    };

    ll ans = 1;

    for (char ch : S) {
        int col = get_col(ch);
        if (c2[col] > 0) {
            ans = (ans * c2[col]) % MOD;
            c2[col]--;
        } else if (c1[(col + 1) % 3] > 0 || c1[(col + 2) % 3] > 0) {
            // Need to match with a 1-ball group of different color.
            // Notice: c1[other] transitions to c2[missing].
            // If both other colors are available, total ways is c1[o1] + c1[o2]
            int o1 = (col + 1) % 3;
            int o2 = (col + 2) % 3;
            ll ways = c1[o1] + c1[o2];
            ans = (ans * ways) % MOD;
            // Does it matter which one?
            // Actually, in the problem, a 2-ball group missing o2 was formed from o1 and col.
            // Since all 1-ball groups arrived earlier, any assignment is symmetric.
            // We can decrement whichever has higher count or either.
            if (c1[o1] > 0 && (c1[o2] == 0 || c1[o1] >= c1[o2])) {
                c1[o1]--;
                c2[o2]++;
            } else {
                c1[o2]--;
                c2[o1]++;
            }
        } else {
            c1[col]++;
        }
    }

    // Multiply by N! for the permutation of the N persons
    for (int i = 1; i <= N; ++i) {
        ans = (ans * i) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc300_g — G. P-smooth number

**Problem ID**: `AtCoder-abc300_g`  
**Contest**: `abc300`  
**Rating / Difficulty**: 2343  
**URL**: https://atcoder.jp/contests/abc300/tasks/abc300_g  
**VJudge Tag**: `[problem:AtCoder-abc300_g]`  
**Category File**: [`../categories/miscellaneous/meet_in_the_middle_smooth_numbers.md`](../categories/miscellaneous/meet_in_the_middle_smooth_numbers.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Meet in the Middle`  

---

## 1. Problem Statement & Key Idea
Count $P$-smooth numbers $\le N$ ($P \le 100, N \le 10^{16}$). Splitting the 25 primes into small primes $\le 19$ (8 primes) and large primes in $[23, 97]$ (17 primes) balances search spaces at $\approx 3 \times 10^6$, solved via meet-in-the-middle in $O(M_1 \log M_1 + M_2 \log M_2)$.

## 2. Core Observation & Invariant
There are at most 25 primes $\le 100$. By splitting the primes into two subsets—small primes $\le 19$ (8 primes) and large primes in $[23, 97]$ (17 primes)—the number of smooth numbers $\le 10^{16}$ generated independently by each half is bounded by $\approx 3.2 \times 10^6$ and $\approx 2.8 \times 10^6$, perfectly balanced for meet-in-the-middle.

## 3. Step-by-Step Algorithm
1. Split primes $\le P$ into $P_1 = \{p \le \min(P, 19)\}$ and $P_2 = \{19 < p \le P\}$.
2. DFS generate all products $\le N$ formed by $P_1$ into array $V_1$, and by $P_2$ into array $V_2$.
3. Sort $V_1$ and $V_2$.
4. Use two pointers or binary search to count pairs $(x, y) \in V_1 \times V_2$ satisfying $x \le \lfloor N / y \rfloor$ in $O(|V_1| + |V_2|)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(M_1 \log M_1 + M_2 \log M_2)`
- **Space Complexity**: `O(M_1 + M_2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    int P;
    if (!(cin >> N >> P)) return 0;

    vector<int> all_primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
    vector<int> p1, p2;
    for (int p : all_primes) {
        if (p <= P) {
            if (p <= 19) p1.push_back(p);
            else p2.push_back(p);
        }
    }

    vector<long long> v1, v2;

    auto dfs1 = [&](auto& self, int idx, long long val) -> void {
        v1.push_back(val);
        for (int i = idx; i < (int)p1.size(); ++i) {
            long long p = p1[i];
            if (val <= N / p) {
                self(self, i, val * p);
            }
        }
    };

    auto dfs2 = [&](auto& self, int idx, long long val) -> void {
        v2.push_back(val);
        for (int i = idx; i < (int)p2.size(); ++i) {
            long long p = p2[i];
            if (val <= N / p) {
                self(self, i, val * p);
            }
        }
    };

    dfs1(dfs1, 0, 1);
    dfs2(dfs2, 0, 1);

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    long long ans = 0;
    int ptr = (int)v1.size() - 1;
    for (long long y : v2) {
        while (ptr >= 0 && v1[ptr] > N / y) {
            ptr--;
        }
        ans += (ptr + 1);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc200_d — D - |A + A|

**Problem ID**: `AtCoder-arc200_d`  
**Contest**: `arc200`  
**Rating / Difficulty**: 2474  
**URL**: https://atcoder.jp/contests/arc200/tasks/arc200_d  
**VJudge Tag**: `[problem:AtCoder-arc200_d]`  
**Category File**: [`../categories/basics/a_plus_a_additive_combinatorics_constructive.md`](../categories/basics/a_plus_a_additive_combinatorics_constructive.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct a sequence $A \subseteq \mathbb{Z}_M$ such that the number of distinct pairwise sumsets $|(A + A) \bmod M|$ equals exactly $K$, or determine that none exists.

## 2. Core Observation & Invariant
By analyzing small cases and sumset parity constraints, a solution is impossible if and only if: (1) $K = 2$ and $M$ is odd, or (2) $K = 4$ and $M$ is not divisible by 4. For all other $(M, K)$, exact arithmetic progression sub-blocks construct the target sumset count directly: $K = M \implies A = \{0, 1, \dots, M-1\}$; $K = 2 \implies \{0, M/2\}$; $K = 4 \implies \{0, M/4, 2M/4, 3M/4\}$; odd $K \implies \{0, 1, \dots, (K-1)/2\}$; even $K \ge 6 \implies \{0, 2, 3, \dots, K/2\}$.

## 3. Step-by-Step Algorithm
1. 1. If $K = 2$ and $M \not\equiv 0 \pmod 2$, output `No`.
2. 2. If $K = 4$ and $M \not\equiv 0 \pmod 4$, output `No`.
3. 3. Otherwise output `Yes` and print the constructed sequence:
4.    - If $M = K$: $A = (0, 1, \dots, M-1)$.
5.    - If $K = 2$: $A = (0, M/2)$.
6.    - If $K = 4$: $A = (0, M/4, 2M/4, 3M/4)$.
7.    - If $K$ is odd: $A = (0, 1, \dots, (K-1)/2)$.
8.    - If $K \ge 6$ is even: $A = (0, 2, 3, \dots, K/2)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M) per testcase`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

void print_res(const vector<int> &a) {
    cout << "Yes\n";
    cout << a.size() << "\n";
    for (size_t i = 0; i < a.size(); ++i) {
        cout << a[i] << (i + 1 == a.size() ? "" : " ");
    }
    cout << "\n";
}

void solve() {
    int m, k;
    if (!(cin >> m >> k)) return;

    if (m == k) {
        vector<int> a(m);
        for (int i = 0; i < m; ++i) a[i] = i;
        print_res(a);
        return;
    }
    if (k == 2) {
        if (m % 2 == 0) {
            print_res({0, m / 2});
        } else {
            cout << "No\n";
        }
        return;
    }
    if (k == 4) {
        if (m % 4 == 0) {
            print_res({0, m / 4, m / 2, 3 * m / 4});
        } else {
            cout << "No\n";
        }
        return;
    }
    if (k % 2 == 1) {
        int sz = (k + 1) / 2;
        vector<int> a(sz);
        for (int i = 0; i < sz; ++i) a[i] = i;
        print_res(a);
        return;
    }
    int sz = k / 2;
    vector<int> a(sz);
    a[0] = 0;
    for (int i = 1; i < sz; ++i) a[i] = i + 1;
    print_res(a);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

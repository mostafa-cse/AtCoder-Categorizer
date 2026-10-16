# Problem Analysis: AtCoder-abc202_d — aab aba baa

**Problem ID**: `AtCoder-abc202_d`  
**Contest**: `abc202`  
**Rating / Difficulty**: 966  
**URL**: https://atcoder.jp/contests/abc202/tasks/abc202_d  
**VJudge Tag**: `[problem:AtCoder-abc202_d]`  
**Category File**: [`../categories/combinatorics/lexicographical_kth_combinatorial_branching.md`](../categories/combinatorics/lexicographical_kth_combinatorial_branching.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Lexicographical Ranking`  
- **Topic (Skill)**: `Lexicographical K-th Permutation via Combinatorial Branching`  

---

## 1. Problem Statement & Key Idea
Find the K-th lexicographically smallest string among all strings consisting of A 'a's and B 'b's (A, B <= 30, K <= C(A+B, A) <= 10^18).

**Key Idea**: Construct the string character by character from left to right. At each position, determine whether the character is 'a' or 'b' by comparing K against the number of combinations that start with 'a'.

## 2. Core Observation & Invariant
If we place 'a' at the current position, the remaining A - 1 'a's and B 'b's can form C(A - 1 + B, A - 1) distinct strings. If K <= C(A - 1 + B, A - 1), the K-th string must start with 'a' (decrement A). Otherwise, it must start with 'b' (decrement B and subtract C(A - 1 + B, A - 1) from K).

## 3. Step-by-Step Algorithm
1. Precompute combinations C(n, r) up to n = 60 using Pascal's triangle.
2. Initialize result string to empty.
3. While A > 0 or B > 0:
4. If A > 0: let count = C(A - 1 + B, A - 1). If K <= count: append 'a', A--; else: append 'b', B--, K -= count.
5. Else: append 'b', B--.
6. Print result string.

## 4. Complexity Analysis
- **Time Complexity**: `O((A + B)^2)`
- **Space Complexity**: `O((A + B)^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    long long k;
    if (!(cin >> a >> b >> k)) return 0;

    int total_len = a + b;
    vector<vector<long long>> c(total_len + 1, vector<long long>(total_len + 1, 0));

    for (int i = 0; i <= total_len; ++i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
        }
    }

    string res = "";
    while (a > 0 || b > 0) {
        if (a > 0) {
            long long count_a = c[a - 1 + b][a - 1];
            if (k <= count_a) {
                res += 'a';
                a--;
            } else {
                res += 'b';
                b--;
                k -= count_a;
            }
        } else {
            res += 'b';
            b--;
        }
    }

    cout << res << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: K-th lexicographical generation via binomial coefficient prefix counting.
- **Reusable Pattern**: `Branching decision: if K <= count('a' prefix) choose 'a', else choose 'b' and K -= count.`

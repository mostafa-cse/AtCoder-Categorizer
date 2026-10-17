# Problem Analysis: AtCoder-arc108_d — AB

**Problem ID**: `AtCoder-arc108_d`  
**Contest**: `arc108`  
**Rating / Difficulty**: 1987  
**URL**: https://atcoder.jp/contests/arc108/tasks/arc108_d  
**VJudge Tag**: `[problem:AtCoder-arc108_d]`  
**Category File**: [`../categories/dp/grammar_rewriting_fibonacci_invariants.md`](../categories/dp/grammar_rewriting_fibonacci_invariants.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Grammar Rewriting / Matrix DP`  
- **Topic (Skill)**: `Formal Grammar String Rewriting Casework and Fibonacci Transition Invariants`  

---

## 1. Problem Statement & Key Idea
Starting with string 'AB', insert characters between adjacent identical or distinct characters according to rules for 'AA', 'AB', 'BA', 'BB' until length N. Find number of distinct reachable strings modulo 10^9 + 7.

If N <= 3, the answer is 1. For N >= 4, the first step produces 'AcB' where c = rule('AB'). If c == 'A': the next insertions can only place rule('AA') between 'A' and 'A', or rule('AB') between 'A' and 'B'. Symmetrically analyze the cases: depending on rule('AA') and rule('BA'), the number of obtainable strings either remains 1, reaches 2^{N-3}, or follows the Fibonacci recurrence F_{N-1} (when consecutive blocks of 'B' are restricted to size 1).

## 2. Core Observation & Invariant
Classification over the 16 binary rule combinations reduces the grammar expansion to either 1, 2^{N-3}, or Fibonacci F_{N-1}.

## 3. Step-by-Step Algorithm
1. If N <= 3, output 1.
2. Read characters for rule AA, AB, BA, BB.
3. If rule('AB') == 'A':
4.   If rule('AA') == 'A': ans = 1.
5.   Else if rule('BA') == 'A': ans = F_{N-1}.
6.   Else: ans = 2^{N-3}.
7. If rule('AB') == 'B':
8.   If rule('BB') == 'B': ans = 1.
9.   Else if rule('BA') == 'B': ans = F_{N-1}.
10.   Else: ans = 2^{N-3}.
11. Print ans % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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
    if (!(cin >> n)) return 0;

    char c_aa, c_ab, c_ba, c_bb;
    cin >> c_aa >> c_ab >> c_ba >> c_bb;

    if (n <= 3) {
        cout << 1 << "\n";
        return 0;
    }

    vector<long long> fib(n + 1, 0);
    fib[1] = 1;
    fib[2] = 1;
    for (int i = 3; i <= n; ++i) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }

    if (c_ab == 'A') {
        if (c_aa == 'A') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'A') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    } else {
        if (c_bb == 'B') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'B') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exhaustive invariant casework on formal grammar rewriting with Fibonacci state transitions.
- **Reusable Pattern**: `Grammar Rewriting DP: Casework on seed pair rules reduces to powers of 2 or Fibonacci recurrences.`

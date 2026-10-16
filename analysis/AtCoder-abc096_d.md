# Problem Analysis: AtCoder-abc096_d — Five, Five Everywhere

**Problem ID**: `AtCoder-abc096_d`  
**Contest**: `abc096`  
**Rating / Difficulty**: 1226  
**URL**: https://atcoder.jp/contests/abc096/tasks/abc096_d  
**VJudge Tag**: `[problem:AtCoder-abc096_d]`  
**Category File**: [`../categories/number_theory/modulo_residue_prime_selection.md`](../categories/number_theory/modulo_residue_prime_selection.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Modulo-5 Arithmetic Residue Selection for Prime Subsets`  

---

## 1. Problem Statement & Key Idea
Find N distinct prime numbers <= 55,555 (N <= 55) such that any 5 chosen primes have a composite sum.

**Key Idea**: To ensure that the sum of ANY 5 chosen numbers is composite, we can enforce that their sum is always a multiple of 5!

## 2. Core Observation & Invariant
If all chosen primes p satisfy p = 1 (mod 5), then the sum of any 5 chosen primes is: sum_{i=1}^5 p_i = 1 + 1 + 1 + 1 + 1 = 5 = 0 (mod 5). Since each prime >= 11, the sum of 5 primes is at least 55 > 5, guaranteeing that the sum is strictly composite!

## 3. Step-by-Step Algorithm
1. Use Sieve of Eratosthenes to generate primes up to 55,555.
2. Filter all primes p with p % 5 == 1.
3. Select the first N such primes.
4. Print the chosen primes.

## 4. Complexity Analysis
- **Time Complexity**: `O(MAX log log MAX)`
- **Space Complexity**: `O(MAX)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 55555;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<bool> is_prime(MAX + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX; i += p) {
                is_prime[i] = false;
            }
        }
    }

    vector<int> selected;
    for (int p = 2; p <= MAX; ++p) {
        if (is_prime[p] && p % 5 == 1) {
            selected.push_back(p);
            if ((int)selected.size() == n) break;
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << selected[i] << (i + 1 == n ? '\n' : ' ');
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Constructive number theory via constant modular residue classes.
- **Reusable Pattern**: `Sum of k primes composite: pick all primes in residue class 1 mod k.`

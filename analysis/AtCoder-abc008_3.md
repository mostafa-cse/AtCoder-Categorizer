# Problem Analysis: AtCoder-abc008_3 — コイン

**Problem ID**: `AtCoder-abc008_3`  
**Contest**: `abc008`  
**Rating / Difficulty**: 1836  
**URL**: https://atcoder.jp/contests/abc008/tasks/abc008_3  
**VJudge Tag**: `[problem:AtCoder-abc008_3]`  
**Category File**: [`../categories/combinatorics/linearity_of_expectation_permutations_divisors.md`](../categories/combinatorics/linearity_of_expectation_permutations_divisors.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Linearity of Expectation`  
- **Topic (Skill)**: `Linearity of Expectation over Permutations via Divisor Relative Rank`  

---

## 1. Problem Statement & Key Idea
N coins are arranged on a line with values C_1..C_N, initially heads up. A random permutation of the coins is processed: each coin flips all subsequent coins whose values are multiples of its own value. Find the expected number of coins that end up heads up.

**Key Insight**: By Linearity of Expectation, E[heads] = sum_{i=1}^N P(coin i is heads). For coin i, let k be the number of other coins that divide C_i. The state of coin i depends solely on its relative order among these k + 1 coins.

## 2. Core Observation & Invariant
Coin i is flipped by each of the divisors that appear before it. If coin i is at index j in {0, ..., k} among the k + 1 coins, it is heads iff j is even. The probability is (floor(k / 2) + 1) / (k + 1).

## 3. Step-by-Step Algorithm
1. For each coin i in 1..N:
2.   Count k = number of other coins j != i such that C_i % C_j == 0.
3.   prob_heads = (k / 2 + 1) / (double)(k + 1).
4.   expected_heads += prob_heads.
5. Print expected_heads with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    double expected_heads = 0.0;

    for (int i = 0; i < n; ++i) {
        int k = 0;
        for (int j = 0; j < n; ++j) {
            if (i != j && c[i] % c[j] == 0) {
                k++;
            }
        }

        double prob = (double)(k / 2 + 1) / (k + 1);
        expected_heads += prob;
    }

    cout << fixed << setprecision(12) << expected_heads << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Computing expectation by isolating relative permutation rank of causal predecessors.
- **Reusable Pattern**: `Permutation Predecessor Parity Expectation: P(even predecessors) = (floor(k/2) + 1) / (k + 1).`

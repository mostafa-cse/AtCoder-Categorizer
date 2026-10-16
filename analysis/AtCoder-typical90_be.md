# Problem Analysis: AtCoder-typical90_be — Flip Flap

**Problem ID**: `AtCoder-typical90_be`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 057)  
**Rating / Difficulty**: 2200 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_be  
**VJudge Tag**: `[problem:AtCoder-typical90_be]`  
**Category File**: [`../categories/math/xor_basis.md`](../categories/math/xor_basis.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra & Basis`  
- **Topic (Skill)**: `Gaussian Elimination over GF(2) / XOR Basis for Linear Systems`  

---

## 1. Problem Statement & Key Idea
N switches, M bulbs. Switch i toggles a subset of bulbs. Target state S specifies desired on/off states for each bulb. Count combinations of switch presses that achieve target S modulo 998244353.

**Core Idea**: System of linear equations over GF(2) (field with 2 elements). Solvable via Gaussian Elimination / XOR Basis.

## 2. Core Observation & Invariant
Each switch is an M-bit vector over GF(2). Insert switches into an XOR basis of size M. If target S reduces to 0 using the basis, the number of solutions is 2^(N - rank) mod 998244353; otherwise 0.

## 3. Step-by-Step Algorithm
1. Represent each switch as a bitset of length M.
2. Insert each switch into XOR basis.
3. Reduce target vector S using the basis.
4. If S != 0: output 0.
5. Else: output 2^(N - rank) % 998244353.

## 4. Complexity Analysis
Time: O(N * M^2 / 64), Space: O(N * M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

const int MOD = 998244353;
const int MAXM = 305;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<bitset<MAXM>> basis(m);
    int rank = 0;

    for (int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        bitset<MAXM> cur;
        for (int j = 0; j < t; ++j) {
            int bulb;
            cin >> bulb;
            cur.set(bulb - 1);
        }

        // Insert into XOR basis
        for (int j = 0; j < m; ++j) {
            if (cur.test(j)) {
                if (!basis[j].test(j)) {
                    basis[j] = cur;
                    rank++;
                    break;
                }
                cur ^= basis[j];
            }
        }
    }

    bitset<MAXM> target;
    for (int j = 0; j < m; ++j) {
        int s;
        cin >> s;
        if (s == 1) target.set(j);
    }

    // Reduce target using basis
    for (int j = 0; j < m; ++j) {
        if (target.test(j)) {
            if (!basis[j].test(j)) {
                cout << 0 << "\n";
                return 0;
            }
            target ^= basis[j];
        }
    }

    cout << power(2, n - rank) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Gaussian elimination over GF(2) with vector basis reduction.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: XOR Basis, linear systems over finite fields, and kernel dimension solution counting.
- **Reusable Pattern**: `GF(2) Gaussian Elimination & XOR Basis.`

---
Back to [Gaussian Elimination over GF(2) / XOR Basis for Linear Systems](../categories/math/xor_basis.md) | [Categories Directory](../categories/README.md)
# Problem Analysis: AtCoder-agc031_c — Differ by 1 Bit

**Problem ID**: `AtCoder-agc031_c`  
**Contest**: `agc031`  
**Rating / Difficulty**: 2217  
**URL**: https://atcoder.jp/contests/agc031/tasks/agc031_c  
**VJudge Tag**: `[problem:AtCoder-agc031_c]`  
**Category File**: [`../categories/graph_theory/differ_by_1_bit_hypercube_hamiltonian_path.md`](../categories/graph_theory/differ_by_1_bit_hypercube_hamiltonian_path.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Find a Hamiltonian path on the N-dimensional hypercube starting at A and ending at B where each step changes exactly one bit.

## 2. Core Observation & Invariant
Each step flips 1 bit, changing the parity of popcount. Since a Hamiltonian path has 2^N - 1 steps (an odd number of steps), popcount(A ^ B) must be odd for a solution to exist. If odd, we can recursively divide the N-cube along a differing bit k, choose an intermediate stepping pair differing only in bit k, and solve two independent subproblems of dimension N - 1.

## 3. Step-by-Step Algorithm
1. 1. If popcount(A ^ B) % 2 == 0, output NO.
2. 2. Otherwise output YES and call recursive function solve(n, a, b, bits).
3. 3. Base case n = 1: return {a, b}.
4. 4. General case: find a bit k in bits where a and b differ. Pick another bit j != k. Set intermediate node c = a ^ (1 << j) and d = c ^ (1 << k).
5. 5. Recursively solve path1 from a to c on subcube without bit k, and path2 from d to b on subcube without bit k.
6. 6. Concatenate path1 and path2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(N * 2^N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> solve(int n, int a, int b, vector<int> bits) {
    if (n == 1) {
        return {a, b};
    }
    // Find bit k where a and b differ
    int k_idx = -1;
    for (int i = 0; i < n; i++) {
        int bit = bits[i];
        if (((a >> bit) & 1) != ((b >> bit) & 1)) {
            k_idx = i;
            break;
        }
    }
    int k_bit = bits[k_idx];

    // Pick another bit j != k
    int j_idx = (k_idx == 0 ? 1 : 0);
    int j_bit = bits[j_idx];

    int c = a ^ (1 << j_bit);
    int d = c ^ (1 << k_bit);

    vector<int> next_bits;
    for (int i = 0; i < n; i++) {
        if (i != k_idx) next_bits.push_back(bits[i]);
    }

    vector<int> path1 = solve(n - 1, a, c, next_bits);
    vector<int> path2 = solve(n - 1, d, b, next_bits);

    path1.insert(path1.end(), path2.begin(), path2.end());
    return path1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    int diff = a ^ b;
    if (__builtin_popcount(diff) % 2 == 0) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n";
    vector<int> bits(n);
    iota(bits.begin(), bits.end(), 0);

    vector<int> path = solve(n, a, b, bits);
    for (int i = 0; i < (1 << n); i++) {
        cout << path[i] << (i + 1 == (1 << n) ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

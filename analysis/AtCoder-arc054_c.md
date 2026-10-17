# Problem Analysis: AtCoder-arc054_c — C. Carnival

**Problem ID**: `AtCoder-arc054_c`  
**Contest**: `arc054`  
**Rating / Difficulty**: 2292  
**URL**: https://atcoder.jp/contests/arc054/tasks/arc054_c  
**VJudge Tag**: `[problem:AtCoder-arc054_c]`  
**Category File**: [`../categories/math/gaussian_elimination_mod2_determinant.md`](../categories/math/gaussian_elimination_mod2_determinant.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Gaussian Elimination Modulo 2`  

---

## 1. Problem Statement & Key Idea
Given a bipartite graph with adjacency matrix $S$, determine whether the number of edge subsets where every vertex has an odd degree (or cycle partitions) is odd or even.

## 2. Core Observation & Invariant
In any bipartite graph with adjacency matrix $S$, the number of cycle covers modulo 2 equals the determinant of $S$ over $\mathbb{F}_2$. A valid set of cycles with odd total ways exists if and only if $\det(S) \equiv 1 \pmod 2$.

## 3. Step-by-Step Algorithm
1. 1. The problem asks whether the number of ways to pick a subset of edges such that every vertex has an odd degree (or cycle partition) is odd or even.
2. 2. By the permanent-determinant equivalence over $\mathbb{F}_2$, $\mathrm{perm}(S) \equiv \det(S) \pmod 2$, since $(-1)^{\sigma} \equiv 1 \pmod 2$ for all permutations $\sigma$.
3. 3. A directed cycle cover in the bipartite graph corresponds exactly to a non-zero term in the permanent of the adjacency matrix $S$.
4. 4. We can compute $\det(S) \pmod 2$ using Gaussian elimination over $\mathbb{F}_2$ with `std::bitset` in $O(N^3 / 64)$.
5. 5. If $\det(S) \equiv 1 \pmod 2$, output `Odd`; otherwise output `Even`.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 / 64)`
- **Space Complexity**: `O(N^2 / 64)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<bitset<305>> mat(N);
    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < N; ++j) {
            if (s[j] == '1') {
                mat[i][j] = 1;
            }
        }
    }

    int rank = 0;
    for (int col = 0; col < N; ++col) {
        int pivot = -1;
        for (int row = rank; row < N; ++row) {
            if (mat[row][col]) {
                pivot = row;
                break;
            }
        }
        if (pivot == -1) continue;

        swap(mat[rank], mat[pivot]);
        for (int row = 0; row < N; ++row) {
            if (row != rank && mat[row][col]) {
                mat[row] ^= mat[rank];
            }
        }
        rank++;
    }

    if (rank == N) {
        cout << "Odd\n";
    } else {
        cout << "Even\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

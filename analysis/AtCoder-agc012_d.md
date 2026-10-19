# Problem Analysis: AtCoder-agc012_d — D - Colorful Balls

**Problem ID**: `AtCoder-agc012_d`  
**Contest**: `agc012`  
**Rating / Difficulty**: 2760  
**URL**: https://atcoder.jp/contests/agc012/tasks/agc012_d  
**VJudge Tag**: `[problem:AtCoder-agc012_d]`  
**Category File**: [`../categories/data_structures_ds/colorful_balls_dsu_transposition_groups.md`](../categories/data_structures_ds/colorful_balls_dsu_transposition_groups.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
N balls have colors c_i and weights w_i. Two balls of the same color can swap if w_i + w_j <= X. Two balls of different colors can swap if w_i + w_j <= Y. Find the number of distinct color arrangements modulo 10^9 + 7.

## 2. Core Observation & Invariant
Allowed swaps form transpositions that generate the full symmetric group S_{|C|} on each connected component C. The number of distinct color arrangements is prod_C (|C|! / prod_{c in C} cnt_C[c]!). To efficiently build the graph, for balls of the same color, it suffices to connect each ball i to the minimum-weight ball of color c_i. For balls of different colors, let B_1 be the globally minimum-weight ball (color c_1) and B_2 be the minimum-weight ball of any other color. Connecting each ball with color != c_1 to B_1 (if w_i + w(B_1) <= Y) and each ball with color == c_1 to B_2 (if w_i + w(B_2) <= Y) captures all connected components in O(N alpha(N)) time using DSU.

## 3. Step-by-Step Algorithm
1. 1. Find the ball of minimum weight for each color.
2. 2. Find the global minimum weight ball B_1, and minimum weight ball B_2 among other colors.
3. 3. Initialize DSU of size N.
4. 4. For each ball i, add edges to min_col[c_i], and to B_1 or B_2 if weights satisfy the thresholds.
5. 5. Group balls by their DSU component and count color frequencies.
6. 6. Compute the multinomial coefficient for each component and multiply them modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(MOD))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int MOD = 1000000007;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int ri = find(i);
        int rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
};

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long X, Y;
    if (!(cin >> n >> X >> Y)) return 0;

    vector<int> c(n);
    vector<long long> w(n);
    vector<int> min_col(n + 1, -1);

    for (int i = 0; i < n; ++i) {
        cin >> c[i] >> w[i];
        if (min_col[c[i]] == -1 || w[i] < w[min_col[c[i]]]) {
            min_col[c[i]] = i;
        }
    }

    int B1 = 0;
    for (int i = 1; i < n; ++i) {
        if (w[i] < w[B1]) B1 = i;
    }
    int c_B1 = c[B1];

    int B2 = -1;
    for (int i = 0; i < n; ++i) {
        if (c[i] != c_B1) {
            if (B2 == -1 || w[i] < w[B2]) {
                B2 = i;
            }
        }
    }

    DSU dsu(n);

    for (int i = 0; i < n; ++i) {
        // Same color
        int mc = min_col[c[i]];
        if (w[i] + w[mc] <= X) {
            dsu.unite(i, mc);
        }

        // Different color
        if (c[i] != c_B1) {
            if (w[i] + w[B1] <= Y) {
                dsu.unite(i, B1);
            }
        } else {
            if (B2 != -1 && w[i] + w[B2] <= Y) {
                dsu.unite(i, B2);
            }
        }
    }

    vector<int> comp_size(n, 0);
    vector<map<int, int>> comp_col_cnt(n);

    for (int i = 0; i < n; ++i) {
        int r = dsu.find(i);
        comp_size[r]++;
        comp_col_cnt[r][c[i]]++;
    }

    vector<long long> fact(n + 1, 1);
    vector<long long> inv(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    long long ans = 1;
    for (int i = 0; i < n; ++i) {
        if (comp_size[i] > 0) {
            long long ways = fact[comp_size[i]];
            for (const auto& entry : comp_col_cnt[i]) {
                ways = (ways * inv[entry.second]) % MOD;
            }
            ans = (ans * ways) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

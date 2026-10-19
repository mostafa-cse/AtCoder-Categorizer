# Problem Analysis: AtCoder-caddi2018_d — F - Square

**Problem ID**: `AtCoder-caddi2018_d`  
**Contest**: `caddi2018`  
**Rating / Difficulty**: 2723  
**URL**: https://atcoder.jp/contests/caddi2018/tasks/caddi2018_d  
**VJudge Tag**: `[problem:AtCoder-caddi2018_d]`  
**Category File**: [`../categories/basics/square_2x2_parity_xor_grid.md`](../categories/basics/square_2x2_parity_xor_grid.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bit Manipulation`  
- **Topic (Skill)**: `The XOR Trick`  

---

## 1. Problem Statement & Key Idea
In an N x N grid (N <= 10^5), M cells have predetermined values in {0, 1}. Fill the remaining cells so that for all 1 <= i < j <= N, the subgrid from (i, i) to (j, j) contains an even number of 1s. Find the number of valid configurations modulo 998244353.

## 2. Core Observation & Invariant
Any subgrid from (i, i) to (j, j) contains cell (r, c) iff it contains (c, r). Thus only the sum a_{i,j} + a_{j,i} (mod 2) matters. Setting a_{i,i} = x_i, the 2x2 square condition forces a_{i, i+1} + a_{i+1, i} = x_i ^ x_{i+1}, the 3x3 square condition forces a_{i, i+2} + a_{i+2, i} = x_{i+1}, and larger squares force a_{i, j} + a_{j, i} = 0 for j - i >= 3. This reduces the problem to solving a linear system of XOR constraints on x_1..x_N using potential DSU. Unconstrained off-diagonal pairs (i, j) with i < j where neither (i, j) nor (j, i) was given contribute an independent factor of 2^{K_none}.

## 3. Step-by-Step Algorithm
1. 1. Identify all off-diagonal pairs (i, j) with i < j mentioned in the M inputs. Let K_none = N*(N-1)/2 - (number of mentioned pairs).
2. 2. Check for contradictions on pairs with j - i >= 3: if both (i, j) and (j, i) are fixed, their XOR must be 0; otherwise return 0.
3. 3. Build a potential DSU on N variables x_1..x_N.
4. 4. For distance 1 (|i - j| = 1), if both cells are fixed, unite x_i and x_{i+1} with weight c(i, i+1) ^ c(i+1, i).
5. 5. For distance 0 (diagonal) and distance 2, assign fixed values to variables x_i and x_{i+1} respectively. Check for consistency with DSU potentials.
6. 6. Count free components among x_1..x_N. The answer is 2^{free_comps} * 2^{K_none} mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

struct DSU {
    vector<int> parent;
    vector<int> pot;
    DSU(int n) : parent(n + 1), pot(n + 1, 0) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        int orig_p = parent[i];
        int root = find(orig_p);
        pot[i] ^= pot[orig_p];
        return parent[i] = root;
    }
    bool unite(int i, int j, int w) {
        int ri = find(i);
        int rj = find(j);
        if (ri == rj) {
            return (pot[i] ^ pot[j]) == w;
        }
        parent[ri] = rj;
        pot[ri] = pot[i] ^ pot[j] ^ w;
        return true;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    int M;
    if (!(cin >> N >> M)) return 0;

    map<pair<int, int>, int> grid_fixed;
    set<pair<int, int>> pairs;

    for (int idx = 0; idx < M; ++idx) {
        int a, b, c;
        cin >> a >> b >> c;
        grid_fixed[{a, b}] = c;
        if (a != b) {
            pairs.insert({min(a, b), max(a, b)});
        }
    }

    long long total_pairs = (N * (N - 1)) / 2;
    long long K_none = total_pairs - (long long)pairs.size();

    // Check constraints on j - i >= 3
    for (const auto& p : pairs) {
        int i = p.first;
        int j = p.second;
        if (j - i >= 3) {
            if (grid_fixed.count({i, j}) && grid_fixed.count({j, i})) {
                if ((grid_fixed[{i, j}] ^ grid_fixed[{j, i}]) != 0) {
                    cout << 0 << "\n";
                    return 0;
                }
            }
        }
    }

    DSU dsu(N);

    // Distance 1: a_{i, i+1} + a_{i+1, i} = x_i + x_{i+1}
    for (int i = 1; i < N; ++i) {
        if (grid_fixed.count({i, i + 1}) && grid_fixed.count({i + 1, i})) {
            int w = grid_fixed[{i, i + 1}] ^ grid_fixed[{i + 1, i}];
            if (!dsu.unite(i, i + 1, w)) {
                cout << 0 << "\n";
                return 0;
            }
        }
    }

    // Check fixed values
    map<int, int> comp_fixed;
    for (int i = 1; i <= N; ++i) {
        if (grid_fixed.count({i, i})) {
            int v = grid_fixed[{i, i}];
            int r = dsu.find(i);
            int exp_val = v ^ dsu.pot[i];
            if (comp_fixed.count(r) && comp_fixed[r] != exp_val) {
                cout << 0 << "\n";
                return 0;
            }
            comp_fixed[r] = exp_val;
        }
    }

    for (int i = 1; i <= N - 2; ++i) {
        if (grid_fixed.count({i, i + 2}) && grid_fixed.count({i + 2, i})) {
            int v = grid_fixed[{i, i + 2}] ^ grid_fixed[{i + 2, i}];
            int var = i + 1;
            int r = dsu.find(var);
            int exp_val = v ^ dsu.pot[var];
            if (comp_fixed.count(r) && comp_fixed[r] != exp_val) {
                cout << 0 << "\n";
                return 0;
            }
            comp_fixed[r] = exp_val;
        }
    }

    set<int> comp_roots;
    for (int i = 1; i <= N; ++i) {
        comp_roots.insert(dsu.find(i));
    }

    long long free_comps = 0;
    for (int r : comp_roots) {
        if (!comp_fixed.count(r)) {
            free_comps++;
        }
    }

    long long ans = power_mod(2, free_comps);
    ans = (ans * power_mod(2, K_none)) % MOD;

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

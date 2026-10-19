# Problem Analysis: AtCoder-abc376_g — G - Treasure Hunting

**Problem ID**: `AtCoder-abc376_g`  
**Contest**: `abc376`  
**Rating / Difficulty**: 2858  
**URL**: https://atcoder.jp/contests/abc376/tasks/abc376_g  
**VJudge Tag**: `[problem:AtCoder-abc376_g]`  
**Category File**: [`../categories/miscellaneous/tree_search_greedy_exchange_dsu_ratio_merge.md`](../categories/miscellaneous/tree_search_greedy_exchange_dsu_ratio_merge.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Exchange Arguments`  

---

## 1. Problem Statement & Key Idea
On a tree rooted at 0 with edge probabilities p_i and search times c_i, search vertices starting from the root such that a vertex can only be searched after its parent. Find the optimal search permutation to minimize expected search cost modulo 998244353.

## 2. Core Observation & Invariant
This is the classic '01 on Tree' / job sequencing with tree precedence constraints. For any two blocks of vertices A and B, processing A before B has relative advantage determined by the ratio P(A) / C(A) vs P(B) / C(B). The block with the largest ratio must be processed immediately after its parent block is processed. By maintaining a max-heap of components and merging each maximal component into its parent component using DSU, the optimal total cost is obtained.

## 3. Step-by-Step Algorithm
1. 1. Represent each vertex i as a component with probability weight P_i and cost C_i.
2. 2. Insert all non-root vertices into a priority queue keyed by P_i / C_i.
3. 3. Repeatedly extract the component with maximum ratio and merge it into its parent component via DSU.
4. 4. When merging component u into parent v, add cross-term contribution C(v) * P(u) to the total cost.
5. 5. Output total expected cost modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

static const long long MOD = 998244353;

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

struct Element {
    int u;
    long long w;
    long long s;

    bool operator<(const Element& other) const {
        // We want largest w / s first
        // w1 / s1 > w2 / s2 <=> w1 * s2 > w2 * s1
        return (__int128)w * other.s < (__int128)other.w * s;
    }
};

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<int> P(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> P[i];
    }

    vector<long long> A(N + 1, 0);
    long long S = 0;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        S = (S + A[i]) % MOD;
    }

    vector<int> dsu(N + 1);
    iota(dsu.begin(), dsu.end(), 0);

    vector<long long> weight = A;
    vector<long long> sz(N + 1, 1);
    sz[0] = 0;
    weight[0] = 0;

    auto find = [&](auto& self, int i) -> int {
        return dsu[i] == i ? i : (dsu[i] = self(self, dsu[i]));
    };

    vector<int> tree_par = P;

    priority_queue<Element> pq;
    for (int i = 1; i <= N; i++) {
        pq.push({i, weight[i], sz[i]});
    }

    long long ans_pairs = 0;

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();

        int u = top.u;
        if (find(find, u) != u) continue;
        if (weight[u] != top.w || sz[u] != top.s) continue;

        int p = find(find, tree_par[u]);

        ans_pairs = (ans_pairs + (sz[p] % MOD) * (weight[u] % MOD)) % MOD;

        dsu[u] = p;
        sz[p] += sz[u];
        weight[p] += weight[u];

        if (p != 0) {
            pq.push({p, weight[p], sz[p]});
        }
    }

    long long total_cost = (S + ans_pairs) % MOD;
    long long ans = total_cost * modInverse(S) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

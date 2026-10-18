# Problem Analysis: AtCoder-abc405_g — G. Range Shuffle Query

**Problem ID**: `AtCoder-abc405_g`  
**Contest**: `abc405`  
**Rating / Difficulty**: 2354  
**URL**: https://atcoder.jp/contests/abc405/tasks/abc405_g  
**VJudge Tag**: `[problem:AtCoder-abc405_g]`  
**Category File**: [`../categories/data_structures/mos_algorithm_multinomial_permutation.md`](../categories/data_structures/mos_algorithm_multinomial_permutation.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Mo's Algorithm`  

---

## 1. Problem Statement & Key Idea
Count permutations of remaining elements in $A[L..R]$ after removing elements $\ge X$ as a multinomial coefficient. Sorting queries via Mo's algorithm and maintaining frequency counts with block-based SQRT decomposition on the value domain achieves $O((N + Q) \sqrt{N})$ time.

## 2. Core Observation & Invariant
The number of distinct permutations of remaining elements in $A[L..R]$ after removing elements $\ge X$ is the multinomial coefficient $S! / \prod_{v < X} c_v!$, where $S = \sum_{v < X} c_v$ and $c_v$ is the frequency of value $v$ in $A[L..R]$. By sorting queries using Mo's algorithm and maintaining frequency counts with block-based SQRT decomposition on the value domain, updates are $O(1)$ and range prefix queries take $O(\sqrt{N})$.

## 3. Step-by-Step Algorithm
1. Order queries $(L, R, X)$ using Mo's ordering with block size $B_{mo} \approx N / \sqrt{Q}$.
2. Maintain value frequencies in blocks of size $B_{val} \approx 500$: when $c_v$ increments by 1, multiply the block's inverse factorial product by $inv[c_v]$ and add 1 to block sum in $O(1)$. When $c_v$ decrements, multiply by $c_v$.
3. For query $X$, aggregate full blocks and the partial block up to $X$ to get total count $S$ and $\prod_{v < X} (c_v!)^{-1}$ in $O(\sqrt{N})$. Multiply by $S!$ modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) \sqrt{N})`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 250005;

long long fact[MAXN], inv[MAXN], ifact[MAXN];

void init() {
    fact[0] = ifact[0] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAXN; i++) inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    for (int i = 1; i < MAXN; i++) {
        fact[i] = fact[i - 1] * i % MOD;
        ifact[i] = ifact[i - 1] * inv[i] % MOD;
    }
}

struct Query {
    int l, r, x, id, b;
    bool operator<(const Query& other) const {
        if (b != other.b) return b < other.b;
        return (b & 1) ? (r < other.r) : (r > other.r);
    }
};

const int B_VAL = 500;
int cnt[MAXN];
int b_sum[MAXN / 500 + 10];
long long b_pinv[MAXN / 500 + 10];

inline void add_val(int v) {
    int b = v / B_VAL;
    cnt[v]++;
    b_sum[b]++;
    b_pinv[b] = (b_pinv[b] * inv[cnt[v]]) % MOD;
}

inline void rem_val(int v) {
    int b = v / B_VAL;
    b_pinv[b] = (b_pinv[b] * cnt[v]) % MOD;
    cnt[v]--;
    b_sum[b]--;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    init();

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    int B_MO = max(1, (int)(n / max(1.0, sqrt(q))));
    vector<Query> qs(q);
    for (int i = 0; i < q; i++) {
        cin >> qs[i].l >> qs[i].r >> qs[i].x;
        qs[i].id = i;
        qs[i].b = qs[i].l / B_MO;
    }
    sort(qs.begin(), qs.end());

    int num_blocks = (n + 1) / B_VAL + 2;
    for (int i = 0; i <= num_blocks; i++) {
        b_sum[i] = 0;
        b_pinv[i] = 1;
    }

    int cur_l = 1, cur_r = 0;
    vector<long long> ans(q);

    for (const auto& qu : qs) {
        while (cur_r < qu.r) add_val(a[++cur_r]);
        while (cur_l > qu.l) add_val(a[--cur_l]);
        while (cur_r > qu.r) rem_val(a[cur_r--]);
        while (cur_l < qu.l) rem_val(a[cur_l++]);

        int limit = qu.x;
        int total_s = 0;
        long long prod_inv = 1;

        int full_b = limit / B_VAL;
        for (int b = 0; b < full_b; b++) {
            total_s += b_sum[b];
            prod_inv = (prod_inv * b_pinv[b]) % MOD;
        }
        for (int v = full_b * B_VAL; v < limit; v++) {
            if (v <= n) {
                total_s += cnt[v];
                prod_inv = (prod_inv * ifact[cnt[v]]) % MOD;
            }
        }

        if (total_s == 0) {
            ans[qu.id] = 1;
        } else {
            ans[qu.id] = (fact[total_s] * prod_inv) % MOD;
        }
    }

    for (int i = 0; i < q; i++) cout << ans[i] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

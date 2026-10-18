# Problem Analysis: AtCoder-arc216_c — C. Count Power of 2

**Problem ID**: `AtCoder-arc216_c`  
**Contest**: `arc216`  
**Rating / Difficulty**: 2346  
**URL**: https://atcoder.jp/contests/arc216/tasks/arc216_c  
**VJudge Tag**: `[problem:AtCoder-arc216_c]`  
**Category File**: [`../categories/basics/power_of_two_subarray_divide_and_conquer.md`](../categories/basics/power_of_two_subarray_divide_and_conquer.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bit Manipulation`  
- **Topic (Skill)**: `Bit Manipulation`  

---

## 1. Problem Statement & Key Idea
Count subarrays whose power-of-two sum $\sum_{i=l}^r 2^{A_i}$ is a single power of 2. Divide and conquer on range maximums checks the smaller half against $O(\log N)$ candidate powers of 2 via rolling hashes in $O(N \log^2 N)$.

## 2. Core Observation & Invariant
A subarray sum $\sum_{i=l}^r 2^{A_i} = 2^k$ is bounded by $M \le k \le M + \lfloor \log_2 N \rfloor + 1$ where $M = \max_{i=l}^r A_i$. In a divide-and-conquer on interval $[L, R]$ splitting at the maximum element $m$, testing the smaller half against $O(\log N)$ candidate powers of 2 via rolling hashes guarantees $O(N \log^2 N)$ total checks.

## 3. Step-by-Step Algorithm
1. Precompute prefix sums of $2^{A_i}$ modulo two large 60-bit primes.
2. Build a Sparse Table to query range maximum index in $O(1)$.
3. Divide-and-conquer on $[L, R]$: find index $m$ of maximum element $M$.
4. Iterate over the smaller half (either $l \in [L, m]$ or $r \in [m, R]$) and check whether target hash $P_{l-1} + 2^k$ (or $P_r - 2^k$) exists in the opposite interval via binary search over sorted prefix hashes in $O(N \log^2 N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

const ull MOD1 = 1000000000000000003ULL; // large 60-bit prime
const ull MOD2 = 1000000000000000009ULL;

const int MAX_A = 200050;
ull pw1[MAX_A + 30];
ull pw2[MAX_A + 30];

void precompute() {
    pw1[0] = 1;
    pw2[0] = 1;
    for (int i = 1; i < MAX_A + 30; ++i) {
        pw1[i] = (__int128)pw1[i - 1] * 2 % MOD1;
        pw2[i] = (__int128)pw2[i - 1] * 2 % MOD2;
    }
}

struct Hash {
    ull h1, h2;
    bool operator<(const Hash& o) const {
        if (h1 != o.h1) return h1 < o.h1;
        return h2 < o.h2;
    }
    bool operator==(const Hash& o) const {
        return h1 == o.h1 && h2 == o.h2;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<Hash> P(N + 1);
    P[0] = {0, 0};
    for (int i = 1; i <= N; ++i) {
        ull add1 = pw1[A[i]];
        ull add2 = pw2[A[i]];
        ull nh1 = P[i - 1].h1 + add1;
        if (nh1 >= MOD1) nh1 -= MOD1;
        ull nh2 = P[i - 1].h2 + add2;
        if (nh2 >= MOD2) nh2 -= MOD2;
        P[i] = {nh1, nh2};
    }

    vector<pair<Hash, int>> sorted_P(N + 1);
    for (int i = 0; i <= N; ++i) {
        sorted_P[i] = {P[i], i};
    }
    sort(sorted_P.begin(), sorted_P.end());

    auto get_pos = [&](const Hash& h) -> int {
        auto it = lower_bound(sorted_P.begin(), sorted_P.end(), make_pair(h, -1));
        if (it != sorted_P.end() && it->first == h) {
            return it->second;
        }
        return -1;
    };

    // Sparse Table for max index
    int K = 20;
    vector<vector<int>> st(K, vector<int>(N + 1));
    for (int i = 1; i <= N; ++i) st[0][i] = i;

    for (int k = 1; k < K; ++k) {
        int len = 1 << (k - 1);
        for (int i = 1; i + (1 << k) - 1 <= N; ++i) {
            int idx1 = st[k - 1][i];
            int idx2 = st[k - 1][i + len];
            st[k][i] = (A[idx1] >= A[idx2]) ? idx1 : idx2;
        }
    }

    auto get_max_idx = [&](int l, int r) -> int {
        int len = r - l + 1;
        int k = 31 - __builtin_clz(len);
        int idx1 = st[k][l];
        int idx2 = st[k][r - (1 << k) + 1];
        return (A[idx1] >= A[idx2]) ? idx1 : idx2;
    };

    long long ans = 0;

    auto dnc = [&](auto& self, int L, int R) -> void {
        if (L > R) return;
        int m = get_max_idx(L, R);
        int M = A[m];
        int max_k = M + (31 - __builtin_clz(R - L + 1)) + 1;

        if (m - L <= R - m) {
            for (int l = L; l <= m; ++l) {
                Hash pl = P[l - 1];
                for (int k = M; k <= max_k; ++k) {
                    ull th1 = pl.h1 + pw1[k];
                    if (th1 >= MOD1) th1 -= MOD1;
                    ull th2 = pl.h2 + pw2[k];
                    if (th2 >= MOD2) th2 -= MOD2;
                    int r = get_pos({th1, th2});
                    if (r >= m && r <= R) {
                        ans++;
                    }
                }
            }
        } else {
            for (int r = m; r <= R; ++r) {
                Hash pr = P[r];
                for (int k = M; k <= max_k; ++k) {
                    ull th1 = (pr.h1 >= pw1[k]) ? (pr.h1 - pw1[k]) : (pr.h1 + MOD1 - pw1[k]);
                    ull th2 = (pr.h2 >= pw2[k]) ? (pr.h2 - pw2[k]) : (pr.h2 + MOD2 - pw2[k]);
                    int pos_idx = get_pos({th1, th2});
                    if (pos_idx != -1) {
                        int l = pos_idx + 1;
                        if (l >= L && l <= m) {
                            ans++;
                        }
                    }
                }
            }
        }

        self(self, L, m - 1);
        self(self, m + 1, R);
    };

    dnc(dnc, 1, N);

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

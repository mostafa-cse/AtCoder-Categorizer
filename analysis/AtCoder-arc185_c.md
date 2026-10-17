# Problem Analysis: AtCoder-arc185_c — Sum of Three Integers

**Problem ID**: `AtCoder-arc185_c`  
**Contest**: `arc185`  
**Rating / Difficulty**: 2242  
**URL**: https://atcoder.jp/contests/arc185/tasks/arc185_c  
**VJudge Tag**: `[problem:AtCoder-arc185_c]`  
**Category File**: [`../categories/math/ntt_convolution_3_sum_integer_retrieval.md`](../categories/math/ntt_convolution_3_sum_integer_retrieval.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
Find an index triple 1 <= i < j < k <= N such that A_i + A_j + A_k = X, where N, X <= 10^6.

## 2. Core Observation & Invariant
If any value appears >= 4 times, capping its frequency to 3 preserves existence of a solution. With frequencies capped at 3, polynomial self-convolution f * f has coefficients at most 3 * 3 * X << 998244353, allowing standard NTT modulo 998244353 without overflow. From f * f, we obtain g(n) = number of pairs (t, u) with t < u and A_t + A_u = n. For any candidate s, the number of pairs (t, u) disjoint from s summing to X - A_s is g(X - A_s) - [f(X - 2A_s) - [X == 3A_s]]. We can check all s in O(N) and recover t, u in O(X).

## 3. Step-by-Step Algorithm
1. 1. Check if any value v satisfies 3v == X with frequency >= 3; if so, output its first 3 indices.
2. 2. Cap frequency array f at min(freq, 3) for each value in [1, X].
3. 3. Compute polynomial self-convolution fa = f * f using standard NTT modulo 998244353.
4. 4. Derive g[n] = (fa[n] - (f[n/2] if n even)) / 2.
5. 5. Iterate s from 1 to N: check if valid disjoint pair count for rem = X - A_s is positive. Upon finding such s, search for v1 in [1, rem/2] with valid indices in O(X).
6. 6. Sort the three indices and output them, or output -1 if no s exists.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + X log X)`
- **Space Complexity**: `O(N + X)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int G = 3;

long long mod_pow(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return mod_pow(n, MOD - 2);
}

void ntt(vector<int>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = mod_pow(G, (MOD - 1) / len);
        if (invert) wlen = mod_inv(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }

    if (invert) {
        long long n_inv = mod_inv(n);
        for (int& x : a) x = (x * n_inv) % MOD;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X;
    if (!(cin >> N >> X)) return 0;

    vector<int> A(N + 1);
    vector<vector<int>> pos(X + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        if (A[i] <= X) {
            pos[A[i]].push_back(i);
        }
    }

    // Check if any element occurs >= 3 times and 3 * val == X
    for (int v = 1; v <= X; ++v) {
        if (3LL * v == X && pos[v].size() >= 3) {
            cout << pos[v][0] << " " << pos[v][1] << " " << pos[v][2] << "\n";
            return 0;
        }
    }

    // Build frequency array f with capped occurrences (at most 3 per value)
    vector<int> f(X + 1, 0);
    for (int v = 1; v <= X; ++v) {
        f[v] = min((int)pos[v].size(), 3);
    }

    // NTT size
    int ntt_size = 1;
    while (ntt_size <= 2 * X) ntt_size <<= 1;

    vector<int> fa(ntt_size, 0);
    for (int i = 1; i <= X; ++i) fa[i] = f[i];

    ntt(fa, false);
    for (int i = 0; i < ntt_size; ++i) {
        fa[i] = (long long)fa[i] * fa[i] % MOD;
    }
    ntt(fa, true);

    // g[n] = count of pairs (t, u) with t < u, A_t + A_u = n
    // in the capped subset
    vector<long long> g(X + 1, 0);
    for (int n = 1; n <= X; ++n) {
        long long total = fa[n];
        long long self_term = (n % 2 == 0 ? f[n / 2] : 0);
        long long pairs = (total - self_term + MOD) % MOD;
        pairs = (pairs * mod_inv(2)) % MOD;
        g[n] = pairs;
    }

    // Find valid index s (1 <= s <= N)
    int found_s = -1;
    for (int s = 1; s <= N; ++s) {
        int as = A[s];
        int rem = X - as;
        if (rem <= 0 || rem > X) continue;

        long long num_pairs = g[rem];
        long long subtract = 0;
        if (rem - as >= 1 && rem - as <= X) {
            subtract += f[rem - as];
            if (X == 3 * as) {
                subtract -= 1;
            }
        }
        if (num_pairs - subtract > 0) {
            found_s = s;
            break;
        }
    }

    if (found_s == -1) {
        cout << -1 << "\n";
        return 0;
    }

    // Recover t and u
    int s = found_s;
    int rem = X - A[s];
    int found_t = -1, found_u = -1;

    for (int v1 = 1; v1 <= rem / 2; ++v1) {
        int v2 = rem - v1;
        if (v2 > X) continue;

        if (v1 == v2) {
            // Need 2 indices with value v1 distinct from s
            vector<int> candidates;
            for (int idx : pos[v1]) {
                if (idx != s) {
                    candidates.push_back(idx);
                    if (candidates.size() == 2) break;
                }
            }
            if (candidates.size() == 2) {
                found_t = candidates[0];
                found_u = candidates[1];
                break;
            }
        } else {
            // Need 1 index with v1 and 1 with v2 distinct from s
            int t_cand = -1, u_cand = -1;
            for (int idx : pos[v1]) {
                if (idx != s) {
                    t_cand = idx;
                    break;
                }
            }
            for (int idx : pos[v2]) {
                if (idx != s) {
                    u_cand = idx;
                    break;
                }
            }
            if (t_cand != -1 && u_cand != -1) {
                found_t = t_cand;
                found_u = u_cand;
                break;
            }
        }
    }

    if (found_t == -1 || found_u == -1) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> ans = {s, found_t, found_u};
    sort(ans.begin(), ans.end());
    cout << ans[0] << " " << ans[1] << " " << ans[2] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

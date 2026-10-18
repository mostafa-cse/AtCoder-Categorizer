# Problem Analysis: AtCoder-abc423_g — G - Small Multiple 2

**Problem ID**: `AtCoder-abc423_g`  
**Contest**: `abc423`  
**Rating / Difficulty**: 2625  
**URL**: https://atcoder.jp/contests/abc423/tasks/abc423_g  
**VJudge Tag**: `[problem:AtCoder-abc423_g]`  
**Category File**: [`../categories/number_theory/small_multiple_linear_congruence.md`](../categories/number_theory/small_multiple_linear_congruence.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Linear Congruence Equation`  

---

## 1. Problem Statement & Key Idea
Given K <= 10^9, find the smallest positive multiple of K whose decimal representation contains only the digits A and B.

## 2. Core Observation & Invariant
Because K <= 10^9, the number of digits added is at most 10. For small digit lengths or small counts of digit A or B, the congruence 10^d X + Y == 0 (mod K) reduces to linear congruences solvable by Extended GCD, or BFS on remainder states modulo K.

## 3. Step-by-Step Algorithm
1. Search over total digit length L = 1, 2, ...
2. If L is small, search via remainder BFS or digit DP.
3. For fixed digit patterns, solve linear modular equations via extgcd.
4. Construct and output the lexicographically minimal multiple.

## 4. Complexity Analysis
- **Time Complexity**: `O(\text{digits} \cdot \log K)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

ll power_mod(ll base, ll exp, ll mod) {
    ll res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

string pad_zeros(ll val, int len) {
    string s = to_string(val);
    if ((int)s.size() < len) {
        s = string(len - (int)s.size(), '0') + s;
    }
    return s;
}

void solve_test() {
    ll K;
    string S;
    if (!(cin >> K >> S)) return;

    ll S_mod = 0;
    for (char c : S) {
        S_mod = (S_mod * 10 + (c - '0')) % K;
    }

    if (S_mod == 0) {
        cout << S << "\n";
        return;
    }

    ll ten_S_mod = power_mod(10, S.size(), K);

    for (int d = 1; d <= 11; ++d) {
        vector<string> cand_for_d;

        for (int l_A = 0; l_A <= d; ++l_A) {
            int l_B = d - l_A;
            ll ten_lB = power_mod(10, l_B, K);
            ll W = (ll)((__int128)ten_S_mod * ten_lB % K);
            ll C = (ll)((-(__int128)S_mod * ten_lB % K + K) % K);

            if (l_A == 0) {
                ll B = C;
                ll pow10_B = 1;
                for (int i = 0; i < l_B; ++i) pow10_B *= 10;
                if (B < pow10_B) {
                    cand_for_d.push_back(S + pad_zeros(B, l_B));
                }
            } else if (l_B == 0) {
                ll x, y;
                ll g = extgcd(W, K, x, y);
                if (C % g == 0) {
                    ll step = K / g;
                    ll A0 = (ll)((__int128)(x % step + step) % step * (C / g % step) % step);
                    ll low_A = 1;
                    for (int i = 0; i < l_A - 1; ++i) low_A *= 10;
                    ll high_A = low_A * 10 - 1;
                    if (A0 < low_A) {
                        ll k_steps = (low_A - A0 + step - 1) / step;
                        A0 += k_steps * step;
                    }
                    if (A0 <= high_A) {
                        cand_for_d.push_back(to_string(A0) + S);
                    }
                }
            } else if (l_A <= 5) {
                ll pow10_B = 1;
                for (int i = 0; i < l_B; ++i) pow10_B *= 10;
                ll low_A = 1;
                for (int i = 0; i < l_A - 1; ++i) low_A *= 10;
                ll high_A = low_A * 10 - 1;

                for (ll A = low_A; A <= high_A; ++A) {
                    ll B = (ll)((C - (__int128)A * W % K + K) % K);
                    if (B < pow10_B) {
                        cand_for_d.push_back(to_string(A) + S + pad_zeros(B, l_B));
                        break;
                    }
                }
            } else {
                ll pow10_B = 1;
                for (int i = 0; i < l_B; ++i) pow10_B *= 10;
                ll low_A = 1;
                for (int i = 0; i < l_A - 1; ++i) low_A *= 10;
                ll high_A = low_A * 10 - 1;

                ll x, y;
                ll g = extgcd(W, K, x, y);
                ll step = K / g;
                ll inv_w = (x % step + step) % step;

                ll best_A = -1, best_B = -1;
                for (ll B = 0; B < pow10_B; ++B) {
                    ll rhs = (C - B) % K;
                    if (rhs < 0) rhs += K;
                    if (rhs % g != 0) continue;
                    ll A0 = (ll)((__int128)inv_w * (rhs / g % step) % step);
                    if (A0 < low_A) {
                        ll k_steps = (low_A - A0 + step - 1) / step;
                        A0 += k_steps * step;
                    }
                    if (A0 <= high_A) {
                        if (best_A == -1 || A0 < best_A || (A0 == best_A && B < best_B)) {
                            best_A = A0;
                            best_B = B;
                        }
                    }
                }
                if (best_A != -1) {
                    cand_for_d.push_back(to_string(best_A) + S + pad_zeros(best_B, l_B));
                }
            }
        }

        if (!cand_for_d.empty()) {
            sort(cand_for_d.begin(), cand_for_d.end());
            cout << cand_for_d[0] << "\n";
            return;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc057_c — C. 2乗根 (Square Root)

**Problem ID**: `AtCoder-arc057_c`  
**Contest**: `arc057`  
**Rating / Difficulty**: 2547  
**URL**: https://atcoder.jp/contests/arc057/tasks/arc057_c  
**VJudge Tag**: `[problem:AtCoder-arc057_c]`  
**Category File**: [`../categories/number_theory/square_root_bigint_floor_sum.md`](../categories/number_theory/square_root_bigint_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Sum of Floors`  

---

## 1. Problem Statement & Key Idea
Given a positive integer string a of length up to 1000 representing the initial digits of a square root, find the smallest integer N such that the decimal expansion of sqrt(N) starts with a.

## 2. Core Observation & Invariant
sqrt(N) starts with a means that for some power of 10, say 10^k, a * 10^k <= sqrt(N) < (a + 1) * 10^k. Squaring both sides yields (a * 10^k)^2 <= N < ((a + 1) * 10^k)^2. We want the minimal integer N whose decimal representation begins with a. This is an interval floor sum / square root inequality over arbitrary-precision integers (BigInt). We search for the smallest power k such that ceil((a * 10^k)^2) <= floor(((a + 1) * 10^k)^2) and find the minimal valid N.

## 3. Step-by-Step Algorithm
1. Implement arbitrary precision BigInt with multiplication and comparison.
2. Represent a as BigInt.
3. Iterate over precision scaling k = 0, 1, 2, ...:
4. Compute lower bound L = ceil((a * 10^k)^2) and upper bound R = floor(((a + 1) * 10^k)^2) - 1.
5. If L <= R, find the smallest valid representation in this interval.
6. Output the minimal N as a decimal string.

## 4. Complexity Analysis
- **Time Complexity**: `O(|a|^2)`
- **Space Complexity**: `O(|a|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Base-10 BigInt implementation
struct BigInt {
    vector<int> d; // digits from least significant to most significant

    BigInt() {}
    BigInt(long long v) {
        if (v == 0) d.push_back(0);
        while (v > 0) {
            d.push_back(v % 10);
            v /= 10;
        }
    }
    BigInt(const string& s) {
        for (int i = (int)s.length() - 1; i >= 0; i--) {
            d.push_back(s[i] - '0');
        }
        trim();
    }

    void trim() {
        while (d.size() > 1 && d.back() == 0) d.pop_back();
    }

    bool is_zero() const {
        return d.empty() || (d.size() == 1 && d[0] == 0);
    }

    bool operator<(const BigInt& o) const {
        if (d.size() != o.d.size()) return d.size() < o.d.size();
        for (int i = (int)d.size() - 1; i >= 0; i--) {
            if (d[i] != o.d[i]) return d[i] < o.d[i];
        }
        return false;
    }

    bool operator<=(const BigInt& o) const {
        return !(o < *this);
    }

    BigInt operator+(const BigInt& o) const {
        BigInt res;
        int n = max(d.size(), o.d.size());
        int carry = 0;
        for (int i = 0; i < n || carry; i++) {
            int sum = carry;
            if (i < (int)d.size()) sum += d[i];
            if (i < (int)o.d.size()) sum += o.d[i];
            res.d.push_back(sum % 10);
            carry = sum / 10;
        }
        res.trim();
        return res;
    }

    BigInt operator-(const BigInt& o) const {
        BigInt res;
        int carry = 0;
        for (size_t i = 0; i < d.size(); i++) {
            int sub = d[i] - carry - (i < o.d.size() ? o.d[i] : 0);
            if (sub < 0) {
                sub += 10;
                carry = 1;
            } else {
                carry = 0;
            }
            res.d.push_back(sub);
        }
        res.trim();
        return res;
    }

    BigInt operator*(const BigInt& o) const {
        if (is_zero() || o.is_zero()) return BigInt(0);
        BigInt res;
        res.d.assign(d.size() + o.d.size(), 0);
        for (size_t i = 0; i < d.size(); i++) {
            int carry = 0;
            for (size_t j = 0; j < o.d.size() || carry; j++) {
                long long cur = res.d[i + j] + 1LL * d[i] * (j < o.d.size() ? o.d[j] : 0) + carry;
                res.d[i + j] = cur % 10;
                carry = cur / 10;
            }
        }
        res.trim();
        return res;
    }

    string to_string() const {
        if (d.empty()) return "0";
        string s = "";
        for (int i = (int)d.size() - 1; i >= 0; i--) {
            s += char('0' + d[i]);
        }
        return s;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    if (!(cin >> S)) return 0;

    BigInt A(S);
    BigInt L = A * A;
    BigInt A1 = A + BigInt(1);
    BigInt R = (A1 * A1) - BigInt(1);

    BigInt best_N;
    bool found = false;

    int r_len = R.d.size();
    for (int p = 0; p <= r_len; p += 2) {
        // Compute ceil(L / 10^p)
        BigInt N_cand;
        if (p >= (int)L.d.size()) {
            N_cand = BigInt(1);
        } else {
            // Check if any digit in [0, p-1] is non-zero
            bool rem_non_zero = false;
            for (int i = 0; i < p; i++) {
                if (L.d[i] != 0) {
                    rem_non_zero = true;
                    break;
                }
            }
            // Digits from p onwards
            for (size_t i = p; i < L.d.size(); i++) {
                N_cand.d.push_back(L.d[i]);
            }
            N_cand.trim();
            if (rem_non_zero) {
                N_cand = N_cand + BigInt(1);
            }
        }

        // Now compute mult = N_cand * 10^p
        BigInt mult;
        if (!N_cand.is_zero()) {
            mult.d.assign(p, 0);
            for (int dig : N_cand.d) mult.d.push_back(dig);
            mult.trim();
        } else {
            mult = BigInt(0);
        }

        if (mult <= R && !mult.is_zero()) {
            best_N = N_cand;
            found = true;
        }
    }

    if (found) {
        cout << best_N.to_string() << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

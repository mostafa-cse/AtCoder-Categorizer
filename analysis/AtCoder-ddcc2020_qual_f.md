# Problem Analysis: AtCoder-ddcc2020_qual_f — F - DISCOSMOS

**Problem ID**: `AtCoder-ddcc2020_qual_f`  
**Contest**: `ddcc2020-qual`  
**Rating / Difficulty**: 2992  
**URL**: https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_f  
**VJudge Tag**: `[problem:AtCoder-ddcc2020_qual_f]`  
**Category File**: [`../categories/miscellaneous/toroidal_grid_robot_flow_orbit_decomposition_burnside.md`](../categories/miscellaneous/toroidal_grid_robot_flow_orbit_decomposition_burnside.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Burnside's Lemma / Polya Enumeration Theorem`  

---

## 1. Problem Statement & Key Idea
On an H x W toroidal grid, place stationary, right-moving, or down-moving robots such that at times 0, T, 2T, ... every cell has exactly one robot. Count valid configurations modulo 10^9+7.

## 2. Core Observation & Invariant
For T = 1, diagonal zones (x - y mod gcd(H, W)) cannot contain both right and down robots. Furthermore, coexistence of stationary robots restricts the grid to pure horizontal or vertical flows. This yields 2^H + 2^W + 2^{\gcd(H, W)} - 3 valid configurations. For general T, the torus decomposes into G_H x G_W independent subgrids where G_H = \gcd(H, T) and G_W = \gcd(W, T), each of size R_X = H / G_H and R_Y = W / G_W.

## 3. Step-by-Step Algorithm
1. 1. Compute G_H = gcd(H, T) and G_W = gcd(W, T).
2. 2. Set R_X = H / G_H, R_Y = W / G_W, and G = gcd(R_X, R_Y).
3. 3. Compute base = (2^{R_X} + 2^{R_Y} + 2^G - 3) mod (10^9 + 7).
4. 4. Exponent is E = (G_H * G_W) mod (10^9 + 6) by Fermat's Little Theorem.
5. 5. Compute base^E mod (10^9 + 7) and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(\log (\min(H, W, T)))`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <numeric>

using namespace std;

const long long MOD = 1000000007;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long H, W, T;
    if (!(cin >> H >> W >> T)) return 0;

    long long GH = gcd_ll(H, T);
    long long GW = gcd_ll(W, T);

    long long RX = H / GH;
    long long RY = W / GW;
    long long G = gcd_ll(RX, RY);

    long long t1 = power(2, RX, MOD);
    long long t2 = power(2, RY, MOD);
    long long t3 = power(2, G, MOD);

    long long base = (t1 + t2 + t3 - 3) % MOD;
    if (base < 0) base += MOD;

    long long total_instances = (GH % (MOD - 1) * (GW % (MOD - 1))) % (MOD - 1);

    long long ans;
    if (base == 0) {
        ans = (GH > 0 && GW > 0) ? 0 : 1;
    } else {
        ans = power(base, total_instances, MOD);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

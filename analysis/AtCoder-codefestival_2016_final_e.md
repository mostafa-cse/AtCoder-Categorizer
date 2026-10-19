# Problem Analysis: AtCoder-codefestival_2016_final_e — Cookies

**Problem ID**: `AtCoder-codefestival_2016_final_e`  
**Contest**: `codefestival_2016_final`  
**Rating / Difficulty**: 2700  
**URL**: https://atcoder.jp/contests/codefestival_2016_final/tasks/codefestival_2016_final_e  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_final_e]`  
**Category File**: [`../categories/basics/cookies_exponential_oven_greedy.md`](../categories/basics/cookies_exponential_oven_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Baking cookies where eating x cookies takes A seconds and multiplies the baking rate to x cookies/sec. If eating is performed k times, the baking durations c_1, ..., c_{k+1} must satisfy prod c_i >= N, minimizing (k * A + sum c_i). By AM-GM inequality, optimal integers c_i are as close as possible (each r or r+1 where r = floor(N^{1/m})), and m <= 40.

## 2. Core Observation & Invariant
Each baking period must be an integer number of seconds >= 2 (c_i = 1 is strictly suboptimal as it costs A seconds to multiply rate by 1). Thus 2^m <= prod c_i approx N <= 10^{12}, implying m <= 40 stages. For fixed m, the integers c_i partition into (m-j) copies of r and j copies of r+1, easily found by binary search.

## 3. Step-by-Step Algorithm
1. 1. Initialize best = N (m = 1, no eating).
2. 2. For m = 2 to 50:
3.    - Binary search for r = floor(N^{1/m}).
4.    - Iterate j from 0 to m to find the smallest j with r^{m-j} * (r+1)^j >= N.
5.    - Compute total time = (m - 1) * A + (m - j) * r + j * (r + 1) and update best.
6. 3. Print best.

## 4. Complexity Analysis
- **Time Complexity**: `O(log^2 N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

typedef __int128_t int128;

int128 int_pow(int128 base, int exp) {
    int128 res = 1;
    while (exp > 0) {
        if (exp % 2 == 1) res = res * base;
        base = base * base;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n_in, a_in;
    if (!(cin >> n_in >> a_in)) return 0;

    int128 N = n_in;
    int128 A = a_in;

    int128 ans = N; // m = 1 (no eating)

    for (int m = 2; m <= 50; ++m) {
        // Binary search for r = floor(N^(1/m))
        int128 low = 1, high = 2000000000LL;
        int128 r = 1;
        while (low <= high) {
            int128 mid = (low + high) / 2;
            // Check if mid^m <= N safely
            int128 p = 1;
            bool over = false;
            for (int step = 0; step < m; ++step) {
                if (N / mid < p) {
                    over = true;
                    break;
                }
                p *= mid;
            }
            if (!over && p <= N) {
                r = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        // Check j from 0 to m of factors being (r + 1) and (m - j) being r
        for (int j = 0; j <= m; ++j) {
            // Compute r^(m - j) * (r + 1)^j safely
            int128 prod = 1;
            bool over = false;
            for (int step = 0; step < m - j; ++step) {
                if (N / r < prod) {
                    over = true;
                    break;
                }
                prod *= r;
            }
            if (!over) {
                for (int step = 0; step < j; ++step) {
                    if (N / (r + 1) < prod) {
                        over = true;
                        break;
                    }
                    prod *= (r + 1);
                }
            }
            if (over || prod >= N) {
                int128 cost = (int128)(m - 1) * A + (int128)(m - j) * r + (int128)j * (r + 1);
                if (cost < ans) {
                    ans = cost;
                }
                break;
            }
        }
    }

    long long out = (long long)ans;
    cout << out << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

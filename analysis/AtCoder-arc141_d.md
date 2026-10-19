# Problem Analysis: AtCoder-arc141_d — D. Non-divisible Set

**Problem ID**: `AtCoder-arc141_d`  
**Contest**: `arc141`  
**Rating / Difficulty**: 2890  
**URL**: https://atcoder.jp/contests/arc141/tasks/arc141_d  
**VJudge Tag**: `[problem:AtCoder-arc141_d]`  
**Category File**: [`../categories/basics/dilworth_antichain_poset_sieve.md`](../categories/basics/dilworth_antichain_poset_sieve.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers from [1, 2M], determine for each element A_i whether there exists a subset of size M containing A_i such that no element divides another.

## 2. Core Observation & Invariant
Partition [1, 2M] into M chains according to their odd part o in {1, 3, ..., 2M - 1}. By Dilworth's Theorem, any antichain under divisibility contains at most one element per chain, so an antichain of size M must pick exactly one power of 2 for each odd part. Divisibility constraints between odd parts o and multiples (2k+1)o restrict the exponent of 2 to an interval [min_pow[o], max_pow[o]]. Sieve propagation yields valid intervals for all odd parts.

## 3. Step-by-Step Algorithm
1. 1. Express each A_i as 2^k * o.
2. 2. Initialize min_pow and max_pow bounds for each odd part.
3. 3. Propagate bounds downward (multiples constrain divisors) and upward (divisors constrain multiples) via sieve in O(M log M).
4. 4. For each element A_i = 2^k * o, check if min_pow[o] <= k <= max_pow[o]. Print Yes or No.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M + N)`
- **Space Complexity**: `O(M + N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    int max_odd = 2 * m;
    vector<vector<int>> powers(max_odd + 1);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        int val = a[i];
        int k = 0;
        while (val % 2 == 0) {
            val /= 2;
            k++;
        }
        powers[val].push_back(k);
    }

    bool has_all_odds = true;
    for (int o = 1; o <= max_odd; o += 2) {
        if (powers[o].empty()) {
            has_all_odds = false;
            break;
        }
        sort(powers[o].begin(), powers[o].end());
    }

    if (!has_all_odds) {
        for (int i = 0; i < n; ++i) {
            cout << "No\n";
        }
        return 0;
    }

    vector<int> min_pow(max_odd + 1, INF);
    for (int o = (max_odd % 2 == 1 ? max_odd : max_odd - 1); o >= 1; o -= 2) {
        int req = 0;
        for (int c = 3; c * o <= max_odd; c += 2) {
            int o2 = c * o;
            if (min_pow[o2] != INF) {
                req = max(req, min_pow[o2] + 1);
            }
        }
        auto it = lower_bound(powers[o].begin(), powers[o].end(), req);
        if (it != powers[o].end()) {
            min_pow[o] = *it;
        }
    }

    vector<int> max_pow(max_odd + 1, -1);
    vector<int> req_high(max_odd + 1, INF);

    for (int o = 1; o <= max_odd; o += 2) {
        auto it = upper_bound(powers[o].begin(), powers[o].end(), req_high[o]);
        if (it != powers[o].begin()) {
            --it;
            max_pow[o] = *it;
        }
        if (max_pow[o] != -1) {
            for (int c = 3; c * o <= max_odd; c += 2) {
                int o2 = c * o;
                req_high[o2] = min(req_high[o2], max_pow[o] - 1);
            }
        }
    }

    bool globally_possible = true;
    for (int o = 1; o <= max_odd; o += 2) {
        if (min_pow[o] == INF || max_pow[o] == -1 || min_pow[o] > max_pow[o]) {
            globally_possible = false;
            break;
        }
    }

    if (!globally_possible) {
        for (int i = 0; i < n; ++i) {
            cout << "No\n";
        }
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        int val = a[i];
        int k = 0;
        while (val % 2 == 0) {
            val /= 2;
            k++;
        }
        if (min_pow[val] <= k && k <= max_pow[val]) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

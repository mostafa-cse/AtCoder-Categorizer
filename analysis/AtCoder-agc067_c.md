# Problem Analysis: AtCoder-agc067_c — C - Divisibility Homomorphism

**Problem ID**: `AtCoder-agc067_c`  
**Contest**: `agc067`  
**Rating / Difficulty**: 2829  
**URL**: https://atcoder.jp/contests/agc067/tasks/agc067_c  
**VJudge Tag**: `[problem:AtCoder-agc067_c]`  
**Category File**: [`../categories/graph_theory/divisibility_preserving_sequence_multiplicative_lattice.md`](../categories/graph_theory/divisibility_preserving_sequence_multiplicative_lattice.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Partially Ordered Set (POSET)`  
- **Topic (Skill)**: `POSET ft Dilworth's and Mirsky's Theorem`  

---

## 1. Problem Statement & Key Idea
Determine whether a prefix sequence (A_1, ..., A_N) of positive integers can be extended to an infinite sequence satisfying a_n <= C * n and a_n | a_m <=> n | m.

## 2. Core Observation & Invariant
Divisibility preservation a_n | a_m <=> n | m defines a lattice embedding from the divisibility poset of integers into itself. The linear bound constraint a_n <= C * n forces the prime valuations v_p(a_x) to strictly respect the valuation layers of x: for every prime p <= N, if v_p(x) > v_p(y), then v_p(a_x) > v_p(a_y). Thus, each valuation layer {x : v_p(x) = k} must map to values with v_p(a_x) strictly greater than all values in layer k-1.

## 3. Step-by-Step Algorithm
1. 1. Verify that all elements in A are distinct.
2. 2. Check divisibility on all divisor pairs: for every x in 1..N and multiple y = 2x, 3x, ..., verify A_x | A_y.
3. 3. Sieve all primes p <= N.
4. 4. For each prime p, group indices x in 1..N by vx = v_p(x), and compute the minimum and maximum of vax = v_p(A_x) in each layer.
5. 5. Verify strict layer monotonicity: max v_p(A_x) in layer k must be strictly less than min v_p(A_y) in layer k+1.
6. 6. Output 'Yes' if all conditions hold, else 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + N pi(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

void solve() {
    int n;
    if (!(cin >> n)) return;

    vector<long long> a(n + 1);
    set<long long> distinct_check;
    bool all_distinct = true;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        if (distinct_check.count(a[i])) {
            all_distinct = false;
        }
        distinct_check.insert(a[i]);
    }

    if (!all_distinct) {
        cout << "No\n";
        return;
    }

    // Check divisibility: for all x | y, a[x] | a[y]
    for (int x = 1; x <= n; ++x) {
        long long ax = a[x];
        for (int y = 2 * x; y <= n; y += x) {
            if (a[y] % ax != 0) {
                cout << "No\n";
                return;
            }
        }
    }

    // Sieve primes up to n
    vector<bool> is_prime(n + 1, true);
    vector<int> primes;
    for (int p = 2; p <= n; ++p) {
        if (is_prime[p]) {
            primes.push_back(p);
            for (int j = 2 * p; j <= n; j += p) {
                is_prime[j] = false;
            }
        }
    }

    for (int p : primes) {
        // Find max v_p(a[x]) for layer k, and min v_p(a[x]) for layer k
        map<int, pair<int, int>> layers; // k -> {min_v, max_v}

        for (int x = 1; x <= n; ++x) {
            int vx = 0;
            int temp_x = x;
            while (temp_x % p == 0) {
                vx++;
                temp_x /= p;
            }

            int vax = 0;
            long long temp_ax = a[x];
            while (temp_ax % p == 0) {
                vax++;
                temp_ax /= p;
            }

            if (layers.find(vx) == layers.end()) {
                layers[vx] = {vax, vax};
            } else {
                layers[vx].first = min(layers[vx].first, vax);
                layers[vx].second = max(layers[vx].second, vax);
            }
        }

        // Check strictly increasing layers
        int prev_max = -1;
        for (auto const& [k, bounds] : layers) {
            if (bounds.first <= prev_max) {
                cout << "No\n";
                return;
            }
            prev_max = bounds.second;
        }
    }

    cout << "Yes\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

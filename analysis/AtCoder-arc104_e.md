# Problem Analysis: AtCoder-arc104_e — E - Random LIS

**Problem ID**: `AtCoder-arc104_e`  
**Contest**: `arc104`  
**Rating / Difficulty**: 2824  
**URL**: https://atcoder.jp/contests/arc104/tasks/arc104_e  
**VJudge Tag**: `[problem:AtCoder-arc104_e]`  
**Category File**: [`../categories/combinatorics/ordered_set_partition_random_lis_expectation.md`](../categories/combinatorics/ordered_set_partition_random_lis_expectation.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Partitions`  
- **Topic (Skill)**: `Partitions of a Set / Bell Number`  

---

## 1. Problem Statement & Key Idea
Given N <= 6 and upper bounds A_1, ..., A_N, random variables X_i are chosen uniformly from [1, A_i]. Compute the expected length of the Longest Increasing Subsequence (LIS) of X modulo 1000000007.

## 2. Core Observation & Invariant
For N <= 6, the relative order of elements X_1, ..., X_N is governed by one of the F(6) = 4683 ordered set partitions (weak orderings). For a fixed weak ordering, the LIS is deterministic. The number of integer assignments Y_1 < Y_2 < ... < Y_k satisfying Y_j <= min_{i in part j} A_i is computed using interval DP over the O(N) coordinate intervals formed by breakpoints {0} union {A_i}.

## 3. Step-by-Step Algorithm
1. 1. Generate all set partitions of {0..N-1} into k parts, and all k! orderings of parts to obtain all 4683 ordered set partitions.
2. 2. For each ordered partition, determine its deterministic LIS value and upper bounds U_rank = min_{r[i] == rank} A_i.
3. 3. Discretize upper bounds into O(N) intervals (coords[m], coords[m+1]] of length L.
4. 4. Run interval DP: dp[j] is the number of ways to assign the first j ranks into intervals, choosing c ranks in interval m with comb(L, c) ways.
5. 5. Multiply dp[k] by the LIS length, accumulate total LIS sum, and divide by prod(A_i) mod 1000000007.

## 4. Complexity Analysis
- **Time Complexity**: `O(F(N) * N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

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

long long nCr(long long n, int r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return num * modInverse(den) % MOD;
}

int calc_lis(const vector<int>& r) {
    vector<int> dp;
    for (int x : r) {
        auto it = lower_bound(dp.begin(), dp.end(), x);
        if (it == dp.end()) dp.push_back(x);
        else *it = x;
    }
    return (int)dp.size();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    long long total_space = 1;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_space = (total_space * a[i]) % MOD;
    }

    // Generate all ordered partitions
    // Recursive generator for set partitions into k parts
    vector<pair<vector<int>, int>> ordered_partitions;

    auto get_partitions = [&](auto& self, vector<int> elements) -> vector<vector<vector<int>>> {
        if (elements.empty()) return {{}};
        int first = elements[0];
        vector<int> rest(elements.begin() + 1, elements.end());
        auto sub = self(self, rest);
        vector<vector<vector<int>>> res;
        for (const auto& p : sub) {
            for (size_t i = 0; i < p.size(); ++i) {
                auto np = p;
                np[i].insert(np[i].begin(), first);
                res.push_back(np);
            }
            auto np = p;
            np.insert(np.begin(), {first});
            res.push_back(np);
        }
        return res;
    };

    vector<int> all_elems(n);
    iota(all_elems.begin(), all_elems.end(), 0);
    auto partitions = get_partitions(get_partitions, all_elems);

    for (auto& p : partitions) {
        int k = (int)p.size();
        vector<int> perm(k);
        iota(perm.begin(), perm.end(), 0);
        do {
            vector<int> r(n);
            for (int rank = 0; rank < k; ++rank) {
                for (int elem : p[perm[rank]]) {
                    r[elem] = rank;
                }
            }
            ordered_partitions.push_back({r, k});
        } while (next_permutation(perm.begin(), perm.end()));
    }

    // Coordinates and intervals
    vector<int> coords = {0};
    for (int x : a) coords.push_back(x);
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    struct Interval {
        int left, right, len;
    };
    vector<Interval> intervals;
    for (size_t i = 0; i + 1 < coords.size(); ++i) {
        intervals.push_back({coords[i] + 1, coords[i + 1], coords[i + 1] - coords[i]});
    }

    int num_intervals = (int)intervals.size();
    vector<vector<long long>> comb(num_intervals, vector<long long>(n + 1, 0));
    for (int m = 0; m < num_intervals; ++m) {
        for (int c = 0; c <= n; ++c) {
            comb[m][c] = nCr(intervals[m].len, c);
        }
    }

    long long total_lis_sum = 0;
    for (const auto& [r, k] : ordered_partitions) {
        int lis_val = calc_lis(r);
        vector<int> U(k, MOD);
        for (int i = 0; i < n; ++i) {
            U[r[i]] = min(U[r[i]], a[i]);
        }

        vector<long long> dp(k + 1, 0);
        dp[0] = 1;

        for (int m = 0; m < num_intervals; ++m) {
            vector<long long> next_dp = dp;
            int right = intervals[m].right;
            for (int j = 0; j < k; ++j) {
                if (!dp[j]) continue;
                for (int c = 1; j + c <= k; ++c) {
                    bool ok = true;
                    for (int t = 0; t < c; ++t) {
                        if (U[j + t] < right) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) {
                        next_dp[j + c] = (next_dp[j + c] + dp[j] * comb[m][c]) % MOD;
                    } else {
                        break;
                    }
                }
            }
            dp = move(next_dp);
        }

        long long ways = dp[k];
        total_lis_sum = (total_lis_sum + ways * lis_val) % MOD;
    }

    long long ans = total_lis_sum * modInverse(total_space) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

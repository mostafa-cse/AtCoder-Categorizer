# Problem Analysis: AtCoder-abc432_f — F. Candy Redistribution

**Problem ID**: `AtCoder-abc432_f`  
**Contest**: `abc432`  
**Rating / Difficulty**: 2273  
**URL**: https://atcoder.jp/contests/abc432/tasks/abc432_f  
**VJudge Tag**: `[problem:AtCoder-abc432_f]`  
**Category File**: [`../categories/dynamic_programming_dp/bitmask_dp_zero_sum_partition_reconstruction.md`](../categories/dynamic_programming_dp/bitmask_dp_zero_sum_partition_reconstruction.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
$N \le 20$ children have candies $A_i$. In one operation, child $x$ can give $z \le A_x$ candies to child $y$. Find the minimum operations to make all children have equal candies, and reconstruct the sequence of transfers.

## 2. Core Observation & Invariant
Let target $T = \frac{\sum A_i}{N}$ (if total not divisible by $N$, impossible). Define net deficits $D_i = A_i - T$. Any valid redistribution partitions children into disjoint zero-sum subsets $\sum_{i \in S_j} D_i = 0$. In each connected component $S_j$, $|S_j| - 1$ operations suffice to balance candies using a star graph rooted at an arbitrary child $r \in S_j$: children with excess first send to $r$, then $r$ sends to children with deficits. Total operations is $\sum (|S_j| - 1) = N - k$, where $k$ is the number of zero-sum subsets. Minimizing operations is equivalent to maximizing $k$. Since $N \le 20$, `dp[mask]` = max zero-sum subsets in `mask` can be computed in $O(N 2^N)$.

## 3. Step-by-Step Algorithm
1. Check if $\sum A_i$ is divisible by $N$; if not, output -1.
2. Compute $D_i = A_i - T$ for all $i$.
3. Compute `sum_d[mask]` and `dp[mask]` for $mask = 1 \dots 2^N - 1$: $dp[mask] = \max_{i \in mask} dp[mask \setminus \{i\}] + (sum_d[mask] == 0 ? 1 : 0)$.
4. Reconstruct disjoint components $C_1, \dots, C_k$ by backtracking from full mask $(1 \ll N) - 1$.
5. For each component $C$: pick root $r$; send candies from all children with $A_i > T$ to $r$; then send from $r$ to all children with $A_j < T$.
6. Output total operations and each triple $(x, y, z)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <tuple>
#include <cassert>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % n != 0) {
        cout << -1 << "\n";
        return 0;
    }

    long long target = total / n;
    vector<long long> d(n);
    for (int i = 0; i < n; ++i) {
        d[i] = a[i] - target;
    }

    int full = 1 << n;
    vector<int> dp(full, 0);
    vector<long long> sum_d(full, 0);

    for (int mask = 1; mask < full; ++mask) {
        int low = mask & -mask;
        int idx = __builtin_ctz(low);
        sum_d[mask] = sum_d[mask ^ low] + d[idx];

        int best = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                int val = dp[mask ^ (1 << i)];
                if (val > best) best = val;
            }
        }
        if (sum_d[mask] == 0) {
            dp[mask] = best + 1;
        } else {
            dp[mask] = best;
        }
    }

    vector<int> components;
    int rem = full - 1;

    while (rem > 0) {
        int low_bit = rem & -rem;
        int rest = rem ^ low_bit;
        bool found = false;

        // Iterate submasks of rest, and include low_bit
        for (int sub = rest; ; sub = (sub - 1) & rest) {
            int cand = sub | low_bit;
            if (sum_d[cand] == 0 && dp[rem ^ cand] == dp[rem] - 1) {
                components.push_back(cand);
                rem ^= cand;
                found = true;
                break;
            }
            if (sub == 0) break;
        }
        if (!found) {
            components.push_back(rem);
            break;
        }
    }

    vector<long long> cur_a = a;
    vector<tuple<int, int, long long>> ops;

    for (int comp : components) {
        vector<int> nodes;
        for (int i = 0; i < n; ++i) {
            if ((comp >> i) & 1) nodes.push_back(i);
        }
        if (nodes.size() <= 1) continue;
        int r = nodes[0];

        // 1: nodes with excess give to r
        for (size_t k = 1; k < nodes.size(); ++k) {
            int i = nodes[k];
            if (cur_a[i] > target) {
                long long z = cur_a[i] - target;
                ops.push_back({i + 1, r + 1, z});
                cur_a[i] -= z;
                cur_a[r] += z;
            }
        }

        // 2: r gives to nodes with deficit
        for (size_t k = 1; k < nodes.size(); ++k) {
            int j = nodes[k];
            if (cur_a[j] < target) {
                long long z = target - cur_a[j];
                ops.push_back({r + 1, j + 1, z});
                cur_a[r] -= z;
                cur_a[j] += z;
            }
        }
    }

    cout << ops.size() << "\n";
    for (auto [x, y, z] : ops) {
        cout << x << " " << y << " " << z << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

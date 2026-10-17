# Problem Analysis: AtCoder-abc143_f — F. Distinct Numbers

**Problem ID**: `AtCoder-abc143_f`  
**Contest**: `abc143`  
**Rating / Difficulty**: 2277  
**URL**: https://atcoder.jp/contests/abc143/tasks/abc143_f  
**VJudge Tag**: `[problem:AtCoder-abc143_f]`  
**Category File**: [`../categories/basics/binary_search_frequency_capped_subset_partition.md`](../categories/basics/binary_search_frequency_capped_subset_partition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Given $N$ integers, for each $K = 1, \dots, N$, find the maximum number of operations possible where each operation chooses $K$ pairwise distinct integers and removes them.

## 2. Core Observation & Invariant
$X$ operations choosing $K$ distinct elements are feasible if and only if the total capped count $\sum_i \min(c_i, X) \ge K \cdot X$. Inverting this relationship allows determining the maximum $X$ for each $K$ via binary search or suffix-maximum sweep over $K \le \lfloor S(X) / X \rfloor$.

## 3. Step-by-Step Algorithm
1. 1. Let $c_1, \dots, c_m$ be the frequencies of each distinct number in the input. In $X$ operations of size $K$, each distinct number can be chosen at most once per operation, hence at most $\min(c_i, X)$ times in total.\n2. By the Gale-Ryser / Hajnal-Szemerédi theorem for bipartite degree sequences, the condition $\sum_i \min(c_i, X) \ge K \cdot X$ is both necessary and sufficient to form $X$ subsets of size $K$ with distinct elements.\n3. Let $S(X) = \sum_i \min(c_i, X)$. By precomputing the frequency distribution of counts using prefix sums, $S(X)$ can be computed in $O(1)$ for each $X \in [1, N]$.\n4. For each $X$, the maximum subset size for which $X$ operations is possible is $K_{max}(X) = \lfloor S(X) / X \rfloor$. Setting $\text{ans}[K_{max}(X)] = \max(\text{ans}[K_{max}(X)], X)$ and taking a backward suffix maximum sweep $\text{ans}[K] = \max(\text{ans}[K], \text{ans}[K+1])$ yields the answer for all $K \in [1, N]$ in $O(N)$ total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> freq(n + 1, 0);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        freq[a]++;
    }

    vector<int> count_of_freq(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        if (freq[i] > 0) {
            count_of_freq[freq[i]]++;
        }
    }

    vector<long long> sum_c(n + 1, 0);
    vector<long long> count_c(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        sum_c[v] = sum_c[v - 1] + 1LL * v * count_of_freq[v];
        count_c[v] = count_c[v - 1] + count_of_freq[v];
    }

    long long total_elements = count_c[n];

    vector<int> ans(n + 2, 0);
    for (int x = 1; x <= n; x++) {
        long long s_x = sum_c[x] + 1LL * x * (total_elements - count_c[x]);
        int k = s_x / x;
        if (k > n) k = n;
        ans[k] = max(ans[k], x);
    }

    for (int k = n; k >= 1; k--) {
        ans[k] = max(ans[k], ans[k + 1]);
    }

    for (int k = 1; k <= n; k++) {
        cout << ans[k] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

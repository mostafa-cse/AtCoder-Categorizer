# Problem Analysis: AtCoder-arc106_f — F - Figures

**Problem ID**: `AtCoder-arc106_f`  
**Contest**: `arc106`  
**Rating / Difficulty**: 2754  
**URL**: https://atcoder.jp/contests/arc106/tasks/arc106_f  
**VJudge Tag**: `[problem:AtCoder-arc106_f]`  
**Category File**: [`../categories/graph_theory/figures_tree_prufer_generating_function.md`](../categories/graph_theory/figures_tree_prufer_generating_function.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Prufer Code`  

---

## 1. Problem Statement & Key Idea
Given N parts where part i has d_i holes, we want to connect them using N-1 components to form a connected tree. Each component connects two distinct holes in different parts. Find the number of valid complete figures modulo 998244353.

## 2. Core Observation & Invariant
By Cayley's tree formula via Prüfer sequences, the number of trees with specified vertex degrees deg_1, ..., deg_N is (N - 2)! / prod (deg_i - 1)!. For part i with d_i available holes, choosing deg_i holes has d_i * (d_i - 1) * ... * (d_i - deg_i + 1) = d_i! / (d_i - deg_i)! ways. Multiplying and summing over all degree sequences sum deg_i = 2N - 2 yields the closed form: prod_{i=1}^N d_i * (sum d_i - N)_{N-2} * (N - 2)! / (N - 2)! = (prod d_i) * (S)_{N-2} mod 998244353, where S = (sum d_i) - N and (S)_k = S * (S - 1) * ... * (S - k + 1) is the falling factorial.

## 3. Step-by-Step Algorithm
1. 1. Compute the product P = prod_{i=1}^N d_i mod 998244353.
2. 2. Compute the sum S = (sum_{i=1}^N d_i - N) mod 998244353.
3. 3. Compute the falling factorial S * (S - 1) * ... * (S - N + 3) mod 998244353.
4. 4. Multiply P by the falling factorial to obtain the final answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> d(n);
    long long prod_d = 1;
    long long sum_d = 0;
    for (int i = 0; i < n; i++) {
        cin >> d[i];
        prod_d = (prod_d * (d[i] % MOD)) % MOD;
        sum_d += d[i];
    }

    long long S = sum_d - n;
    if (S < n - 2) {
        cout << 0 << "\n";
        return 0;
    }

    long long fall = 1;
    for (int i = 0; i < n - 2; i++) {
        long long term = (S - i) % MOD;
        fall = (fall * term) % MOD;
    }

    long long ans = (prod_d * fall) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

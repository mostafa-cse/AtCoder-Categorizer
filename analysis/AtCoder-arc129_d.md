# Problem Analysis: AtCoder-arc129_d — D. -1 +2 -1

**Problem ID**: `AtCoder-arc129_d`  
**Contest**: `arc129`  
**Rating / Difficulty**: 2300  
**URL**: https://atcoder.jp/contests/arc129/tasks/arc129_d  
**VJudge Tag**: `[problem:AtCoder-arc129_d]`  
**Category File**: [`../categories/basics/difference_array_second_differences_circular.md`](../categories/basics/difference_array_second_differences_circular.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `More Techniques`  
- **Topic (Skill)**: `Difference Array`  

---

## 1. Problem Statement & Key Idea
Given a circular array $A_1, \dots, A_N$ of sum 0, determine the minimum number of operations $(-1, +2, -1)$ at positions $(i-1, i, i+1)$ needed to reduce all elements to 0, or report impossible.

## 2. Core Observation & Invariant
Applying the operation $(-1, 2, -1)$ at position $i$ corresponds to $A_{i-1} \leftarrow A_{i-1} - 1, A_i \leftarrow A_i + 2, A_{i+1} \leftarrow A_{i+1} - 1$. In terms of operation counts $x_i$, this gives $A_i = 2x_i - x_{i-1} - x_{i+1} = -(d_{i+1} - d_i)$ where $d_i = x_i - x_{i-1}$. A valid solution exists iff $\sum A_i = 0$ and the first prefix sum of $A$ sums to $0 \pmod N$.

## 3. Step-by-Step Algorithm
1. 1. Let $x_i \ge 0$ be the number of times operation $i$ is performed. The final state condition is $A_i = -(x_{i+1} - 2x_i + x_{i-1})$ for all $1 \le i \le N$ (with indices modulo $N$).
2. 2. Notice that the sum $\sum A_i = 0$ must hold since each operation changes the sum by $0$. If $\sum A_i \ne 0$, output -1.
3. 3. Let $d_i = x_i - x_{i-1}$. Then $A_{i-1} = -(d_i - d_{i-1}) = d_{i-1} - d_i \implies d_i = d_1 + P_{i-1}$ where $P_k = -\sum_{j=1}^k A_j$.
4. 4. Because the array is circular, $\sum_{i=1}^N d_i = \sum (x_i - x_{i-1}) = 0$. This forces $N d_1 + \sum_{i=1}^N P_{i-1} = 0$, uniquely determining $d_1 = -(\sum P_{i-1}) / N$.
5.    - If $\sum P_{i-1}$ is not divisible by $N$, no integer solution exists $\implies$ output -1.
6. 5. Once all $d_i$ are fixed, $x_i = x_1 + Q_i$ where $Q_i = \sum_{j=2}^i d_j$. To minimize $\sum x_i$ subject to $x_i \ge 0$ for all $i$, we choose $x_1 = \max(0, -\min_i Q_i)$.
7. 6. Output the total operations $\sum_{i=1}^N x_i$. Total complexity is $O(N)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    long long sum_A = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        sum_A += A[i];
    }

    if (sum_A != 0) {
        cout << -1 << "\n";
        return 0;
    }

    vector<long long> P(N, 0);
    for (int i = 1; i < N; ++i) {
        P[i] = P[i - 1] + A[i - 1];
    }

    long long sum_P = 0;
    for (int i = 0; i < N; ++i) {
        sum_P += P[i];
    }

    if (sum_P % N != 0) {
        cout << -1 << "\n";
        return 0;
    }

    long long d1 = -(sum_P / N);
    vector<long long> d(N);
    d[0] = d1;
    for (int i = 1; i < N; ++i) {
        d[i] = d1 + P[i];
    }

    vector<long long> Q(N, 0);
    for (int i = 1; i < N; ++i) {
        Q[i] = Q[i - 1] + d[i];
    }

    long long min_Q = 0;
    for (int i = 0; i < N; ++i) {
        min_Q = min(min_Q, Q[i]);
    }

    long long x1 = (min_Q < 0 ? -min_Q : 0);
    long long total_ops = 0;
    for (int i = 0; i < N; ++i) {
        total_ops += (x1 + Q[i]);
    }

    cout << total_ops << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

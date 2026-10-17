# Problem Analysis: AtCoder-arc159_c — C. Permutation Addition

**Problem ID**: `AtCoder-arc159_c`  
**Contest**: `arc159`  
**Rating / Difficulty**: 2304  
**URL**: https://atcoder.jp/contests/arc159/tasks/arc159_c  
**VJudge Tag**: `[problem:AtCoder-arc159_c]`  
**Category File**: [`../categories/basics/complementary_permutation_pair_transfer.md`](../categories/basics/complementary_permutation_pair_transfer.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given array $A$ of length $N \le 50$, repeatedly add permutations of $(1, \dots, N)$ in at most $10^4$ operations to equalize all elements, or determine impossible.

## 2. Core Observation & Invariant
Adding a permutation adds $N(N+1)/2$ to the total sum. A uniform state is achievable if and only if $\sum A_i \equiv 0 \pmod N$ for odd $N$, or $\sum A_i \in \{0, N/2\} \pmod N$ for even $N$.

## 3. Step-by-Step Algorithm
1. If $N$ is even and $\sum A_i \equiv N/2 \pmod N$, apply one standard permutation $(1, \dots, N)$ to reach $\sum A_i \equiv 0 \pmod N$.
2. Construct a pair of complementary permutations $(P_1, P_2)$ that transfers exactly 1 unit from the current maximum element index $u$ to the minimum element index $v$ while adding $N+1$ uniformly to all other positions.
3. Repeatedly transfer unit mass until all elements become equal, requiring at most $2 \times 2500 \le 5000$ operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sum |A_i|)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> A(N);
    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        sum += A[i];
    }

    vector<vector<int>> ops;

    long long rem = (sum % N + N) % N;
    if (N % 2 != 0) {
        if (rem != 0) {
            cout << "No\n";
            return 0;
        }
    } else {
        if (rem != 0 && rem != N / 2) {
            cout << "No\n";
            return 0;
        }
        if (rem == N / 2) {
            vector<int> p(N);
            for (int i = 0; i < N; ++i) p[i] = i + 1;
            ops.push_back(p);
            for (int i = 0; i < N; ++i) A[i] += p[i];
        }
    }

    auto transfer = [&](int u, int v) {
        vector<int> p1(N), p2(N);
        p1[u] = 1; p2[u] = N - 1;
        p1[v] = 2; p2[v] = N;

        int cur_val1 = 3;
        for (int i = 0; i < N; ++i) {
            if (i == u || i == v) continue;
            p1[i] = cur_val1;
            p2[i] = N + 1 - cur_val1;
            cur_val1++;
        }
        ops.push_back(p1);
        ops.push_back(p2);
        for (int i = 0; i < N; ++i) {
            A[i] += p1[i] + p2[i];
        }
    };

    while (true) {
        long long mn = *min_element(A.begin(), A.end());
        long long mx = *max_element(A.begin(), A.end());
        if (mn == mx) break;

        int u = -1, v = -1;
        for (int i = 0; i < N; ++i) {
            if (A[i] == mx) u = i;
            if (A[i] == mn) v = i;
        }
        transfer(u, v);
    }

    cout << "Yes\n";
    cout << ops.size() << "\n";
    for (const auto& p : ops) {
        for (int i = 0; i < N; ++i) {
            cout << p[i] << (i == N - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

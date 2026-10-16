# Problem Analysis: AtCoder-abc128_d — equeue

**Problem ID**: `AtCoder-abc128_d`  
**Contest**: `abc128`  
**Rating / Difficulty**: 1354  
**URL**: https://atcoder.jp/contests/abc128/tasks/abc128_d  
**VJudge Tag**: `[problem:AtCoder-abc128_d]`  
**Category File**: [`../categories/basics/deque_brute_force_priority_queue.md`](../categories/basics/deque_brute_force_priority_queue.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `Double-Ended Queue Brute Force Insertion/Deletion with Priority Queue`  

---

## 1. Problem Statement & Key Idea
N jewels in a row (values V_1..V_N, can be negative). You can perform K operations: pull from left, pull from right, or put a jewel back into the row. Maximize jewel value in hand.

**Key Idea**: Any valid sequence of operations pulls A jewels from the left and B jewels from the right (A + B <= min(N, K)), then throws back at most C = K - (A + B) negative jewels.

## 2. Core Observation & Invariant
Because N <= 50 and K <= 100, we can iterate over all choices of A and B with A + B <= min(N, K). Collect all jewels pulled into a list, sort them ascending, and discard the most negative jewels up to min(A + B, K - (A + B)).

## 3. Step-by-Step Algorithm
1. Initialize max_value = 0.
2. For A from 0 to min(N, K):
3.   For B from 0 to min(N - A, K - A):
4.     Collect jewels: V[0..A-1] and V[N-B..N-1].
5.     Sort jewels ascending.
6.     Throw back negative jewels up to K - (A + B) times.
7.     Sum remaining jewels; max_value = max(max_value, sum).
8. Print max_value.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * N log N) <= 50^3 * 6 = 7.5 * 10^5 operations`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    long long max_sum = 0;

    for (int a = 0; a <= min(n, k); ++a) {
        for (int b = 0; a + b <= min(n, k); ++b) {
            vector<long long> pulled;
            for (int i = 0; i < a; ++i) pulled.push_back(v[i]);
            for (int i = 0; i < b; ++i) pulled.push_back(v[n - 1 - i]);

            sort(pulled.begin(), pulled.end());

            int drop_budget = k - (a + b);
            long long current_sum = 0;

            for (size_t i = 0; i < pulled.size(); ++i) {
                if (pulled[i] < 0 && drop_budget > 0) {
                    drop_budget--;
                } else {
                    current_sum += pulled[i];
                }
            }

            max_sum = max(max_sum, current_sum);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Separating pull operations from discard operations in deque optimization.
- **Reusable Pattern**: `Pull A left, B right, drop worst elements using remaining budget K - A - B.`

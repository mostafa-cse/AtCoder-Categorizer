# Problem Analysis: AtCoder-arc051_c — 掛け算

**Problem ID**: `AtCoder-arc051_c`  
**Contest**: `arc051`  
**Rating / Difficulty**: 1898  
**URL**: https://atcoder.jp/contests/arc051/tasks/arc051_c  
**VJudge Tag**: `[problem:AtCoder-arc051_c]`  
**Category File**: [`../categories/basics/octave_saturation_round_robin_exponentiation.md`](../categories/basics/octave_saturation_round_robin_exponentiation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Priority Queue / Math`  
- **Topic (Skill)**: `Octave Saturation / Min-Heap Transition to Modular Round-Robin Exponentiation`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers. Perform B operations: in each operation, multiply the current minimum element by multiplier A. Output the final array in sorted order, modulo 10^9 + 7.

**Key Insight**: If multiplier A == 1, array never changes. If A > 1: using a min-heap, repeatedly multiply the minimum element by A until all elements are within the same 'octave' [max, max * A) or operations run out. Once saturated, operations cycle round-robin across all N elements.

## 2. Core Observation & Invariant
Remaining operations rem = B - used can be applied via modular exponentiation: each element is multiplied by A^{floor(rem / N)}, and the rem % N smallest elements receive one extra factor of A.

## 3. Step-by-Step Algorithm
1. If A == 1: sort and print.
2. Insert all elements into min-heap.
3. While B > 0 and min_val * A < max_val:
4.   pop min_val, push min_val * A, B--.
5. // All elements are in same octave
6. Sort the N elements in ascending order.
7. q = B / N, r = B % N.
8. For i = 0 to N - 1:
9.   power_exp = q + (i < r ? 1 : 0);
10.   final_val[i] = element * power(A, power_exp) % MOD.
11. Print final elements starting from index r (since the r smallest were multiplied and moved up).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max_val) + N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long A, B;
    if (!(cin >> n >> A >> B)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    if (A == 1) {
        sort(a.begin(), a.end());
        for (int i = 0; i < n; ++i) {
            cout << a[i] % MOD << "\n";
        }
        return 0;
    }

    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        pq.push(a[i]);
        max_val = max(max_val, a[i]);
    }

    while (B > 0 && pq.top() * A <= max_val) {
        long long mn = pq.top();
        pq.pop();
        pq.push(mn * A);
        max_val = max(max_val, mn * A);
        B--;
    }

    vector<long long> elems;
    while (!pq.empty()) {
        elems.push_back(pq.top());
        pq.pop();
    }

    long long q = B / n;
    long long r = B % n;

    vector<long long> ans(n);
    for (int i = 0; i < n; ++i) {
        long long exp = q + (i < r ? 1 : 0);
        ans[i] = (elems[i] % MOD) * power(A, exp) % MOD;
    }

    // Output starting from index r to maintain sorted order
    for (int i = 0; i < n; ++i) {
        int idx = (r + i) % n;
        cout << ans[idx] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Transitioning from greedy priority queue simulation to closed-form round-robin modular exponentiation.
- **Reusable Pattern**: `Octave Saturation Exponentiation: Simulate min-heap until max/min < A, then apply round-robin modular powers.`

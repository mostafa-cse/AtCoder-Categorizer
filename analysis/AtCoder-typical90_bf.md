# Problem Analysis: AtCoder-typical90_bf — Original Calculator

**Problem ID**: `AtCoder-typical90_bf`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 058)  
**Rating / Difficulty**: 1250 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bf  
**VJudge Tag**: `[problem:AtCoder-typical90_bf]`  
**Category File**: [`../categories/graph_theory/functional_graphs.md`](../categories/graph_theory/functional_graphs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Functional Graphs`  
- **Topic (Skill)**: `Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)`  

---

## 1. Problem Statement & Key Idea
A calculator displays integer x (0 <= x < 10^5). Pressing button replaces x with (x + digit_sum(x)) mod 10^5. Find display value after K presses (K <= 10^18).

**Core Idea**: The transition x -> f(x) forms a functional graph with 10^5 vertices where every vertex has out-degree 1. Finite functional graphs always lead into a cycle.

## 2. Core Observation & Invariant
Track visited step indices step[x]. When a state repeats, the path consists of a pre-period tail of length t and a cycle of length c. For K >= t, remaining steps modulo c gives the exact state in O(MOD) time.

## 3. Step-by-Step Algorithm
1. Maintain pos[x] = -1.
2. Simulate step by step, storing history array.
3. If state repeats at step i with previous visit pos[x]: cycle_len = i - pos[x], tail_len = pos[x].
4. If K < tail_len: return history[K].
5. Else: return history[tail_len + (K - tail_len) % cycle_len].

## 4. Complexity Analysis
Time: O(M) where M = 10^5, Space: O(M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 100000;

int next_val(int x) {
    int sum = 0, temp = x;
    while (temp > 0) {
        sum += temp % 10;
        temp /= 10;
    }
    return (x + sum) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<int> step(MOD, -1);
    vector<int> history;

    int cur = n;
    while (step[cur] == -1 && (long long)history.size() < k) {
        step[cur] = history.size();
        history.push_back(cur);
        cur = next_val(cur);
    }

    if ((long long)history.size() == k) {
        cout << cur << "\n";
        return 0;
    }

    int tail = step[cur];
    int cycle_len = (int)history.size() - tail;
    long long rem = (k - tail) % cycle_len;

    cout << history[tail + rem] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Cycle detection on functional graph with periodic loop index calculation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Functional graphs, tail-and-cycle decomposition (Floyd's/Brent's idea), and large step exponentiation via modulo.
- **Reusable Pattern**: `Functional Graph Cycle Detection.`

---
Back to [Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)](../categories/graph_theory/functional_graphs.md) | [Categories Directory](../categories/README.md)
# Problem Analysis: AtCoder-abc030_d — Strange Dictionary

**Problem ID**: `AtCoder-abc030_d`  
**Contest**: `abc030`  
**Rating / Difficulty**: 1586  
**URL**: https://atcoder.jp/contests/abc030/tasks/abc030_d  
**VJudge Tag**: `[problem:AtCoder-abc030_d]`  
**Category File**: [`../categories/basics/functional_graph_large_k_modulo.md`](../categories/basics/functional_graph_large_k_modulo.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Functional Graphs`  
- **Topic (Skill)**: `Functional Graph Cycle Detection with Large K (K up to 10^100000)`  

---

## 1. Problem Statement & Key Idea
A functional graph with N words. Word i points to word b_i. Start at word a and follow pointers K times, where K is a huge integer with up to 100,000 digits. Find the word reached after K steps.

**Key Insight**: The path from a eventually enters a cycle of length L_cycle after a tail of length L_tail <= N. If K <= L_tail, simulate directly. Otherwise, compute (K - L_tail) % L_cycle using big-integer modular reduction and take that many steps along the cycle.

## 2. Core Observation & Invariant
Because N <= 10^5, the tail and cycle are both <= 10^5 steps. A single traversal finds the cycle. Reducing string K modulo L_cycle takes O(|K|) time.

## 3. Step-by-Step Algorithm
1. Trace path from start a, recording visit step in visited[u].
2. When reaching an already visited node u:
3.   L_tail = visited[u], L_cycle = current_step - visited[u].
4. If |K| is small and K <= L_tail, output node at step K.
5. Otherwise, compute rem = (K - L_tail) % L_cycle by reading digits of K.
6. Take rem steps starting from node u along the cycle.
7. Print final node.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + |K|)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    string K_str;
    if (!(cin >> n >> a >> K_str)) return 0;

    vector<int> b(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
    }

    vector<int> path;
    vector<int> step_at(n + 1, -1);

    int curr = a;
    int step = 0;

    while (step_at[curr] == -1) {
        step_at[curr] = step++;
        path.push_back(curr);
        curr = b[curr];
    }

    int tail_len = step_at[curr];
    int cycle_len = step - tail_len;

    // Check if K fits in simple integer <= tail_len
    if (K_str.size() <= 7) {
        long long k_val = stoll(K_str);
        if (k_val <= tail_len) {
            cout << path[k_val] << "\n";
            return 0;
        }
    }

    // Compute (K - tail_len) % cycle_len
    long long rem = 0;
    for (char c : K_str) {
        rem = (rem * 10 + (c - '0')) % cycle_len;
    }

    rem = (rem - (tail_len % cycle_len) + cycle_len) % cycle_len;

    int ans = path[tail_len + rem];
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Functional graph periodic cycle detection combined with big-integer modular arithmetic.
- **Reusable Pattern**: `Huge K on Functional Graph: find tail and cycle, compute (BigInt(K) - tail) % cycle.`

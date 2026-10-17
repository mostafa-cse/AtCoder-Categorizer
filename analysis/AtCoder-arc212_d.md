# Problem Analysis: AtCoder-arc212_d — Two Rooms

**Problem ID**: `AtCoder-arc212_d`  
**Contest**: `arc212`  
**Rating / Difficulty**: 2018  
**URL**: https://atcoder.jp/contests/arc212/tasks/arc212_d  
**VJudge Tag**: `[problem:AtCoder-arc212_d]`  
**Category File**: [`../categories/basics/local_search_potential_ascent_two_partition.md`](../categories/basics/local_search_potential_ascent_two_partition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Local Search Potential Ascent for Two-Partition Intimacy Maximization`  

---

## 1. Problem Statement & Key Idea
N people have pairwise intimacy values A_{i, j} (symmetric, A_{i, i} = 0). Assign each person to room X or room Y such that every person's total intimacy with roommates is >= their total intimacy with people in the other room. Output any valid assignment.

**Key Idea**: Represent room assignment by s_i in {-1, +1}. The potential function Phi = sum_{i < j} A_{i, j} * s_i * s_j measures total same-room intimacy minus different-room intimacy. A person i is unsatisfied iff sum_{j != i} A_{i, j} * s_i * s_j < 0. Flipping s_i <- -s_i strictly increases Phi by -2 * sum_{j != i} A_{i, j} * s_i * s_j >= 2. Because Phi is bounded by sum |A_{i, j}|, a simple local search (iteratively flipping any unsatisfied person) is guaranteed to terminate at a valid state in at most O(N^2 * max |A|) steps.

## 2. Core Observation & Invariant
Local search with monotonic potential energy ascent guarantees reaching a Nash equilibrium where every individual condition is satisfied.

## 3. Step-by-Step Algorithm
1. Initialize all people in room X: s_i = +1 for all i from 1 to N.
2. Loop:
3.   Find any person i where sum_{j != i} A_{i, j} * s_i * s_j < 0.
4.   If no such person exists: break (valid state reached).
5.   Flip s_i <- -s_i.
6. Construct result string: 'X' if s_i == +1 else 'Y'.
7. Print result string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 * max |A|)`
- **Space Complexity**: `O(N^2)`

## 5. Core Algorithmic Skill & Learning Takeaway
Potential function monovariant ascent and local search convergence for partition satisfaction.

**Reusable Pattern**: Local Search Potential Flip: Moving an unsatisfied node to the opposite partition strictly increases global potential until all local constraints hold.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }

    // s[i] in {+1, -1}
    vector<int> s(n, 1);

    while (true) {
        bool changed = false;
        for (int i = 0; i < n; ++i) {
            int current_contribution = 0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                current_contribution += a[i][j] * s[i] * s[j];
            }
            if (current_contribution < 0) {
                s[i] = -s[i];
                changed = true;
                break;
            }
        }
        if (!changed) break;
    }

    string ans = "";
    for (int i = 0; i < n; ++i) {
        ans += (s[i] == 1 ? 'X' : 'Y');
    }
    cout << ans << "\n";

    return 0;
}
```

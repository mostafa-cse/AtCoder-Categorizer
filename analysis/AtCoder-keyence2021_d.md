# Problem Analysis: AtCoder-keyence2021_d — Choosing Up Sides

**Problem ID**: `AtCoder-keyence2021_d`  
**Contest**: `keyence2021`  
**Rating / Difficulty**: 2115  
**URL**: https://atcoder.jp/contests/keyence2021/tasks/keyence2021_d  
**VJudge Tag**: `[problem:AtCoder-keyence2021_d]`  
**Category File**: [`../categories/basics/hadamard_matrix_sylvester_construction.md`](../categories/basics/hadamard_matrix_sylvester_construction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
For 2^N people and 2^N - 1 rounds, partition people into two teams of size 2^{N-1} each round such that every pair of people are on the same team in exactly 2^{N-2} - 1 rounds.

**Key Insight**: The condition that all pairs of columns have the identical dot product across team indicators (+1 and -1) is uniquely satisfied by the construction of a Hadamard Matrix of order 2^N. Using Sylvester's recursive Kronecker product construction, H[r][c] = (-1)^{popcount(r & c)}. Row 0 consists entirely of 1s (all on team A). The remaining 2^N - 1 rows have exactly equal counts of +1 ('A') and -1 ('B') and their column dot products are orthogonal, giving equal pairwise shared rounds for all pairs of people.

## 2. Core Observation & Invariant
Pairwise balanced tournament rounds correspond exactly to the orthogonal rows of a Sylvester Hadamard Matrix.

## 3. Step-by-Step Algorithm
1. Set total_rounds = 2^N - 1, total_people = 2^N.
2. For row r from 1 to 2^N - 1:
3.   Construct string of length 2^N where character c is 'A' if popcount(r & c) is even, and 'B' if odd.
4. Output total_rounds followed by the team assignment strings.

## 4. Complexity Analysis
- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(2^N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Sylvester Hadamard matrix construction for balanced bipartite orthogonal tournament pairings.
- **Reusable Pattern**: Generating balanced pairwise tournament designs using bitwise AND popcount parity.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
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

    int total_people = 1 << n;
    int total_rounds = (1 << n) - 1;

    cout << total_rounds << "\n";
    for (int r = 1; r < total_people; ++r) {
        string s = "";
        for (int c = 0; c < total_people; ++c) {
            int sign = __builtin_popcount(r & c) % 2;
            s += (sign == 0 ? 'A' : 'B');
        }
        cout << s << "\n";
    }

    return 0;
}
```

# Problem Analysis: AtCoder-arc041_c — ウサギ跳び

**Problem ID**: `AtCoder-arc041_c`  
**Contest**: `arc041`  
**Rating / Difficulty**: 1808  
**URL**: https://atcoder.jp/contests/arc041/tasks/arc041_c  
**VJudge Tag**: `[problem:AtCoder-arc041_c]`  
**Category File**: [`../categories/basics/converging_clusters_greedy_compression.md`](../categories/basics/converging_clusters_greedy_compression.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `1D Compression Invariant on Converging Directed Clusters`  

---

## 1. Problem Statement & Key Idea
N rabbits on a 1D line of length L. Rabbit i starts at x_i and faces 'L' or 'R'. A rabbit can jump over any contiguous block of rabbits to the immediately adjacent empty space in its direction. Maximize total jumps.

**Key Insight**: Rabbits decompose into independent converging blocks of 'R' followed by 'L'. Each 'R...RL...L' cluster will compress together. The gap between the rightmost R and leftmost L is traversed by either all R rabbits jumping right, or all L rabbits jumping left.

## 2. Core Observation & Invariant
Greedy choice: let cnt_R be the number of R rabbits and cnt_L be the number of L rabbits in the pair. The gap size is multiplied by max(cnt_R, cnt_L). Internal compression jumps within each block are fixed and invariant.

## 3. Step-by-Step Algorithm
1. Parse consecutive blocks of R rabbits and L rabbits.
2. Pair each R block with the immediately following L block.
3. Add fixed internal compression jumps for both blocks.
4. Let gap = x_{first_L} - x_{last_R} - 1.
5. Add gap * max(cnt_R, cnt_L) to total.
6. Handle edge boundary gaps at coordinates 1 and L.
7. Print total jumps.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Rabbit {
    long long x;
    char dir;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<Rabbit> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i].x >> r[i].dir;
    }

    long long ans = 0;
    int idx = 0;

    while (idx < n) {
        vector<long long> R_pos, L_pos;
        while (idx < n && r[idx].dir == 'R') {
            R_pos.push_back(r[idx++].x);
        }
        while (idx < n && r[idx].dir == 'L') {
            L_pos.push_back(r[idx++].x);
        }

        if (R_pos.empty() && !L_pos.empty()) {
            for (int i = 0; i < (int)L_pos.size(); ++i) {
                ans += (L_pos[i] - (i + 1));
            }
        } else if (!R_pos.empty() && L_pos.empty()) {
            int k = R_pos.size();
            for (int i = 0; i < k; ++i) {
                ans += ((L - k + 1 + i) - R_pos[i]);
            }
        } else {
            int k_r = R_pos.size();
            int k_l = L_pos.size();

            for (int i = 0; i < k_r; ++i) {
                ans += (R_pos.back() - (k_r - 1 - i) - R_pos[i]);
            }
            for (int i = 0; i < k_l; ++i) {
                ans += (L_pos[i] - (L_pos.front() + i));
            }

            long long gap = L_pos.front() - R_pos.back() - 1;
            ans += gap * max(k_r, k_l);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy assignment of shared boundary intervals to the larger of two converging clusters.
- **Reusable Pattern**: `Converging Cluster Invariant: Assign gap between opposing clusters to max(cnt_R, cnt_L).`

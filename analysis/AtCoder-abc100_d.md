# Problem Analysis: AtCoder-abc100_d — Patisserie ABC

**Problem ID**: `AtCoder-abc100_d`  
**Contest**: `abc100`  
**Rating / Difficulty**: 1331  
**URL**: https://atcoder.jp/contests/abc100/tasks/abc100_d  
**VJudge Tag**: `[problem:AtCoder-abc100_d]`  
**Category File**: [`../categories/basics/octant_sign_projection_3d.md`](../categories/basics/octant_sign_projection_3d.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `8-Sign Octant Projection for 3D Extremal Sums`  

---

## 1. Problem Statement & Key Idea
N cakes, cake i has beauty x_i, taste y_i, popularity z_i. Choose M cakes to maximize |sum x_i| + |sum y_i| + |sum z_i|.

**Key Idea**: The absolute value expression |X| + |Y| + |Z| equals max_{(s_x, s_y, s_z) in {+1, -1}^3} (s_x * X + s_y * Y + s_z * Z).

## 2. Core Observation & Invariant
There are only 2^3 = 8 sign assignments (s_x, s_y, s_z). For any fixed sign tuple, the objective becomes a simple linear sum: sum (s_x * x_i + s_y * y_i + s_z * z_i). To maximize this sum over M cakes, simply evaluate score_i = s_x * x_i + s_y * y_i + s_z * z_i for all N cakes, sort in descending order, and take the top M. The global maximum over all 8 sign configurations is the exact answer!

## 3. Step-by-Step Algorithm
1. Iterate sx in {-1, 1}, sy in {-1, 1}, sz in {-1, 1} (8 cases).
2. For each cake i: compute score[i] = sx * x[i] + sy * y[i] + sz * z[i].
3. Sort scores descending, sum the first M scores.
4. Track global maximum over all 8 octant configurations.
5. Print the maximum.

## 4. Complexity Analysis
- **Time Complexity**: `O(8 * N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Cake {
    long long x, y, z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Cake> cakes(n);
    for (int i = 0; i < n; ++i) {
        cin >> cakes[i].x >> cakes[i].y >> cakes[i].z;
    }

    long long max_val = 0;

    for (int sx : {-1, 1}) {
        for (int sy : {-1, 1}) {
            for (int sz : {-1, 1}) {
                vector<long long> scores(n);
                for (int i = 0; i < n; ++i) {
                    scores[i] = sx * cakes[i].x + sy * cakes[i].y + sz * cakes[i].z;
                }
                sort(scores.rbegin(), scores.rend());

                long long current_sum = 0;
                for (int i = 0; i < m; ++i) {
                    current_sum += scores[i];
                }

                max_val = max(max_val, current_sum);
            }
        }
    }

    cout << max_val << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decoupling multi-dimensional absolute value sums via sign projection.
- **Reusable Pattern**: `Multidimensional absolute sum: enumerate 2^D sign combinations, take top M greedy sum.`

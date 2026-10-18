# Problem Analysis: AtCoder-arc103_b — Robot Arms

**Problem ID**: `AtCoder-arc103_b`  
**Contest**: `arc103`  
**Rating / Difficulty**: 2677  
**URL**: https://atcoder.jp/contests/arc103/tasks/arc103_b  
**VJudge Tag**: `[problem:AtCoder-arc103_b]`  
**Category File**: [`../categories/basics/robot_arms_binary_basis.md`](../categories/basics/robot_arms_binary_basis.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Reach all given target coordinates using at most 40 robot arms by rotating coordinates by 45 degrees into u = x + y and v = x - y, constructing a binary basis of powers of 2.

## 2. Core Observation & Invariant
Each step in {R, L, U, D} by length d shifts (u, v) by (+d, +d), (-d, -d), (+d, -d), and (-d, +d), completely decoupling the signs of u and v. All target points must share the same parity of |X_i| + |Y_i|. Using arm lengths d = {2^30, 2^29, ..., 2^0} (appended with 1 if parity is even), any odd coordinate in [-2*10^9, 2*10^9] is greedily reachable from top to bottom.

## 3. Step-by-Step Algorithm
1. 1. Check parity of |X_i| + |Y_i| for all points; if inconsistent, output -1.
2. 2. Set arm lengths d = {2^30, 2^29, ..., 2^0}, appending an arm of length 1 if parity is even.
3. 3. For each point, transform to rotated coordinates u = X + Y, v = X - Y (adjusted by -1 if even).
4. 4. Greedily determine the sign of each power of 2 for u and v from highest to lowest.
5. 5. Map sign pairs (+, +) -> R, (-, -) -> L, (+, -) -> U, (-, +) -> D.
6. 6. Print arm count m, arm lengths, and direction strings for all points.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * m)`
- **Space Complexity**: `O(N * m)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> X(N), Y(N);
    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
    }

    int parity = (abs(X[0]) + abs(Y[0])) % 2;
    for (int i = 1; i < N; ++i) {
        if ((abs(X[i]) + abs(Y[i])) % 2 != parity) {
            cout << -1 << "\n";
            return 0;
        }
    }

    bool is_even = (parity == 0);

    vector<long long> powers;
    for (int k = 30; k >= 0; --k) {
        powers.push_back(1LL << k);
    }

    vector<long long> d = powers;
    if (is_even) {
        d.push_back(1);
    }

    int m = (int)d.size();
    cout << m << "\n";
    for (int i = 0; i < m; ++i) {
        cout << d[i] << (i + 1 == m ? "" : " ");
    }
    cout << "\n";

    for (int i = 0; i < N; ++i) {
        long long target_x = is_even ? (X[i] - 1) : X[i];
        long long target_y = Y[i];

        long long u = target_x + target_y;
        long long v = target_x - target_y;

        string w = "";
        for (long long p : powers) {
            int su = (u > 0) ? 1 : -1;
            int sv = (v > 0) ? 1 : -1;
            u -= su * p;
            v -= sv * p;

            if (su == 1 && sv == 1) w += 'R';
            else if (su == -1 && sv == -1) w += 'L';
            else if (su == 1 && sv == -1) w += 'U';
            else if (su == -1 && sv == 1) w += 'D';
        }

        if (is_even) {
            w += 'R';
        }

        cout << w << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

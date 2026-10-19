# Problem Analysis: AtCoder-arc169_d — D - Add to Make a Permutation

**Problem ID**: `AtCoder-arc169_d`  
**Contest**: `arc169`  
**Rating / Difficulty**: 2812  
**URL**: https://atcoder.jp/contests/arc169/tasks/arc169_d  
**VJudge Tag**: `[problem:AtCoder-arc169_d]`  
**Category File**: [`../categories/basics/permutation_cyclic_increment_greedy.md`](../categories/basics/permutation_cyclic_increment_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given an array A and integer M, find the minimum number of cyclic range increment operations of size M to transform A into a permutation of (x, x+1, ..., x+N-1) for some integer x, or report -1.

## 2. Core Observation & Invariant
Sorting A allows matching elements to target B_i = x + i - 1. The total required increment S = sum(B_i - A_i) must be divisible by M. Each element requires B_i >= A_i, establishing a lower bound on x. By cyclic difference analysis, the required operations are non-negative iff the maximum individual increment does not exceed S / M, and modular compatibility holds with gcd(N, M). If violated, jumping x by steps of M / gcd(N, M) finds the minimal valid configuration.

## 3. Step-by-Step Algorithm
1. 1. Sort A ascending.
2. 2. Set initial bound x_min = max_i(A_i - i + 1).
3. 3. Adjust x upward so that sum(x + i - 1 - A_i) is divisible by M.
4. 4. Check if max_i(x + i - 1 - A_i) <= S / M.
5. 5. If not, increase x in steps of M / gcd(N, M) until the bound is satisfied.
6. 6. Output S / M.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());

    long long x = 0;
    for (int i = 1; i <= n; i++) {
        x = max(x, a[i - 1] - i + 1);
    }

    long long total_sum = 0;
    for (int i = 1; i <= n; i++) {
        total_sum += (x + i - 1) - a[i - 1];
    }

    bool flag = false;
    for (int i = 0; i <= m; i++) {
        if ((total_sum + n * i) % m == 0) {
            x += i;
            total_sum += n * i;
            flag = true;
            break;
        }
    }

    if (!flag) {
        cout << -1 << "\n";
        return 0;
    }

    long long mx = 0;
    for (int i = 1; i <= n; i++) {
        mx = max(mx, x + i - 1 - a[i - 1]);
    }

    long long g = gcd(n, m);
    long long step_x = m / g;
    long long delta = (n - m) / g;

    if (mx > total_sum / m) {
        long long diff = mx - total_sum / m;
        long long steps = (diff + delta - 1) / delta;
        mx += steps * step_x;
        total_sum += steps * n * step_x;
    }

    cout << total_sum / m << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

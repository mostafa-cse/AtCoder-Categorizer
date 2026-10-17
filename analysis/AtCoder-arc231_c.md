# Problem Analysis: AtCoder-arc231_c — C. One Sky, Many Stars

**Problem ID**: `AtCoder-arc231_c`  
**Contest**: `arc231`  
**Rating / Difficulty**: 2267  
**URL**: https://atcoder.jp/contests/arc231/tasks/arc231_c  
**VJudge Tag**: `[problem:AtCoder-arc231_c]`  
**Category File**: [`../categories/geometry/euclidean_geometry_1d_stargazing_intervals.md`](../categories/geometry/euclidean_geometry_1d_stargazing_intervals.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Euclidean Geometry`  
- **Topic (Skill)**: `Euclidean Geometry`  

---

## 1. Problem Statement & Key Idea
There are $N$ people on a 1D line at coordinates $x_1 < x_2 < \dots < x_N$. Each person claims the distance to their nearest star is $d_i$. Stars can be placed at any coordinates. We must determine if a valid star configuration exists, supported under $Q$ point updates on $d_i$.

## 2. Core Observation & Invariant
Each person $i$'s claim implies that at least one star must be placed at $x_i - d_i$ or $x_i + d_i$, and NO star may be placed strictly inside the open interval $(x_i - d_i, x_i + d_i)$.
A coordinate $pos \in \{x_i - d_i, x_i + d_i\}$ is valid if it does not fall into any other person's forbidden interval. Crucially, by monotonicity of $x_i$, checking validity against the immediately adjacent neighbors $i-1$ and $i+1$ is both necessary and sufficient! Person $i$ is valid if at least one of $x_i - d_i$ or $x_i + d_i$ is not strictly inside $(x_{i-1} - d_{i-1}, x_{i-1} + d_{i-1})$ and not strictly inside $(x_{i+1} - d_{i+1}, x_{i+1} + d_{i+1})$. Maintaining the count of invalid people allows $O(1)$ updates per query affecting only $P-1, P, P+1$.

## 3. Step-by-Step Algorithm
1. Define helper `check_person(i)` checking if $x_i - d_i$ or $x_i + d_i$ avoids the open intervals of neighbors $i-1$ and $i+1$.
2. Initialize an array `bad` of size $N+2$ and count total invalid people `bad_count`.
3. For each of the $Q$ queries $(P, S)$:
4. Update $d_P = S$.
5. Re-evaluate validity for indices in $\{P - 1, P, P + 1\}$, updating `bad` and `bad_count` accordingly.
6. Output 'Yes' if `bad_count == 0`, else 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

bool check_person(int i, int n, const vector<long long>& x, const vector<long long>& d) {
    auto is_pos_good = [&](long long pos) {
        for (int j : {i - 1, i + 1}) {
            if (j >= 1 && j <= n) {
                if (x[j] - d[j] < pos && pos < x[j] + d[j]) {
                    return false;
                }
            }
        }
        return true;
    };

    return is_pos_good(x[i] - d[i]) || is_pos_good(x[i] + d[i]);
}

void solve() {
    int n;
    if (!(cin >> n)) return;

    vector<long long> a(n + 1), b(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int i = 1; i <= n; ++i) cin >> b[i];

    vector<int> bad(n + 2, 0);
    int bad_count = 0;

    for (int i = 1; i <= n; ++i) {
        if (!check_person(i, n, a, b)) {
            bad[i] = 1;
            bad_count++;
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int p;
        long long s;
        cin >> p >> s;
        b[p] = s;

        for (int i : {p - 1, p, p + 1}) {
            if (i >= 1 && i <= n) {
                if (bad[i]) {
                    bad_count--;
                    bad[i] = 0;
                }
                if (!check_person(i, n, a, b)) {
                    bad[i] = 1;
                    bad_count++;
                }
            }
        }

        if (bad_count == 0) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

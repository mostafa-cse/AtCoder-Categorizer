# Problem Analysis: AtCoder-tenka1_2017_e — CAR CAR CAR

**Problem ID**: `AtCoder-tenka1_2017_e`  
**Contest**: `tenka1_2017`  
**Rating / Difficulty**: 2703  
**URL**: https://atcoder.jp/contests/tenka1_2017/tasks/tenka1_2017_e  
**VJudge Tag**: `[problem:AtCoder-tenka1_2017_e]`  
**Category File**: [`../categories/data_structures_ds/cartesian_coordinate_lines_median_bit.md`](../categories/data_structures_ds/cartesian_coordinate_lines_median_bit.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Minimizing sum of Manhattan distances to N(N-1)/2 intersection points decouples into 1D median problems for X and Y independently. The number of intersection points with x_coord <= X is equal to the number of line pairs whose vertical order at x = X is inverted relative to x -> -infinity (i.e. sorted by slope). We count intersections in O(N log N) using merge sort / BIT, allowing binary search for the median coordinate in O(N log N log(range)).

## 2. Core Observation & Invariant
Normalizing lines to B_i > 0, the y-value at x = X is (C_i - A_i X) / B_i. Sorting lines by slope m_i = -A_i / B_i ascending, line i and j (with i < j) cross at or before X iff y_i(X) <= y_j(X). Counting pairs (i, j) with i < j and y_i <= y_j is standard inversion counting via merge sort.

## 3. Step-by-Step Algorithm
1. 1. For X: normalize all lines A_i x + B_i y = C_i to B_i > 0. Sort lines by slope ascending.
2. 2. Binary search for X in [-10^7, 10^7]: compute y_i(X) for all lines, count crossed pairs using merge sort in O(N log N). Target rank is ceil((N(N-1)/2) / 2).
3. 3. Symmetrically for Y: normalize lines to A_i > 0 and binary search.
4. 4. Print optimal (X, Y) to 15 decimal places.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N log(range))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Line {
    double a, b, c;
};

long long merge_sort_count(vector<double>& arr, vector<double>& temp, int l, int r) {
    if (l >= r) return 0;
    int mid = (l + r) / 2;
    long long cnt = merge_sort_count(arr, temp, l, mid) + merge_sort_count(arr, temp, mid + 1, r);
    int i = l;
    int j = mid + 1;
    int k = l;
    while (i <= mid && j <= r) {
        if (arr[i] <= arr[j]) {
            cnt += (r - j + 1);
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    for (int idx = l; idx <= r; ++idx) arr[idx] = temp[idx];
    return cnt;
}

double solve_1d(int n, vector<Line> lines) {
    // sort lines by slope ascending: -a/b
    sort(lines.begin(), lines.end(), [](const Line& l1, const Line& l2) {
        return -l1.a / l1.b < -l2.a / l2.b;
    });

    long long total_pairs = 1LL * n * (n - 1) / 2;
    long long target = (total_pairs + 1) / 2;

    vector<double> vals(n);
    vector<double> temp(n);

    auto count_intersections = [&](double X) {
        for (int i = 0; i < n; ++i) {
            vals[i] = (lines[i].c - lines[i].a * X) / lines[i].b;
        }
        return merge_sort_count(vals, temp, 0, n - 1);
    };

    double low = -1e7;
    double high = 1e7;
    for (int iter = 0; iter < 75; ++iter) {
        double mid = (low + high) / 2.0;
        if (count_intersections(mid) >= target) {
            high = mid;
        } else {
            low = mid;
        }
    }
    return high;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Line> lines_x(n);
    vector<Line> lines_y(n);

    for (int i = 0; i < n; ++i) {
        double a, b, c;
        cin >> a >> b >> c;
        // for X: a*x + b*y = c, normalize b > 0
        double ax = a, bx = b, cx = c;
        if (bx < 0) {
            ax = -ax; bx = -bx; cx = -cx;
        }
        lines_x[i] = {ax, bx, cx};

        // for Y: b*y + a*x = c, normalize a > 0
        double ay = b, by = a, cy = c;
        if (by < 0) {
            ay = -ay; by = -by; cy = -cy;
        }
        lines_y[i] = {ay, by, cy};
    }

    double ans_x = solve_1d(n, lines_x);
    double ans_y = solve_1d(n, lines_y);

    cout << fixed << setprecision(15) << ans_x << " " << ans_y << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

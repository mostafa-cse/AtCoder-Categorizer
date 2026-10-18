# Problem Analysis: AtCoder-abc220_g — G. Isosceles Trapezium

**Problem ID**: `AtCoder-abc220_g`  
**Contest**: `abc220`  
**Rating / Difficulty**: 2439  
**URL**: https://atcoder.jp/contests/abc220/tasks/abc220_g  
**VJudge Tag**: `[problem:AtCoder-abc220_g]`  
**Category File**: [`../categories/geometry/isosceles_trapezium_perpendicular_bisectors.md`](../categories/geometry/isosceles_trapezium_perpendicular_bisectors.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Polygons(2D)`  

---

## 1. Problem Statement & Key Idea
Choose 4 points out of $N \le 1000$ to form an isosceles trapezoid of maximum total weight. Four points form an isosceles trapezoid iff they can be paired into two parallel segments whose perpendicular bisectors are identical lines. Grouping all $\binom{N}{2}$ pairs by their canonical perpendicular bisector line equation $(A, B, C)$ allows finding the two heaviest disjoint pairs along each symmetry line.

## 2. Core Observation & Invariant
Pairs sharing the same midpoint along the line are collinear and cannot form a valid quadrilateral. For each distinct parallel position on the bisector line, we keep only the pair with maximum weight, and then test the top pairs with disjoint vertex sets.

## 3. Step-by-Step Algorithm
1. 1. For every pair of points $(i, j)$, compute the canonical integer line equation $(A, B, C)$ of their perpendicular bisector: $2 \Delta x \cdot x + 2 \Delta y \cdot y = x_j^2 - x_i^2 + y_j^2 - y_i^2$, reduced by GCD.
2. 2. Compute the parallel line coordinate $mid\_val = -B(x_i + x_j) + A(y_i + y_j)$.
3. 3. Group pairs by line $(A, B, C)$ and position $mid\_val$, storing the maximum weight pair for each position.
4. 4. For each line group, sort the deduplicated pairs by weight descending, and check the top pairs to find the maximum sum of weights with disjoint vertex indices.
5. 5. Output the global maximum weight (or -1 if no isosceles trapezoid exists).

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Line {
    long long A, B, C;
    bool operator<(const Line& other) const {
        if (A != other.A) return A < other.A;
        if (B != other.B) return B < other.B;
        return C < other.C;
    }
};

Line canonical_line(long long x1, long long y1, long long x2, long long y2) {
    long long dx = x2 - x1;
    long long dy = y2 - y1;
    long long A = 2 * dx;
    long long B = 2 * dy;
    long long C = (x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1);
    long long g = gcd(gcd(abs(A), abs(B)), abs(C));
    A /= g;
    B /= g;
    C /= g;
    if (A < 0 || (A == 0 && B < 0)) {
        A = -A;
        B = -B;
        C = -C;
    }
    return {A, B, C};
}

struct PairInfo {
    long long weight;
    int u, v;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> X(N), Y(N), C(N);
    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i] >> C[i];
    }

    map<Line, map<long long, PairInfo>> lines_map;

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            Line line = canonical_line(X[i], Y[i], X[j], Y[j]);
            long long mid_val = -line.B * (X[i] + X[j]) + line.A * (Y[i] + Y[j]);
            long long weight = C[i] + C[j];

            auto& group = lines_map[line];
            auto it = group.find(mid_val);
            if (it == group.end() || weight > it->second.weight) {
                group[mid_val] = {weight, i, j};
            }
        }
    }

    long long ans = -1;

    for (auto& entry : lines_map) {
        auto& group = entry.second;
        if (group.size() < 2) continue;

        vector<PairInfo> pairs;
        pairs.reserve(group.size());
        for (auto& p : group) {
            pairs.push_back(p.second);
        }

        sort(pairs.begin(), pairs.end(), [](const PairInfo& a, const PairInfo& b) {
            return a.weight > b.weight;
        });

        int limit = min((int)pairs.size(), 6);
        for (int a = 0; a < limit; ++a) {
            for (int b = a + 1; b < limit; ++b) {
                if (pairs[a].u != pairs[b].u && pairs[a].u != pairs[b].v &&
                    pairs[a].v != pairs[b].u && pairs[a].v != pairs[b].v) {
                    ans = max(ans, pairs[a].weight + pairs[b].weight);
                    break;
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

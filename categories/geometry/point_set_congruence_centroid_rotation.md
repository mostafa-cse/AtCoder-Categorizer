# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Domain**: `Geometry`  
**Subtopic**: `Geometry 2D`  

This workbook contains curated, high-quality competitive programming problems teaching **Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)**.

---

## Curated Problems

### `[problem:AtCoder-abc207_d]` — Congruence Points
- **Rating / Difficulty**: 2074
- **Contest**: `abc207`
- **Analysis**: [`analysis/AtCoder-abc207_d.md`](../../analysis/AtCoder-abc207_d.md)
- **Key Idea**: Translation invariance is eliminated by shifting both point sets so their centroids lie at the origin (scaling coordinates by N to retain exact integer arithmetic). Under rotation around the origin, Euclidean distance from the origin is preserved. To test rotational congruence, pick a non-origin anchor point in S, test aligning it with every candidate point in T having the identical squared norm. The rotation angle theta is uniquely determined by the dot and cross product of the two vectors, which allows rotating every point of S using integer arithmetic and testing set equality in O(N log N) via sorting.
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> S(n), T(n);
    long long sx = 0, sy = 0, tx = 0, ty = 0;
    for (int i = 0; i < n; ++i) {
        cin >> S[i].x >> S[i].y;
        sx += S[i].x;
        sy += S[i].y;
    }
    for (int i = 0; i < n; ++i) {
        cin >> T[i].x >> T[i].y;
        tx += T[i].x;
        ty += T[i].y;
    }

    if (n == 1) {
        cout << "Yes\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        S[i].x = S[i].x * n - sx;
        S[i].y = S[i].y * n - sy;
        T[i].x = T[i].x * n - tx;
        T[i].y = T[i].y * n - ty;
    }

    sort(T.begin(), T.end());

    int non_zero = -1;
    for (int i = 0; i < n; ++i) {
        if (S[i].x != 0 || S[i].y != 0) {
            non_zero = i;
            break;
        }
    }

    if (non_zero == -1) {
        cout << "Yes\n";
        return 0;
    }

    long long x0 = S[non_zero].x, y0 = S[non_zero].y;
    long long norm0 = x0 * x0 + y0 * y0;

    for (int j = 0; j < n; ++j) {
        long long xt = T[j].x, yt = T[j].y;
        if (xt * xt + yt * yt != norm0) continue;

        long long c = x0 * xt + y0 * yt;
        long long s = x0 * yt - y0 * xt;

        vector<Point> S_rot(n);
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            long long rx = S[i].x * c - S[i].y * s;
            long long ry = S[i].x * s + S[i].y * c;
            if (rx % norm0 != 0 || ry % norm0 != 0) {
                ok = false;
                break;
            }
            S_rot[i] = {rx / norm0, ry / norm0};
        }
        if (!ok) continue;

        sort(S_rot.begin(), S_rot.end());
        if (S_rot == T) {
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
    return 0;
}
```

# Exact Circle Lattice Point Counting via Fixed-Point Integer Scaling and 1D Sweep

**Domain**: `Geometry`  
**Subtopic**: `Lattice Points`  

This workbook contains curated, high-quality competitive programming problems teaching **Exact Circle Lattice Point Counting via Fixed-Point Integer Scaling and 1D Sweep**.

---

## Curated Problems

### `[problem:AtCoder-abc191_d]` — Circle Lattice Points
- **Rating / Difficulty**: 1953
- **Contest**: `abc191`
- **Analysis**: [`analysis/AtCoder-abc191_d.md`](../../analysis/AtCoder-abc191_d.md)
- **Key Idea**: Scale X, Y, R by 10^4 into exact 64-bit integers to eliminate floating point error. An integer coordinate x corresponds to scaled coordinate X_scaled = x * 10^4. For each integer x in [ceil((X - R)/10^4), floor((X + R)/10^4)], let dx = x * 10^4 - X. We need (y * 10^4 - Y)^2 <= R^2 - dx^2. Compute D = floor(sqrt(R^2 - dx^2)) using integer square root. The valid integer y values satisfy Y - D <= y * 10^4 <= Y + D, giving floor((Y + D)/10^4) - ceil((Y - D)/10^4) + 1 lattice points.
- **Time Complexity**: `O(R * 10^-4)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

long long parse_fixed(const string& s) {
    bool neg = (s[0] == '-');
    int start = neg ? 1 : 0;
    size_t dot = s.find('.');
    long long integer_part = 0;
    long long frac_part = 0;

    if (dot == string::npos) {
        integer_part = stoll(s.substr(start));
    } else {
        integer_part = stoll(s.substr(start, dot - start));
        string frac_str = s.substr(dot + 1);
        while (frac_str.size() < 4) frac_str += '0';
        if (frac_str.size() > 4) frac_str = frac_str.substr(0, 4);
        frac_part = stoll(frac_str);
    }
    long long val = integer_part * 10000 + frac_part;
    return neg ? -val : val;
}

long long floor_div(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && ((a < 0) ^ (b < 0))) res--;
    return res;
}

long long ceil_div(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && !((a < 0) ^ (b < 0))) res++;
    return res;
}

long long isqrt(long long n) {
    if (n <= 0) return 0;
    long long r = sqrt((double)n);
    while ((r + 1) * (r + 1) <= n) r++;
    while (r * r > n) r--;
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string sx, sy, sr;
    if (!(cin >> sx >> sy >> sr)) return 0;

    long long X = parse_fixed(sx);
    long long Y = parse_fixed(sy);
    long long R = parse_fixed(sr);

    long long min_x = ceil_div(X - R, 10000);
    long long max_x = floor_div(X + R, 10000);

    long long ans = 0;
    for (long long x = min_x; x <= max_x; ++x) {
        long long dx = x * 10000 - X;
        long long rem_sq = R * R - dx * dx;
        if (rem_sq < 0) continue;

        long long D = isqrt(rem_sq);
        long long min_y = ceil_div(Y - D, 10000);
        long long max_y = floor_div(Y + D, 10000);

        if (max_y >= min_y) {
            ans += (max_y - min_y + 1);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

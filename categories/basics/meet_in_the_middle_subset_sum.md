# Meet-in-the-Middle on Subset Sum N <= 40

**Domain**: `Basics`  
**Subtopic**: `Meet-in-the-Middle`  

This workbook contains curated, high-quality competitive programming problems teaching **Meet-in-the-Middle on Subset Sum N <= 40**.

---

## Curated Problems

### `[problem:AtCoder-abc184_f]` — Programming Contest
- **Rating / Difficulty**: 1423
- **Contest**: `abc184`
- **Analysis**: [`analysis/AtCoder-abc184_f.md`](../../analysis/AtCoder-abc184_f.md)
- **Key Idea**: Split the N problems into two halves of size <= 20. Generate all 2^(N/2) subset sums for each half, sort one half, and binary search for each sum in the first half.
- **Time Complexity**: `O(2^(N/2) * N)`
- **Space Complexity**: `O(2^(N/2))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generate_sums(const vector<long long>& a, vector<long long>& res, long long T) {
    res.push_back(0);
    for (long long x : a) {
        int sz = res.size();
        for (int i = 0; i < sz; ++i) {
            if (res[i] + x <= T) {
                res.push_back(res[i] + x);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int mid = n / 2;
    vector<long long> left_a(a.begin(), a.begin() + mid);
    vector<long long> right_a(a.begin() + mid, a.end());

    vector<long long> left_sums, right_sums;
    generate_sums(left_a, left_sums, T);
    generate_sums(right_a, right_sums, T);

    sort(right_sums.begin(), right_sums.end());
    right_sums.erase(unique(right_sums.begin(), right_sums.end()), right_sums.end());

    long long best = 0;
    for (long long s : left_sums) {
        auto it = upper_bound(right_sums.begin(), right_sums.end(), T - s);
        if (it != right_sums.begin()) {
            --it;
            best = max(best, s + *it);
        }
    }

    cout << best << "\n";
    return 0;
}
```

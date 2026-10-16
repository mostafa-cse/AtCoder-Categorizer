# Meet-in-the-Middle on Subset Sum N <= 32

**Domain**: `Basics`  
**Subtopic**: `Meet-in-the-Middle`  

This workbook contains curated, high-quality competitive programming problems teaching **Meet-in-the-Middle on Subset Sum N <= 32**.

---

## Curated Problems

### `[problem:AtCoder-arc017_3]` — Minimalist
- **Rating / Difficulty**: 1625
- **Contest**: `arc017`
- **Analysis**: [`analysis/AtCoder-arc017_3.md`](../../analysis/AtCoder-arc017_3.md)
- **Key Idea**: Split the N items into two halves of size <= 16. Generate all 2^16 subset sums for the first half, sort them, and for each sum in the second half, count matching complements X - sum.
- **Time Complexity**: `O(2^(N/2) * (N/2))`
- **Space Complexity**: `O(2^(N/2))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generate_sums(const vector<long long>& a, vector<long long>& sums) {
    sums.push_back(0);
    for (long long x : a) {
        int sz = sums.size();
        for (int i = 0; i < sz; ++i) {
            sums.push_back(sums[i] + x);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long X;
    if (!(cin >> n >> X)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int mid = n / 2;
    vector<long long> left_a(a.begin(), a.begin() + mid);
    vector<long long> right_a(a.begin() + mid, a.end());

    vector<long long> sums1, sums2;
    generate_sums(left_a, sums1);
    generate_sums(right_a, sums2);

    sort(sums2.begin(), sums2.end());

    long long count = 0;
    for (long long s : sums1) {
        auto [it1, it2] = equal_range(sums2.begin(), sums2.end(), X - s);
        count += (it2 - it1);
    }

    cout << count << "\n";
    return 0;
}
```

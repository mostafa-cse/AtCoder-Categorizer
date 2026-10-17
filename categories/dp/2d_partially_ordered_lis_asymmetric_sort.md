# 2D Partially-Ordered LIS via Asymmetric Sorting (w ascending, h descending)

**Domain**: `Dynamic Programming`  
**Subtopic**: `LIS / Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Partially-Ordered LIS via Asymmetric Sorting (w ascending, h descending)**.

---

## Curated Problems

### `[problem:AtCoder-abc038_d]` — プレゼント
- **Rating / Difficulty**: 1804
- **Contest**: `abc038`
- **Analysis**: [`analysis/AtCoder-abc038_d.md`](../../analysis/AtCoder-abc038_d.md)
- **Key Idea**: Sort boxes by width w ascending, and by height h DESCENDING for ties. Then the problem reduces to finding the standard 1D strictly increasing Longest Increasing Subsequence on h.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Box {
    int w, h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Box> boxes(n);
    for (int i = 0; i < n; ++i) {
        cin >> boxes[i].w >> boxes[i].h;
    }

    sort(boxes.begin(), boxes.end(), [](const Box& a, const Box& b) {
        if (a.w != b.w) return a.w < b.w;
        return a.h > b.h;
    });

    vector<int> lis;
    for (int i = 0; i < n; ++i) {
        int val = boxes[i].h;
        auto it = lower_bound(lis.begin(), lis.end(), val);
        if (it == lis.end()) {
            lis.push_back(val);
        } else {
            *it = val;
        }
    }

    cout << lis.size() << "\n";
    return 0;
}
```

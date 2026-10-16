# Binary Lifting on Fenwick Tree for K-th Smallest Element

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Lifting on Fenwick Tree for K-th Smallest Element**.

---

## Curated Problems

### `[problem:AtCoder-arc033_3]` — Data Structure
- **Rating / Difficulty**: 1641
- **Contest**: `arc033`
- **Analysis**: [`analysis/AtCoder-arc033_3.md`](../../analysis/AtCoder-arc033_3.md)
- **Key Idea**: Maintain a frequency array using a Fenwick tree of size 200,000. Finding the X-th smallest element is finding the smallest index idx such that prefix_sum(idx) >= X, done via binary lifting directly on the Fenwick tree in O(log MAX).
- **Time Complexity**: `O(Q log(MAX))`
- **Space Complexity**: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX_VAL = 200000;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    // Binary lifting to find smallest index with prefix sum >= k
    int find_kth(int k) {
        int idx = 0;
        for (int step = (1 << 18); step > 0; step >>= 1) {
            if (idx + step <= n && tree[idx + step] < k) {
                idx += step;
                k -= tree[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    Fenwick bit(MAX_VAL);

    while (q--) {
        int type, x;
        cin >> type >> x;
        if (type == 1) {
            bit.add(x, 1);
        } else {
            int val = bit.find_kth(x);
            cout << val << "\n";
            bit.add(val, -1);
        }
    }

    return 0;
}
```

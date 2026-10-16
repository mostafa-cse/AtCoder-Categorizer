# Point Update Range XOR Query on Fenwick Tree

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Point Update Range XOR Query on Fenwick Tree**.

---

## Curated Problems

### [problem:AtCoder-abc185_f] — Range Xor Query
- **Contest**: `abc185`
- **Rating / Difficulty**: 1053
- **Specific Skill**: Point Update Range XOR Query on Fenwick Tree
- **Individual Analysis**: [`../../analysis/AtCoder-abc185_f.md`](../../analysis/AtCoder-abc185_f.md)
- **Problem Statement Summary**: Given an array A of N integers. Process Q queries: (1) Replace A[X] with A[X] XOR Y; (2) Calculate A[X] XOR A[X+1] ... XOR A[Y] (N, Q <= 3 * 10^5).
- **Core Insight**: Prefix XOR: pref_xor(x) = A[1] ^ ... ^ A[x]. Range XOR on [L, R] is simply pref_xor(R) ^ pref_xor(L - 1). Point update: XORing A[X] with Y is achieved by applying bit.add(X, Y).
- **Complexity**: Time: `O((N + Q) log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct FenwickXOR {
    int n;
    vector<long long> tree;
    FenwickXOR(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, long long val) {
        for (; i <= n; i += i & -i) {
            tree[i] ^= val;
        }
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) {
            sum ^= tree[i];
        }
        return sum;
    }
    long long query_range(int l, int r) {
        return query(r) ^ query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    FenwickXOR bit(n);
    for (int i = 1; i <= n; ++i) {
        long long a;
        cin >> a;
        bit.add(i, a);
    }

    while (q--) {
        int t, x;
        long long y;
        cin >> t >> x >> y;
        if (t == 1) {
            bit.add(x, y);
        } else {
            cout << bit.query_range(x, y) << "\n";
        }
    }

    return 0;
}
```

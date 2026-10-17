# Basic Greedy Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Greedy Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-abc140_f]` — Many Slimes
- **Rating / Difficulty**: 2105
- **Contest**: `abc140`
- **Analysis**: [`analysis/AtCoder-abc140_f.md`](../../analysis/AtCoder-abc140_f.md)
- **Key Idea**: The initial slime must be the maximum element of the multiset. In each round k (from 1 to N), every slime in the current population must spawn a smaller slime. To maximize the chances of future slimes being able to spawn even smaller slimes, each existing slime should greedily choose the largest available slime in the remaining multiset that is strictly smaller than itself. If at any step an existing slime cannot find any strictly smaller slime, reproduction is impossible.
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 1 << n;
    multiset<int> s;
    for (int i = 0; i < total; ++i) {
        int x;
        cin >> x;
        s.insert(x);
    }

    vector<int> current;
    auto it = prev(s.end());
    current.push_back(*it);
    s.erase(it);

    for (int step = 0; step < n; ++step) {
        vector<int> next_gen;
        for (int val : current) {
            auto it2 = s.lower_bound(val);
            if (it2 == s.begin()) {
                cout << "No\n";
                return 0;
            }
            --it2;
            next_gen.push_back(*it2);
            s.erase(it2);
        }
        for (int v : next_gen) {
            current.push_back(v);
        }
        sort(current.rbegin(), current.rend());
    }

    cout << "Yes\n";
    return 0;
}
```

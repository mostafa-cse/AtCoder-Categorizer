# Dual Multiset (Multiset of Multiset Maxima) Dynamic Maintenance

**Domain**: `Data Structures`  
**Subtopic**: `Multiset`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Multiset (Multiset of Multiset Maxima) Dynamic Maintenance**.

---

## Curated Problems

### `[problem:AtCoder-abc170_e]` — Smart Infants
- **Rating / Difficulty**: 1502
- **Contest**: `abc170`
- **Analysis**: [`analysis/AtCoder-abc170_e.md`](../../analysis/AtCoder-abc170_e.md)
- **Key Idea**: Maintain a multiset of ratings for each kindergarten, and a global multiset containing the maximum rating of every non-empty kindergarten.
- **Time Complexity**: `O(Q log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int MAX_K = 200005;

multiset<int> kg[MAX_K];
multiset<int> top_ratings;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> rating(n + 1), loc(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> rating[i] >> loc[i];
        kg[loc[i]].insert(rating[i]);
    }

    for (int i = 1; i < MAX_K; ++i) {
        if (!kg[i].empty()) {
            top_ratings.insert(*kg[i].rbegin());
        }
    }

    while (q--) {
        int c, dst;
        cin >> c >> dst;
        int src = loc[c];
        int val = rating[c];

        if (src == dst) {
            cout << *top_ratings.begin() << "\n";
            continue;
        }

        // Remove old max from top_ratings
        top_ratings.erase(top_ratings.find(*kg[src].rbegin()));
        if (!kg[dst].empty()) {
            top_ratings.erase(top_ratings.find(*kg[dst].rbegin()));
        }

        // Move infant
        kg[src].erase(kg[src].find(val));
        kg[dst].insert(val);
        loc[c] = dst;

        // Reinsert new max
        if (!kg[src].empty()) {
            top_ratings.insert(*kg[src].rbegin());
        }
        top_ratings.insert(*kg[dst].rbegin());

        cout << *top_ratings.begin() << "\n";
    }

    return 0;
}
```

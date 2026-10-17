# Greedy Exchange Argument with Two Compensating Quantities

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Exchange Argument with Two Compensating Quantities**.

---

## Curated Problems

### `[problem:AtCoder-abc116_d]` — Various Sushi
- **Rating / Difficulty**: 1712
- **Contest**: `abc116`
- **Analysis**: [`analysis/AtCoder-abc116_d.md`](../../analysis/AtCoder-abc116_d.md)
- **Key Idea**: Start with the top K most delicious sushi. This maximizes sum(d_i). To increase diversity x to x+1, exchange the least delicious duplicate sushi in our chosen set with the most delicious unused sushi of a new type.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

struct Sushi {
    int t;
    long long d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Sushi> sushi(n);
    for (int i = 0; i < n; ++i) {
        cin >> sushi[i].t >> sushi[i].d;
    }

    sort(sushi.begin(), sushi.end(), [](const Sushi& a, const Sushi& b) {
        return a.d > b.d;
    });

    unordered_set<int> chosen_types;
    vector<long long> duplicates;
    long long current_sum = 0;

    for (int i = 0; i < k; ++i) {
        current_sum += sushi[i].d;
        if (chosen_types.count(sushi[i].t)) {
            duplicates.push_back(sushi[i].d);
        } else {
            chosen_types.insert(sushi[i].t);
        }
    }

    vector<Sushi> unused_distinct;
    for (int i = k; i < n; ++i) {
        if (!chosen_types.count(sushi[i].t)) {
            chosen_types.insert(sushi[i].t);
            unused_distinct.push_back(sushi[i]);
        }
    }

    long long distinct_count = chosen_types.size() - unused_distinct.size();
    long long max_score = current_sum + distinct_count * distinct_count;

    int dup_idx = duplicates.size() - 1;
    int unused_idx = 0;

    while (dup_idx >= 0 && unused_idx < (int)unused_distinct.size()) {
        current_sum -= duplicates[dup_idx--];
        current_sum += unused_distinct[unused_idx++].d;
        distinct_count++;
        long long score = current_sum + distinct_count * distinct_count;
        max_score = max(max_score, score);
    }

    cout << max_score << "\n";
    return 0;
}
```

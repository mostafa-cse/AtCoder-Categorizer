# Basic Constructive Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Constructive Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-keyence2021_d]` — Choosing Up Sides
- **Rating / Difficulty**: 2115
- **Contest**: `keyence2021`
- **Analysis**: [`analysis/AtCoder-keyence2021_d.md`](../../analysis/AtCoder-keyence2021_d.md)
- **Key Idea**: The condition that all pairs of columns have the identical dot product across team indicators (+1 and -1) is uniquely satisfied by the construction of a Hadamard Matrix of order 2^N. Using Sylvester's recursive Kronecker product construction, H[r][c] = (-1)^{popcount(r & c)}. Row 0 consists entirely of 1s (all on team A). The remaining 2^N - 1 rows have exactly equal counts of +1 ('A') and -1 ('B') and their column dot products are orthogonal, giving equal pairwise shared rounds for all pairs of people.
- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_people = 1 << n;
    int total_rounds = (1 << n) - 1;

    cout << total_rounds << "\n";
    for (int r = 1; r < total_people; ++r) {
        string s = "";
        for (int c = 0; c < total_people; ++c) {
            int sign = __builtin_popcount(r & c) % 2;
            s += (sign == 0 ? 'A' : 'B');
        }
        cout << s << "\n";
    }

    return 0;
}
```

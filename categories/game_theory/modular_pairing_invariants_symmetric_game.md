# Modular Pairing Invariants and Symmetric Strategy in Mod-M Sum Games

**Domain**: `Game Theory`  
**Subtopic**: `Combinatorial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Modular Pairing Invariants and Symmetric Strategy in Mod-M Sum Games**.

---

## Curated Problems

### `[problem:AtCoder-arc148_d]` — mod M Game
- **Rating / Difficulty**: 2009
- **Contest**: `arc148`
- **Analysis**: [`analysis/AtCoder-arc148_d.md`](../../analysis/AtCoder-arc148_d.md)
- **Key Idea**: Bob wants the final sum difference sum(A) - sum(B) = 0 mod M. Identical elements can be symmetrically paired (if Bob copies Alice's choice, their contribution cancels to 0). After cancelling all identical pairs: if M is odd, any unpaired element allows Alice to force sum(A) != sum(B) mod M, so Bob wins iff all elements pair up identically. If M is even, elements with difference M/2 can also pair up, because two such pairs yield difference 0 or M = 0 mod M. Thus Bob wins iff all remaining elements pair up into pairs (x, x + M/2) and the number of such pairs is even.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    map<long long, int> freq;
    for (int i = 0; i < 2 * n; ++i) {
        long long a;
        cin >> a;
        freq[a % m]++;
    }

    map<long long, int> rem;
    for (const auto& [val, cnt] : freq) {
        if (cnt % 2 != 0) {
            rem[val] = 1;
        }
    }

    if (rem.empty()) {
        cout << "Bob\n";
        return 0;
    }

    if (m % 2 != 0) {
        cout << "Alice\n";
        return 0;
    }

    long long half = m / 2;
    int pair_count = 0;

    while (!rem.empty()) {
        auto it = rem.begin();
        long long x = it->first;
        long long target = (x + half) % m;

        if (rem.find(target) == rem.end()) {
            cout << "Alice\n";
            return 0;
        }

        rem.erase(x);
        rem.erase(target);
        pair_count++;
    }

    if (pair_count % 2 == 0) {
        cout << "Bob\n";
    } else {
        cout << "Alice\n";
    }

    return 0;
}
```

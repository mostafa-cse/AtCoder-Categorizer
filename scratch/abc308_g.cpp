#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<int> s;
    multiset<int> diffs;

    auto add_diff = [&](int val) {
        diffs.insert(val);
    };

    auto remove_diff = [&](int val) {
        auto it = diffs.find(val);
        if (it != diffs.end()) {
            diffs.erase(it);
        }
    };

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            auto it = s.lower_bound(x);
            if (it != s.end() && it != s.begin()) {
                remove_diff(*prev(it) ^ *it);
            }
            if (it != s.end()) {
                add_diff(x ^ *it);
            }
            if (it != s.begin()) {
                add_diff(*prev(it) ^ x);
            }
            s.insert(x);
        } else if (type == 2) {
            int x;
            cin >> x;
            auto it = s.find(x);
            auto prv = (it != s.begin() ? prev(it) : s.end());
            auto nxt = next(it);

            if (prv != s.end()) {
                remove_diff(*prv ^ x);
            }
            if (nxt != s.end()) {
                remove_diff(x ^ *nxt);
            }
            if (prv != s.end() && nxt != s.end()) {
                add_diff(*prv ^ *nxt);
            }
            s.erase(it);
        } else {
            cout << *diffs.begin() << "\n";
        }
    }

    return 0;
}

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

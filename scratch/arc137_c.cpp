#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (a[n - 1] - a[n - 2] > 1) {
        cout << "Alice\n";
    } else {
        if ((a[n - 1] - n) % 2 != 0) {
            cout << "Bob\n";
        } else {
            cout << "Alice\n";
        }
    }

    return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;

bool good(long long n, long long x, long long y, long long t) {
    return t / x + t / y >= n;
}

int main() {
    long long n, x, y;
    cin >> n >> x >> y;

    if (x > y) swap(x, y);

    if (n == 1) {
        cout << x << endl;
        return 0;
    }
    long long l = 0;
    long long r = (n - 1) * y;
    while (r - l > 1) {
        long long m = (l + r) / 2;

        if (good(n - 1, x, y, m)) {
            r = m;
        }
        else {
            l = m;
        }
    }
    cout << r + x << endl;
    return 0;
}

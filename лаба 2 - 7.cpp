#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool good(vector<int>& a, int k, int x) {
    int cnt = 0;
    for (int i = 0; i < a.size(); i++) {
        cnt += a[i] / x;
    }
    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int l = 0;
    int r = *max_element(a.begin(), a.end()) + 1;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (good(a, k, m)) {
            l = m;
        }
        else {
            r = m;
        }
    }
    
    cout << l << endl;

    return 0;
}

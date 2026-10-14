
#include <iostream>
#include <sstream>
using namespace std;

void CountSort(int A[], int n) {
    int count[101] = {};

    for (int i = 0; i < n; i++) {
        count[A[i]]++;
    }

    int k = 0;

    for (int i = 0; i <= 100; i++) {
        while (count[i] > 0) {
            A[k++] = i;
            count[i]--;
        }
    }
}

int main() {
    int A[200000];
    int n = 0;
    string line;

    getline(cin, line);
    stringstream ss(line);

    while (ss >> A[n]) {
        n++;
    }

    CountSort(A, n);

    for (int i = 0; i < n; i++) {
        if (i > 0) cout << " ";
        cout << A[i];
    }

    cout << endl;
    return 0;
}

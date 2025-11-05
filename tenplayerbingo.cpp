#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int k;
    for (int i = 0; i < 100; i++) {
        cin >> k;
    }
    int res = k%10;
    if (res == 0) {
        cout << 10 << endl;
    } else {
        cout << res << endl;
    }
}
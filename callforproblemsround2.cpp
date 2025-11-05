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
    int n, k, d;
    cin >> n >> k;
    unordered_map<int, bool> seen;
    int res = 0;
    for (int i = 0; i < n; i++) {
        cin >> d;
        if (!seen[d]) {
            res ++;
            seen[d] = true;
        }
    }
    cout << min(res, k) << endl;

    
}
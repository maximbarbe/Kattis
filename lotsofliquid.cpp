#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
#include <algorithm>
using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    double res = 0;
    double v;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> v;
        res += pow(v, 3.0);
    }
    cout << setprecision(10) << fixed << pow(res, 1/3.0) << endl;
}
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
    int k, s;
    cin >> k >> s;
    cout << s/k + s - k * (s/k) << endl;
}
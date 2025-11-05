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
    int n, d;
    cin >> n;
    vector<int> distances;
    for (int i = 0; i < n; i++) {
        cin >> d;
        distances.push_back(d);
    }
    cout << distances[0] / 3 << " " << distances[1] - 2 * (distances[0]/3) << " " << distances[n - 1]/3 << endl;
}
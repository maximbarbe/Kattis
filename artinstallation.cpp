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
    int r, g, b, cr, cg, cb, crg, cgb;
    cin >> r >> g >> b;
    cin >> cr >> cg >> cb;
    cin >> crg >> cgb;


    int redNeeded = max(r - cr, 0);
    int blueNeeded = max(b - cb, 0);
    int greenNeeded = max(g - cg, 0);
    int total = redNeeded + blueNeeded + greenNeeded;

    if (redNeeded > crg || blueNeeded > cgb || greenNeeded > (crg - redNeeded) + (cgb - blueNeeded)) {
        cout << -1 << endl;
    } else {
        cout << total << endl;
    }

    
}
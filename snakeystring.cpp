#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
#include <string>
#include <algorithm>
using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    int r, c;
    vector<string> grid;
    string res = "";
    cin >> r >> c;
    getline(cin, s);
    for (int i = 0; i< r; i++) {
        getline(cin, s);
        grid.push_back(s);
    }
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++) {
            if(grid[i][j] != '.') {
                res += grid[i][j];
            }
        }
    }
    cout << res << endl;
}
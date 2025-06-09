#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")



#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <string>
#include <unordered_map>
typedef long long ll;



using namespace std;







int main() {
    int r, c, n;
    cin >> r >> c;
    cin >> n;

    vector<vector<int>> grid;
    grid.assign(r, vector<int>());
    for (int i = 0; i < r; i++) {
        grid[i].assign(c, 0);
    }

    int row, col;

    for (int i = 0; i < n; i++) {
        cin >> row >> col;
        row -= 1;
        col -=1;
        grid[row][col] = 1;
    }
    vector<int> res;
    vector<pair<int, int>> dir = {{0, 1}, {0, -1}, {1, 0}, {1, 1}, {1, -1}, {-1, 0}, {-1, 1}, {-1, -1}};
    res.assign(9, 0);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            
            if (grid[i][j] == 1) {
                int cur = 0;
                for (auto [x, y]:dir) {
                        if (i + x >= 0 && i + x < r && j + y >= 0 && j + y < c && grid[i + x][j + y] == 1) {
                            cur ++;
                        }
                }
                res[cur] ++;
            }
 
        }
    }
    for (int i = 0; i < 8; i++) {
        cout << res[i] << " ";
    }
    cout << res[8]<<endl;
}
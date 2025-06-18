#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")



#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <climits>
#include <math.h>
#include <string>
#include <queue>
#include <string>
#include <unordered_map>
typedef long long ll;



using namespace std;



int bfs(int r, int c, int gr, int gc, int lr, int lc) {
    queue<tuple<int, int, int>> q = queue<tuple<int, int, int>>();
    vector<bool> visited;
    visited.assign(r*c, false);
    q.push({gr, gc, 0});
    vector<pair<int, int>> directions = {{2, 1}, {-2, 1}, {2, -1}, {-2, -1}, {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};
    visited[gr*c + gc] = true;

    while (q.size() != 0) {
        tuple<int, int, int> cur = q.front();
        q.pop();
        int curRow = get<0>(cur);
        
        int curCol = get<1>(cur);
        int curMoves = get<2>(cur);
        if (curRow == lr && curCol == lc) {
            return curMoves;
        }
        for (auto &[i, j]:directions) {
            if (curRow + i >= 0 && curRow + i < r && curCol + j >= 0 && curCol + j < c && visited[(curRow + i)*c + curCol + j] == false) {
                visited[(curRow + i)*c + curCol + j] = true;
                q.push({curRow +i, curCol + j, curMoves + 1});
            }
        }


    }
    return INT_MAX;
}



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c, gr, gc, lr, lc;
    while (cin >> r >> c >> gr >> gc >> lr >> lc) {
        int res = bfs(r, c, gr - 1, gc - 1, lr - 1, lc - 1);
        if (res == INT_MAX) {
            cout << "impossible" << endl;
        } else {
            cout << res << endl;
        }
    }
}
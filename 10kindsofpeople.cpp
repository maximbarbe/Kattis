#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <climits>
#include <sstream>
#include <list>
#include <tuple>
#include <queue>
#include <map>

using namespace std;

vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

void bfs(vector<vector<int>> &grid, int a, int b, int color, vector<vector<bool>> &visited) {
    int init = grid[a][b];
    queue<pair<int, int>> q;
    q.push({a, b});
    visited[a][b] = true;
    
    int i, j;
    while (!q.empty()) {
        i = q.front().first;
        j = q.front().second;
        q.pop();
        grid[i][j] = color;
        for (auto [x, y]:directions) {
            if (i + x >= 0 && i + x < grid.size() && j + y >= 0 && j + y < grid[0].size() && !visited[i+x][j+y] && grid[i + x][j + y] == init) {
                visited[i+x][j+y] = true;
                q.push({i+x, j+y});
            }
        }
    }
    
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int r,c;
    vector<vector<int>> grid;
    vector<vector<int>> gridCopy;
    vector<vector<bool>> visited;
    cin >> r >> c;
    visited.assign(r, vector<bool>());
    string temp;
    for (int i = 0; i < r; i++) {
        visited[i].assign(c, false);
        vector<int> row;
        cin >> temp;
        for (auto ch:temp) {
            row.push_back(ch - '0');
        }

        vector<int> rowCopy(row);
        grid.push_back(row);
        gridCopy.push_back(rowCopy);
    }
    int color = 1;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c;j++) {
            if (!visited[i][j]) {
                color ++;
                bfs(gridCopy, i, j, color, visited);
            }
        }
    }
    int t, r1, c1, r2, c2;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> r1 >> c1 >> r2 >> c2;
        r1 --;
        c1 --;
        r2 --;
        c2 --;
        if (gridCopy[r1][c1] != gridCopy[r2][c2]) {
            cout << "neither" << endl;
        } else {
            if (grid[r1][c1] == 1) {
                cout << "decimal" << endl;
            } else {
                cout << "binary" << endl;
            }
        }
    }

}
#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")


#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string>
using namespace std;

class UnionFind{
    private:
        vector<int> sets;
        vector<int> rank;
        


    public:
        int numberSets;
        UnionFind(int n) {
            numberSets = n;
            for (int i = 0; i < n; i++) {
                sets.push_back(i);
                rank.push_back(0);
                
            }
        }

        int find(int id) {
            if (sets[id] == id) {
                return id;
            }
            return find(sets[id]);
        }

        bool isSameSet(int id1, int id2) {
            return find(id1) == find(id2);
        }

        void Union (int id1, int id2) {
            int smaller = find(id1);
            int larger = find(id2);
            if (smaller == larger) {
                return;
            }
            if (rank[smaller] > rank[larger]) {
                swap(smaller, larger);
            } else if (rank[smaller] == rank[larger]) {
                rank[larger] += 1;
            }
            sets[smaller] = larger;
            numberSets --;
            return;
        }
};



int main() {
    int t, n;
    cin >> t;
    while (t != 0) {
        
        cin.ignore();
        cin >> n;
        UnionFind ufds = UnionFind(n);
        vector<pair<double, double>> points;
        vector<tuple<double, int, int>> edges;
        double x, y;
        for (int i = 0; i < n; i++) {
            cin >> x >> y;
            for (int j = 0; j < points.size(); j++) {
                double distance =hypot(abs(x - points[j].first), abs(y - points[j].second));
                edges.push_back(make_tuple(distance, i, j));
            }
            points.push_back({x, y});
        }
        double res = 0;
        sort(edges.begin(), edges.end());
        double dist;
        int src, dest;
        for (int i = 0; i < edges.size(); i++) {
            if (ufds.numberSets == 1) {
                break;
            }
            dist = get<0>(edges[i]);
            src = get<1>(edges[i]);
            dest = get<2>(edges[i]);
            if (!ufds.isSameSet(src, dest)) {
                res += dist;
                ufds.Union(src, dest);
            }
        }
        t --;
        cout << fixed << setprecision(2) << res  << endl;
    }
    
}
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <climits>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::map<int, int> candidates;
    int n;

    std::cin >> n;

    for (int i = 0; i < n; i++) {
        int count = 0;
        int total_votes = 0;
        int max_votes = INT_MIN;
        int winner = 0;
        int m;
        std:: cin >>m;
        for (int j = 1; j < m + 1;j++) {
            std:: cin>>candidates[j];
            total_votes += candidates[j];
            if (candidates[j] > max_votes) {
                winner = j;
                max_votes = candidates[j];
                count = 1;
            } else if (candidates[j] == max_votes) {
                count ++;
            }
        }
        if (count != 1) {
            std::cout<<"no winner\n";
        } else {
            if (max_votes > total_votes/2) {
                std::cout<<"majority winner " <<winner<<"\n";
            } else {
                std::cout<<"minority winner " <<winner<<"\n";
            }
        }
    }

    
}
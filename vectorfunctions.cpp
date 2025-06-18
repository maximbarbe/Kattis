#include <algorithm>


#include "vectorfunctions.h"

using namespace std;
void backwards(vector<int>& vec){
    int start = 0;
    int end = vec.size() - 1;
    while (start < end) {
        swap(vec[start], vec[end]);
        start += 1;
        end -= 1;
    }
}

vector<int> everyOther(const vector<int>& vec){
    vector<int> new_vector;
    for (int i = 0; i < vec.size(); i += 2) {
        new_vector.push_back(vec[i]);
    }
    return new_vector;
}

int smallest(const vector<int>& vec){

    return *min_element(vec.begin(), vec.end());
}

int sum(const vector<int>& vec){
    int res = 0;
    for (int i = 0; i < vec.size(); i++) {
        res += vec[i];
    }
    return res;
}

int veryOdd(const vector<int>& suchVector){
    int res = 0;
    for (int i = 0; i < suchVector.size(); i++) {
        if (suchVector[i] % 2 == 1 && i % 2 == 1) {
            res += 1;
        }
    }
    return res;
}
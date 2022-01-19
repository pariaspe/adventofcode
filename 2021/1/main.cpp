#include <iostream>
#include <fstream>
#include<vector>
using namespace std;
 
ifstream infile("input.txt");

int count_increment(){
    int current, previous, cont = 0;
    while (infile >> current){
        if (current > previous) {
            cont += 1;
        }
        previous = current;
    }
    return cont;
}

vector<int> count_sums(){
    vector<int>measurements;

    int m;
    while(infile >> m){
        measurements.push_back(m);
    }

    return measurements;
}

int main()
{
    // Part 1
    //int increment = count_increment();
    //cout << "Increment: " << increment << "\n";


    // Part 2
    vector<int> test = count_sums();
    vector<int>::size_type sz = test.size();
    int current, prev, cont = -1;
    for (auto i=0; i<sz; i++) {
        if (i-1 < 0) { continue; }  // skip partial window
        if (i+1 > sz) { break; }  // last window

        current = test[i-1] + test[i] + test[i+1];
        if (current > prev) { cont += 1; }
        prev = current;
    }

    cout << cont << "\n";
    return 0;
}
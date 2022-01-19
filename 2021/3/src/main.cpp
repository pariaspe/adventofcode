#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

struct Bit {
    unsigned int value:1;
};
typedef struct Bit bit;
typedef vector<bit> bits;


ifstream infile("../2021/3/input.txt");

void read_input(vector<bits> &input){
    string line; 
    while (infile >> line){
        bits bline;
        for (uint i=0; i<line.length(); i++) {
            bit b;
            b.value = line[i];
            bline.push_back(b);
        }
        input.push_back(bline);
    }
}

void print_bits(bits input){
    bits::size_type sz = input.size();
    for (uint i=0; i<sz; i++) {
        cout << input[i].value;
    }
}

void proccess_input(vector<bits> input, int conts[]){
    vector<bits>::size_type sz = input.size();
    for (uint i=0; i<sz; i++) {
        bits::size_type sz2 = input[i].size();
        for (uint j=0; j<sz2; j++){
            if ( input[i][j].value ) {
                conts[j] += 1;
            } else {
                conts[j] -= 1;
            }
        }
    }
}

long fromBin(long n)
{
    long factor = 1;
    long total = 0;

    while (n != 0)
    {
        total += (n%10) * factor;
        n /= 10;
        factor *= 2;
    }

    return total;
}

int calc_gamma(int conts[]){
    long bin_number = 0;
    for (auto i=0; i<12; i++) {
        cout << conts[i] << " ";
        if ( conts[i] > 0 ) {
            bin_number += pow(10, (11-i));
        }
    }
    cout << bin_number << "\n";
    long number = fromBin(bin_number);
    return number;
}

int calc_epsilon(int conts[]){
    long bin_number = 0;
    for (auto i=0; i<12; i++) {
        cout << conts[i] << " ";
        if ( conts[i] < 0 ) {
            bin_number += pow(10, (11-i));
        }
    }
    cout << bin_number << "\n";
    long number = fromBin(bin_number);
    return number;
}

void filterBits(vector<bits> &bitList, int pose, int criteria){
    vector<bits>::iterator it = bitList.begin();
    for ( ; it != bitList.end(); ){
        if ( (*it)[pose].value != criteria) {
            it = bitList.erase(it);
        } else {
            ++it;
        }
    }
}

bits getOxygen(vector<bits> bitList){
    int i = 0;
    while (bitList.size() > 1) {
        // cout << "Iteracion " << i << " filtadros " << bitList.size() << "\n";

        int conts[bitList[0].size()] = {0};
        proccess_input(bitList, conts);
        // for (int j=0; j<12; j++) cout << conts[j] << " "; cout << "\n";

        int bitCriteria;
        if ( conts[i] >= 0 ) { bitCriteria = 1; } else { bitCriteria = 0; }
        filterBits(bitList, i, bitCriteria);
        i += 1;
        if (i > 12) { cout << "error\n"; break; }
    }
    // cout << bitList.size() << "\n";
    // print_bits(bitList[0]);
    return bitList[0];
}

bits getCO2(vector<bits> bitList){
    int i = 0;
    while (bitList.size() > 1) {
        // cout << "Iteracion " << i << " filtadros " << bitList.size() << "\n";

        int conts[bitList[0].size()] = {0};
        proccess_input(bitList, conts);
        // for (int j=0; j<12; j++) cout << conts[j] << " "; cout << "\n";

        int bitCriteria;
        if ( conts[i] >= 0 ) { bitCriteria = 0; } else { bitCriteria = 1; }
        filterBits(bitList, i, bitCriteria);
        i += 1;
        if (i > 12) { cout << "error\n"; break; }
    }
    // cout << bitList.size() << "\n";
    // print_bits(bitList[0]);
    return bitList[0];
}


long fromBits(bits n){
    long bin_number = 0;
    for (uint i=0; i<n.size(); i++) {
        bin_number += n[i].value*pow(10, (11-i));
    }
    // cout << bin_number << "\n";
    long number = fromBin(bin_number);
    return number;
}

int main()
{
    // Part 1
    vector<bits> bitsInput;
    read_input(bitsInput);
    print_bits(bitsInput[0]);

    int conts[bitsInput[0].size()] = {};
    proccess_input(bitsInput, conts);
    cout << conts[0] << conts[1] << "\n";

    int gamma = calc_gamma(conts);
    cout << gamma << "\n";
    int epsilon = calc_epsilon(conts);
    cout << epsilon << "\n";

    cout << "Sol: " << gamma*epsilon << "\n";

    // Part 2
    vector<bits> myBits = bitsInput;
    long oxygen = fromBits(getOxygen(myBits));
    cout << oxygen << "\n";
    myBits = bitsInput;
    long co2 = fromBits(getCO2(myBits));
    cout << co2 << "\n";
    cout << "Sol: " << oxygen*co2 << "\n";

    return 0;
}
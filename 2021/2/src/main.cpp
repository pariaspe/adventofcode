#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
 
ifstream infile("../2021/2/input.txt");

int read_cmds(int cmds[]){
    string cmd;
    int n; 
    while (infile >> cmd >> n){
        if (cmd == "forward") { cmds[0] += n; } else 
        if (cmd == "down") { cmds[1] += n; } else 
        if (cmd == "up") { cmds[2] += n; } else { cout << cmd << n; }
    }
    return 0;
}

void calc_output(int cmds[]){
    cout << cmds[0] << " " << cmds[1] << " " << cmds[2] << "\n";
    cout << cmds[0] << " " << cmds[1] - cmds[2] << "\n";
    cout << cmds[0] * (cmds[1] - cmds[2]) << "\n";
}

void new_method(int &hor, int &depth) {
    string cmd;
    int n;
    int aim = 0;
    while (infile >> cmd >> n){
        if (cmd == "forward") { hor += n; depth += aim * n; } else 
        if (cmd == "down") { aim += n; } else 
        if (cmd == "up") { aim -= n; } else { cout << cmd << n; }
    }
}

int main()
{
    // Part 1
    // int cmds[3] = {0, 0, 0};  // forward down up
    // read_cmds(cmds);
    // calc_output(cmds);

    // Part 2
    int hor = 0;
    int depth = 0;
    new_method(hor, depth);
    cout << hor << " " << depth << " " << hor*depth << "\n";
    return 0;
}
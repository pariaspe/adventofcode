#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

const unsigned int BOARDSIZE = 5;

class Board {
  struct Cell {
    unsigned int value;
    bool called = false;
  };
  typedef struct Cell cell;

public:
  cell board[BOARDSIZE][BOARDSIZE];
  bool winner_;

  Board() {
    for (uint i = 0; i < BOARDSIZE; i++) {
      for (uint j = 0; j < BOARDSIZE; j++) {
        board[i][j].value = 0;
      }
    }
  }

  Board(int b[BOARDSIZE][BOARDSIZE]) {
    for (uint i = 0; i < BOARDSIZE; i++) {
      for (uint j = 0; j < BOARDSIZE; j++) {
        board[i][j].value = b[i][j];
      }
    }
  }

  bool winner() { return checkHor() || checkVert(); }

  vector<uint> getUncalled() {
    vector<uint> numbers;
    for (uint i = 0; i < BOARDSIZE; i++) {
      for (uint j = 0; j < BOARDSIZE; j++) {
        if (!board[i][j].called) {
          numbers.push_back(board[i][j].value);
        }
      }
    }
    return numbers;
  }

  void callNumber(uint n) {
    for (uint i = 0; i < BOARDSIZE; i++) {
      for (uint j = 0; j < BOARDSIZE; j++) {
        if (n == board[i][j].value) {
          board[i][j].called = true;
        }
      }
    }
  }

  void print() {
    for (uint i = 0; i < BOARDSIZE; i++) {
      for (uint j = 0; j < BOARDSIZE; j++) {
        if (board[i][j].called) {
          cout << " \e[1m" << board[i][j].value << "\e[0m";
        } else {
          cout << " " << board[i][j].value;
        }
      }
      cout << "\n";
    }
  }

private:
  bool checkHor() {
    bool winner = true;
    for (uint i = 0; i < BOARDSIZE; i++) {
      winner = true;
      for (uint j = 0; j < BOARDSIZE; j++) {
        winner = winner && board[i][j].called;
      }
      if (winner) {
        break;
      }
    }
    return winner;
  }

  bool checkVert() {
    bool winner = true;
    for (uint i = 0; i < BOARDSIZE; i++) {
      winner = true;
      for (uint j = 0; j < BOARDSIZE; j++) {
        winner = winner && board[j][i].called;
      }
      if (winner) {
        break;
      }
    }
    return winner;
  }
};

class Bingo {
public:
  vector<unsigned int> numbers;
  vector<Board> boards;

  vector<uint> uncalledNumbers;
  int lastNumber = -1;

  Bingo(string filename) {
    ifstream infile(filename);

    string header;
    infile >> header;
    size_t pos;
    string token;
    while ((pos = header.find(",")) != header.npos) {
      token = header.substr(0, pos);
      numbers.push_back(stoi(token));
      header.erase(0, pos + 1);
    }
    numbers.push_back(stoi(header));

    while (infile.peek() != EOF) {
      unsigned int value;
      int b[BOARDSIZE][BOARDSIZE];
      for (uint i = 0; i < BOARDSIZE; i++) {
        for (uint j = 0; j < BOARDSIZE; j++) {
          infile >> value;
          b[i][j] = value;
        }
      }

      Board board(b);
      boards.push_back(board);
    }
  }

  vector<Board> getNonWinners() {
    vector<Board> nonWinners;
    vector<Board>::iterator it;
    for (it = boards.begin(); it != boards.end(); it++) {
      if (!(*it).winner()) {
        nonWinners.push_back((*it));
      }
    }
    return nonWinners;
  }

  void callNumber(int n) {
    vector<Board>::iterator it;
    for (it = boards.begin(); it != boards.end(); it++) {
      (*it).callNumber(n);
    }
  }

  vector<Board>::iterator getWinner() {
    vector<Board>::iterator it;
    for (it = boards.begin(); it != boards.end(); it++) {
      if ((*it).winner()) {
        return it;
      }
    }
    return boards.end(); // empty iterator
  }

  void findFirstWinner() {
    vector<uint>::iterator it;
    vector<Board>::iterator itWinner;
    for (it = numbers.begin(); it != numbers.end(); it++) {
      callNumber((*it));
      if ((itWinner = getWinner()) != boards.end()) {
        break;
      }
    }

    lastNumber = (*it);
    uncalledNumbers = (*itWinner).getUncalled();
  }

  void findLastWinner() {
    Board last;
    vector<uint>::iterator it;
    for (it = numbers.begin(); it != numbers.end(); it++) {
      callNumber((*it));
      cout << "N: " << (*it) << " " << getNonWinners().size() << endl;
      if (getNonWinners().size() == 1) {
        last = getNonWinners()[0];
      }
      if (getNonWinners().size() < 1) {
        break;
      }
    }

    lastNumber = (*it);
    last.callNumber(lastNumber);
    uncalledNumbers = last.getUncalled();

    last.print();
  }

  void printNumbers() {
    vector<unsigned int>::iterator it;
    for (it = numbers.begin(); it != numbers.end(); it++) {
      cout << (*it) << " ";
    }
    cout << endl;
  }

  void printBoards() {
    vector<Board>::iterator it;
    for (it = boards.begin(); it != boards.end(); it++) {
      (*it).print();
      cout << endl;
    }
  }

  void printWinner() {
    if (lastNumber == -1) {
      cout << "No winner" << endl;
      return;
    }

    cout << "Last number: " << lastNumber << endl;

    vector<uint>::iterator it;
    for (it = uncalledNumbers.begin(); it != uncalledNumbers.end(); it++) {
      cout << (*it) << " ";
    }

    cout << endl;
  }

  int getScore() {
    if (lastNumber == -1) {
      return 0;
    }

    int sum = 0;
    vector<uint>::iterator it;
    for (it = uncalledNumbers.begin(); it != uncalledNumbers.end(); it++) {
      sum += (*it);
    }
    return sum * lastNumber;
  }
};

int main() {
  Bingo myBingo("../4/input.txt");
  // myBingo.printBoards();
  // myBingo.printNumbers();

  // Part 1
  // myBingo.findFirstWinner();
  // myBingo.printWinner();
  // cout << "Score: " << myBingo.getScore() << endl;

  // Part 2
  myBingo.findLastWinner();
  myBingo.printWinner();
  cout << "Score: " << myBingo.getScore() << endl;

  return 0;
}

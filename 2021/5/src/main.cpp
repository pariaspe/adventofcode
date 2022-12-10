#include <algorithm> // std::max
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

template <typename T> int sgn(T val) { return (T(0) < val) - (val < T(0)); }

struct Coord {
  uint x = 0;
  uint y = 0;

  bool const operator==(const Coord &o) const { return x == o.x && y == o.y; }
  bool const operator<(const Coord &o) const {
    return x < o.x || (x == o.x && y < o.y);
  }
};
typedef Coord coord;
struct Line {
  coord start;
  coord end;
};
typedef Line line;
typedef vector<line> lines;

class Vent {
public:
  coord start;
  coord end;

public:
  Vent(){};
  Vent(line p) {
    start = p.start;
    end = p.end;
  };
  Vent(coord s, coord e) {
    start = s;
    end = e;
  };
  Vent(uint x1, uint y1, uint x2, uint y2);
  ~Vent(){};

  void print() {
    cout << start.x << "," << start.y << " -> " << end.x << "," << end.y
         << endl;
  };
  bool isStraight() { return (start.x == end.x || start.y == end.y); };
  bool isDiagonal();
  vector<coord> getPoints();
};

Vent::Vent(uint x1, uint y1, uint x2, uint y2) {
  start.x = x1;
  start.y = y1;
  end.x = x2;
  end.y = y2;
}

bool Vent::isDiagonal() {
  int dx = end.x - start.x, dy = end.y - start.y;
  return abs(dx) == abs(dy);
}

vector<coord> Vent::getPoints() {
  vector<coord> myCoords;
  if (start.x == end.x && start.y == end.y) {
    myCoords.push_back(start);
  } else if (start.x == end.x) {
    for (uint i = min(start.y, end.y); i <= max(start.y, end.y); i++) {
      coord c;
      c.x = start.x;
      c.y = i;
      myCoords.push_back(c);
    }
  } else if (start.y == end.y) {
    for (uint i = min(start.x, end.x); i <= max(start.x, end.x); i++) {
      coord c;
      c.x = i;
      c.y = start.y;
      myCoords.push_back(c);
    }
  } else if (isDiagonal()) {
    int dx = end.x - start.x, dy = end.y - start.y;
    for (int i = 0; i <= abs(dx); i++) { // abs(dx) == abs(dy)
      coord c;
      c.x = start.x + i * sgn(dx);
      c.y = start.y + i * sgn(dy);
      myCoords.push_back(c);
    }
  } else {
    ; // TODO
  }

  return myCoords;
}

vector<Vent> readVents(string filename) {
  ifstream infile(filename);
  size_t pos;
  string start, arrow, end;
  vector<Vent> vents;
  while (infile.peek() != EOF) {
    infile >> start >> arrow >> end;
    pos = start.find(",");
    uint x1 = stoi(start.substr(0, pos));
    uint y1 = stoi(start.substr(pos + 1, start.length()));
    pos = end.find(",");
    uint x2 = stoi(end.substr(0, pos));
    uint y2 = stoi(end.substr(pos + 1, end.length()));
    Vent ventRead(x1, y1, x2, y2);
    // ventRead.print();
    vents.push_back(ventRead);
  }
  return vents;
}

int main() {
  vector<Vent> myVents = readVents("../5/input.txt");

  map<coord, int> ventPoses;
  vector<Vent>::iterator it;
  for (it = myVents.begin(); it != myVents.end(); ++it) {
    if (it->isStraight() ||
        it->isDiagonal()) { // Part 1 --> only straight lines
      // it->print();
      vector<coord> pts;
      pts = it->getPoints();
      vector<coord>::iterator it3;
      for (it3 = pts.begin(); it3 != pts.end(); ++it3) {
        ++ventPoses[(*it3)];
      }
    }
  }

  int cont = 0;
  map<coord, int>::iterator it2;
  for (it2 = ventPoses.begin(); it2 != ventPoses.end(); ++it2) {
    if (it2->second > 1) {
      // cout << it2->first.x << " " << it2->first.y << " => " << it2->second <<
      // '\n';
      cont++;
    }
  }

  cout << cont << endl;
  return 0;
}
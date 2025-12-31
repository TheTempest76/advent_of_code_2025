# include <string>
# include <fstream>

using namespace std;


int main() {
    ifstream inputFile("input.txt");
    string line;
    int sum = 0;

    while (getline(inputFile, line)) {
        sum += stoi(line);
    }

    inputFile.close();
    return sum;
}
#include <iostream>
#include <fstream>
using namespace std;

// int main() {
//     ofstream filestream("testout.txt");
//     if (filestream.is_open()) {
//         filestream << "Welcome to C++. \n";
//         filestream << "C++ YYDS.\n";
//         filestream.close();
//     }
//     else cout << "File opening is fail.";

//     return 0;
// }

// int main() {
//     string srg;
//     ifstream filestream("testout.txt");
//     if (filestream.is_open()) {
//         while (getline(filestream, srg)) {
//             cout << srg << endl;
//         }
//         filestream.close();
//     }
//     else cout << "File opening is fail." << endl;

//     return 0;
// }

int main() {
    char input[75];
    ofstream os;
    os.open("testout.txt");
    cout << "Writing to a text file: " << endl;
    cout << "Please Enter your name: ";
    cin.getline(input, 100);
    os << input << endl;
    cout << "Please Enter your age: ";
    cin >> input;
    cin.ignore();
    os << input << endl;
    os.close();

    ifstream is;
    string line;
    is.open("testout.txt");
    cout << "Reading from a text file: " << endl;
    while (getline(is, line)) {
        cout << line << endl;
    }
    is.close();

    return 0;
}
/*

Objective
In this challenge, we review some basic concepts that will get you started with
this series. You will need to use the same (or similar) syntax to read input and
 write output in challenges throughout HackerRank. Check out the Tutorial tab
 for learning materials and an instructional video!

Task
To complete this challenge, you must save a line of input from stdin to a
variable, print Hello, World. on a single line, and finally print the value of
your variable on a second line.

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    // Declare a variable named 'input_string' to hold our input.
    string input_string;

    // Read a full line of input from stdin (cin) and save it to our variable, input_string.
    getline(cin, input_string);

    // Print a string literal saying "Hello, World." to stdout using cout.
    cout << "Hello, World." << endl;

    // TODO: Write a line of code here that prints the contents of input_string to stdout.
    cout<<input_string;
    return 0;
}

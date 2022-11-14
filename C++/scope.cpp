# include <iostream>
# include <iomanip>
using namespace std;
int c = 10;
int main (){
    int c=5;
    cout<<"local value of c is = "<<c<<endl<<"The Global value of c is = "<<::c<<endl;
    // Constants in C++
    const int a = 3;
    cout<<"Variable (a) is a constant value and it's value = "<<a;
    /*manipulators are the operators that modify data display
    They are:
        *endl
        *setw(<width_size>): you can use it to display matrix
                             This ensures that every output occupies just the size of width
    */
}
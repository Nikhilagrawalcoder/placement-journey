#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    char c;
    cout << "enter two number";
    cin >> a >> b;
    cout << "enter operation ";
    cin >> c;
    switch (c)
    {
    case ('+'):
        cout << a + b;
        break;
    case ('-'):
        cout << a - b;
        break;
    case ('*'):
        cout << a * b;
        break;
    case ('/'):
        cout << (float)a / b;
        break;
    case ('%'):
        cout << a % b;
        break;
    default:
        cout << "invalid operation";
    }
    return 0;
}
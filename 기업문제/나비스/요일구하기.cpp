#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	char input[100];
    int a,b = 0;
	cin >> a >> b;
    string answer = "";
    string day[7] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int month[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int sum = 0;
    for(int i = 0; i < a; i++) {
        sum += month[i];
    }

    sum += b-1;
    
    if(month[a] < b){
        cout << "ERROR" << endl;    
        return 0;
    }
    answer = day[sum%7];
	cout << answer << endl;

	return 0;
}


#include <iostream>
#include <vector>

using namespace std;
int main() {
	char input[100];
    int shop, day;
	int i,j,total,n;
    cin >> shop >> day;
    std::vector<int> numbers;
    std::vector<int> a_shop;

    for(i=0;i<shop;i++){
        for(i=0;i<day;i++){
            cin >> n;
            a_shop.push_back(n);
        }
    }

	cout << "Hello Goorm! Your input is " << input << endl;
	return 0;
}
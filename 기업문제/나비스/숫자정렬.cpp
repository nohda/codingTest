// #include <iostream>
// #include <algorithm>
 
// using namespace std;
// int  count;

// bool desc(int a, int b){
//     ::count+=1;
//     return a > b;
// }
// int main(void){
//     // int count = 0;
//     int data[10] = {9, 3, 5, 7, 8, 1, 2, 4, 6, 10};
    
//     sort(data, data+10);
//     for(int i=0; i<10; i++){
//         cout << data[i] << ' ';
//     }
//     cout << endl;

//     sort(data, data+10, desc);
//     for(int i=0; i<10; i++){
//         cout << data[i] << ' ';
//     }
//     std::cout << ::count << ' ';
//     return 0;
// }

#include <iostream>
#include <algorithm>
 
using namespace std;
int  count;

bool desc(int a, int b){
    ::count+=1;
    return a > b;
}
int main(void){
    // int count = 0;
    int n = 5;
    int data[5] = {1,3,2,5,4};
    
    sort(data, data+n);
    for(int i=0; i<n; i++){
        cout << data[i] << ' ';
    }
    cout << endl;

    sort(data, data+n, desc);
    for(int i=0; i<n; i++){
        cout << data[i] << ' ';
    }
    std::cout << ::count << ' ';
    return 0;
}

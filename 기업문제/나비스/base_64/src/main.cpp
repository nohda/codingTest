#include <iostream>
#include <string>

using namespace std;

void convert_encode(string input){
    char base64_ascii[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    const int n = 8;
    int i;
    string conv_input;
    string output;
    string tmp;
    for(i=0;i<input.size();i++){
        string binary = bitset<n>(input.at(i)).to_string();
        conv_input+= binary;
    }
    for(i=0;i<conv_input.size();i=i+6){
        string conv = conv_input.substr(i,6);
        if(conv.size()<6){
            tmp = conv;
            break;
        }
        output += base64_ascii[(int)(bitset<10>(conv).to_ullong())];
    }
    if(input.size()%3 !=0 && tmp != ""){
        for(i=0;i<3-(input.size()%3);i++){
            tmp+="00000000";
        }
        for(i=0;i<tmp.size();i=i+6){
            string conv = tmp.substr(i,6);
            if(tmp.substr(i,6)=="000000"){
                output+="=";
                break;
            }
            output += base64_ascii[(int)(bitset<10>(conv).to_ullong())];
        }
    }

    cout << "Result : " << output << "\n" << endl;
}

void convert_decode(string input){
    int i;
    string tmp;
    string output;
    string base64_ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    string del;
    for(i=0;i<input.size();i++){
        // cout << input.at(i) << endl;
        // cout << base64_ascii.find(input.at(i)) << endl;
        if(input.at(i) == '='){
            del += "00";
        }
        else{
            tmp.append(bitset<6>(base64_ascii.find(input.at(i))).to_string());
        }
    }
    if(del.size()>0){
        tmp = tmp.substr(0,tmp.size()-2);
    }
    // cout << tmp << " " <<  tmp.size() << endl;
    for(i=0;i<tmp.size();i=i+8){
        int m =  bitset<8>(tmp.substr(i,i+8)).to_ulong();
        output+=static_cast<char>(m);
    }
    cout << "Result : " << output << endl;
    
}


int main(){

    // string input = "TmF2a2luZ2RvbQ==";
    // string input = "Navis";
    // string input = "TmF2aXM=";
    string mode;
    string input;
    const static int n = 10;
    string binary = bitset<n>('a').to_string();
    cout << binary << endl;
    // convert_decode(input);
    // cout << "Input mode (E:Encode, D:Decode, Q:Quit)" << endl;
    // cin >> mode;

    // while(mode != "Q"){
    //     cin >> input;
    //     if(mode == "E"){
    //         convert_encode(input);
    //     }
    //     else if(mode == "D"){
    //         convert_decode(input);
    //     }   
    //     cout << "Input mode (E:Encode, D:Decode, Q:Quit)" << endl;
    //     cin >> mode;
    // }
    
    return 0;
}
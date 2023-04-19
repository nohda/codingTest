#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//===========================================================
// base64
//===========================================================
std::wstring base64Encode(const wstring input){
	//string utf8_input = wstrToUtf8(input);

	unsigned char const* buffer = (unsigned const char*)(input.c_str());
	size_t size = input.length();

    using std::wstring;
    static wchar_t const* base64Table =
        L"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    
	// for =
    // size_t base64Size = (size + 2 - ((size + 2) % 3)) / 3 * 4;
	// wstring result(base64Size, L'=');

	size_t base64Size = ceil(size * 4.0 / 3);
    wstring result(base64Size, L'');

    unsigned char const* s = buffer;  // source pointer
    size_t di = 0;                    // destination index
    for(size_t i = 0; i < size / 3; i++){
        // input: 0000_0000 0000_0000 0000_0000
        // 
        // out1:  0000_00
        // out2:         00 0000
        // out3:                _0000 00
        // out4:                        00_0000
        
        result[di++] = base64Table[s[0] >> 2];
        result[di++] = base64Table[((s[0] << 4) | (s[1] >> 4)) & 0x3f];
        result[di++] = base64Table[((s[1] << 2) | (s[2] >> 6)) & 0x3f];
        result[di++] = base64Table[s[2] & 0x3f];
        s += 3;
    }

    size_t remainSize = size % 3;
    switch(remainSize){
    case 0:
        break;
    case 1:
        result[di++] = base64Table[s[0] >> 2];
        result[di++] = base64Table[(s[0] << 4) & 0x3f];
        break;
    case 2:
        result[di++] = base64Table[s[0] >> 2];
        result[di++] = base64Table[((s[0] << 4) | (s[1] >> 4)) & 0x3f];
        result[di++] = base64Table[(s[1] << 2) & 0x3f];
        break;
    default:
        throw std::logic_error("Should not happen.");
    }
    return result;
}

int main() {
	wcout.imbue(locale("korean"));

	wstring plain(L"대한민국");
	wcout << base64Encode(plain).c_str() << endl;

	return 0;
}

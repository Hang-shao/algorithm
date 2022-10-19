#include <iostream>
#include "string"
#include "math.h"
using namespace std;

//二进制转换为十六进制函数实现
string BinToHex(string str) {
    string hex = "";//用来存储最后生成的十六进制数
    int temp = 0;//用来存储每次四位二进制数的十进制值
    while (str.size() % 4 != 0) {//因为每四位二进制数就能够成为一个十六进制数，所以将二进制数长度转换为4的倍数
        str = "0" + str;//最高位添0直到长度为4的倍数即可
    }
    for (int i = 0; i < str.size(); i += 4) {
        temp = (str[i] - '0') * 8 + (str[i + 1] - '0') * 4 + (str[i + 2] - '0') * 2 + (str[i + 3] - '0') * 1;//判断出4位二进制数的十进制大小为多少
        if (temp < 10) {//当得到的值小于10时，可以直接用0-9来代替
            hex += to_string(temp);
        }
        else {//当得到的值大于10时，需要进行A-F的转换
            hex += 'A' + (temp - 10);
        }
    }
    return hex;
}

//十六进制转换为二进制函数实现
string HexToBin(string str) {
    string bin = "";
    string table[16] = { "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111" };
    for (int i = 0; i < str.size(); i++) {
        if (str[i] >= 'A'&&str[i] <= 'F') {
            bin += table[str[i] - 'A' + 10];
        }
        else {
            bin += table[str[i] - '0'];
        }
    }
    return bin;
}

//二进制转换为十进制的函数实现
int BinToDec(string str) {
    int dec = 0;
    for (int i = 0; i < str.size(); i++) {
        dec += (str[i] - '0')*pow(2, str.size() - i - 1);
    }
    return dec;
}

//十进制转换为二进制的函数实现
string DecToBin(int str) {
    string bin = "";
    while (str >= 1) {
        bin = to_string(str % 2) + bin;
        str = str / 2;
    }
    return bin;
}

//十六进制转换为十进制的函数实现
int HexToDec(string str) {
    int dec = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] >= 'A'&&str[i] <= 'F') {
            dec += (str[i] - 'A' + 10)*pow(16, str.size() - i - 1);
        }
        else {
            dec += (str[i] - '0')*pow(16, str.size() - i - 1);
        }
    }
    return dec;
}

//十进制转换为十六进制的函数实现
string DecToHex(int str) {
    string hex = "";
    int temp = 0;
    while (str >= 1) {
        temp = str % 16;
        if (temp < 10 && temp >= 0) {
            hex = to_string(temp) + hex;
        }
        else {
            hex += ('A' + (temp - 10));
        }
        str = str / 16;
    }
    return hex;
}
int main() {
    int a=1005;
    cout << "十进制："<<a<<endl;
    cout << "十六进制："<<DecToHex(a)<< endl;
    cout << "二进制："<<DecToBin(a)<< endl;
    return 0;
}

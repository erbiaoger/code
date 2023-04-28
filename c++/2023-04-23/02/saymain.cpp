/* saymain.cpp */
#include "say.h"
int main(int argc, char *argv[]) {
    extern Say librarysay;
    Say localsay = Say("local intstance of Say");
    sayhello();
    librarysay.sayThis("howdy");
    librarysay.sayString();
    localsay.sayString();
    return(0);

}
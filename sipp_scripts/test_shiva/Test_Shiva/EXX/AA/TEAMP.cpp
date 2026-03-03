#include <iostream>
#include <cstdio>
using namespace std;

typedef struct
{
    int        len;          // Maximum length of the string
    char        string[1];    // Pointer to first byte of the string
} cmn_string_t;


int main() {
cmn_string_t *flags;
cmn_string_t *ptr;

cout<<"FLAGS ="<<flags;
cout<<"\n ptr  =" <<ptr;
return 0;
}



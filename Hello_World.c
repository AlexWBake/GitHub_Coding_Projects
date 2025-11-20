/* To compile go to command prompt and go to directory containing this file
 and run gcc Hello_World.c */
#include <stdio.h>
#include <stdbool.h>

int main() //main function
{
    printf("Hello World\n");
    printf("I like Pizza\n");

    /* escape sequence = character combination consisting of a backslash \ 
                        followed by a letter or combination of digits.
                        They specify actions within a line or string of text
                        \n = newline
                        \t = tab
                        \" Ignores " as a string same for \'
                        */
    printf("Hello\tWorld\n\"Wassup\'");
    /* variables = Allocated space in memory to store a value
                    we refer to variables's name to access stored value
                    that variable now behaves as if it was the value it contains
                    But we need to declare what type of data we are storing*/
    int x; //declaration
    x = 20; //initialization
    int y = 3; //integer
    float gpa = 2.05; //floating point number
    float pi = 3.141592653589793;
    char grade = 'C'; //single character (use ')
    char name[]= "Alex Baker"; //array of characters
    
    // %letter = format specifier
    printf("\nHello my name is %s I am %d years old. I am %d", name, y); // %s = string type 
    printf("\nYou are %d years old",y); // %d = interger type
    printf("\nYou average grade is a %c",grade); // %c = character type
    printf("\nYou have a %f gpa",gpa); // %f = float / %lf = long float
    printf("\npi is equal to %f",pi); // This is considered a float 
    printf("\npi is equal to %0.15lf",pi);// This is considered a double or long float 0.15 says how many characters to display from the float
    bool T = true;
    bool F = false;
    printf("\n%d",T); // 1 = True / 0 = 
    printf("\n%d",F);
    char num = 100; // char can store any number between -128 to 127 becaue it has 1 byte of memory
    unsigned char num1 = 255; /* when you make char unsigned it disregards negative 
    number so it can store a number between 0 to 255. If made into 256 it will overflow and become 0*/
    printf("\n%c",num); // %c will display a number in the ASCII representation (d)
    printf("\n%d",num); // %d will display the number
    // for short int you can just type short
    short int h = 32767; // can store 2 bytes of memory -32,768 to 32,767
    unsigned short i = 65535; // can store 0 to 65,535
    printf("\n%d",h);
    printf("\n%d",i);
    int j = 2147483647; // stores 4 bytes > -2,147,483,648 to 2,147,483,647
    unsigned int k = 4294967295;  // stores 4 bytes > 0 to 4,294,967,
    printf("\n%d",j);
    printf("\n%u",k); // with unsigned int you have to use %u
    // int are already considered long int so long long int must be used
    long long int l = 9223372036854775807; // 8 bytes > -9 quintillion to 9 quintillion
    unsigned long long int m = 18446744073709551615U; // 8 bytes > 0 to 18 quintillion
    // if you display number this ^ large than it will give warning so put U at end of number
    printf("\n%lld",l); //%lld is used for signed long long integer
    printf("\n%llu",m); //%llu is for unsigned long long integer

    /*format specifiers
    %c = character
    %s = string
    %f = float
    %lf = double or long float
    %d = integer
    %.1 = decimal precision
    %1 = minimum field width
    %- = left align
    */
   float item1 = 5.75;
   float item2 = 10.34823623;
   float item3 = 100.99;
   
    printf("\nItem 1: $%8.2f", item1); // The 8 in %8.2f tell it the field width
    printf("\nItem 2: $%6.4f", item2); // the .2 in %6.2f tell it how many decimal places to go to
    printf("\nItem 3: $%-12.2fsus", item3); // the - will add extra space after text

    // constant = fixed value that can't be changed by program during its execution
    const float PI = 3.14159; // It's good practice to make name all uppercase
    // float PI = 25; if you try and change the value of PI it will give you can error
    
    // arithmetic opperators (Math)
    // + add
    // - subtract
    // * multiply
    // / divid
    // % modulus
    // ++ increment
    // -- decrement

    //int x = 20;
    //int y = 3;

    int add = x + y;
    printf("\n%d",add);

    int sub = x - y;
    printf("\n%d",sub);
    
    int mult = x * y;
    printf("\n%d",mult);
    
    float div = x / (float) y; // if dividing becomes decimal make sure it is a float
    printf("\n%f",div); // Also the divisor (y) has to be a float

    int z = x % y; // modulus is remainer of any division
    printf("\n%d",z);

    x++; // increases x by 1
    printf("\n%d", x);
    
    y--;
    printf("\n%d", y);
    
    //augmented asignment operator

    // x = x + 2 == x+=2
    // x = x - 5 == x-=5
    // x = x * 10 == x*=10
    // x = x / 1 == x+=1
    return 0; 
}  
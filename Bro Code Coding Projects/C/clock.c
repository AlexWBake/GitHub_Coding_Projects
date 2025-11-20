#include<stdio.h>
#include<windows.h>
#include<time.h>

int main (){
    int hour, minute, second;

    time_t now = time(NULL);
    struct tm *t = localtime(&now);

    hour = t->tm_hour;
    minute = t->tm_hour;
    second = t->tm_sec;

    while (1) {
        system("cls");
        printf("Currect Time: %02d:%02d:%02d\n", hour, minute, second);

    second++;
    if (second == 60) {
        minute++;
        second = 0;
    
        if (minute == 60) {
            hour++;
            minute = 0;

           if (hour == 24) {
                hour = 0;
           }
        }
    }
    
    
    Sleep(1000);
    }
    return 0;
}
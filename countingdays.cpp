#include "countingdays.h"

int curDay = 1;
int curHour = 0;
int curMinute = 0;
void lookAtClock(int hours, int minutes) {
    if (hours < curHour) {
        curHour = hours;
        curMinute = minutes;
        curDay += 1;
    } else if (hours == curHour && minutes <= curMinute) {
        curHour = hours;
        curMinute = minutes;
        curDay += 1;
    } else {
        curHour = hours;
        curMinute = minutes;  
    }
}

int getDay() {
    return curDay;
}
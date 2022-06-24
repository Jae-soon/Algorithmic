#include <stdio.h>
 
int main(){
    int h, m;
    scanf("%d %d", &h, &m);
    int plus_m;
    scanf("%d", &plus_m);
 
    if(m + plus_m < 60) {
        printf("%d %d", h, m + plus_m);
    } else{
        int hour = (m + plus_m)/60;
        int min = (m + plus_m) % 60;
        if(h + hour < 24)
            printf("%d %d", h + hour, min);
        else    //A+hour>=24
            printf("%d %d", h + hour - 24, min);
    }
}
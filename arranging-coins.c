#include <stdio.h>

int arrangeCoins(int n){
    int i = 0;
    while(i < n){
        i++;
        n -= i;
    }
    return i;
}

int main(){
    printf("%d",arrangeCoins(5));
}
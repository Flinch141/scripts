#include <stdio.h>
#include <string.h>

int cnt_uniq_letters(char s[]){
    int cnt = 0;
    int total = 0;
    int len = strlen(s);
    
    for(int i = 0; i < len;i++){
        cnt = 0;
        for(int j = 0; j < len; j++){
            if(s[j] == s[i]){
                cnt++;
            }
        }
        if(cnt == 1){
            printf("letter = %c \n",s[i]);
            total ++;
        }

    }
        return total;
}

int main(){
    char s[] = "qwertyt";
    int n = cnt_uniq_letters(s);
    printf("Count uniq letters = %d\n",n);
    return 0;
}
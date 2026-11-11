#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void sdvig(int size, int **data){

    for(int i = 0; i < size; i++){
        int znach = 0;
        int index = 0;

        for(int j = 0; j < size; j++){
            if(data[i][j] != 0){
                znach = data[i][j];
                data[i][j] = 0;
                data[i][index] = znach;
                index++;
            }
        } 
    }
}

void summa(int size, int **data, int *score){

    int scores = 0;

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size - 1; j++){
            if((data[i][j] == data[i][j+1]) && data[i][j] != 0){
                data[i][j] *= 2;
                data[i][j+1] = 0;
                scores += data[i][j];
            }
        }
    }
    *score += scores;

}

void reverse(int size, int **a){

    int buf = 0;

    for(int s = 0; s < size; s++){
        for(int r = 0; r < size / 2; r++){
            buf = a[s][size - r - 1];
            a[s][size - r - 1] = a[s][r];
            a[s][r] = buf;
        }
    }
}
void transport(int size, int **a){

    int buf = 0;

    for(int i = 0; i < size - 1; i++){
        for(int j = i + 1;j < size; j++){
            buf = a[i][j];
            a[i][j] = a[j][i];
            a[j][i] = buf;

        }
    }
}
void steps(int size, int **a, int *score, char cmd){

    switch(cmd){
        
        case('a'):
            sdvig(size,a);
            summa(size, a, score);
            sdvig(size, a);
        break;

        case('d'):
            reverse(size,a);
            sdvig(size,a);
            summa(size, a, score);
            sdvig(size, a);
            reverse(size,a);
        break;
        
        case('w'):
            transport(size,a);
            sdvig(size,a);
            summa(size, a, score);
            sdvig(size, a);
            transport(size,a);
        break;

        case('s'):
            transport(size,a);
            reverse(size,a);
            sdvig(size,a);
            summa(size, a, score);
            sdvig(size, a);
            reverse(size,a);
            transport(size,a);
            break;

        default:
            break;
        }      
}

void add_plit(int size, int **a){

    int empty = 0;

    for(int i = 0;i < size; i++){
        for(int j = 0;j < size;j++){
            if(a[i][j] == 0){
                empty++;
            }
        }
    }

    if(empty == 0){
        return;
    }

    int k = rand() % empty;

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            if(a[i][j] == 0){
                if(k == 0){
                    a[i][j] = (rand() % 10 == 0) ? 4 : 2;
                    return;
                }
            k--;
            }
        }
    }
}

int game_over(int size, int **a){

    int k = 0;

    for(int i = 0;i < size;i++){
        for(int j = 0;j < size;j++){
            if(a[i][j] == 0){
                k += 1;
            }
        }
    }

    if(k == 0){
        return 1;
    } 
    else{
        return 0;
    }
}
void print(int size,int **a, int score){

    printf("\033[2J\033[H");

    for(int i = 0;i < size;i++){
        printf("\n");
        for(int j = 0;j < size;j++){
            printf("%4d",a[i][j]);
        }
    }

    printf("\nscore: %d\n", score);
}
int victory(int size, int **a){
    int k = 0;

    for(int i = 0;i < size;i++){
        for(int j = 0;j < size;j++){
            if(a[i][j] == 2048){
                k += 1;
                break;
            }
        }
    }

    if(k = 1) return 1;
    else return 0;
    
}
int main(){
    
    int size = 0;
    scanf("%d",&size);

    int score = 0;

    int **a = malloc(size * sizeof(int *));
    int *data = calloc(size * size, sizeof(int));

    for (int i = 0; i < size; i++) {
        a[i] = data + i * size;
    }

    char cmd = '0';

    add_plit(size,a);

    for(int i = 0;i < size;i++){
        printf("\n");
        for(int j = 0;j < size;j++){
            printf("%4d",a[i][j]);
        }
    }

    int *copy = malloc(size * size * sizeof(int));

    while(cmd != 'e' &&  !game_over(size,a)){

        if(victory(size,a)){
            printf('You won');
        }

        scanf(" %c",&cmd);
        if(cmd == 'e') break;
        
        if (strchr("wasde", cmd) == NULL){
        printf("Неверная команда\n");
        continue;
        }

        memcpy(copy,data,size*size*sizeof(int));
        steps(size,a,&score,cmd);

        if(memcmp(copy,data,size*size*sizeof(int)) != 0){
            add_plit(size,a);
        }

        print(size,a,score);
        }
    printf("Game over");
    
    free(copy);
    free(a);
    free(data);

    return 0;
}
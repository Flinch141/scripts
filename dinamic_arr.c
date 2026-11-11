#include <stdio.h>
#include <stdlib.h>

int main(){
    // int size = 0;
    // scanf("%d",&size);
    // int *arr = malloc(size * sizeof(int));
    // for(int i = 0; i < size; i++){
    //     arr[i] = i;
    // }

    // for(int i = 0; i < size; i++){
    //     printf("%d ",arr[i]);
    // }
    // free(arr);
    // return 0;

    int siski = 'd';
    int *jopa = &siski;

    printf("peremennaya = %d",*jopa);
    return 0;
}
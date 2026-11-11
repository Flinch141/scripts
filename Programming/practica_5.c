//на 3
// #include<stdio.h>
// #define N 12
// int main(){
// int temp[N] = {-19,-17,-10,2,15,20,23,21,15,1,-10,-18};
// int sum = temp[0];
// int min[2] = {temp[0],0};
// int max[2] = {temp[0],0};
// for(int i = 0;i < N; i++){
//     sum += temp[i];
//     if(temp[i] > min[0]) min[0] = temp[i]; min[1] = i;
//     if(temp[i] < max[0]) max[0] = temp[i]; max[1] = i;
//     //printf("temp[0] = %d ",temp[i]);
//     }
// printf("\n");

// printf("avg = %.3f\nmin = %d, ind = %d\nmax = %d, ind = %d", (float)sum / 12.0,min[0],min[1],max[0],max[1]);
// return 0;
// }
//на 4 
// #include<stdio.h>
// #define n 20
// int main(){
//     double re_arr[n] = {1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0,
//          5.0, 6.0, 6.0, 7.0, 7.0, 8.0, 8.0, 9.0, 9.0, 10.0, 10.0};

//     for(int i = 0; i < n; i+=2){
//         printf("s[%d] = %.1lf + i * %.1lf\n", i,re_arr[i], re_arr[i+1]);
//     }
//     int summ_eng = 0;
//     for(int i = 0;i < n; i+=2){
//         summ_eng += re_arr[i] * re_arr[i] + re_arr[i+1] * re_arr[i+1];        
//     }
//     printf("%d\n",summ_eng);
//     double max = re_arr[0];
//     for(int i = 0;i < n; i+=2){
//         if(re_arr[i] > max) max = re_arr[i];
//     }
//     printf("Максимальное число среди реальной части: %.2lf\n",max);
//     return 0;
// }
// #include <stdio.h>
// #define N 20
// void func_1(int signal[],int raw[],int lower,int upper,int n){
//     int state = 0;
//     for(int i = 0; i < N; i++){
//         if(raw[i] > upper){
//             state = 1;
//         }else if(raw[i] < lower){
//             state = 0;
//         }
//         signal[i] = state;
//     }
// }
// void func_2(int n,int signal[]){
//     int cnt = 0;
//     for(int i = 0; i < n-1; i++){
//         if(signal[i] < signal[i+1]){
//             cnt += 1;
//         } 
//     }    
//     printf("\nКоличество фронтов: %d\n",cnt);
    
// }
// void func_3(int n, int signal[]){
//     int cnt = 0;
//     int k = 0;
//     for(int i = 0; i <= n; i++){
//         if (signal[i] == 1) {
//             cnt++;
//         } else if (cnt > 0) {
//             k++;
//             printf("Импульс %d: %d отсчёта(ов)\n",
//                    k, cnt);
//             cnt = 0;
//         }
//     }
// }
// int main(){
//     int raw[20] = {120, 300, 900, 1500, 1700, 1600, 900, 700, 850,
// 1100, 1400, 1600, 1500, 900, 600, 400, 300, 500, 1200, 1500};
//     int signal[N];
//     printf("Гистреризес: ");
//     func_1(signal, raw, 800, 1200, N);
//     for(int i = 0;i < N;i++){
//         printf("%d",signal[i]);
//     }
//     func_2(N,signal);
//     printf("\n");
//     func_3(N,signal);
//     return 0;
// }
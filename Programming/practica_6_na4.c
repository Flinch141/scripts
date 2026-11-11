#include <stdio.h>
#include <math.h>

void solve_for_2(float raw[][3]){
    float det = (raw[0][0] * raw[1][1]) - (raw[0][1] * raw[1][0]);   //определиитель матрицы 2 на 2
    if(fabs(det) < 0.0001){
        printf("det = 0");
    }
    
    else{
        float detx = (raw[0][2] * raw[1][1]) - (raw[1][2] * raw[0][1]);
                                                                            //определитель x и y
        float dety = (raw[0][0] * raw[1][2]) - (raw[1][0] * raw[0][2]);   

        float x = detx / det;
        float y = dety / det;
    
    printf("\nx = %.4f,y = %.4f\n", x, y);
    }    
}

float det3(float raw[3][3]){
    return ((raw[0][0] * raw[1][1] * raw[2][2]
        + raw[2][0] * raw[1][2] * raw[0][1]
        + raw[1][0] * raw[2][1] * raw[0][2]) -   //ищем определитель матрицы 3 на 3 
        (raw[0][2] * raw[1][1] * raw[2][0]
        + raw[0][0] * raw[2][1] * raw[1][2]
        + raw[0][1] * raw[1][0] * raw[2][2]));    
    }

void cramer3(float raw[][4]){
    float A[3][3];

    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            A[i][j] = raw[i][j];

    float D = det3(A);
    if(fabsf(D) < 1e-6){
        printf("Определитель равен 0: нет единственного решения\n");
        return;
    }

    float res[3];

    for(int k = 0; k < 3; k++){
        float M[3][3];
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++)
                M[i][j] = (j == k) ? raw[i][3] : raw[i][j];  // заменяем k-й столбец
        res[k] = det3(M) / D;
    }

    printf("x = %.3f, y = %.3f, z = %.3f\n", res[0], res[1], res[2]);

}

int main(){
    int N;
    scanf("%d",&N);

    if(N == 2){
        float raw[2][3] = {};
        for(int i = 0; i < 2;i++){
            scanf("%f %f %f",&raw[i][0],&raw[i][1],&raw[i][2]);
        }

       solve_for_2(raw);
       printf("\n");
    }
    else{
        float raw[3][4];
        for(int i = 0; i < 3;i++){
            scanf("%f %f %f %f",&raw[i][0],&raw[i][1],&raw[i][2],&raw[i][3]);

    }
        cramer3(raw);
        printf("\n");

}
    return 0;
    
}

// 1.0 2.0 10.0 
// 0.0 -10.0 -90.0 
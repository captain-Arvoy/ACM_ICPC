#include <stdio.h>
void input(int m1_r, int m1_c, int m2_r, int m2_c, int (*m1)[m1_r], int (*m2)[m2_r])
{
    int arr[2][2] = {{m1_r, m1_c}, {m2_r, m2_c}};
    for (int z = 0; z < 2; z++)
    {
        printf("Enter for Matrix %d\n", z + 1);
        for (int i = 0; i < arr[0][z]; i++)
        {
            for (int j = 0; j < arr[1][z]; j++)
            {
                printf("Enter value for row %d, column %d:", i + 1, j + 1);
                if (z == 0)
                {
                    scanf("%d", (*(m1 + i) + j));
                }
                else if (z == 1)
                {
                    scanf("%d", (*(m2 + i) + j));
                }
            }
        }
    }
}
void print(int m1_r, int m1_c, int m2_r, int m2_c, int (*x_matrix)[m1_r])
{
    for (int i = 0; i < m1_r; i++)
    {
        for (int j = 0; j < m2_c; j++)
        {
            printf("%d\t", *(*(x_matrix + i) + j));
        }
        printf("\n");
    }
}
void multiplication(int m1_r, int m1_c, int m2_r, int m2_c, int (*m1)[m1_r], int (*m2)[m2_r])
{
    int m3[m1_r][m2_c], prod = 0;
    for (int i=0; i < m1_r; i++)
    {
        for (int k = 0; k < m2_c; k++)
        {
            prod = 0;
            for (int j=0; j < m2_r; j++)
            {
                prod += ((*(*(m1 + i) + j)) * (*(*(m2 + j) + k))) ;
            }
            m3[i][k] = prod;
        }
    }
    print(m1_r, m1_c, m2_r, m2_c, m3);
}
int main()
{
    printf("Enter dimensions for the matrix multiplication.\n");
    int m1_r, m1_c, m2_r, m2_c, procced;
    printf("Matrix 1...\nEnter number of rows:");
    scanf("%d", &m1_r);
    printf("Enter number of columns:");
    scanf("%d", &m1_c);
    printf("Matrix 2...\nEnter number of rows:");
    scanf("%d", &m2_r);
    printf("Enter number of columns:");
    scanf("%d", &m2_c);
    if (m1_c != m2_r)
    {
        procced = 0;
        printf("Matrix multiplication is not possible!");
    }
    if (procced != 0)
    {
        int m1[m1_r][m1_c], m2[m2_r][m2_c];
        input(m1_r, m1_c, m2_r, m2_c, m1, m2);
        multiplication(m1_r, m1_c, m2_r, m2_c, m1, m2);
    }
    return 0;
}
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int number, guess, nguesses=1;
    srand(time(0));

    number = rand()%100 + 1;

    do
    {
        printf("advinhe um numero de 1 a 100\n");
        scanf("%d", &guess);
        if(guess>number)
        {
            printf("advinhou muito alto\n");
        }
        else if(guess<number)
        {
            printf("adivinhou muito baixo\n");
        }
        else
        {
            printf("Acertou!");
            printf("tentativas: %d\n", nguesses);
        }
        nguesses++;
    } while(guess!=number);

    return 0;
}

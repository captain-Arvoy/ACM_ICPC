#include <stdio.h>
void parser(char *inp2)
{
    int i = 0, i2 = 0;
    int flag = 1;
    while (*(inp2 + i2) != '\0'){
        if (*(inp2 + i2) == '<'){   
            i=i2;
            *(inp2 + i) = '0';//for erasing the opening bracket of the tag

            // for erasing  the closing brackets of the tags
            if (flag % 2 == 0){
                *(inp2 + i - 1) = '0';
            }

            // for erasing the content between the brackets of the tags (<''>)
            while (*(inp2 + i) != '>') {
                *(inp2 + i) = '0';
                i++;
            }        
            *(inp2 + i) = '0';//for erasing the closing bracket of the tag

            if (flag % 2 != 0)//for erasing spaces in comes before the ending tag
            {
                *(inp2 + i + 1) = '0';
            }
            flag++;
        }
        i2++;
    }
}
int main()
{
    char inp[100];
    int i2 = 0, i = 0;
    printf("Enter HTML line to be parsed\n"); // delete it
    scanf("%[^\n]s", inp);
    printf("\nYour input is: %s",inp);
    printf("\n-------------------------\n\n");
    parser(inp);
    while (inp[i2] != '\0')
    {
        if (inp[i2] == '0')
        {
            i2++;
            continue;
        }
        printf("%c", inp[i2]);
        i2++;
    }
    printf("\n");
    return 0;
}
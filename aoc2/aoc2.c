#include <stdio.h>
#include <stdlib.h>

int check_safe(int farr[], int fsize);
int dampener(int farr[], int fsize);

int main() {
    int safe_count = 0;
    int count = 1000; 

    for (int i = 0; i < count; i++) {
        int arr[8];  
        int size = 0;
        int num;

        while (scanf("%d", &num) == 1) {
            arr[size++] = num;
            char next = getchar();
            if (next == '\n' || next == EOF) {
                break;
            }
        }
        safe_count += check_safe(arr, size);
        if (check_safe(arr, size) == 0)
        {
            safe_count += dampener(arr, size);
        }
        
        
    }
    printf("Safe: %d\n", safe_count);
    return 0;
}

int check_safe(int farr[], int fsize) {
    for (int j = 1; j < fsize-1; j++) {
        if (((farr[j]-farr[j-1])*(farr[j+1]-farr[j])<=0)||(abs(farr[j]-farr[j-1])<1 || abs(farr[j]-farr[j+1])<1) || (abs(farr[j]-farr[j-1])>3 || abs(farr[j]-farr[j+1])>3)) {
            return 0;
        }
    }
    return 1;
}

int dampener(int farr[], int fsize) {
    int temp[fsize-1];
    
    for (int i = 0; i < fsize; i++)
    {
        int temp_size = 0;
        for (int j = 0; j < fsize; j++)
        {
            if(j!=i)    
            {
                temp[temp_size++] = farr[j];
            }
        }
        if (check_safe(temp, temp_size) == 1)
        {
            return 1;
        }
        
    }
    return 0;
    
}
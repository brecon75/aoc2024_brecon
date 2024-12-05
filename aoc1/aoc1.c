#include<stdio.h>
#include<stdlib.h>

void sort(int *p, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (p[j] > p[j + 1]){
                int temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

int main(){
    int count = 1000;
    int l[count], r[count];
    for (int i = 0; i < count; i++){
        scanf("%d %d", &l[i], &r[i]);
    }
    sort(l, count);
    sort(r, count);
    // int pair_dist[count];
    // for (int i = 0; i < count; i++){
    //     pair_dist[i] = r[i] - l[i];
    // }
    // int sum = 0;
    // for (int i = 0; i < count; i++){
    //     sum += abs(pair_dist[i]);
    // }
    // printf("%d", sum);
    int sim_score = 0;
    for (int i = 0; i < count; i++)
    {
        int temp_count = 0;
        for (int j = 0; j < count; j++)
        {
            if (l[i]== r[j])
            {
                temp_count++;
            }
        }
        sim_score+= temp_count*l[i];
    }
    printf("%d", sim_score);
}
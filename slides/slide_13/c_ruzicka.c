// C_RUZICKA.C
#include <stdint.h>
double c_ruzicka (uint16_t* array_a, uint16_t* array_b) {
    double max_ab = min_ab =  0.0;
    int tmp = index = 0;
    for (index = 0; index < 1024; index++) {
        tmp = array_b[index] * (1023-index);
        if(array_a[index] > tmp){
            max_ab = max_ab + array_a[index];
            min_ab = min_ab + tmp;
        }else{
            min_ab = min_ab + array_a[index];
            max_ab = max_ab + tmp;
        }
    }
    return min_ab/max_ab;
}
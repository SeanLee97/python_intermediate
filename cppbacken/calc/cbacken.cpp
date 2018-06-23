#include <iostream>
#include <string>
#include <cstdlib>
#define LEN(arr) sizeof(arr)/sizeof(arr[0])


/**
 * 使用python ctypes接口实现python调用C++（C）
 */

class Cbacken{
private:
    void _swap(int *, int, int);
    int _partition(int *, int, int);
    void _quick_sort(int *, int, int);
public:
    // 排序
    void sort(int *arr, int n);
    
};

void Cbacken::_swap(int *arr, int i, int j){
    int t;
    t = *(arr+j);
    *(arr+j) = *(arr+i);
    *(arr+i) = t;
}

int Cbacken::_partition(int *arr, int low, int high){
    int randint = rand()%high + low;
    this->_swap(arr, randint, high);

    int store_idx=low, i, j, privot= *(arr+high);
    for (i=low; i<high; i++){
        if (*(arr+i) < privot){
            this->_swap(arr, i, store_idx);
            store_idx++;
        }
    }
    this->_swap(arr, store_idx, high);
    return store_idx;
}

void Cbacken::_quick_sort(int *arr, int low, int high){
    if (low < high){
        int mid = this->_partition(arr, low, high);
        this->_quick_sort(arr, low, mid-1);
        this->_quick_sort(arr, mid+1, high);
    }
}

void Cbacken::sort(int *arr, int n){
    this->_quick_sort(arr, 0, n-1);
}


// 封装C接口
extern "C"{
    // 创建对象
    Cbacken* cbacken_new(){
        return new Cbacken;
    }
    void cbacken_sort(Cbacken* cb, int *arr, int n){
        cb->sort(arr, n);
    }
}

#include <iostream>

/**
 * python interface ,cpp backen
 */

class Calculate{
public:
    int add(int, int);
};

int Calculate::add(int n1, int n2){
    return n1+n2;
}

// 由于ctype仅支持C故这里要定义C函数
extern "C"{
    Calculate* Calculate_new(){
        return new Calculate;
    }
    int Calculate_add(Calculate* cal, int n1, int n2){
        return cal->add(n1, n2);
    }
}

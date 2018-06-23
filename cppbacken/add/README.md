# 编译成.so文件
#For Linux
$ g++ -shared -Wl,-soname,adder -o adder.so -fPIC add.cpp

#For Mac
$ g++ -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.cpp

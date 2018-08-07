# 常用的魔术方法

## 构造和初始化

### __init__(self, args) 
构造函数

### __new__(cls) 
传入的是类实例

### __del__(self)
析构函数，调用 `del cls` 时会被调用

## 属性访问控制
### __getattr__(self, name)
直接获取属性 `cls.name`, 该方法定义了你试图访问一个不存在的属性时的行为。因此，重载该方法可以实现捕获错误拼写然后进行重定向, 或者对一些废弃的属性进行警告。

### __setattr__(self, name, value)
直接给属性赋值 `cls.name = value`, 如果该函数内部内部使用`self.name = value` 时会产生**"无限递归"**的错误，正确的方式应该是
```python 
def __setattr__(self, name, value):
    self.__dict__[name] = value
```

### __delattr__(self, name)
`del cls.name` 时会被调用

## 描述器对象
### __set__(self, cls, value)
`cls.innercls = value` 用于类中的其他类对象赋值

### __get__(self, cls)
`cls.innercls` 返回类中其他对象传回的值

### __delete__(self, cls)
`del cls.innercls` 

### 综合实例
```python
class Meter(object):
    '''Descriptor for a meter.'''
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    '''Descriptor for a foot.'''
    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    meter = Meter()
    foot = Foot()

d = Distance()
print d.meter, d.foot  # 0.0, 0.0
d.meter = 1
print d.meter, d.foot  # 1.0 3.2808
d.meter = 2
print d.meter, d.foot  # 2.0 6.5616
```

## 自定义容器(Container)
### __len__(self)
`len(con)` 返回容器长度

### __setitem__(self, name, value)
`con[name] = value` 直接下标赋值

### __getitem__(self, name)
`con[name]` 直接下标访问

### __delitem__(name)
`del con[name]` 删除下标

### __iter__(self)
使得容器支持迭代器方式访问 `for x in con`

### __contains__(self, item)
`name in con` 可以返回布尔值

### __missing__(self, name)
容器中没有name时会被调用

## 上下文管理
`with` 关键字可实现上下文(环境)管理

### __enter__(self)
进入环境时触发

### __exit__(self, exception_type, exception_value, traceback)
退出环境时触发，一般用来关闭资源

## 运算符重载
### __eq__(self, other)
重载 `=`

### __ne__(self, other)
重载 `!=`

### __lt__(self, other)
重载 `<`

### __gt__(self, other)
重载 `>`

### __le__(self, other)
重载 `<=`

### __ge__(self, other)
重载 `>=`

## 其他

### __str__(self)
`print(cls)` 和 `str(cls)` 时被调用，必须返回字符`str`类型

### __repr__(self)
对实例使用`repr()`时调用。`str()`和`repr()`都是返回一个代表该实例的字符串，主要区别在于: `str()`的返回值要方便人来看,而`repr()`的返回值方便计算机看。

### __call__(self, \*args, \*\*kwargs)
```python
class XClass:
    def __call__(self, a, b):
        return a + b

def add(a, b):
    return a + b

x = XClass()
print 'x(1, 2)', x(1, 2)
print 'callable(x)', callable(x)  # True
print 'add(1, 2)', add(1, 2)
print 'callable(add)', callable(add)  # True
```

# Refrence
https://segmentfault.com/a/1190000007256392#articleHeader3

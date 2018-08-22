# -*- coding: utf-8 -*-

"""
本类实现了一个简单的ORM（对象-关系映射），使用了元类，描述器等
"""

"""描述器"""

class Field(object):
    pass
    
class IntField(Field):
    def __init__(self, db_column="", min=None, max=None):
        self._value = None # 表的数据
        self.min = min
        self.max = max
        self.db_column = db_column

        if min is not None:
            if not isinstance(min, int):
                raise ValueError("min should be an Integer")
            if min < 0:
                raise ValueError("min should be greater than 0")

        if max is not None:
            if not isinstance(max, int):
                raise ValueError("max should be an Integer")
            if max < 0:
                raise ValueError("max should be greater than 0")
        if min is not None and max is not None:
            if min > max:
                raise ValueError("min should be less than max")

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("input should be a Integer")
        if value < self.min or value > self.max:
            raise ValueError("out of range")
        self._value = value

    def __get__(self, instance, owner):
        return self._value

class  CharField(Field):
    def __init__(self, db_column, max_length):
        self._value  = None 
        self.db_column = db_column
        self.max_length = max_length

        if max_length is None:
            raise ValueError("max_length can`t be None")
        if not isinstance(max_length, int):
            raise ValueError("max_length should be a Integer")
        if max_length < 0:
            raise ValueError("max_length must greater than 0.")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("input should be a String")
        if len(value) > self.max_length:
            raise ValueError("the length of input should be less than max_length")
        self._value = value

"""定义元类"""
class MetaModel(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        # 本类是User
        # 把attrs中与数据库表有关的列提取出来
        fields = {}
        for key, val in attrs.items():
            if isinstance(val, Field):
                fields[key] = val   # value 直接走描述器__get__()

        # 在user中取出数据表属性meta
        attrs_meta = attrs.get('Meta', None) # 取本类（User）内部类
        _meta = {}
        db_table = name.lower()  # 数据表名称默认取小写类名称
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', 'None') # 取出Meta类中db_table属性
            if table is not None:
                db_table = table  # 使用用户指定的表名
            del attrs['Meta']

        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['_fields'] = fields

        # 以上过程相当于对类进行了修改
        return super(MetaModel, cls).__new__(cls, name, bases, attrs, **kwargs)

"""定义模型基类"""
class Model(metaclass=MetaModel):
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return super(Model, self).__init__()

    def save(self):
        fields = []
        values = []
        for key, val in self._fields.items():
            db_column = val.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key) # 字段的值
            values.append(str(value))
        sql = "insert {name} ({field}) values ({value})".format(name=self._meta['db_table'],
                                                             field=','.join(fields),
                                                             value=','.join(values))
        return sql

    def select(self):
        fields = []
        where = []
        for key, val in self._fields.items():
            db_column = val.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            v = getattr(self, key, None)
            if v is not None:
                where.append([key, str(v)])

        sql = 'select {fields} from {name} where {where}'.format(name=self._meta['db_table'],
                                                                 fields=','.join(fields),
                                                                 where=' and '.join(['='.join(x) for x in where]),
                                                                 )
        return sql


class User(Model):
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min=0, max=100)

    class Meta: # 使用内部类来定义数据表的其他属性
        db_table = "db_user"

if __name__ == '__main__':
    user = User(name='seanlee', age=15)
    user.name = 'sean'
    print(user.save())
    print(user.select())

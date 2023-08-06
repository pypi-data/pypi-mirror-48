# refdict

![PyPI](https://img.shields.io/pypi/v/refdict.svg)
![GitHub](https://img.shields.io/github/license/DiscreteTom/refdict.svg)

在Python使用refdict更好地组织与访问数据

![](https://raw.githubusercontent.com/DiscreteTom/refdict/master/img/readme.png)

兼容dict/list/tuple/str！

- [refdict](#refdict)
	- [Install](#Install)
	- [Usage](#Usage)
	- [Features](#Features)
	- [Warnings](#Warnings)
	- [FAQ](#FAQ)
	- [Change Log](#Change-Log)
		- [v3.2.0](#v320)
		- [v3.1.0](#v310)
		- [v3.0.0](#v300)
		- [v2.2.0](#v220)
		- [v2.1.0](#v210)
		- [v2.0.0](#v200)
		- [v1.0.0](#v100)

## Install

`pip install refdict`

## Usage

在字符串值前面加上**引用前缀**使其变成**另一个对象的引用**。默认的引用前缀是`@`。可以在构造函数中传入参数`refPrefix`来改变引用前缀

在`[]`运算符中使用一个字符串实现refdict内容的链式访问。使用`.`作为多个key的连接符。可以在构造函数传入参数`separator`来改变分隔符

```python
data = {
	'player': {
		'name': 'DiscreteTom',
		'items': [
			'@apple',
			'@potion.red'
		],
		'weapon': '@sword',
		'attack': '@player.weapon.attack',
		'me': '@player'
	},
	'apple': 'restore your health by 10%',
	'potion': {
		'red': 'restore your health by 20%',
	},
	'sword': {
		'attack': 123,
		'value': 50
	},
}
rd = refdict(data)
print(rd['player.items.1']) # => restore your health by 20%
print(rd['player.attack']) # => 123
rd['player.items.1'] = 'empty'
print(rd['player.items.1']) # => empty
print(rd['player.items.:.1']) # => empty
rd['player.items.:'] = []
print(rd['player.items']) # => []
print(rd.text('player.me.attack')) # => @player.weapon.attack
```

## Features

- 能够像使用`dict`/`list`/`tuple`/`str`一样使用`refdict`
  - 能够调用对应类型的函数，如`refdict({}).keys()`或`refdict([]).append(123)`
  - 迭代与成员判断`for x in refdict([1, 2, 3])`
  - 切片与切片赋值`refdict([1, 2, 3])[:] => [1, 2, 3]`
  - ...
- 能够通过一个字符串链式访问内部成员
  - `refdict({'1':{'1':{'1':{'1':'1'}}}})['1.1.1.1'] => 1`
- 能够通过引用字符串实现对象与对象之间的互相引用

## Warnings

使用形如`item: @item`的**递归引用**会导致**死循环**，包括间接递归引用

```python
data = {
	'item': '@item', # => infinite loop!
	'wrapper': {
		'item': '@wrapper.item' # => infinite loop!
	},
	'a': '@b' # => infinite loop!
	'b': '@a' # => infinite loop!
}
```

## FAQ

- Q - 为什么我用1作为下标访问不到list/tuple/str的第一个元素？
  - A - 和python一样，下标从0开始计数。虽然用起来有时候感觉有些反直觉，但是是合理的
- Q - 为什么我不能像`refdict[1][2][3]`这样使用引用的特性？
  - A - 引用解析仅限于第一个`[]`，第一个`[]`会返回一个正常的`tuple`/`list`/`dict`/`str`而不是一个`refdict`对象。可以使用`refdict(1)(2)[3]`这样使用引用特性与链式访问，因为`()`会返回一个临时的子`refdict`对象

## Change Log

### v3.2.0

- 支持链式创建`dict`
  - 创建空refdict：`rd = refdict({})`
  - 赋值：`rd['a.b'] = 1`，此时`rd = refdict({'a': {'b': 1}})`

### v3.1.0

- 添加函数`refdict.get(keys, default = None)`实现类似于`dict.get(key, default)`的功能，但是`refdict`的`keys`可以是链式的
- 修复`refdict.__str__()`
- 修复`refdict.__repr__()`

### v3.0.0

- 添加静态函数`findItem()`使非refdict对象也可以使用引用与链式访问的功能
  - `refdict.findItem(data, 'key1.key2')`
- 添加多次链式访问的实现方案，使用`()`实现
  - `rd('player.me')`会返回一个子`refdict`，里面包含父`refdict`的所有数据，但是自身表示了父`refdict`的部分数据。比如`rd('player.me')`包含整个rd的数据，但是它仅表示player
  - 可以链式使用`()`，且参数可以是链式的，如`rd('player.me')('me.me.me')`
  - 最后使用`[]`返回非`refdict`的对象完成取值，如`rd('player.me')('me.me')['attack'] = 0`
- 为了实现上述“局部结果”的功能，成员变量`data`变为`refdict`的`private`内容，使`refdict`不向前兼容

### v2.2.0

- `__contains__`支持链式访问特性
  - `'player.weapon.attack' in rd`会返回`True`

### v2.1.0

- 可以调用根数据类型的非内置函数
  - 比如`refdict({})`可以使用`dict`的`keys`函数，`refdict([])`可以使用`list`的`append`函数
- `[]`运算的参数`keys`添加`int`类型和`slice`类型的支持，以便更好地访问`list/tuple/str`。目前参数`keys`仅支持`str`、`int`和`slice`三种类型
- 实现`__contains__`
- 实现`__str__`以便输出
- 实现`__delitem__`以使用引用解析来删除元素

### v2.0.0

改名。还是小写看起来舒服。但是不向前兼容了所以就用2.0.0的版本号好了

### v1.0.0

- 实现基本的`[]`取值与赋值
- 实现`text`函数以获得字面值
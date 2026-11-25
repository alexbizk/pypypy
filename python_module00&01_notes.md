
flake8 名字是两个工具拼起来的：
flake8 = pyflakes + pep8

flake 来自 pyflakes：一个检查代码里明显错误的工具，比如变量没定义、import 了没用。
8 来自 PEP 8：Python 官方的代码风格规范。当时有个检查 PEP 8 的工具就叫 pep8，后来改名为 pycodestyle。

flake8 把这几个工具打包在一起，一条命令全部检查完。你刚才 pip install flake8 的输出里能看到它顺带装了这几个：

pyflakes      → 检查错误（报错代码 F 开头）
pycodestyle   → 检查 PEP 8 风格（E、W 开头）
mccabe        → 检查函数复杂度（C 开头）

所以看报错代码的第一个字母，就知道是哪个工具报的。

顺便说一下 PEP：全称 Python Enhancement Proposal（Python 改进提案），是 Python 社区的正式文档，按编号排列。PEP 8 正好是讲代码风格的那一篇。

把变量和文字一起打印，有两种常用写法：
python
print("Hello", name)        # 逗号会自动加一个空格
print(f"Hello {name}")      # f-string：在引号前加 f，变量放进 {}


__pycache__/是每运行一次main就有的吗

不是每次都新建。__pycache__ 只在第一次导入你的文件时生成，之后就一直复用：

第一次运行 main.py、导入 ft_garden_name.py 时，Python 编译它，在 __pycache__ 里存一个 .pyc 文件。
之后再运行，如果你的 .py 文件没改过，Python 直接用缓存，不会再生成。
如果你改了 .py 文件，Python 发现源文件比缓存新，就会重新编译，覆盖原来的 .

range(a, b) 生成从 a 开始、到 b 之前结束的数字，不包括 b。所以 range(1, 4) 是 1、2、3。

我之前的函数ex0-6有返回值吗

都没有返回值。

你在 ex0–ex6 里写的函数都只用了 print()，没有写 return。在 Python 里，没有 return 的函数会自动返回 None，None 的意思就是"什么都没有"。
def a():
    print(5)      # 把 5 显示在屏幕上，但不交给调用者

def b():
    return 5      # 不显示，把 5 交还给调用者

x = a()   # 屏幕显示 5，但 x 是 None
y = b()   # 屏幕什么都不显示，y 是 5

mypy ft_seed_inventory.py 是一条终端命令，意思是：用 mypy 这个工具检查 ft_seed_inventory.py 里的类型对不对。

（你消息开头多了个 x，变成 xmypy 的话终端会报 command not found，要去掉。）

mypy 是什么

Python 本身不会检查类型。比如你写了 quantity: int，但调用时传进去一个字符串，Python 照样运行，不会报错：

python
ft_seed_inventory("tomato", "abc", "packets")   # Python 不管，照样运行

: int、: str、-> None 这些类型注解，对 Python 来说只是"说明文字"。

mypy 是专门读这些注解的检查工具。它不运行代码，只是读一遍，看类型有没有对不上。比如：

python
def add(a: int, b: int) -> int:
    return a + b

add(1, "hello")    # mypy 会报错：第二个参数应该是 int，你给了 str
和 flake8 的区别
工具	检查什么
python3 main.py	代码能不能跑、结果对不对
flake8	代码格式规不规范（空格、缩进、行长）
mypy	代码类型对不对得上

subject 要求 ex7 必须用类型注解，并且要用 mypy 检查，所以要跑一次。

subject 为什么要求 ex7 要过这个检查

subject 没有写具体原因，但从它的安排能看出用意：ex7 是用来教你"类型注解"这个概念的。

你看 subject 的规定：

ex0–ex6：类型注解可选
ex7：类型注解必须写，而且必须过 mypy

也就是说，前面几题先让你熟悉基础语法，最后一题专门引入这个新技能。

为什么要学这个

1. 只写注解没人检查，等于没写

前面说过，Python 本身不看类型标签。如果只要求写注解、不要求检查，标签写错了也不会发现。要求过 mypy，才能确保你真的写对了。

2. 提前发现 bug

比如你写了一个函数，以为 quantity 是整数，结果某处传了字符串进去。不检查的话，可能要等程序运行到那里出了怪结果才发现。mypy 在运行之前就能指出来。

3. 代码更好读

别人看到 quantity: int，不用读函数内容就知道该传什么。项目越大、合作的人越多，这一点越重要。

4. 实际工作中很常用

现在很多公司的 Python 项目都要求写类型注解并用 mypy 之类的工具检查，和 flake8 一样属于基本规范。42 后面的 Python 模块很可能也会继续要求，所以第一个模块先让你接触一下。

简单说：flake8 让你养成写规范代码的习惯，mypy 让你养成写清楚类型的习惯。 两个都是写 Python 的基本功。


if __name__ == "__main__":
    print("程序从这里开始")

每个 Python 文件都有一个隐藏的变量 __name__：
直接运行这个文件（python3 文件.py）时，__name__ 的值是 "__main__"
被别的文件 import 时（就像 Module 00 里 main.py 导入你的文件），__name__ 的值是文件名

先建三个变量 需要声明变量类型吗

不需要。 Python 和 C 不一样，变量不用提前声明类型，直接赋值就行：

python
name = "Rose"      # Python 自动知道这是 str
height = 25        # 自动知道是 int
age = 30           # 自动知道是 int

Python 会根据等号右边的值自动判断类型。mypy 也一样，看到 height = 25 就知道 height 是 int。

可以写，但不是必须的：

python
name: str = "Rose"
height: int = 25
age: int = 30

这种写法叫变量注解


shebang（答辩时会让你现场加）

shebang 是文件第一行以 #! 开头的特殊注释，告诉系统"用哪个程序来运行这个文件"：

python
#!/usr/bin/env python3
if __name__ == "__main__":
    ...
#!：shebang 的标志
/usr/bin/env python3：让系统去找 python3 来运行

有什么用： 加上它，再给文件加上"可执行"权限，就可以不用写 python3，直接运行：

bash
chmod +x ft_garden_intro.py     # 给文件加执行权限（只需一次）
./ft_garden_intro.py            # 直接运行

没有 shebang 的话，系统不知道该用什么来运行，会把它当成 shell 脚本，然后报错。

为什么用 /usr/bin/env python3，不直接写 /usr/bin/python3？ 因为每台电脑上 python3 装的位置可能不一样。env 会去 PATH 里帮你找，所以在不同电脑上都能用。
# 在英文里叫 sharp（或 hash）
! 在程序员圈子里叫 bang

#! 连起来就是 sharp-bang，读快了变成 shebang。也有人叫它 hashbang。

#!/usr/bin/env python3
#!	告诉系统：后面指定运行这个脚本的解释器
/usr/bin/env	根据环境变量 PATH 查找程序
python3	要查找并运行的程序
这样就不用写死 Python 的安装位置，因为不同电脑的 Python 可能安装在不同目录。

{self.height:.1f} 为什么把高度显示为小数点后一位
:.1f 是 Python 规定的数字显示格式。
部分	意思
self.height	要显示的值
:	后面开始指定显示格式
.1	小数点后保留 1 位
f	使用固定小数格式
例如
height = 25.867
print(f"{height:.1f}")  # 25.9
print(f"{height:.2f}")  # 25.87
print(f"{height:.0f}")  # 26
这和在 C 中用的写法很相似：printf("%.1f", height);

print("Created: ", end="") 中的 end="" 表示打印后不换行，所以随后 show() 的输出会接在同一行：

self.height
self._height
它们都是普通的属性名。 加上 _ 不会自动检查数值，也不会禁止修改。

区别在于，Python 程序员有一个约定：
名字	向使用者表达的意思
height	可以直接访问这个属性
_height	这是内部属性，请通过提供的方法访问

例如，看到 _height，我们就应该这样修改：
rose.set_height(25)

def get_height(self, _height: float) -> float:
    return self._height
这次语法没问题了，Python 能运行。但这个参数多余而且会出问题：
def get_height(self, _height: float) -> float:
这样定义的话，每次调用都必须传一个值进去：

python
rose.get_height()        # ❌ TypeError: missing 1 required positional argument: '_height'
rose.get_height(999)     # 能运行，但 999 完全没被用到，很奇怪

class 内部的method必须传self进去对吗
对，但要区分定义时和调用时：

定义时：第一个参数必须写 self
python
class Plant:
    def get_height(self) -> float:      # ✅ 必须写 self
        return self._height

    def get_height() -> float:          # ❌ 忘了 self
        return self._height

忘了写 self，方法里就拿不到"自己"，self._height 无从说起；调用时也会报 TypeError。

调用时：不用传 self，Python 自动帮你传
python
rose.get_height()        # ✅ 括号里什么都不写
rose.set_height(25)      # ✅ 只传 height，不传 self

Python 看到 rose.get_height()，会自动把 rose 塞进 self。所以：

定义	调用
def get_height(self)	rose.get_height()
def set_height(self, height)	rose.set_height(25)

`super()` 是 Python 内置的工具（a Python built-in）
super() 返回一个代理对象，让你访问继承关系中下一个类的方法。在你现在的 Flower(Plant) 中，下一个就是 Plant。
super() 不只用于 __init__，也可以用来调用 show()、`grow()` 等方法。
super() is a Python built-in that returns a proxy object used to access methods from the next class in the method resolution order (MRO).
简单一点： super() lets us call methods from a base class

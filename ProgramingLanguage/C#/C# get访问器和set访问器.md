# C# get访问器和set访问器

首先，要先了解一下 `C#` 语言中**属性**的概念。**属性**是对现实实体特征的抽象，提供对类或对象的访问。访问**属性**时，其行为类似于字段。但与字段不同的是，**属性**通过访问器实现；访问器用于定义访问**属性**或为**属性**赋值时执行的语句。

**属性声明语法：**

```C#
[权限修饰符] [类型] [属性名]    1   `
{
    get {   
            get访问器体；
            return 值；
        }

    set {
            set访问器体；
        }
}
```


## **get 访问器**

相当于一个具有属性类型值的无参数方法，`get` 访问器需要 `return` 语句返回，并且所有的 `return` 语句都必须返回一个可隐式转换为属性类型的表达式。


## **set 访问器**
相当于一个具有单个属性类型参数和 void 返回值的方法。set 访问器的隐式参数始终命名为 value，因此在set 访问器中不能定义名称为 value 的局部变量。

**示例一：**
```C#
namespace Application
{
    internal class Program
    {   
        private int hp;
        public int Hp
        {
            get { return hp; }

            set { hp = value; }
        }
        static void Main(string [] args)
        {
            Program p = new Program();
            p.Hp = 100;
            Console.WriteLine("私有变量hp的值为：{0}", p.Hp);
        }
    }
}

```

**运行结果：**
>   私有变量hp的值为：100

**示例二：**

```C#
namespace Application
{
    internal class Program
    {   
        public int Hp
        {
            get;
            set;
        }
        static void Main(string [] args)
        {
            Program p = new Program();
            p.Hp = 100;
            Console.WriteLine("Hp属性的值：{0}", p.Hp);
        }
    }
}
```

**运行结果：**

>   Hp属性的值：100

**解析：**

C# 中支持自动实现的属性，即在属性的 get 访问器和 set 访问器中没有任何逻辑，但是在使用自动实现的属性时，必须同时包含 get 访问器和 set 访问器。




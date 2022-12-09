# C# 类方法的参数

C# 中的方法的参数主要有4种，分别为**值参数**、**ref 参数**、**out 参数**、**params 参数**。


## **值参数**

值参数就是在声明时不加修饰的参数，表明实参和形参之间按值传递。调用值参数的方法时，编译器为形参分配存储单元，将对应实参的值复制到对应的形参中，因此，在`值参数的方法`中,修改形参的值并不会影响实参的值。

**示例：**

```C#
namespace App
{
    internal class Program
    {   
        public int Add(int x, int y)
        {
            x = x + y;
            return x;
        }

        static void Main(string[] args)
        {   
            int x = 10;
            int y = 20;
            int z = 0;

            Program p = new Program();
            z = p.Add(x, y);

            Console.WriteLine("实参x的值为：{0}", x);
        }
    }
}
```

**运行结果：**

>     实参x的值为：10


## **ref参数**

**ref** 参数使形参按引用传递，方法声明和方法调用都必须要显示的使用 **ref** 关键字且传入的实参必须在调用前赋值，在方法中对形参的任何修改都会反映到实参中。

**示例：**

```C#
namespace App
{
    internal class Program
    {
        public int Add(ref int x, int y)
        {
            x = x + y;
            return x;
        }

        static void Main(string[] args)
        {
            int x = 10;
            int y = 20;
            int z = 0;

            Program p = new Program();
            Console.WriteLine("调用Add()方法前，实参 x 的值为：{0}", x);
            z = p.Add(ref x, y);
            Console.WriteLine("调用Add()方法后，实参 x 的值为：{0}", x);
        }
    }
}
```

**运行结果：**
>     调用Add()方法前，实参 x 的值为：10
>     调用Add()方法前，实参 x 的值为：30

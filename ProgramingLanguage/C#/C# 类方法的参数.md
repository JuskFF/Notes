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


## **out参数**

**out** 参数使形参按引用传递，方法声明和方法调用都必须要显示的使用 **out** 关键字, **out** 与 **ref** 的不同之处是：**out** 参数可以不赋值就可以使用，在方法中对形参的任何修改都会反映到实参中。

**示例：**

```C#
namespace App
{
    internal class Program
    {   
       public int Add(out int x, int y)
        {
            x = x + y;
            return x;
        }

        static void Main(string[] args)
        {
            int x;
            int y = 20;
            int z = 0;

            Program p = new Program();
            z = p.Add(out x, y);
            Console.WriteLine("调用Add()方法后，实参 x 的值为：{0}", x);
        }
    }
}
```

**运行结果：**
>     调用Add()方法前，实参 x 的值为：20


## **params参数**

在声明方法时，如果有多个相同类型的参数，则可以定义为 **params** 参数。

**使用注意事项：**

- params参数只支持一维数组使用
- 在方法声明中的 params 关键字之后不允许有任何其他参数，并且在方法声明中只允许有一个 params 关键字
- 可以不指定数组的长度和里面元素的类型



**示例：**

```C#
namespace App;
{   
    static void use_params(params int[] list)
    {
        for(int i = 0; i < list.Length; i ++)
        {
            Console.Write(list[i] + " ");
        }
    }

    static void use_params1(params object[] list)
    {
        for(int i = 0; i < list.Length; i ++)
        {
            Console.Write(list[i] + " " );
        }
    }

    static void Main(string[] args)
    {   
            Console.WriteLine("==========");
            use_params(1, 2, 3);
            Console.WriteLine();
            use_params1("one", 2, 1.6f);
            Console.WriteLine();

            // 下面输出是空白
            Console.WriteLine("==========");
            use_params();
            Console.WriteLine();
            use_params1();
            Console.WriteLine();

            Console.WriteLine("==========");
            int[] list = { 8, 9, 10 };
            use_params(list);
            Console.WriteLine();
            use_params1(list);
            Console.WriteLine();

            Console.WriteLine("==========");
            object[] list1 = { 8, "list1" };
            use_params(list1);          // 报错：无法从"object[]" 转化 "int"
            use_params1(list1);

    }
}
```

**运行结果：**

>     ==========
>     1 2 3
>     one 2 1.6
>     ==========
>     
>     
>     ==========
>     8 9 10
>     System.Int32[]
>     ==========
>     8 list1
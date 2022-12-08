# C# 构造函数和析构函数

## 构造函数(构造方法)

构造函数是一种特殊的函数，它是在创建对象时执行的方法，与类具有相同的名称，通常用来初始化对象的数据成员。


**构造函数的特点：**

- 构造函数没有返回值
- 构造函数的名称要与本类的名称一样


**构造函数的定义：**

```C#
public class Human
{   
    // 无参构造函数
    public Human()
    {
    }

    // 有参构造函数
    public Human(int age)
    {
        age = 18;
    }

}
```


**默认构造函数和有参构造函数**：

在定义类的时，如果没有定义构造函数，则编译器会自动创建一个无参的构造函数。
```C#
public class Human
{

}

Human boy = new Human()     # 自动创建并调用默认的构造函数
```
`如果存在有参的构造函数，还想调用默认的构造函数，这时就需要显示的定义出默认的构造函数即无参构造函数。`


## 静态构造函数

静态构造函数用于初始化`任何静态数据`，或执行仅需要执行一次的特定操作。在创建第一个实例或引用任何静态成员之前，将自动调用它。


**静态构造函数的特点：**

- 静态构造函数不使用访问修饰符且不具有参数
- 静态构造函数不能继承和重载
- 静态构造函数不能直接被调用，由公共语言库(CLR)调用
- 一个类或结构中只有一个静态构造函数，只能访问静态数据
- 如果不提供静态构造函数来初始化静态字段，则所有静态字段都将初始化为它们的默认值，如C#类型的默认值中所列

**示例一：**

```C#
using system;
namespace app1;
internal class Program
{
    static void Main(string[] args)
        {
            Console.WriteLine(Enemy.text);
            Console.WriteLine(Tank.text);
        }
}

// 一个敌人类
public class Enemy
{   
    public static string text;

    static Enemy()
    {   
        text = "class Enemy" ;
        Console.WriteLine("Hi, static Enemy");
    }

    public Enemy()
    {
        Console.WriteLine("Hi,Enemy");
    }
}

// 一个坦克类，继承敌人类
public class Tank : Enemy
{
    static Tank()
        {   
            text = "class Tank";
            Console.WriteLine("Hi, static Tank");
        }
    
    public Tank()
    {
        Console.WriteLine("Hi,Tank");
    }
}
```

**运行结果：**
>     Hi, static Enemy
>     class Enemy
>     class Enemy

**解析：**

运行到Enemy.text时，由于text是静态变量，.net框架会自动调用上述程序`Enemy`类的静态构造函数`static Enemy()`，然后在输出text变量的值；当运行到Tank.text时，虽然text是静态变量，但是静态的构造函数只执行一次，所以此处只输出text变量的值。

**示例二：**

```C#
using system;
namespace app1;
internal class Program
{
    static void Main(string[] args)
        {
            Enemy enemy = new enemy();
            Tank tank = new Tank();
        }
}

// 一个敌人类
public class Enemy
{   
    public static string text;

    static Enemy()
    {   
        text = "class Enemy" ;
        Console.WriteLine("Hi, static Enemy");
    }

    public Enemy()
    {
        Console.WriteLine("Hi,Enemy");
    }
}

// 一个坦克类，继承敌人类
public class Tank : Enemy
{
    static Tank()
        {   
            text = "class Tank";
            Console.WriteLine("Hi, static Tank");
        }
    
    public Tank()
    {
        Console.WriteLine("Hi,Tank");
    }
}
```

**运行结果：**
>     Hi, static Enemy
>     Hi,Enemy
>     Hi, static Tank
>     Hi,Enemy
>     Hi,Tank

**解析：**

实例化Enemy类，首先会调用静态构造函数，然后再调用无参构造函数；实例化Tank类，首先也是调用自身的静态构造函数，然后由于实例tank继承Enemy类，所以调用Enemy类中的无参构造函数，最后调用Tank类的无参构造函数。


## 析构函数

析构函数主要用来释放资源对象，.NET Framework 类库具有垃圾回收的功能，当某个类的实例被认为不再有效，并符合析构的条件时，.MET Framework 就会调用该类的析构函数实现垃圾回收。


**析构函数的特点：**

- 严格来说，析构函数是自动调用的，不需要显示定义
- 一个类中只能定义一个析构函数


**析构函数的定义：**
析构函数是以类名加~来命名的
```C#
~program()
{
    Console.WriteLine("析构函数自动调用");
}
```












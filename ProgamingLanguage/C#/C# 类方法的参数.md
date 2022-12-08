# C# 类方法的参数

C# 中的方法的参数主要有4种，分别为**值参数**、**ref 参数**、**out 参数**、**params 参数**。


## **值参数**

值参数就是在声明时不加修饰的参数，表明实参和形参之间按值传递。调用值参数的方法时，编译器为形参分配存储单元，将对应实参的值复制到对应的形参中，因此，在`值参数的方法`中,x修改形参的值并不会影响实参的值。

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

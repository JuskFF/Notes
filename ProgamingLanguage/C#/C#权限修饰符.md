# C#权限修饰符

C# 中的权限修饰符主要包括`public`、`protected internal`、`internal`、`protected`、`private`。

## public

- 访问范围：任何代码都可以访问
- 应用范围：所有类或成员

## proctected internal

- 访问范围：同一程序集和子类中访问
- 应用范围：类和内嵌类的所有成员

## internal

- 访问范围：同一程序集中访问
- 应用范围：类和内嵌类的所有成员

## proctected

- 访问范围：在本类和其子类中访问
- 应用范围：类和内嵌类的所有成员

## private

- 访问范围：只能在本类中访问
- 应用范围：所有类或成员

## 默认修饰符
- 类、结构默认的修饰符是 **`internal`**
- 类中所有的成员的默认修饰符是 **`private`**
- 接口的默认修饰符是 **`internal`**
- 接口成员的默认修饰符是 **`public`**
- 命名空间、枚举类型的成员的默认修饰符是 **`public`**
- 委托的默认修饰符是 **internal**
- 在命名空间内部或编译单元顶部的所有类型，默认修饰符 **`internal`**



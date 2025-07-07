The `char` type keyword is an alias for the .NET [System.Char](https://learn.microsoft.com/en-us/dotnet/api/system.char) structure type that represents a Unicode UTF-16 code unit, typically a UTF-16 character.

|Type|Range|Size|.NET type|
|---|---|---|---|
|`char`|U+0000 to U+FFFF|16 bit|[System.Char](https://learn.microsoft.com/en-us/dotnet/api/system.char)|
The default value of the `char` type is `\0`, that is, U+0000.

The `char` type supports [comparison](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/comparison-operators), [equality](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators), [increment](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators#increment-operator-), and [decrement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators#decrement-operator---) operators. Moreover, for `char` operands, [arithmetic](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators) and [bitwise logical](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators) operators perform an operation on the corresponding code points and produce the result as an `int` value.

The [[String]] type represents text as a sequence of `char` values.
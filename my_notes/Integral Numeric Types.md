
The _integral numeric types_ represent integer numbers. All integral numeric types are [[Value Type]]s. They're also [simple types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types#built-in-value-types) and can be initialized with [literals](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types#integer-literals). All integral numeric types support [arithmetic](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators), [bitwise logical](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators), [comparison](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/comparison-operators), and [equality](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators) operators.

C# supports the following predefined integral types:

|C# type/keyword|Range|Size|.NET type|
|---|---|---|---|
|`sbyte`|-128 to 127|Signed 8-bit integer|[System.SByte](https://learn.microsoft.com/en-us/dotnet/api/system.sbyte)|
|`byte`|0 to 255|Unsigned 8-bit integer|[System.Byte](https://learn.microsoft.com/en-us/dotnet/api/system.byte)|
|`short`|-32,768 to 32,767|Signed 16-bit integer|[System.Int16](https://learn.microsoft.com/en-us/dotnet/api/system.int16)|
|`ushort`|0 to 65,535|Unsigned 16-bit integer|[System.UInt16](https://learn.microsoft.com/en-us/dotnet/api/system.uint16)|
|`int`|-2,147,483,648 to 2,147,483,647|Signed 32-bit integer|[System.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32)|
|`uint`|0 to 4,294,967,295|Unsigned 32-bit integer|[System.UInt32](https://learn.microsoft.com/en-us/dotnet/api/system.uint32)|
|`long`|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|Signed 64-bit integer|[System.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64)|
|`ulong`|0 to 18,446,744,073,709,551,615|Unsigned 64-bit integer|[System.UInt64](https://learn.microsoft.com/en-us/dotnet/api/system.uint64)|
|`nint`|Depends on platform (computed at runtime)|Signed 32-bit or 64-bit integer|[System.IntPtr](https://learn.microsoft.com/en-us/dotnet/api/system.intptr)|
|`nuint`|Depends on platform (computed at runtime)|Unsigned 32-bit or 64-bit integer|[System.UIntPtr](https://learn.microsoft.com/en-us/dotnet/api/system.uintptr)|     |     |



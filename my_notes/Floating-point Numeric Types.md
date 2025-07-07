The _floating-point numeric types_ represent real numbers. All floating-point numeric types are [[Value Type]]s. They are also [simple types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types#built-in-value-types) and can be initialized with [literals](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types#real-literals). All floating-point numeric types support [arithmetic](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators), [comparison](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/comparison-operators), and [equality](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators) operators.

C# supports the following predefined floating-point types:

|C# type/keyword|Approximate range|Precision|Size|.NET type|
|---|---|---|---|---|
|`float`|±1.5 x 10−45 to ±3.4 x 1038|~6-9 digits|4 bytes|[System.Single](https://learn.microsoft.com/en-us/dotnet/api/system.single)|
|`double`|±5.0 × 10−324 to ±1.7 × 10308|~15-17 digits|8 bytes|[System.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double)|
|`decimal`|±1.0 x 10-28 to ±7.9228 x 1028|28-29 digits|16 bytes|[System.Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal)|
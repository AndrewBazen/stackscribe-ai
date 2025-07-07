Variables of reference types store references to their data (objects), while variables of [[Value Type]]s directly contain their data. With reference types, two variables can reference the same [[Object]]; therefore, operations on one [[Variable]] can affect the object referenced by the other variable. With value types, each variable has its own copy of the data, and it's not possible for operations on one variable to affect the other (except in the case of `in`, `ref`, and `out` parameter variables; see [in](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters#in-parameter-modifier), [ref](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref), and [out](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters#out-parameter-modifier) parameter modifier).

The following keywords are used to declare reference types:

- [[Class]]
- [[Interface]]
- [[Delegate]]
- [[Record]]

C# also provides the following built-in reference types:

- Dynamic
- [[Object]]
- [[String]]
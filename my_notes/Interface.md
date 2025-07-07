An interface defines a contract. Any [[Class]], [[Record]], [[Struct]] that implements that contract must provide an implementation of the members defined in the interface. 


```c#
interface ISampleInterface
{
    void SampleMethod();
}

class ImplementationClass : ISampleInterface
{
    // Explicit interface member implementation:
    void ISampleInterface.SampleMethod()
    {
        // Method implementation.
    }

    static void Main()
    {
        // Declare an interface instance.
        ISampleInterface obj = new ImplementationClass();

        // Call the member.
        obj.SampleMethod();
    }
}
```

An interface can be a member of a namespace or a class. An interface declaration can contain declarations (signatures without any implementation) of the following members:

- [[Method]]
- [[Property]]
- [[Indexers]]
- [[Event]]
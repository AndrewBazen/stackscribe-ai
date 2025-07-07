Means to notify something.

this event follows the delNewMail delegate definitions
```c#
public event delNewMail NewMail;
```

A delegate is a contract between the instance that raises the event and the method that handles the event
```c#
public delegate void delNewMail(Mailbox theMailboxThatRaisedTheEvent, string MailFrom);
```

This is how you invoke an event:
```c#
NewMail?.Invoke(this, mail.From);
```

Examples of methods that have events:
```c#
public int MethodA(int a, int b) { return a + b; }
public int MethodC(int a, int b) { return a - b; }
public int MethodD(int a, int b) { return a * b; }

public string MethodB(DateTime d, float f) { return "Hello"; }
```
The delegates that match the above events:
```c#
public delegate int something(int x, int y);

public delegate string somthingelse(DateTime d, float f);
```
Note: the **something** delegate works for methods A, C, and D.

### Generic Delegates
1. _Action<.....>_ 
	- lets you use model methods with up to 16 parameters.
2. _Func<......>_ 
	- models methods that can have up to 16 parameters and a return value.
3. _EventHandler<>_ 
	- 

### Sample Test Method
```c#
[TestMethod]
public void Method() 
{
	int a = 20000;
	decimal b = 2000.55m;
	something c = MethodA;  //Method that matches the 
						   //delegate is used to assign.
	// delegate is a type strong method description
	int result = c(5,5);
	Assert.AreEqual(10,result);

	// MethodB model using Func<> generic
	Func<DateTime, float, string> b = MethodB
}
```

A delegate can point to any method that matches the signature
This allows decoupling of the code

Generic delegates can be used to model methods instead of creating new delegates.

Generic delegate as an input to a method
```c#
public void Tester(Func<int,int,int> m) 
{
	int result = m(10,10);
}
```
Allows you to make reusable code that is decoupled from the specific method implementation
```c#
Tester(MethodA);
Tester(MethodC);
Tester(MethodD);
```

Invoking is decided by the Tester function, but the implementation after the invocations is determined by the caller method.
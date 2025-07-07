## Default Constructor
takes no arguments and has defaults for [[Class]] [[Field]]s

```C#
 public Invoice()
 {
     _invoiceNumber = 0;
     _customerName = string.Empty;
     _amount = 0.0m;
     _invoiceDate = DateOnly.MinValue;
     _dueDate = DateOnly.MinValue;
 }
```

## Parameterized Constructor
takes in arguments that set the [[Class]] fields
```c#
public Invoice(int invoiceNumber, string customerName, decimal amount, DateOnly invoiceDate, DateOnly dueDate)
{
	_invoiceNumber = invoiceNumber;
	_customerName = customerName;
	_amount = amount;
	_invoiceDate = invoiceDate;
	_dueDate = dueDate;
}
```

## Primary Constructor
Allows you to declare the class, constructor and properties at one time, saving space and code.
the fields name, cost, calories, quantity, and measurement all remain private with accessible public propertys.
```c#
public class Ingredient(string name, decimal cost, int calories, int quantity, Measurement measurement)
{

  public string Name => name;
  public decimal Cost => cost;
  public int Calories => calories;
  public int Quantity => quantity;
  public Measurement Measurement => measurement;

}
```
usually used to return a piece or data, or set data with a new value.

```c#
// properties provide GET/SET access to the fields
public int InvoiceNumber //property is READ ONLY, so only getter
{
  get { return _invoiceNumber; }
}
public string CustomerName //property is READ/WRITE, so has both getter and setter
{
  get { return _customerName; }
  set { _customerName = value; }
}
```

## Auto Implemented Property
allows you to define the property and field at the same time
```c#
public decimal Tax { get; set; }
```

## GET/SET
---
Exposes the data for READ/WRITE access
```c#
public int Calories { get; set; }
```

Get has a shorthand, but Set does not
```c#
 // short hand for getter
 public decimal AmountInCAD => this._amount * 1.25m;
```

private set allows the property to only be set by using the constructor
```c#
public string Name { get; private set; }
```

## Memory

properties do not consume memory

the backing [[Field]]s consume memory if the property stores data (e.g. auto-implemented or explicitly backed properties)

Computed properties do not consume memory as they are calculated on demand
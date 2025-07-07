A [[Field]] is a way to expose data that needs to be stored

```c#
    public class Invoice
    {
        //field - each instance of Invoice may have its own value
        private int _invoiceNumber;
        private string _customerName;
        private decimal _amount;
        private DateOnly _invoiceDate;
        private DateOnly _dueDate;
    }
```
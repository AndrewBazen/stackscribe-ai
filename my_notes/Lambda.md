uses => to create a shorthand implementation of a [[Method]].

test method that implements lambda expressions
```c#
public void ApplyDelegate() 
{
	int[] numbers = {5,7,10,1,3,6};

	var result = numbers.Where(i => true);
	Assert.IsTrue(result.Count() == 6);
	var result2 = numbers.Where(i => i < 5);
	Assert.IsTrue(result2.Count() == 2);
	var result3 = numbers.Where(i => i % 2 == 0);
	Assert.IsTrue(result3.Count() == 2);
	var result4 = numbers.Where(i => i % 2 != 0);
	Assert.IsTrue(result4.Count() == 4);
}
```

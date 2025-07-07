prefer to declare _what_ we want the computer to do, rather than muck around with the details of _how_ to do it.

## Declarative Styling

The following CSS changes all [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) elements to have red text:
```
button {
  color: red;
}
```

It does _not_ execute line-by-line like an [[imperative]] language. Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.
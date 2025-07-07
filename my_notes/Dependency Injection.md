### 🔧 **What is Dependency Injection (DI)?**

Dependency Injection (DI) is a _design pattern_ used to reduce coupling between software components and improve code [[Maintainability]], [[Testability]], and [[Flexibility]]. It’s especially important in modern software development where codebases are complex and frequently tested or reused.

At its core, DI is about giving an object everything it needs to do its job—_from the outside_—rather than letting the object create or find its [[Dependencies]] itself.

Instead of this:
```c#
public class GameManager {
    private Player player = new Player(); // tightly coupled
}
```

You do this:
```c#
public class GameManager {
    private Player player;
    public GameManager(Player player) {
        this.player = player; // dependency injected
    }
}

```

### ✅ **Why is DI important?**

1. **Loose Coupling**  
    Makes code easier to change or extend because components don’t hardcode their [[Dependencies]].
    
2. **Easier Testing**  
    You can inject mock objects during tests instead of relying on real implementations.
    
3. **Reusability**  
    You can reuse the same component in different contexts by injecting different [[Dependencies]].
    
4. **Scalability**  
    Great for larger applications where multiple components depend on shared services (e.g., logging, data access, API clients).

#### Scoped
---
Client-side doesn't currently have a concept of DI scopes. `Scoped`-registered services behave like `Singleton` services.

>The default scope in ASP.net is "a page request"

Server-side development supports the `Scoped` lifetime across HTTP requests but not across SignalR connection/circuit messages among components that are loaded on the client. The Razor Pages or MVC portion of the app treats scoped services normally and recreates the services on _each HTTP request_ when navigating among pages or views or from a page or view to a component. Scoped services aren't reconstructed when navigating among components on the client, where the communication to the server takes place over the SignalR connection of the user's circuit, not via HTTP requests. In the following component scenarios on the client, scoped services are reconstructed because a new circuit is created for the user:

- The user closes the browser's window. The user opens a new window and navigates back to the app.
- The user closes a tab of the app in a browser window. The user opens a new tab and navigates back to the app.
- The user selects the browser's reload/refresh button.

#### Singleton
---
DI creates a _single instance_ of the service. All components requiring a [[Singleton]] service receive the same [[Instance]] of the [[Service]].


```c#
builder.Services.AddSingleton<Sign>(new Sign{ cssClass = "neontext" });
```


#### Transient
---
Whenever a component obtains an instance of a [[Transient]] service from the service [[Container]], it receives a _new [[Instance]]_ of the service.

```c#
builder.Services.AddTransient<Sign>(p => new Sign { cssClass = "neonText" });
```


### 🧪 **When and Why You Should Use It**

#### 🧩 1. **Unit Testing**

Let’s say you have a [[Class]] that fetches data from a [[Database]]:
```c#
public class DataService {
    private IDatabase _db;
    public DataService(IDatabase db) {
        _db = db;
    }

    public string GetData() => _db.Query("SELECT * FROM data");
}
```

In tests, you can inject a `FakeDatabase` or `MockDatabase` to avoid hitting the real DB:
```c#
var fakeDb = new Mock<IDatabase>();
fakeDb.Setup(db => db.Query(It.IsAny<string>())).Returns("Fake Data");

var service = new DataService(fakeDb.Object);
Assert.Equal("Fake Data", service.GetData());
```

**Advantage:** Clean, isolated, fast tests.

#### 🕹️ 2. **Game Development with Unity or MAUI**

Instead of hardcoding a [[Logger]] or config manager:
```c#
public class PlayerStats {
    private ILogger _logger;
    public PlayerStats(ILogger logger) {
        _logger = logger;
    }

    public void TakeDamage(int amount) {
        _logger.Log($"Player took {amount} damage.");
    }
}
```

Now you can inject a different logger in dev vs prod or inject a fake logger during testing.

**Advantage:** Makes debugging and profiling tools swappable and testable.

#### 🌐 3. **Web API Services**

Suppose you’re building a .NET web app. You can register services with the DI container:
```c#
builder.Services.AddScoped<IUserService, UserService>();
```
Then your controller just asks for `IUserService` in its [[Constructor]], and the DI system wires it up.

**Advantage:** Clean separation of concerns. Also allows for easy swapping of implementations (e.g., `MockUserService` in dev).

### 🔄 **Comparison with Other Options**

|Approach|Pros|Cons|
|---|---|---|
|**DI** (Constructor Injection)|Clean, testable, scalable|Slightly more boilerplate, needs DI container|
|**Service Locator**|Easy to use|Hides dependencies, harder to test|
|**Hardcoded Dependencies**|Fast to write|Very hard to test, modify, or reuse|
|**Factory Pattern**|Good for runtime decisions|Still couples object creation logic|
is a way to organize ideas/data/action/routines/events of related things or objects

## Example Class
---
```c#
    public class MSSAStopwatch
    {
        const long DEFAULT_RESOLUTION_IN_TICKS = 100_000; // 100 microseconds
        const long DEFAULT_EVENT_FREQUENCY_IN_TICKS = 1_000_000; // 1 second

        private readonly TimeSpan elapsedTime;
        private readonly TimeSpan eventFrequency;
        private readonly TimeSpan resolution;

        public TimeSpan ElapsedTime { get => elapsedTime; }
        public TimeSpan EventFrequency { get => eventFrequency; }
        public TimeSpan Resolution { get => resolution; }
        public MSSAStopwatch()
        {
            elapsedTime = TimeSpan.Zero;
	        eventFrequency = 
		        TimeSpan.FromTicks(DEFAULT_EVENT_FREQUENCY_IN_TICKS);
            resolution = TimeSpan.FromTicks(DEFAULT_RESOLUTION_IN_TICKS);
        }

        public MSSAStopwatch(TimeSpan eventFrequency, TimeSpan resolution)
        {
            elapsedTime = TimeSpan.Zero;
            this.eventFrequency = eventFrequency;
            this.resolution = resolution;
        }
    }
```

## Class Members
---
- [[Constructor]]
- [[Field]]
- [[Property]]
- [[Method]]
- [[Event]]
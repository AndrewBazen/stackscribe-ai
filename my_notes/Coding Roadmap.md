[[Coding Ledger]]

## 3-Phase Fast-Track (≈ 8 months total)

|Phase|Duration|Core Objectives|Primary Activities|Output / Signal|
|---|---|---|---|---|
|**1 · Algorithmic Turbo**|**Weeks 1 – 8**|Sharpen pattern recognition and error-spotting speed|_Daily_ 1 medium + 1 hard LeetCode; _Weekend_ 3-hour Codeforces contest.  <br>Log every miss in your “failure ledger” that evening.|Median solve time ↓ 40 %; “ledger” ≥ 60 distilled lessons|
|**2 · System-Design Sprint**|**Weeks 9 – 20**|Connect code decisions to scalability & cost|**Mon-Thu**: one small design prompt/night (queue, cache, sharding).  <br>**Fri**: write a one-pager translating design choices into latency + dollar impact.  <br>**Sat**: live-sketch a real-world system on whiteboard, record yourself critiquing it.|12 one-pagers + recorded sketches; able to defend trade-offs in 5-minute pitch|
|**3 · Product-in-the-Wild**|**Weeks 21 – 32**|Tie engineering work to metric movement|Build & iterate an MVP in **4 two-week sprints**.  <br>After each sprint: measure one metric (load time, conversion) and link every PR to that metric Δ.|Case-study blog post + GitHub repo with commit→metric annotations|
> **Why the phases overlap:**  
> Problem-solving stamina (Phase 1) feeds directly into the architecture sketches you’ll do in Phase 2, while Phase 3 forces you to wield both under real constraints. Running them partly in parallel avoids skill atrophy.

---

### Weekly Cadence Template (accelerated)

|Day|2-Hour Block|1-Hour Block|30-min Cool-down|
|---|---|---|---|
|Mon–Thu|Algorithm drill or design prompt|Review yesterday’s “failure ledger” entry|Quick skim of _Designing Data-Intensive Apps_ chapter summary|
|Fri|Write cost/latency one-pager|Self-check with peer or AI code reviewer|Light refactor of any brittle code|
|Sat|3-hr live contest **or** whiteboard system|Sprint retro / metric analysis|Post mortem journal|
|Sun|Rest / Non-tech reading (business case study)|—|Sketch upcoming week goals|
## Tactical Accelerators

1. **Deliberate pair programming once a week** – doubles the pattern pool and forces “explain-while-coding” clarity.
    
2. **Spaced-repetition flashcards** for complexity classes, CAP trade-offs, common scaling numbers (latency at L3 vs. disk).
    
3. **90-minute deep-work sprints** with Pomodoro inside (25-5-25-5-25-5) to hit flow quickly and recover.
    
4. **Diet of tiny deliverables** – every night ends with a commit, a diagram, or a ledger entry; no zero-progress days.
    

---

## Guardrails Against Burnout

| Symptom                                                 | Early Fix                                                           |
| ------------------------------------------------------- | ------------------------------------------------------------------- |
| Consistently > 2 wrong submissions per LeetCode session | Insert 10-minute constraint-mapping ritual before coding            |
| Skipped retros two weeks running                        | Shorten them to bullet lists; perfection is the enemy of cadence    |
| Diminishing contest performance                         | Swap one contest for a rest weekend; sleep is a performance feature |

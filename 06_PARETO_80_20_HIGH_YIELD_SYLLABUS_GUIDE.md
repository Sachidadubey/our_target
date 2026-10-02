# 🎯 The 80/20 "High-Yield" Syllabus Master Blueprint
### The Minimum Topics for Maximum Marks to Reliably Crack Cutoffs
**Strategy:** The Pareto Principle (20% of the topics generate 80% of the exam marks).  
**Target Candidate:** B.Tech CSE (Diploma + Lateral Entry, Fresher, Age ~23, General / EWS)  
**Objective:** Do **NOT** study the whole dictionary. Master this exact, tightly defined core list to score comfortably above the cutoffs with calm, consistent, smart preparation.  
**Date:** October 2026  

---

## 🧭 THE CORE PHILOSOPHY

Government exam syllabi look terrifying because coaching institutes dump 100 chapters on you. 

In actual question papers:
* **80% of the questions come from the same 6–8 recurring chapters.**
* The remaining 20% of questions come from 40 obscure chapters that take 80% of your time to learn.
* **Smart Rule:** Completely ignore the obscure 20%. Master the core 80% with 100% accuracy.

```
       TOTAL SYLLABUS DUMP (100% Chapters)
       ├── 20% High-Yield Core Chapters ───────► PRODUCES 80% OF ALL EXAM MARKS! (Your Focus)
       └── 80% Low-Yield Obscure Chapters ────► Produces only 20% of marks (Ignore initially)
```

---

## 💻 PART 1: THE TECHNICAL CS CORE (FOR SEBI IT, IBPS SO, RRB JE, ISRO & PSUs)

In technical exams (IBPS SO IT, SEBI Grade A IT, RRB JE, Coal India, ISRO), you do **NOT** need to read every engineering subject. 

**Four subjects alone constitute 75% to 80% of all technical questions:**
1. Database Management Systems (DBMS) & SQL
2. Computer Networks (CN)
3. Operating Systems (OS)
4. Data Structures & Core Object-Oriented Programming (Java/C++)

---

### SUBJECT 1: Database Management Systems (DBMS) & SQL
> **Weightage:** ~22% to 25% of all technical marks. (Guaranteed 12–15 questions in a 60-mark paper).

#### Exactly What to Prepare (Only 4 Topics):
1. **Normalization (The #1 Most Repeated Topic in Govt Exams):**
   * Functional Dependencies (FDs) and Armstrong's axioms.
   * How to find **Candidate Keys** from a set of FDs (Shortcut: Check which attribute never appears on the Right-Hand Side).
   * Exact rules to distinguish:
     * **1NF:** Atomic values (no multi-valued attributes).
     * **2NF:** 1NF + No partial dependency (non-prime attributes must depend on the whole candidate key, not part of it).
     * **3NF:** 2NF + No transitive dependency ($X \rightarrow Y$, where $X$ is a super key or $Y$ is a prime attribute).
     * **BCNF:** For every non-trivial FD $X \rightarrow Y$, $X$ must be a super key.
   * *Exam Trick:* Every exam has at least 3 questions asking: *"Which normal form is this relation in?"*
2. **SQL Queries (Crucial for SEBI IT, IBPS SO & C-DAC):**
   * **Joins:** Inner Join, Left Outer Join, Right Outer Join, Full Outer Join (predicting output rows from two small tables).
   * **Clauses:** `GROUP BY` and `HAVING` (Rule: `WHERE` filters rows before grouping; `HAVING` filters aggregated groups).
   * **Subqueries:** `IN`, `EXISTS`, `NOT EXISTS`, `UNION` vs `UNION ALL` (UNION eliminates duplicates; UNION ALL keeps duplicates and is faster).
   * **Aggregate Functions:** `COUNT(*)`, `COUNT(column)` (know the difference: `COUNT(column)` ignores NULL values!).
3. **Transactions & ACID Properties:**
   * **A**tomicity (All or nothing — handled by Transaction Manager / Rollback).
   * **C**onsistency (Database remains in a valid state).
   * **I**solation (Concurrent execution yields same result as serial execution — handled by Concurrency Control).
   * **D**urability (Committed changes survive system crash — handled by Recovery Manager / Write-Ahead Logging).
   * **Schedules:** Conflict Serializability (drawing precedence graphs; detecting cycles).
   * **Locking Protocols:** Shared (S) lock vs Exclusive (X) lock, Two-Phase Locking (2PL) ensures conflict serializability.
4. **Relational Keys:**
   * Primary Key, Super Key, Candidate Key, Foreign Key (Referential Integrity Constraint and `ON DELETE CASCADE`).

---

### SUBJECT 2: Computer Networks (CN)
> **Weightage:** ~20% of all technical marks.

#### Exactly What to Prepare (Only 4 Topics):
1. **The 7-Layer OSI & TCP/IP Model (Guaranteed 4 Questions):**
   * Physical Layer: Hubs, Repeaters, Bits.
   * Data Link Layer: Switches, Bridges, Frames, MAC Address (48-bit), Error control (CRC).
   * Network Layer: Routers, Packets, IP Address (32-bit IPv4 / 128-bit IPv6), ICMP, ARP (IP $\rightarrow$ MAC), RARP.
   * Transport Layer: Segments, Ports, TCP (Reliable, Connection-oriented), UDP (Unreliable, Connectionless).
   * Application Layer: HTTP (Port 80), HTTPS (Port 443), DNS (Port 53, uses UDP), FTP (Port 20/21), SSH (Port 22), SMTP (Port 25).
   * *Exam Trick:* Memorize which protocol and device belongs to which layer and standard port numbers.
2. **IPv4 Addressing & CIDR Subnetting:**
   * Classful addressing ranges:
     * Class A: `1.0.0.0` to `126.255.255.255` (Default mask `/8`).
     * Class B: `128.0.0.0` to `191.255.255.255` (Default mask `/16`).
     * Class C: `192.0.0.0` to `223.255.255.255` (Default mask `/24`).
     * Class D: `224.0.0.0` to `239.255.255.255` (Multicasting).
     * Class E: `240.0.0.0` to `255.255.255.255` (Experimental).
   * CIDR Notation (e.g., `192.168.1.0/26`):
     * Number of host bits = $32 - 26 = 6$.
     * Total IP addresses = $2^6 = 64$.
     * Usable hosts = $2^6 - 2 = 62$ (subtract Network ID and Broadcast ID).
3. **TCP Protocol Mechanics:**
   * 3-Way Handshake: `SYN` $\rightarrow$ `SYN + ACK` $\rightarrow$ `ACK`.
   * Flow Control: Sliding Window Protocol (Stop-and-Wait, Go-Back-N, Selective Repeat window sizes).
   * Congestion Control: Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery.
4. **Network Security Basics:**
   * Symmetric Key (DES, AES - same key for encryption/decryption) vs Asymmetric Key (RSA - Public key encrypts, Private key decrypts).
   * Firewalls (Packet filtering vs Application proxy).

---

### SUBJECT 3: Operating Systems (OS)
> **Weightage:** ~18% to 20% of all technical marks.

#### Exactly What to Prepare (Only 4 Topics):
1. **CPU Scheduling Algorithms (Guaranteed 3–4 Questions):**
   * **FCFS (First-Come, First-Served):** Convoy effect.
   * **SJF (Shortest Job First):** Optimal average waiting time (Non-preemptive vs Preemptive / SRTF).
   * **Round Robin:** Time Quantum selection (If quantum is too large, behaves like FCFS; if too small, excessive context switching).
   * *What to Practice:* Given a table of 4 processes with Arrival Time and Burst Time, calculate **Average Waiting Time** and **Turnaround Time** ($TAT = Completion\ Time - Arrival\ Time$; $WT = TAT - Burst\ Time$).
2. **Process Synchronization & Semaphores:**
   * Critical Section Problem: 3 Requirements (Mutual Exclusion, Progress, Bounded Waiting).
   * **Counting Semaphore vs Binary Semaphore (Mutex):**
     * Wait operation (`P()`): Decrements value ($S = S - 1$). If $S < 0$, process blocks.
     * Signal operation (`V()`): Increments value ($S = S + 1$).
     * *Standard calculation:* If initial semaphore value is 7, and 12 P operations and 8 V operations are executed, final value = $7 - 12 + 8 = 3$.
3. **Deadlocks (Guaranteed 2–3 Questions):**
   * 4 Necessary Conditions: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.
   * Deadlock Prevention: Invalidate at least one of the 4 conditions.
   * Deadlock Avoidance: **Banker's Algorithm** (calculating Need Matrix: $Need = Max - Allocation$).
4. **Memory Management & Virtual Memory:**
   * Paging: Logical address divided into Page Number and Offset; Physical address into Frame Number and Offset.
   * TLB (Translation Lookaside Buffer): Effective Memory Access Time calculation ($EMAT = Hit\ Ratio \times (TLB + Memory) + (1 - Hit\ Ratio) \times (TLB + 2 \times Memory)$).
   * Page Replacement Algorithms: FIFO (Belady's Anomaly), LRU (Least Recently Used), Optimal.

---

### SUBJECT 4: Data Structures & Core OOP (Java / C++)
> **Weightage:** ~15% to 18% of all technical marks.

#### Exactly What to Prepare:
1. **Asymptotic Complexity (Big O) Chart (Guaranteed 2 Questions):**
   * Sorting Algorithms:
     * Quicksort: Best/Avg $O(n \log n)$, Worst $O(n^2)$.
     * Mergesort: Best/Avg/Worst $O(n \log n)$ (Stable, requires $O(n)$ space).
     * Heapsort: Best/Avg/Worst $O(n \log n)$ (In-place).
2. **Binary Search Trees (BST):**
   * Traversals: Inorder (always yields sorted ascending order for BST), Preorder, Postorder.
   * Insertion and search complexity: $O(\log n)$ average, $O(n)$ worst case.
3. **Stacks & Queues Applications:**
   * Infix to Postfix conversion using Stacks.
   * Queue using two Stacks.
4. **Core OOP Concepts (Java):**
   * Method Overloading (Compile-time polymorphism) vs Method Overriding (Run-time polymorphism).
   * Abstract Class vs Interface (Default methods in Java 8, multiple inheritance).
   * Static keyword, Final keyword, Garbage collection basics.

---

## 📊 PART 2: THE APTITUDE CORE (FOR RRB NTPC, SSC CGL & DSSSB)

In non-technical exams, **90% of students fail because they try to solve 30 different chapters in maths and read encyclopedias of history**. 

To reliably crack the cutoffs (e.g., RRB NTPC, SSC CGL Tier-1, DSSSB), master **only these specific high-frequency chapters**:

---

### 1. Quantitative Aptitude (The "Power 6" Chapters)
Mastering these 6 chapters covers **75% of all quant questions**:

1. **Percentages (The Foundation of Everything):**
   * Fraction-to-percentage conversion shortcuts:
     $$\frac{1}{2} = 50\%,\ \frac{1}{3} = 33.33\%,\ \frac{1}{4} = 25\%,\ \frac{1}{5} = 20\%,\ \frac{1}{6} = 16.66\%,\ \frac{1}{7} = 14.28\%,\ \frac{1}{8} = 12.5\%,\ \frac{1}{9} = 11.11\%$$
   * Successive percentage change formula: $a + b + \frac{ab}{100}$.
2. **Ratio & Proportion:**
   * Combining ratios (If $A:B = 2:3$ and $B:C = 4:5$, then $A:B:C = 8:12:15$).
   * Proportional division of money/assets.
3. **Profit, Loss & Discount:**
   * Cost Price (CP), Selling Price (SP), Marked Price (MP).
   * Formulas: $Profit\% = \frac{SP - CP}{CP} \times 100$; Discount is always calculated on Marked Price (MP).
   * Dishonest shopkeeper problems (using false weights).
4. **Time & Work (The Easiest & Most Scoring Chapter):**
   * The LCM Method: If A does a work in 10 days and B in 15 days $\rightarrow$ Total work = LCM(10, 15) = 30 units.
   * Efficiency of A = 3 units/day; B = 2 units/day. Together = 5 units/day $\rightarrow$ Days = $30 / 5 = 6$ days.
   * Pipes and Cisterns (Inlet pipe + efficiency, Outlet pipe - efficiency).
5. **Speed, Time & Distance:**
   * Unit conversion: $1\text{ km/hr} = \frac{5}{18}\text{ m/s}$.
   * Relative speed (Same direction: $S_1 - S_2$; Opposite direction: $S_1 + S_2$).
   * Trains crossing a pole (distance = train length) vs crossing a platform (distance = train length + platform length).
6. **Simple Interest (SI) & Compound Interest (CI):**
   * $SI = \frac{P \times R \times T}{100}$.
   * Difference between CI and SI for 2 years: $Diff = P \times \left(\frac{R}{100}\right)^2$.

> [!TIP]
> **What to Skip for Now:** Leave out complex Trigonometric identities, Coordinate Geometry, and Permutation/Combination. They take 30 days to learn and appear as only 1 or 2 isolated questions.

---

### 2. General Intelligence & Reasoning (The 100% Score Engine)
Reasoning is where you can get **28 out of 30 marks** in RRB NTPC or SSC with just **5 logical patterns**:

1. **Syllogisms (Venn Diagrams):**
   * Statements with "All", "Some", "No", and "Some Not".
   * Possibility cases (If conclusion is not definitely contradicted, possibility is true).
2. **Coding-Decoding:**
   * Letter position numbering (A=1 to Z=26, using the memory word `EJOTY` = 5, 10, 15, 20, 25).
   * Opposite letters (A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N).
3. **Blood Relations:**
   * Drawing standard generation trees: Males as $[+]$, Females as $[-]$, Marriage as $[\Leftrightarrow]$, Siblings as $[—]$.
4. **Direction & Distance Sense:**
   * Cardinal directions (North, South, East, West) + Pythagoras theorem ($H^2 = P^2 + B^2$) for shortest distance.
5. **Non-Verbal / Visual Reasoning (Huge in RRB & SSC):**
   * Mirror images, Water images, Paper folding, Embedded figures. (100% visual, zero formulas needed).

---

### 3. General Awareness (The Smart Filter)
Do **NOT** open encyclopedias of Indian history. Follow this 3-pillar filter:

1. **Indian Polity (Highest Return on Investment):**
   * Fundamental Rights (Articles 12 to 35) — Know Article 14 (Equality), 19 (Freedoms), 21 (Life & Liberty), 32 (Constitutional Remedies & Writs).
   * President & Governor powers (Veto, Pardoning, Ordinance).
   * Key Amendments: 42nd (Mini-Constitution), 44th (Right to Property removed), 86th (Right to Education), 103rd (10% EWS Quota).
2. **General Science (Class 9th & 10th NCERT Basics):**
   * Biology: Vitamins and deficiency diseases (Vitamin A: Night Blindness; Vitamin C: Scurvy; Vitamin D: Rickets), Blood groups (AB+ universal recipient, O- universal donor).
   * Physics: SI Units (Force: Newton, Power: Watt, Work/Energy: Joule, Frequency: Hertz), Lenses & Mirrors (Concave vs Convex uses).
   * Chemistry: Chemical names (Baking soda: $\text{NaHCO}_3$, Washing soda: $\text{Na}_2\text{CO}_3$, Bleaching powder: $\text{CaOCl}_2$), pH scale.
3. **Current Affairs (Last 6 Months Only):**
   * Major government digital schemes (IndiaAI, DigiLocker, UPI global tie-ups).
   * ISRO space missions & DRDO defence missile tests.
   * Major sports winners (Olympics, ICC Cricket, Grand Slams).

---

## 🪖 PART 3: THE DEFENCE SSB INTERVIEW CORE (INDIAN ARMY TGC-145)

Because Indian Army TGC-145 has **zero written exam**, your selection depends entirely on the **5-Day Service Selection Board (SSB)**:

```
DAY 1: SCREENING TEST (The Only Elimination Barrier)
├── 1. Officer Intelligence Rating (OIR) Test:
│   └── 50 Verbal & Non-Verbal reasoning questions (Letter series, dice, cube rotation).
│       Easy for a B.Tech graduate; target 45+ correct to get OIR Rank 1.
└── 2. Picture Perception and Description Test (PPDT):
    └── A hazy picture is shown for 30 seconds.
    └── Write a positive, constructive 4-minute story with:
        • A relatable hero (around age 23).
        • A practical problem being solved (e.g., setting up a rural solar pump or tech workshop).
        • A successful outcome.
    └── Group Discussion: Speak calmly 2–3 times with clear articulation (do not shout).
```
* **If you clear Day 1 Screening, you stay for the full 5 days and your chance of final recommendation multiplies by 10x.**

---

## 📅 4. YOUR DAILY "SMART WORK" TIMETABLE (ONLY 3.5 HOURS A DAY)

You do not need to study 10 hours a day. Follow this balanced routine:

```
DAILY 3.5-HOUR ROUTINE
│
├── BLOCK 1: CORE TECHNICAL CS (1.5 Hours)
│   ├── Monday & Tuesday   : DBMS & SQL (Normalization, Joins, Transactions)
│   ├── Wednesday & Thursday: Operating Systems (CPU Scheduling, Semaphores, Paging)
│   └── Friday & Saturday  : Computer Networks (OSI, Subnetting, TCP/IP)
│
├── BLOCK 2: SPEED APTITUDE & REASONING (1.5 Hours)
│   ├── 45 Mins: Quantitative Aptitude (Percentages, Time & Work, or Ratios)
│   └── 45 Mins: Reasoning (Syllogisms, Coding-Decoding, or Blood Relations)
│
└── BLOCK 3: CURRENT AFFAIRS & REVISION (30 Minutes)
    └── Read a monthly current affairs digest or solve 1 previous year paper set.
```

---

## 🏆 SUMMARY OF CUTOFF SAFETY MARGINS

By mastering **only this 80/20 list**:
* In **IBPS SO (IT Officer)**: Cutoff is ~14.50 marks out of 60. You will comfortably score **28 to 35 marks**.
* In **SEBI Grade A IT**: Qualifying cutoff is 40%. You will comfortably score **55 to 65 marks**.
* In **RRB NTPC (CBT-1)**: Cutoff is ~70 out of 100. You will comfortably score **78 to 84 marks**.
* In **Army TGC-145**: Day 1 OIR test requires ~70%. You will easily achieve **OIR Rank 1 (90%+)**.

*All topics, formulas, and rules are saved in your workspace at [`06_PARETO_80_20_HIGH_YIELD_SYLLABUS_GUIDE.md`](file:///c:/Users/ankus/Desktop/gov%20jobs/06_PARETO_80_20_HIGH_YIELD_SYLLABUS_GUIDE.md).*

# 🏦 IBPS SO (I.T. Officer Scale I)
## Professional Knowledge (Core CS) Shift Papers & Solutions

---

### 1. Database Management Systems
* **Q1:** In an SQL database, which command is used to revoke previously granted table permissions from a user?
  * **Answer:** `REVOKE` (e.g., `REVOKE SELECT, INSERT ON Employees FROM user1;`).
* **Q2:** Which of the following normal forms deals with multi-valued dependencies?
  * **Answer:** **4NF (Fourth Normal Form)**. (A table is in 4NF if it is in BCNF and contains no multi-valued dependencies $X 	woheadrightarrow Y$).
* **Q3:** What is a Phantom Read phenomenon in transaction management?
  * **Answer:** When a transaction reads a set of rows matching a condition, and a second transaction inserts or deletes rows matching that condition and commits, causing the first transaction to see different rows on a re-read. Prevented by **Serializable Isolation Level**.

---

### 2. Software Engineering & Web Technologies
* **Q4:** What is the HTTP status code returned by a REST API when a requested resource is created successfully?
  * **Answer:** **201 Created**.
* **Q5:** What is the primary difference between White-Box Testing and Black-Box Testing?
  * **Answer:** White-Box testing tests internal logic, code paths, and branch coverage; Black-Box testing tests input-output functionality without knowledge of internal code.
* **Q6:** Which vulnerability is mitigated by using Parameterized Prepared Statements in SQL?
  * **Answer:** **SQL Injection (SQLi)**.

---

### 3. Operating Systems
* **Q7:** What is Belady's Anomaly?
  * **Answer:** The counter-intuitive phenomenon where increasing the number of page frames results in an **increase** in the number of page faults. It occurs in **FIFO (First-In, First-Out)** page replacement, but never in Stack-based algorithms like LRU or Optimal.

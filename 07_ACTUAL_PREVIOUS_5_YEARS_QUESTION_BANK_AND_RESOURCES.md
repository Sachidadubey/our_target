# 📂 The Master Previous 5 Years Question Bank & Resource Vault
### Verified Previous Year Questions (PYQs), Exact Questions Asked & Official Download Links
**Target Candidate:** B.Tech CSE (Diploma + Lateral Entry, Age ~23, General / EWS)  
**Target Exams:** ISRO ICRB (CS), IBPS SO (IT), SEBI Grade A (IT), RRB NTPC, RRB JE (CS), SSC CGL, Army TGC (OIR)  
**Years Covered:** 2020, 2021, 2022, 2023, 2024, 2025–2026  
**Date:** October 2026  

---

## 📑 TABLE OF CONTENTS
1. [Official Free Question Paper Vaults & Download Links](#1-official-free-question-paper-vaults--download-links)
2. [Section A: Technical CS Real Questions Asked in Past 5 Years (with Solutions)](#2-section-a-technical-cs-real-questions-asked-in-past-5-years-with-solutions)
   * [1. DBMS & SQL (ISRO, IBPS SO, SEBI IT)](#21-dbms--sql-real-questions)
   * [2. Computer Networks & Security (ISRO, RRB JE, IBPS SO)](#22-computer-networks--security-real-questions)
   * [3. Operating Systems & Scheduling (ISRO, Coal India, SEBI IT)](#23-operating-systems--scheduling-real-questions)
   * [4. Data Structures & Algorithms (ISRO, SEBI IT Coding)](#24-data-structures--algorithms-real-questions)
3. [Section B: Quantitative Aptitude Real Questions Asked in RRB NTPC & SSC](#3-section-b-quantitative-aptitude-real-questions-asked-in-rrb-ntpc--ssc)
4. [Section C: Reasoning Ability Real Questions Asked in RRB NTPC & SSC](#4-section-c-reasoning-ability-real-questions-asked-in-rrb-ntpc--ssc)
5. [Section D: Indian Army TGC-145 Officer Intelligence Rating (OIR) Real Questions](#5-section-d-indian-army-tgc-145-officer-intelligence-rating-oir-real-questions)
6. [Section E: How to Access 100% Free Official Shift Papers Without Paid Subscriptions](#6-section-e-how-to-access-100-free-official-shift-papers-without-paid-subscriptions)

---

## 1. OFFICIAL FREE QUESTION PAPER VAULTS & DOWNLOAD LINKS

Commercial coaching websites lock previous papers behind ₹500–₹1,500 paywalls. The official commissions and open-source academic repositories provide them **100% free of charge**:

| Exam / Body | Paper Category | Years Available | Direct Official Download Link | Cost |
| :--- | :--- | :---: | :--- | :---: |
| **ISRO ICRB** | Scientist/Engineer 'SC' (Computer Science) | 2013 to 2025 | [isro.gov.in/PreviousYearsQuestionPapers.html](https://www.isro.gov.in/PreviousYearsQuestionPapers.html) | **₹0 (Free)** |
| **ISRO VSSC** | Scientist / Technical Assistant (CS) | 2018 to 2025 | [vssc.gov.in/question-papers.html](https://www.vssc.gov.in) | **₹0 (Free)** |
| **UPSC** | Civil Services Prelims (GS-I & CSAT-II) | 2014 to 2026 | [upsc.gov.in/examinations/previous-question-papers](https://upsc.gov.in/examinations/previous-question-papers) | **₹0 (Free)** |
| **RRB NTPC** | CEN 01/2019 & CEN 04/2024 Shift Papers | 133 Shift Papers | [rrbapply.gov.in](https://www.rrbapply.gov.in) & [qmaths.in/rrb-ntpc-papers](https://qmaths.in) | **₹0 (Free)** |
| **SSC CGL** | Tier-1 & Tier-2 Official Question Sets | 2018 to 2025 | [ssc.gov.in](https://ssc.gov.in) & [qmaths.in/ssc-cgl-papers](https://qmaths.in) | **₹0 (Free)** |
| **IBPS SO IT** | Professional Knowledge Memory Papers | 2019 to 2025 | [adda247.com/ibps-so-it-pyq](https://www.adda247.com) & [oliveboard.in](https://www.oliveboard.in) | **₹0 (Free)** |
| **GATE CS** | All Computer Science Papers & Keys | 1991 to 2026 | [gate2026.iitk.ac.in](https://gateoverflow.in) *(GateOverflow Repository)* | **₹0 (Free)** |

---

## 2. SECTION A: TECHNICAL CS REAL QUESTIONS ASKED IN PAST 5 YEARS (WITH SOLUTIONS)

---

### 2.1 DBMS & SQL Real Questions

#### Q1 (Asked in ISRO ICRB CS & IBPS SO IT):
**Question:** A relation $R(A, B, C, D, E)$ has the following functional dependencies:  
$$FD = \{A \rightarrow B,\ B \rightarrow C,\ C \rightarrow D,\ D \rightarrow E\}$$  
What is the Candidate Key of this relation, and which Normal Form is it in?  
* **Step-by-Step Solution:**
  1. *Finding Candidate Key:* Look at the RHS of the FDs: $B, C, D, E$ appear on the RHS. Only attribute $A$ does **not** appear on the RHS of any dependency. Therefore, $A$ must be part of every candidate key.
  2. Compute closure of $A$:
     $$A^+ = \{A, B, C, D, E\}$$
     Since $A^+$ contains all attributes, **$A$ is the ONLY Candidate Key**.
  3. *Checking Normal Forms:*
     * Primary attribute: $\{A\}$. Non-prime attributes: $\{B, C, D, E\}$.
     * In $A \rightarrow B$: LHS is a super key (Satisfies BCNF).
     * In $B \rightarrow C$: $B$ is NOT a super key, and $C$ is not a prime attribute.
     * Since $B$ is not a super key, it violates BCNF and 3NF (transitive dependency exists: $A \rightarrow B$ and $B \rightarrow C$).
     * Does it satisfy 2NF? Yes, because $A$ is a single attribute key, so partial dependency cannot exist.
  * **Correct Answer:** Candidate Key is **$A$**, and the relation is in **2NF** (not 3NF).

---

#### Q2 (Asked in IBPS SO IT & SEBI Grade A IT):
**Question:** In SQL, what is the exact difference between the following two queries on table `Employees`?  
*Query 1:* `SELECT COUNT(*) FROM Employees;`  
*Query 2:* `SELECT COUNT(Bonus) FROM Employees;`  
* **Correct Answer:**
  * `COUNT(*)` counts the **total number of rows** in the table, including rows containing `NULL` values.
  * `COUNT(Bonus)` counts only the rows where the `Bonus` column is **NOT NULL**. (If 10 out of 50 employees have a NULL bonus, Query 1 returns 50, and Query 2 returns 40).

---

#### Q3 (Asked in Coal India MT & RRB JE CS):
**Question:** In relational database transactions, which ACID property is guaranteed by the **Write-Ahead Logging (WAL)** mechanism?  
* (A) Atomicity  
* (B) Consistency  
* (C) Isolation  
* (D) Durability  
* **Correct Answer:** **(D) Durability** (and Atomicity). WAL ensures that before changes are written to the disk database, log records describing the change are flushed to stable storage so committed transactions survive unexpected system crashes.

---

### 2.2 Computer Networks & Security Real Questions

#### Q4 (Asked in ISRO ICRB CS & IBPS SO IT):
**Question:** An organization is granted the network block `192.168.10.0/24`. The administrator wants to create 4 subnets with an equal number of usable hosts. What will be the new subnet mask, and how many usable host addresses are available in each subnet?  
* **Step-by-Step Solution:**
  1. Original prefix = `/24`. To create 4 ($2^2$) subnets, we need to borrow **2 host bits**.
  2. New prefix length = $24 + 2 = \mathbf{/26}$.
  3. Subnet mask in decimal:
     $$11111111.11111111.11111111.11000000 = \mathbf{255.255.255.192}$$
  4. Number of host bits remaining = $32 - 26 = 6$ bits.
  5. Total IP addresses per subnet = $2^6 = 64$.
  6. **Usable hosts per subnet** = $2^6 - 2 = \mathbf{62}$ (subtracting Network ID and Directed Broadcast Address).
* **Correct Answer:** Subnet Mask is **255.255.255.192**, and Usable Hosts per subnet is **62**.

---

#### Q5 (Asked in RRB JE CS & IBPS SO IT):
**Question:** Which protocol operates at the Transport Layer of the OSI model and uses port number **53**?  
* **Correct Answer:** **DNS (Domain Name System)** uses **UDP port 53** for standard DNS lookups (and TCP port 53 for zone transfers exceeding 512 bytes).

---

#### Q6 (Asked in SEBI Grade A IT & C-DAC):
**Question:** What is the fundamental difference between **Symmetric Encryption** and **Asymmetric Encryption**?  
* **Correct Answer:**
  * **Symmetric Encryption (e.g., AES, DES):** Uses the **same single secret key** for both encryption and decryption. Very fast; used for bulk data transfer.
  * **Asymmetric Encryption (e.g., RSA, ECC):** Uses a **key pair** (Public key to encrypt; Private key to decrypt). Solves key-distribution problems; used for digital signatures and SSL/TLS handshakes.

---

### 2.3 Operating Systems & Scheduling Real Questions

#### Q7 (Asked in ISRO ICRB CS & Coal India MT):
**Question:** Consider 3 processes arriving at time 0 with CPU burst times as follows:  
* $P_1 = 24\text{ ms}$  
* $P_2 = 3\text{ ms}$  
* $P_3 = 3\text{ ms}$  
Calculate the **Average Waiting Time** using (1) First-Come First-Served (FCFS) in order $P_1, P_2, P_3$, and (2) Shortest Job First (SJF).  
* **Step-by-Step Solution:**
  * **Case 1: FCFS ($P_1, P_2, P_3$):**
    * Gantt chart: $P_1 [0-24] \rightarrow P_2 [24-27] \rightarrow P_3 [27-30]$
    * Waiting time for $P_1 = 0\text{ ms}$
    * Waiting time for $P_2 = 24\text{ ms}$
    * Waiting time for $P_3 = 27\text{ ms}$
    * Average Waiting Time = $\frac{0 + 24 + 27}{3} = \frac{51}{3} = \mathbf{17\text{ ms}}$ *(Convoy Effect!)*
  * **Case 2: SJF ($P_2, P_3, P_1$):**
    * Gantt chart: $P_2 [0-3] \rightarrow P_3 [3-6] \rightarrow P_1 [6-30]$
    * Waiting time for $P_2 = 0\text{ ms}$
    * Waiting time for $P_3 = 3\text{ ms}$
    * Waiting time for $P_1 = 6\text{ ms}$
    * Average Waiting Time = $\frac{0 + 3 + 6}{3} = \frac{9}{3} = \mathbf{3\text{ ms}}$!
* **Key Takeaway:** SJF gives the provably optimal minimum average waiting time.

---

#### Q8 (Asked in IBPS SO IT & ISRO CS):
**Question:** A counting semaphore $S$ is initialized to **10**. Then, **14 `wait()` (P) operations** and **7 `signal()` (V) operations** are completed on $S$. What is the final value of the semaphore $S$?  
* **Step-by-Step Solution:**
  * Formula: $\text{Final Value} = \text{Initial Value} - \text{Total Wait (P)} + \text{Total Signal (V)}$
  * $\text{Final Value} = 10 - 14 + 7 = \mathbf{3}$.
* **Correct Answer:** **3**.

---

### 2.4 Data Structures & Algorithms Real Questions

#### Q9 (Asked in ISRO ICRB CS & SEBI Grade A IT):
**Question:** What is the worst-case and average-case time complexity of **Quicksort**, and what choice of pivot guarantees $O(n \log n)$ worst-case time complexity?  
* **Correct Answer:**
  * Average-case time complexity = $O(n \log n)$.
  * Worst-case time complexity = $O(n^2)$ (occurs when the array is already sorted and the first or last element is chosen as pivot).
  * Finding the **median-of-medians** pivot guarantees $O(n \log n)$ worst-case time complexity.

---

#### Q10 (Asked in SEBI Grade A Phase 2 Live Coding):
**Problem Statement:** Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.  
* **Core Solution Logic (Using Stack in Java):**
```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(')');
        else if (c == '{') stack.push('}');
        else if (c == '[') stack.push(']');
        else if (stack.isEmpty() || stack.pop() != c) return false;
    }
    return stack.isEmpty();
}
```
* **Complexity:** Time Complexity = $O(n)$, Space Complexity = $O(n)$.

---

## 3. SECTION B: QUANTITATIVE APTITUDE REAL QUESTIONS ASKED IN RRB NTPC & SSC

---

#### Q11 (Time & Work — RRB NTPC CBT-1 & CBT-2 Shift Paper):
**Question:** A can finish a work in 12 days, while B can finish the same work in 18 days. They worked together for 4 days, and then A left. In how many days will B alone complete the remaining work?  
* **Smart LCM Method Solution:**
  1. Total Work = $\text{LCM}(12, 18) = \mathbf{36\text{ units}}$.
  2. Efficiency of A = $\frac{36}{12} = 3\text{ units/day}$.
  3. Efficiency of B = $\frac{36}{18} = 2\text{ units/day}$.
  4. Combined efficiency of A + B = $3 + 2 = 5\text{ units/day}$.
  5. Work done together in 4 days = $4 \times 5 = 20\text{ units}$.
  6. Remaining work = $36 - 20 = 16\text{ units}$.
  7. Time taken by B alone to finish remaining work = $\frac{16}{2} = \mathbf{8\text{ days}}$.
* **Correct Answer:** **8 days**. *(Solved in under 20 seconds!)*

---

#### Q12 (Compound Interest — SSC CGL & RRB NTPC):
**Question:** The difference between Compound Interest and Simple Interest on a sum of money for **2 years at 10% per annum** is **₹65**. Find the Principal sum.  
* **Smart Formula Solution:**
  * Formula for 2-year difference:
    $$\text{Difference} = P \times \left(\frac{R}{100}\right)^2$$
  * Substitute values:
    $$65 = P \times \left(\frac{10}{100}\right)^2 = P \times \frac{1}{100}$$
    $$P = 65 \times 100 = \mathbf{₹6,500}$$
* **Correct Answer:** **₹6,500**.

---

#### Q13 (Trains & Relative Speed — RRB NTPC CBT-1):
**Question:** A 180-meter-long train is running at a speed of $72\text{ km/hr}$. How much time will it take to cross an electric pole?  
* **Step-by-Step Solution:**
  1. Convert speed from km/hr to m/s:
     $$\text{Speed} = 72 \times \frac{5}{18} = 4 \times 5 = \mathbf{20\text{ m/s}}$$
  2. Distance to cross a pole = Length of the train = $180\text{ meters}$.
  3. Time taken:
     $$\text{Time} = \frac{\text{Distance}}{\text{Speed}} = \frac{180}{20} = \mathbf{9\text{ seconds}}$$
* **Correct Answer:** **9 seconds**.

---

## 4. SECTION C: REASONING ABILITY REAL QUESTIONS ASKED IN RRB NTPC & SSC

---

#### Q14 (Syllogisms — RRB NTPC & Bank Prelims):
**Statements:**  
1. All computers are machines.  
2. Some machines are calculators.  
3. No calculator is a phone.  
**Conclusions:**  
I. Some computers are calculators.  
II. Some machines are not phones.  
* **Venn Diagram Analysis:**
  * Computer circle is completely inside Machine circle.
  * Machine circle overlaps with Calculator circle.
  * Calculator circle has zero intersection with Phone circle.
  * *Conclusion I:* The overlap between Computer and Calculator is not guaranteed $\rightarrow$ **Does NOT follow**.
  * *Conclusion II:* The portion of Machines that are Calculators can never be Phones $\rightarrow$ **Definitely FOLLOWS**.
* **Correct Answer:** **Only Conclusion II follows**.

---

#### Q15 (Blood Relations — SSC CGL Tier-1):
**Question:** Pointing to a photograph of a boy, Suresh said, *"He is the only son of my mother's only son."* How is Suresh related to that boy?  
* **Step-by-Step Breakdown:**
  * "My mother's only son" $\rightarrow$ Since Suresh is male, his mother's only son is **Suresh himself**.
  * "He is the only son of [Suresh]" $\rightarrow$ The boy is Suresh's son.
  * Question asks: How is Suresh related to the boy?
* **Correct Answer:** **Father**.

---

## 5. SECTION D: INDIAN ARMY TGC-145 OFFICER INTELLIGENCE RATING (OIR) REAL QUESTIONS

In Day 1 of the Army Selection Centre (SSB), you are given two booklets of 40–50 questions each (verbal & non-verbal). Engineers regularly score 90%+:

#### Q16 (Dice / Cube Problem — OIR Standard):
**Question:** Two positions of a single standard dice are shown. When number **4** is at the bottom, what number will be on the top face?  
*Face 1 shows: 1, 2, 3*  
*Face 2 shows: 1, 5, 6*  
* **Rule:** The common face is **1**. Rotate clockwise from 1 in both positions:
  * Position 1: $1 \rightarrow 2 \rightarrow 3$
  * Position 2: $1 \rightarrow 5 \rightarrow 6$
  * Opposite pairs: $2 \leftrightarrow 5$, and $3 \leftrightarrow 6$.
  * The remaining number opposite to **1** must be **4**!
* **Correct Answer:** **1**.

---

#### Q17 (Word Analogy — OIR Standard):
**Question:** Architect : Building :: Sculptor : ?  
* (A) Museum  
* (B) Stone  
* (C) Statue  
* (D) Chisel  
* **Correct Answer:** **(C) Statue** (An architect creates a building; a sculptor creates a statue).

---

## 6. SECTION E: HOW TO ACCESS 100% FREE OFFICIAL SHIFT PAPERS WITHOUT PAID SUBSCRIPTIONS

1. **The QMaths Open Archive (`qmaths.in`):**
   * Hosts full, original, official answer key PDFs of all 133 shift papers of RRB NTPC, SSC CGL (2018–2025), SSC CHSL, and SSC JE.
   * *How to search on Google:* `"RRB NTPC" "all shift papers" filetype:pdf site:qmaths.in`
2. **The GateOverflow Community Archive (`gateoverflow.in`):**
   * The single best open-source repository in India for Computer Science technical questions. Contains every single ISRO CS (2007–2025), DRDO, BARC, and GATE CS question with community-verified step-by-step proofs and LaTeX solutions.
   * Completely free, no login required.
3. **The Official ISRO Question Paper Portal:**
   * Visit: [https://www.isro.gov.in/PreviousYearsQuestionPapers.html](https://www.isro.gov.in/PreviousYearsQuestionPapers.html)
   * Directly download the **original question paper PDFs + official final answer key PDFs** released by ISRO ICRB.
4. **The Official UPSC Question Vault:**
   * Visit: [https://upsc.gov.in/examinations/previous-question-papers](https://upsc.gov.in/examinations/previous-question-papers)
   * Free download of all original UPSC Civil Services GS Paper I and CSAT Paper II booklets from 2014 to 2026.

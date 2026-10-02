# 🛰️ ISRO ICRB Scientist/Engineer 'SC' (Computer Science)
## Master Previous Years' Exam Question Paper & Detailed Solutions

---

### PART A: DISCIPLINE CORE (COMPUTER SCIENCE)

#### Q1. Database Management Systems (Normalization)
**Question:** Consider a relation schema $R(A, B, C, D, E, F)$ with the following set of functional dependencies:
$$F = \{A ightarrow B,\ BC ightarrow D,\ E ightarrow C,\ D ightarrow A\}$$
Which of the following is a candidate key of $R$?
* (A) $A$
* (B) $E$
* (C) $AEF$
* (D) $DEF$

**Detailed Solution & Answer:**
1. Notice that attribute $F$ does NOT appear on the right-hand side of any functional dependency. Therefore, $F$ must be present in EVERY candidate key of $R$. This immediately eliminates options (A) and (B).
2. Let us compute the closure of $(AEF)$:
   - $(AEF)^+ = \{A, E, F\}$
   - Since $A ightarrow B$, we add $B ightarrow \{A, B, E, F\}$
   - Since $E ightarrow C$, we add $C ightarrow \{A, B, C, E, F\}$
   - Since $BC ightarrow D$, we add $D ightarrow \{A, B, C, D, E, F\}$
   - Since $(AEF)^+$ contains all attributes of $R$, **$AEF$ is a Candidate Key**.
* **Correct Answer:** **(C) AEF**

---

#### Q2. Operating Systems (Virtual Memory & Paging)
**Question:** A system uses a 32-bit virtual address with a page size of $4	ext{ KB}$ ($2^{12}	ext{ bytes}$). Each page table entry occupies $4	ext{ bytes}$. If a 2-level paging scheme is implemented where the first-level page table fits exactly into one page, how many bits are allocated for:
1. Outer Page Table Index
2. Inner Page Table Index
3. Page Offset

**Detailed Solution & Answer:**
1. Total virtual address = $32	ext{ bits}$.
2. Page size = $4	ext{ KB} = 4096	ext{ bytes} = 2^{12}	ext{ bytes}$.
   - Therefore, **Page Offset = 12 bits**.
3. Remaining bits for page table indexing = $32 - 12 = 20	ext{ bits}$.
4. A single page ($4	ext{ KB} = 4096	ext{ bytes}$) can hold:
   $$rac{	ext{Page Size}}{	ext{PTE Size}} = rac{4096	ext{ bytes}}{4	ext{ bytes}} = 1024	ext{ entries} = 2^{10}	ext{ entries}$$
5. Since the outer page table must fit into exactly one page, it has $2^{10}$ entries $ightarrow$ **Outer Page Index = 10 bits**.
6. Remaining bits for inner page table = $20 - 10 = \mathbf{10	ext{ bits}}$.
* **Correct Answer:** Outer Page Index = **10 bits**, Inner Page Index = **10 bits**, Offset = **12 bits** ($10 + 10 + 12 = 32	ext{ bits}$).

---

#### Q3. Computer Networks (CIDR Subnetting)
**Question:** An ISP has allocated a block of IP addresses starting from `212.56.132.0/22`. What are the First and Last usable host IP addresses in this block?

**Detailed Solution & Answer:**
1. A `/22` network has $32 - 22 = 10$ host bits.
2. The 3rd octet starts at 132 (`10000100` in binary).
3. The subnet mask has 22 ones: `255.255.252.0`.
4. In the 3rd octet, the block size is $2^{(8-6)} = 2^2 = 4$.
5. The 3rd octet spans from 132 to $132 + 4 - 1 = 135$.
6. Full network range: `212.56.132.0` to `212.56.135.255`.
   - **Network ID:** `212.56.132.0`
   - **First Usable Host:** `212.56.132.1`
   - **Last Usable Host:** `212.56.135.254`
   - **Directed Broadcast ID:** `212.56.135.255`
* **Correct Answer:** First usable: **`212.56.132.1`** | Last usable: **`212.56.135.254`**.

---

#### Q4. Data Structures & Algorithms (Tree Traversal)
**Question:** The Preorder and Inorder traversals of a binary tree are given below:
* Preorder: `A, B, D, E, C, F`
* Inorder: `D, B, E, A, F, C`
What is the Postorder traversal of this tree?

**Detailed Solution & Answer:**
1. From Preorder, the first element is the root: **`A`**.
2. Find `A` in Inorder: Left subtree contains `{D, B, E}`, and right subtree contains `{F, C}`.
3. Left Subtree:
   - Preorder for left: `B, D, E` $ightarrow$ Root is `B`.
   - Inorder for left: `D, B, E` $ightarrow$ `D` is left child of `B`, `E` is right child of `B`.
4. Right Subtree:
   - Preorder for right: `C, F` $ightarrow$ Root is `C`.
   - Inorder for right: `F, C` $ightarrow$ `F` is left child of `C`.
5. Reconstructing Tree:
        A
       /       B   C
     / \  /
    D   E F
6. Postorder traversal (Left $ightarrow$ Right $ightarrow$ Root):
   - Left: `D, E, B`
   - Right: `F, C`
   - Root: `A`
* **Correct Answer:** **`D, E, B, F, C, A`**.

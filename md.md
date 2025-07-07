# Linear Algebra Day 3 — Basis and Dimension

---

## 🎯 Objectives

- Understand what a **basis** is in a vector space  
- Learn the meaning of **dimension** and how it relates to the basis  
- Identify **linearly independent** vs **dependent** sets  
- Use visuals and examples to build intuition

---

## 1️⃣ Concept Summary

### ▪ Definition

A **basis** of a vector space is a set of vectors that:
1. **Span** the space  
2. Are **linearly independent**

---

### ▪ Intuition

- A basis is like the **coordinate frame** of a space  
- Every vector in the space can be expressed **uniquely** as a combination of basis vectors  
- The **dimension** of a space is the number of vectors in any basis for that space

---

### ▪ Visual: Independence vs Dependence

Below, blue and red vectors point in the same direction → linearly dependent.  
Blue and green vectors point in different directions → linearly independent.

![Linear Independence Visualization](insert_image_here)

---

## 2️⃣ Key Formulas and Rules

### ▪ Linear independence

A set of vectors \( v_1, v_2, ..., v_k \) is linearly independent if:

$$
a_1 v_1 + a_2 v_2 + \dots + a_k v_k = \begin{bmatrix} 0 \\ \vdots \\ 0 \end{bmatrix}
$$

only when:

$$
a_1 = a_2 = \dots = a_k = 0
$$

---

### ▪ Dimension

The **dimension** of a vector space is:

> the number of vectors in a basis of that space

Examples:

- ℝ² → dimension 2  
- ℝ³ → dimension 3  
- A line through the origin in ℝ² → dimension 1

---

## 3️⃣ Worked Examples

### ✅ Example 1: Check if vectors form a basis

Are these a basis of ℝ²?

$$
v_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix},\quad
v_2 = \begin{bmatrix} 3 \\ 6 \end{bmatrix}
$$

Check: is one a multiple of the other?

$$
v_2 = 3 \cdot v_1
$$

→ Yes → **Linearly dependent** → ❌ **Not a basis**

---

### ✅ Example 2: Standard basis in ℝ³

$$
\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix},\quad
\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix},\quad
\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

→ These are linearly independent and span ℝ³  
✅ **They form a basis**

---

## 4️⃣ Practice Problems

1. Do the vectors form a basis of ℝ²?

$$
\begin{bmatrix} 1 \\ 1 \end{bmatrix},\quad
\begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

---

2. Are these vectors linearly independent?

$$
\begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix},\quad
\begin{bmatrix} -1 \\ 3 \\ 1 \end{bmatrix},\quad
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
$$

---

3. What's the dimension of the span of:

$$
\begin{bmatrix} 1 \\ 2 \end{bmatrix},\quad
\begin{bmatrix} 2 \\ 4 \end{bmatrix}
$$

---

## 5️⃣ Metacognition Check

- [ ] Can I test independence with the zero vector condition?  
- [ ] Can I explain dimension in terms of basis count?  
- [ ] Can I visualize basis vs non-basis examples?

---

## 6️⃣ Real-World Applications

- **Robotics**: Robot movement spaces depend on basis and dimensionality  
- **Data Science**: Dimensionality reduction = choosing a new basis  
- **Physics**: Vectors like forces and velocities live in vector spaces with defined bases

---

## 📌 Tomorrow's Preview

**Day 4: Matrix Representation & Linear Transformations**  
We'll use matrices to represent how vectors move, rotate, stretch, or shrink.


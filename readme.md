# 📝 Rubric — Python User System (7 Tasks)

---

## 🧩 Task 1 — Fix the Broken Class  
**Weight:** 15 points  
**Fix the class**

### Criteria  
- Correct `__init__`  
- No trailing commas  
- Proper indentation  
- Type hints  
- Docstring  
- `__repr__`  
- Three example users  
- Explanation of original errors

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (13–15)** | Fully correct class, clean style, strong explanation. |
| **Good (10–12)** | Minor style issues; explanation mostly correct. |
| **Satisfactory (7–9)** | Missing type hints/docstring; explanation incomplete. |
| **Poor (0–6)** | Class still broken; missing key elements. |

---

## 🔐 Task 2 — Validation & Utility Methods  
**Weight:** 15 points  
**Add validation**

### Criteria  
- Username validation  
- Password validation  
- `to_dict()`  
- Improved `__repr__`  
- Manual tests

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (13–15)** | All methods correct; tests thorough. |
| **Good (10–12)** | Minor mistakes in validation or tests. |
| **Satisfactory (7–9)** | Some methods incomplete; minimal tests. |
| **Poor (0–6)** | Validation incorrect; missing methods. |

---

## 📦 Task 3 — In‑Memory User Database  
**Weight:** 20 points  
**Create user storage**

### Criteria  
- `UserDB` implemented  
- Duplicate usernames prevented  
- CRUD operations  
- 5 sample users  
- Time complexity explanation

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Fully functional DB; strong complexity analysis. |
| **Good (14–17)** | CRUD works; minor issues. |
| **Satisfactory (10–13)** | Basic functionality; weak complexity explanation. |
| **Poor (0–9)** | CRUD broken; no complexity explanation. |

---

## 🔑 Task 4 — Password Hashing  
**Weight:** 15 points  
**Hash passwords**

### Criteria  
- Hashing implemented  
- `check_password()`  
- Login success/failure demo  
- Explanation of password security risks

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (13–15)** | Hashing correct; strong security explanation. |
| **Good (10–12)** | Hashing works; explanation acceptable. |
| **Satisfactory (7–9)** | Hashing simplistic; demo incomplete. |
| **Poor (0–6)** | Plain passwords still used; missing explanation. |

---

## 🗂️ Task 5 — JSON Persistence  
**Weight:** 20 points  
**Add file persistence**

### Criteria  
- Save to JSON  
- Load from JSON  
- Corrupted JSON handling  
- Full save/load cycle

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Robust persistence; graceful error handling. |
| **Good (14–17)** | Persistence works; minimal error handling. |
| **Satisfactory (10–13)** | Save/load works but fragile. |
| **Poor (0–9)** | Persistence broken; no error handling. |

---

## 🧪 Task 6 — CLI Menu  
**Weight:** 15 points  
**Build CLI menu**

### Criteria  
- Menu loop  
- All required actions  
- Input validation  
- Sample transcript  
- Runs until “exit”

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (13–15)** | Fully functional CLI; polished UX. |
| **Good (10–12)** | CLI works; minor UX issues. |
| **Satisfactory (7–9)** | Some options incomplete; minimal transcript. |
| **Poor (0–6)** | CLI broken; missing options. |

---

## 🧱 Task 7 — Add Unit Tests (pytest or manual)  
**Weight:** 20 points  
**Add unit tests**

### Goal  
Create a **complete test suite** for `User` and `UserDB`.

### Requirements  
Tests must cover:

- User creation  
- Username validation  
- Password validation  
- Password hashing + checking  
- `to_dict()`  
- CRUD operations in `UserDB`  
- Duplicate username rejection  
- JSON save/load cycle  
- CLI logic (if using manual tests, simulate input)

### Scoring  
| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Comprehensive tests; covers edge cases; clear structure. |
| **Good (14–17)** | Good coverage; minor gaps. |
| **Satisfactory (10–13)** | Basic tests; missing edge cases. |
| **Poor (0–9)** | Minimal or broken tests; major gaps. |

---

# 📊 Total Score  
**120 points**
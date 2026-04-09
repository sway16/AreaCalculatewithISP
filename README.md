# 📐 Area Calculator (ISP Demonstration in Python)

This project demonstrates two different approaches to designing an **area and volume calculation system** using **Object-Oriented Programming (OOP)** in Python. It highlights the importance of the **Interface Segregation Principle (ISP)** from SOLID design principles.

---

## 🚀 Features

* Calculate **area** of shapes (Circle, Square, Cube)
* Calculate **volume** for 3D shapes (Cube)
* Comparison of two design approaches:

  * ❌ **Bad Design (Violates ISP)**
  * ✅ **Good Design (Follows ISP)**

---

## 🧠 Concepts Demonstrated

* Abstract Base Classes (`ABC`)
* Method overriding
* Interface design
* Interface Segregation Principle (ISP)
* Clean and modular architecture

---

## ⚙️ Approach Overview

### 🔹 Version 1 (Violates ISP)

* A single abstract class `Shape` forces all shapes to implement:

  * `area()`
  * `volume()`
* Problem:

  * 2D shapes like Circle and Square **don’t need volume**
  * Leads to unnecessary method implementation (returns 0)

**Flow:**
Shape → Circle / Square / Cube

❌ Not clean
❌ Violates ISP

---

### 🔹 Version 2 (Follows ISP)

* Interfaces are split into:

  * `AreaShape`
  * `VolumeShape`

* Each class implements only what it needs:

  * Circle → only area
  * Square → only area
  * Cube → area + volume

* Introduced `AreaCalculator` for better abstraction

**Flow:**
AreaCalculator → AreaShape → Specific Shape

✔ Clean design
✔ Follows ISP
✔ Scalable and maintainable

---

## 🖥️ Example Output

```
Circle Area: 78.5
Square Area: 16
Cube Area: 54
Cube Volume: 27
```

---

## 📂 Project Structure

```
main.py
└── All classes and implementation
```

---

## 🔧 How to Run

1. Install Python (if not installed)
2. Save the code in a `.py` file (e.g., `main.py`)
3. Run the file:

```
python main.py
```

---

## 💡 Future Improvements

* Add more shapes (Cylinder, Sphere, etc.)
* Improve accuracy using `math.pi`
* Add user input system
* Separate files for better modularity

---

## 🏁 Summary

This project clearly shows why **Interface Segregation Principle (ISP)** matters:

* ❌ Forcing unnecessary methods leads to bad design
* ✅ Splitting interfaces creates flexible and clean code

A simple example, but a powerful design lesson for real-world software development.

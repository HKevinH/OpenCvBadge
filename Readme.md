# Room Capacity Optimization

## 1. Define the Problem

**Objective:**  
Maximize the number of people that can occupy a room without exceeding the available area and complying with space restrictions per person.

**Constraints:**

- **Total area of the room:** Determine the maximum usable space.
- **Minimum space required per person:** Based on safety or comfort standards.
- **Obstacles or unusable areas within the room:** Consider areas occupied by furniture, columns, etc.

---

## 2. Collect Data

- **Room dimensions:** Length, width, and areas that are unusable.
- **Minimum space per person:** According to safety or comfort standards.
- **Other factors:** Emergency exits, evacuation routes, and any additional considerations for safe and efficient use of space.

---

## 3. Model the Problem Using the Knapsack Algorithm

- **Room as a "backpack":** Represent the room's available area as the capacity of a backpack.
- **Person as a "weight":** Each person occupies an area equal to the minimum space required.
- **Objective:** Maximize the number of people (value) that can fit into the room without exceeding the available area.

---

## Density Scenarios for Room Capacity

### High Density

- **Density:** 1 person per 0.5 square meters (ideal for crowded events or standing conferences).
- **Capacity:** Approximately 200 people in a 100 square meter area.

### Moderate Density

- **Density:** 1 person per 1 square meter (suitable for mixed events or meetings with a few chairs).
- **Capacity:** Approximately 100 people in a 100 square meter area.

### Low Density

- **Density:** 1 person per 1.5 to 2 square meters (ideal for events with chairs and tables or more spacious meetings).
- **Capacity:** Approximately 50-67 people in a 100 square meter area.

---

## Classroom Configurations

### Standard Classroom (Individual Desks)

- **Space per student:** Approximately 1.5 to 2 square meters.
- **Capacity:** Approximately 50-67 students in a 100 square meter area.

### Classroom with Large Desks or Group Work Tables

- **Space per student:** Approximately 2 to 2.5 square meters (additional space for group tables).
- **Capacity:** Approximately 40-50 students in a 100 square meter area.

### Lab-Type Classroom (Additional Equipment and Work Space)

- **Space per student:** Approximately 3 to 4 square meters.
- **Capacity:** Approximately 25-33 students in a 100 square meter area.

---

This model provides flexible estimates based on different configurations and density needs for maximizing room capacity.

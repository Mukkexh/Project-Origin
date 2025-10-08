# 🧠 Concept Note: The Ancestral Map Generator

**Purpose:**  
Demonstrate how genetic ancestry data (e.g., 23andMe summaries) can be converted into visual geographic paths using open datasets.

---

## 🔬 Overview

This concept explores the link between **genetic data** and **human migration mapping**.  
By combining small personal ancestry files with public archaeological and linguistic data, we can approximate where a user’s ancestors may have lived, migrated, or adapted.

---

## 🧩 Technical Breakdown

| Layer | Function | Example |
|-------|-----------|----------|
| **Input** | JSON or CSV with ancestry data | `examples/ancestry_example.json` |
| **Processing** | Python script converts ancestry to coordinate list | `scripts/origin_map.py` |
| **Output** | GeoJSON migration map | `examples/your_lineage.geojson` |
| **Visualization** | Leaflet web view | `examples/viewer.html` |

---

## 🧭 Future Expansion

- Integrate **climate overlays** (temperature, sea level, vegetation).  
- Add **archaeological site pins** matching ancestral periods.  
- Enable **time-slider animation** to show movement through eras.  
- Use **VR playback** to immerse users in their ancestral environments.

---

## 🧬 Why It Matters

Understanding one’s origins visually helps reframe identity:  
> “We didn’t appear divided — we drifted apart and adapted.”

This concept serves as the foundation for *Project Origin’s* core goal:  
**Teaching unity through shared ancestry, adaptation, and survival.**

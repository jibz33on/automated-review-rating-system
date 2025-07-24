# 📂 Data Folder

This folder contains the datasets used for the **Automated Review Rating System**.

---

## 📦 Dataset: Amazon Fine Food Reviews

- **Source**: [Kaggle - Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- **Downloaded**: July 24, 2025
- **Original Size**: ~300.9 MB
- **Format**: CSV
- **License**: Public domain (for educational and research use)

---

## 🧩 File Structure

Due to GitHub's 100MB file limit, the original `Reviews.csv` has been split into smaller parts:

| File                  | Size  | Description          |
|-----------------------|-------|----------------------|
| `Reviews_part1.csv`   | 97 MB | First 1/3 of reviews |
| `Reviews_part2.csv`   | 95 MB | Second 1/3           |
| `Reviews_part3.csv`   | 95 MB | Final 1/3 + overflow |

Total Combined Rows: **568,454**

---

## ⚙️ How to Recombine in Python

```python
import pandas as pd

df1 = pd.read_csv('data/kaggle/Reviews_part1.csv')
df2 = pd.read_csv('data/kaggle/Reviews_part2.csv')
df3 = pd.read_csv('data/kaggle/Reviews_part3.csv')

full_df = pd.concat([df1, df2, df3], ignore_index=True)

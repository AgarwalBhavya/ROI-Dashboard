# Influencer Campaign ROI Dashboard
Track and visualize the performance and return on investment (ROI) of influencer marketing campaigns across platforms like Instagram, YouTube, and Twitter.

**Live App**: [Click here to access the dashboard](https://agarwalbhavya-roi-dashboard-dashboard-ip84qp.streamlit.app/)

## Objective

Build a dashboard that:

* Uploads influencer campaign data
* Tracks influencer and post performance
* Calculates ROAS (Return on Ad Spend)
* Offers deep insights into top-performing influencers and poor ROI areas
* Visualizes payouts and revenue contributions

## Datasets Used (CSV Format)

### 1. `influencers.csv`

| Column          | Description                 |
| --------------- | --------------------------- |
| influencer\_id  | Unique influencer ID        |
| name            | Influencer's name           |
| category        | Fitness, Wellness, etc.     |
| gender          | M / F                       |
| follower\_count | Number of followers         |
| platform        | Instagram, YouTube, Twitter |

### 2. `posts.csv`

| Column         | Description               |
| -------------- | ------------------------- |
| influencer_id  | Link to `influencers.csv` |
| platform       | Platform where posted     |
| date           | Date of post              |
| url            | Link to post              |
| caption        | Caption of post           |
| reach          | Total reach               |
| likes          | Number of likes           |
| comments       | Number of comments        |

### 3. `tracking_data.csv`

| Column         | Description                |
| -------------- | -------------------------- |
| source         | Platform (e.g., Instagram) |
| campaign       | Campaign name              |
| influencer_id  | Link to influencer         |
| user_id        | Buyer ID                   |
| product        | Product purchased          |
| date           | Purchase date              |
| orders         | Number of orders           |
| revenue        | Revenue generated          |

### 4. `payouts.csv`

| Column         | Description                 |
| -------------- | --------------------------- |
| influencer_id  | Link to influencer          |
| basis          | "post" or "order"           |
| rate           | Rate per post/order         |
| orders         | Orders fulfilled (if order) |
| total_payout   | Final payout                |

---

## Features

Upload influencer, post, tracking, and payout data
View overall performance metrics
Analyze ROAS per influencer
Visualize engagement vs reach
Filter by platform, gender, category
Export ROAS data as CSV

## How to Run Locally

1. **Clone the repo**

```bash
git clone <https://github.com/AgarwalBhavya/ROI-Dashboard>
cd ROI-Dashboard
```

2. **Install dependencies**

```bash
pip install requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run dashboard.py
```

4. **Upload the CSVs** when prompted.

---

## File Structure

```
├── dashboard.py           # Streamlit app
├── influencers.csv        # Sample influencer data
├── posts.csv              # Post engagement data
├── tracking_data.csv      # Attribution and revenue data
├── payouts.csv            # Influencer payout info
├── README.md              # Setup documentation
└── insights_summary.pdf   # Insight report (attached)
```

---

## Notes & Assumptions

* All revenue in tracking_data is attributed to influencers via coupon/UTM tagging.
* Incremental ROAS assumes zero baseline (can be extended).
* Payout basis determines how influencers are paid (per post vs per order).
* All calculations are simulated on synthetic data.

---

## Author

**Bhavya Agarwal**
Feel free to connect via GitHub or LinkedIn!

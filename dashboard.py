import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Influencer Campaign Dashboard", layout="wide")
st.title("Influencer Campaign ROI Tracker")

st.sidebar.header("Upload Data")
influencers_file = st.sidebar.file_uploader("Upload influencers.csv", type=["csv"])
posts_file = st.sidebar.file_uploader("Upload posts.csv", type=["csv"])
tracking_file = st.sidebar.file_uploader("Upload tracking_data.csv", type=["csv"])
payouts_file = st.sidebar.file_uploader("Upload payouts.csv", type=["csv"])

if influencers_file and posts_file and tracking_file and payouts_file:
    influencers = pd.read_csv(influencers_file)
    posts = pd.read_csv(posts_file)
    tracking = pd.read_csv(tracking_file)
    payouts = pd.read_csv(payouts_file)

    with st.sidebar.expander("Filter Options"):
        platforms = st.multiselect("Select Platforms", influencers["platform"].unique(), default=influencers["platform"].unique())
        categories = st.multiselect("Select Categories", influencers["category"].unique(), default=influencers["category"].unique())
        genders = st.multiselect("Select Gender", influencers["gender"].unique(), default=influencers["gender"].unique())

    filtered_influencers = influencers[
        influencers["platform"].isin(platforms) &
        influencers["category"].isin(categories) &
        influencers["gender"].isin(genders)
    ]

    tracking_merged = tracking.merge(filtered_influencers, on="influencer_id")
    payouts_merged = payouts.merge(filtered_influencers, on="influencer_id")

    total_revenue = tracking_merged["revenue"].sum()
    total_orders = tracking_merged["orders"].sum()
    total_payout = payouts_merged["total_payout"].sum()
    roas = total_revenue / total_payout if total_payout else 0

    st.markdown("###Overall Campaign Performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col2.metric("Total Orders", f"{total_orders}")
    col3.metric("Total Payout", f"₹{total_payout:,.0f}")
    col4.metric("ROAS", f"{roas:.2f}x")

    st.markdown("###Top Influencers by ROAS")
    revenue_per_influencer = tracking_merged.groupby("influencer_id")["revenue"].sum()
    payout_per_influencer = payouts_merged.set_index("influencer_id")["total_payout"]
    roas_df = pd.DataFrame({
        "Revenue": revenue_per_influencer,
        "Payout": payout_per_influencer
    })
    roas_df["ROAS"] = roas_df["Revenue"] / roas_df["Payout"]
    roas_df = roas_df.fillna(0).sort_values("ROAS", ascending=False).reset_index()
    roas_df = roas_df.merge(influencers, on="influencer_id")

    st.dataframe(roas_df[["name", "platform", "category", "Revenue", "Payout", "ROAS"]].round(2))

    fig = px.bar(roas_df.head(10), x="name", y="ROAS", color="platform", title="Top 10 Influencers by ROAS")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Post Engagement")
    posts_merged = posts.merge(influencers, on="influencer_id", suffixes=('_post', '_inf'))
    posts_filtered = posts_merged[posts_merged["influencer_id"].isin(filtered_influencers["influencer_id"])]
    posts_filtered["engagement"] = (posts_filtered["likes"] + posts_filtered["comments"]) / posts_filtered["reach"]
    st.dataframe(posts_filtered[["name", "platform_post", "reach", "likes", "comments", "engagement"]].round(3).rename(
        columns={"platform_post": "platform"}))

    fig2 = px.scatter(posts_filtered, x="reach", y="engagement", color="platform_post", hover_name="name",
                      title="Engagement vs Reach")

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Payout Overview")
    st.dataframe(payouts_merged[["name", "platform", "basis", "rate", "orders", "total_payout"]])

    fig3 = px.pie(payouts_merged, names="platform", values="total_payout", title="Payout Distribution by Platform")
    st.plotly_chart(fig3, use_container_width=True)

    st.download_button("Download ROAS Data (CSV)", roas_df.to_csv(index=False), "roas_summary.csv")
else:
    st.warning("Please upload all four CSV files to view the dashboard.")

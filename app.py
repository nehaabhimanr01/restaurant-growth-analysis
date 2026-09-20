
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="Restaurant Growth Dashboard", page_icon="🍽️", layout="wide")

st.title("🍽️ Restaurant Growth Dashboard")
st.caption("SkyCity Auckland Restaurants & Bars • Project 2")

@st.cache_data
def load_data():
    df = pd.read_csv("Project_2_Restaurant_Growth_Analysis.csv")
    return df

df = load_data()

st.sidebar.header("Filters")
regions = st.sidebar.multiselect("Subregion", sorted(df["Subregion"].unique()), default=sorted(df["Subregion"].unique()))
segments = st.sidebar.multiselect("Segment", sorted(df["Segment"].unique()), default=sorted(df["Segment"].unique()))
cuisines = st.sidebar.multiselect("Cuisine", sorted(df["CuisineType"].unique()), default=sorted(df["CuisineType"].unique()))
growth = st.sidebar.multiselect("Growth class", ["High","Medium","Low"], default=["High","Medium","Low"])

f = df[
    df["Subregion"].isin(regions) &
    df["Segment"].isin(segments) &
    df["CuisineType"].isin(cuisines) &
    df["GrowthClass"].isin(growth)
].copy()

revenue = f["TotalRevenue"].sum()
profit = f["TotalNetProfit"].sum()
orders = f["MonthlyOrders"].sum()
margin = profit / revenue if revenue else 0

c1,c2,c3,c4 = st.columns(4)
c1.metric("Restaurants", f"{len(f):,}")
c2.metric("Revenue", f"${revenue/1e6:.2f}M")
c3.metric("Net Profit", f"${profit/1e6:.2f}M")
c4.metric("Profit Margin", f"{margin:.1%}")

st.divider()

left,right = st.columns(2)
with left:
    st.subheader("Profit by Segment")
    seg = f.groupby("Segment")["TotalNetProfit"].sum().sort_values(ascending=False)
    st.bar_chart(seg)
with right:
    st.subheader("Profit by Subregion")
    reg = f.groupby("Subregion")["TotalNetProfit"].sum().sort_values(ascending=False)
    st.bar_chart(reg)

st.subheader("Channel Economics")
channel_map = {
    "In-store": ("InStoreRevenue","InStoreNetProfit"),
    "Uber Eats": ("UberEatsRevenue","UberEatsNetProfit"),
    "DoorDash": ("DoorDashRevenue","DoorDashNetProfit"),
    "Self-delivery": ("SelfDeliveryRevenue","SelfDeliveryNetProfit")
}
rows=[]
for name,(r,p) in channel_map.items():
    rev=f[r].sum(); prof=f[p].sum()
    rows.append([name,rev,prof,(prof/rev if rev else 0)])
ch=pd.DataFrame(rows,columns=["Channel","Revenue","Net Profit","Margin"])
st.dataframe(ch.style.format({"Revenue":"${:,.0f}","Net Profit":"${:,.0f}","Margin":"{:.1%}"}), use_container_width=True)

st.subheader("Restaurant Growth Classification")
show_cols=["RestaurantName","CuisineType","Segment","Subregion","GrowthPotentialScore","GrowthClass","TotalRevenue","TotalNetProfit","ProfitMargin"]
out=f[show_cols].sort_values("GrowthPotentialScore",ascending=False)
st.dataframe(
    out.style.format({
        "GrowthPotentialScore":"{:.1f}",
        "TotalRevenue":"${:,.0f}",
        "TotalNetProfit":"${:,.0f}",
        "ProfitMargin":"{:.1%}"
    }),
    use_container_width=True,
    height=450
)

st.info("GPI methodology: Growth Factor 30% + Profit Margin 35% + Monthly Orders 20% + AOV 15%, using min-max normalization. The score is a prioritization tool, not a forecast guarantee.")

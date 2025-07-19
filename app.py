import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pycountry import countries
import pycountry_convert as pc
from io import BytesIO
import zipfile
import os

st.set_page_config(layout="wide", page_title="Kaggle Country Insights")
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🌍 Beyond Borders, Beyond Limits: Global AI Talent on Kaggle</h1>", unsafe_allow_html=True)
st.title("🌐 Kaggle Country Medal Efficiency Dashboard")

# === Load Data ===

@st.cache_data
def load_data():
    if not os.path.exists("data"):
        if not os.path.exists("data.zip"):
            st.error("❌ data.zip not found. Make sure it's pushed via Git LFS.")
            st.stop()

        with zipfile.ZipFile("data.zip", "r") as zip_ref:
            zip_ref.extractall("data")
        
        # Give Streamlit time to recognize new files
        st.info("🔄 Extracting data... Please refresh in a few seconds.")
        st.stop()  # Stops app execution until next rerun

    # Proceed once data/ is available
    users = pd.read_csv("data/users_clean.csv")
    medal_eff = pd.read_csv("data/medal_efficiency.csv", index_col=0)
    token_trend = pd.read_csv("data/notebook_token_trends.csv")
    keywords = pd.read_csv("data/top_modeling_keywords.csv")
    tools = pd.read_csv("data/popular_tools.csv")
    medal_eff.reset_index(inplace=True)
    return users, medal_eff, token_trend, keywords, tools


users, medal_eff_df, token_trend_df, keyword_df, tools_df = load_data()

# === Add Region Mapping ===
@st.cache_data
def add_region_info(df):
    def get_region(country_name):
        try:
            country_code = countries.lookup(country_name).alpha_2
            continent_code = pc.country_alpha2_to_continent_code(country_code)
            return pc.convert_continent_code_to_continent_name(continent_code)
        except:
            return "Unknown"
    df["Region"] = df["Country"].apply(get_region)
    return df

medal_eff_df = add_region_info(medal_eff_df)

# === Sidebar Filters ===
st.sidebar.header("📊 Filters")
regions = sorted(medal_eff_df['Region'].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect("Select Regions", regions, default=regions)

min_eff, max_eff = float(medal_eff_df["MedalEfficiency"].min()), float(medal_eff_df["MedalEfficiency"].max())
eff_range = st.sidebar.slider("Medal Efficiency Range", min_value=min_eff, max_value=max_eff, value=(min_eff, max_eff))

# Filter based on selections
filtered_df = medal_eff_df[
    (medal_eff_df["Region"].isin(selected_regions)) &
    (medal_eff_df["MedalEfficiency"].between(*eff_range))
]

# === Export Options ===
st.sidebar.markdown("### 📤 Export Data")
export_btn_col1, export_btn_col2 = st.sidebar.columns(2)

with export_btn_col1:
    excel_buffer = BytesIO()
    filtered_df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    st.download_button("⬇️ Excel", data=excel_buffer, file_name="kaggle_efficiency.xlsx", mime="application/vnd.ms-excel")

with export_btn_col2:
    pdf_buffer = BytesIO()
    pdf_buffer.write(filtered_df.to_string(index=False).encode())
    pdf_buffer.seek(0)
    st.download_button("⬇️ PDF", data=pdf_buffer, file_name="kaggle_efficiency.pdf", mime="application/pdf")

# === Top Countries by Users ===
st.subheader("👥 Top 15 Countries by Kaggle Users")

top_users = (
    users["Country"]
    .value_counts()
    .reset_index()
    .rename(columns={"index": "Country", "Country": "User Count"})
    .head(15)
)

st.dataframe(top_users)

if {"Country", "User Count"}.issubset(top_users.columns) and not top_users.empty:
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_users, y="Country", x="User Count", palette="Blues_d", ax=ax1)
    ax1.set_title("Top 15 Countries by Number of Kaggle Users")
    st.pyplot(fig1)

# === Most Medal-Efficient Country ===
st.subheader("🥇 Most Medal-Efficient Country (Filtered)")
if not filtered_df.empty:
    top = filtered_df.sort_values("MedalEfficiency", ascending=False).iloc[0]
    st.success(f"🏆 {top['Country']} ({top['Region']}) is the most medal-efficient country with a score of **{top['MedalEfficiency']:.2f}**")
else:
    st.warning("No countries match the selected filters.")

# === Country Flag Utility ===
@st.cache_data
def get_flag_url(country_name):
    try:
        code = countries.lookup(country_name).alpha_2
        return f"https://flagcdn.com/w80/{code.lower()}.png"
    except:
        return None

# === Country-wise Medal Efficiency Cards ===
st.subheader("📦 Country Medal Efficiency Cards (Filtered Top 15)")
cols = st.columns(5)
top_cards = filtered_df.sort_values("MedalEfficiency", ascending=False).head(15).reset_index(drop=True)

for idx, row in top_cards.iterrows():
    col = cols[idx % 5]
    with col:
        st.markdown(f"### {row['Country']}")
        flag_url = get_flag_url(row['Country'])
        if flag_url:
            st.image(flag_url, width=60)
        st.metric("Efficiency", f"{row['MedalEfficiency']:.2f}")
        st.caption(f"Region: {row['Region']}")

# === Token Trend: Average Title Token Count Over Time ===
st.subheader("🕒 Average Notebook Title Token Count Over Time (Top 15 Countries)")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=token_trend_df, x="Year", y="NotebookLength", hue="Country", ax=ax2)
ax2.set_title("Average Notebook Title Length Over Time")
st.pyplot(fig2)

# === Optimized Modeling Keywords Plot (Memory Efficient) ===
st.subheader("🧠 Top Modeling Keywords in Top Countries")

# Limit to top 5 countries by appearance in keyword_df
top_keyword_countries = keyword_df["Country"].value_counts().head(5).index.tolist()
subset = keyword_df[keyword_df["Country"].isin(top_keyword_countries)]

# Compute top 20 keywords globally (without melting)
keyword_cols = [col for col in subset.columns if col != "Country"]
top_keywords = subset[keyword_cols].sum().sort_values(ascending=False).head(20).index.tolist()

# Plot for each keyword by country
plot_df = (
    subset.groupby("Country")[top_keywords]
    .sum()
    .T
    .sort_values(by=top_keyword_countries[0], ascending=False)
    .reset_index()
    .melt(id_vars="index", var_name="Country", value_name="Frequency")
    .rename(columns={"index": "Keyword"})
)

fig3, ax3 = plt.subplots(figsize=(12, 7))
sns.barplot(data=plot_df, y="Keyword", x="Frequency", hue="Country", dodge=True, ax=ax3)
ax3.set_title("Top 20 Modeling Keywords by Frequency (Top 5 Countries)")
st.pyplot(fig3)
# 🛠️ Popular Tools in Top 15 Countries
st.subheader("🛠️ Popular Tools in Top 15 Countries")

# Identify top 15 countries by notebook/tool usage count
top5_countries = tools_df['Country'].value_counts().head(5).index.tolist()

# Subset DataFrame to only those countries
tools_top5 = tools_df[tools_df['Country'].isin(top5_countries)]

# Identify tool columns (everything except 'Country')
tool_columns = [col for col in tools_top5.columns if col != 'Country']

# Group by country and sum usage of each tool
tools_summary = (
    tools_top5.groupby('Country')[tool_columns]
    .sum()
    .T
    .reset_index()
    .rename(columns={'index': 'Tool'})
    .melt(id_vars='Tool', var_name='Country', value_name='Usage')
)

# Optional: sort to keep most used tools on top
tools_summary = tools_summary.sort_values("Usage", ascending=False)

# Plot using seaborn
fig4, ax4 = plt.subplots(figsize=(14, 8))
sns.barplot(data=tools_summary, y="Tool", x="Usage", hue="Country", ax=ax4, dodge=True)
ax4.set_title("Top Tool Usage in Top 5 Countries", fontsize=16)
ax4.set_xlabel("Usage Count")
ax4.set_ylabel("Tool")
ax4.legend(title='Country',loc='lower right')
st.pyplot(fig4)


# === Raw Filtered Table ===
with st.expander("🧾 View Raw Filtered Table"):
    st.dataframe(filtered_df, use_container_width=True)

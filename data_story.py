import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import plotly.express as px

# Load Data
df = pd.read_csv("df_updated.csv", index_col=0)

arabic_font_path = 'Amiri/Amiri-Regular.ttf'
prop = fm.FontProperties(fname=arabic_font_path)
plt.rcParams['font.family'] = prop.get_name()

# Centering all elements using CSS
st.markdown(
    """
    <style>
    .main {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("خريج؟ خلني اساعدك")

st.write("""
هلا والله! اول شي مبروك! 🎉
أدري إنك تدور وظيفة، ويمكن الموضوع يحسسك إنك ضايع شوي، بس لا تشيل هم، أنا هنا عشان أسهّلها عليك. خلنا نستعرض البيانات سوا ونشوف كيف ممكن نلقى لك الفرصة اللي تناسبك. سواء تبي تعرف عن الرواتب، أو وين فيه أكثر فرص، أنا معك خطوة بخطوة!
""")


st.write("### توزيع الرواتب")
st.write("""
واحدة من أهم الأسئلة يوم تدور وظيفة هي: "كم تتوقع الراتب؟" خلني اوريك توزيع الرواتب للخريجين عشان تكون عندك فكرة واضحة.
""")

# Create a histogram with Plotly
fig_salary = px.histogram(df, x='salary', nbins=30, title="توزيع الرواتب",
                           labels={'salary': 'الراتب (بالعملة المحلية)'},
                           histnorm='density',
                           template='plotly_white')
fig_salary.update_layout(xaxis_title="الراتب بالريال",
                         yaxis_title="عدد الوظايف")
st.plotly_chart(fig_salary)

st.write("### فرص العمل حسب الجنس")
st.write("""
بعض الوظايف تستهدف فئات معينة أكثر من غيرها. خلّنا نشوف كيف توزع الوظايف بين الجنسين، ووش يعني لك هذا وأنت تدور وظيفتك.
""")
gender_counts = df.groupby('gender')['positions'].sum().reset_index()
fig = px.pie(gender_counts, values='positions', names='gender', title='إجمالي الوظايف حسب الجنس')
st.plotly_chart(fig)

# Opportunities by Region
st.write("### الفرص في المناطق")
st.write("""
الموقع الجغرافي ممكن يغير أشياء كثيرة في رحلة بحثك عن الوظيفة. خلّنا نشوف المناطق اللي فيها أكثر فرص وظيفية!
""")

# Count job opportunities by region and get the top 5
region_counts = df['region'].value_counts().reset_index()
region_counts.columns = ['region', 'count']
top_regions = region_counts.nlargest(5, 'count')  # Get the top 5 regions

# Create a line chart with Plotly
fig = px.line(top_regions, x='region', y='count',
               title='أعلى 5 مناطق للوظايف',
               labels={'region': 'المنطقة', 'count': 'عدد الوظائف'},
               template='plotly_white')

st.plotly_chart(fig)

# Contracts and company type
st.write("### نوع الشركة وأنواع العقود")
st.write("""
الحين، خلّنا نستعرض أنواع المزايا اللي تقدّمها الشركات، وأنواع العقود المتاحة. هذي الأشياء بتساعدك تحدد وش اللي يناسبك في وظيفتك الجاية.
""")
comp_type_count = df['comp_type'].value_counts().head(10)
contract_count = df['contract'].value_counts()

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(comp_type_count)
with col2:
    st.bar_chart(contract_count)

st.write("### نصايح البحث عن وظيفة بناءً على البيانات")
st.write("بناءً على المعلومات اللي شفناها:")
st.write("**ركز على المناطق**: إذا كنت ناوي تنقل، فيه مناطق عندها فرص أكثر من غيرها.")
st.write("**تابع نطاق الرواتب**: قدم على الشركات اللي تناسب توقعاتك في الراتب.")
st.write("**الخبرة**: تأكد إن عندك الخبرة المطلوبة للوظائف اللي تبي تقدم عليها.")
st.write("تذكر، البحث عن الوظيفة المناسبة يحتاج منك تعرف وين تدور، وش تتوقع، وكيف تتصرف بذكاء. موفقً في رحلتك، ولا تنسى إنك وصلت الى هنا! 💪")



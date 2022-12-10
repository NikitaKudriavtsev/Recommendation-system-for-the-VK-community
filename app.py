import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Рекомендации")
st.write(""" Проведя аналитику постов и количества подписчиков за каждый месяц,
мы можем дать несколько советов по продвижению вашего сообщества в VK\n
1. Увеличить количество постов на тему мероприятия для семей в Лагерях, так как они меньше всех похожи на остальные посты, 
\tс точки зрения статистики, а так же интереса аудитории
2. Записи на темы связанные с поздравлениями Сотрудников, мероприятиями РГООИ "Надежда" и Ириной Викторовной
\tпомогут в продвижении сообщества
3. Приглашенные гости освещённые в записях, так же привлекают вашу аудитории и вызывают у неё особый интерес
""")

df = pd.read_csv('DataSet (1).csv')
df2 = df
df2 = df2.set_index('DateMonth')
df2 = df2.corr()
plt.figure(figsize = (20,15))
sns.heatmap(df2, cmap="coolwarm", annot = True)
st.pyplot()


df3 = pd.read_csv("DataSETSUB.csv")
df3 = df3.drop(columns = ["Unnamed: 0"])
df3 = df3.groupby(['DateMonth']).sum()
DateMonth = [1,2,3,4,5,6,7,8,9]
sr = pd.Series(data=df3["Subscribed"], index=DateMonth)
plt.figure(figsize=(15, 10))
sns.set_theme(style="whitegrid")
plt.title("Теоретический прирост подписчиков за каждый месяц")
plt.xlabel("Колличество подписчиков")
plt.ylabel("Месяцы")
sr.plot.barh()
st.pyplot()
st.dataframe(df2.describe())


st.header("Разработчики")
st.write("""[Никита Кудрявцев](https://vk.com/nkudr07) - создание веб-приложения\n
[Даниил Бардадымов ](https://vk.com/donttouchthisplz) - аналитика\n
[Кристина Николаева](https://vk.com/twinfield) - создание методички, обработка данных
""")
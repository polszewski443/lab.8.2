import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
df1 = pd.read_excel(xlsx, header=0)
print(df1)
print('##########Zad1##########')
print('tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku')
print(df1[df1['Liczba'] > 1000])
print('##########Zad2##########')
print('tylko rekordy gdzie nadane imię jest takie jak Twoje ')
print(df1[df1['Imie'] == 'PAWEŁ'])
print('##########Zad3##########')
print('sumę wszystkich urodzonych dzieci w całym danym okresie')
print(f"Suma: {df1['Liczba'].sum()}")
print('##########Zad4##########')
print('sumę dzieci urodzonych w latach 2000-2005')
print(f"Suma: {df1[(df1['Rok'] >= 2000) & (df1['Rok'] <= 2005)]['Liczba'].sum()}")
print('##########Zad5##########')
print('sumę urodzonych chłopców i dziewczynek ')
print(f"Suma ur. chlopcow: {df1[(df1.Plec == 'M')]['Liczba'].sum()}")
print(f"Suma ur. dziewczynek: {df1[(df1.Plec == 'K')]['Liczba'].sum()}")
print(
    f'najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)):\n'
    f'{df1.groupby(["Rok", "Plec"])["Liczba"].max()}')
# tutaj niestety mialem problem, zeby wyswietlic imie zamiast wartosci liczbowej, mimo prob i korzystania z wiedzy
# znalezionej w internecie nie bylem w stanie znalezc odpowiedniego rozwiazania
print(
    f'najbardziej popularne imię dziewczynki i chłopca w całym danym okresie:\n'
    f'{df1.groupby(["Plec"])["Liczba"].max()}')
# tutaj niestety podobny mialem problem wynikajacy z niewykonania zadania wczesniejszego
# znalezionej w internecie nie bylem w stanie znalezc odpowiedniego rozwiazania

df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df2)
print(f"listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame):"
      f"{df2.Sprzedawca.unique()}")
print(f"5 najwyższych wartości zamówień:\n {df2.sort_values('Utarg', ascending=False).head(5)}")
print(f"ilość zamówień złożonych przez każdego sprzedawcę\n {df2.groupby(['Sprzedawca'])['Utarg'].sum()}")
print(f"sumę zamówień dla każdego kraju\n {df2.groupby(['Kraj'])[['idZamowienia']].count()} ")
print(f"sumę zamówień dla sprzedawcow z polski\n {df2.groupby(['Kraj'])[['idZamowienia']].count()} ")
print(f"sumę zamówień dla roku 2005, dla sprzedawców z Polski \n")
print(f" {print(df2.loc[(df2['Kraj'] == 'Polska') & (pd.DatetimeIndex(df2['Data zamowienia']).year == 2005)].groupby(['Sprzedawca']).agg({'Sprzedawca': {'count'}}))}")
print(f"średnią kwotę zamówienia w 2004 roku  {round((df2.loc[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]['Utarg'].mean()), 2)}")
daneza2004 = df2.loc[((pd.DatetimeIndex(df2['Data zamowienia']).year == 2004))]
daneza2005 = df2.loc[((pd.DatetimeIndex(df2['Data zamowienia']).year == 2005))]
daneza2004.to_csv('zamowienia_2004.csv', index=False)
daneza2005.to_csv('zamowienia_2005.csv', index=False)



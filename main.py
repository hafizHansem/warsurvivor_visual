import pandas as pd
import plotly.express as px

# Membaca data dari CSV
df = pd.read_csv('war_survival_data.csv')

# Membuat scatter plot interaktif
fig = px.scatter(df, x='Food Supply (Days)', y='Water per Day (Liters)', color='Training Level',
           size='Weapons Available', hover_name='Name',
           labels={'Food Supply (Days)': 'Masa Persediaan Makanan (Hari)',
                   'Water per Day (Liters)': 'Konsumsi Air per Hari (Liter)',
                   'Training Level': 'Tingkat Pelatihan',
                   'Weapons Available': 'Senjata Tersedia'},
           title='Data Supplies and Training Level')

# Menambahkan informasi tambahan pada hover
fig.update_traces(hovertemplate='<b>%{hovertext}</b><br><br>' +
                                 'Masa Persediaan Makanan: %{x} hari<br>' +
                                 'Konsumsi Air per Hari: %{y} liter<br>' +
                                 'Senjata Tersedia: %{marker.size}<br>' +
                                 'Tingkat Pelatihan: %{marker.color}')

# Menampilkan plot
fig.show()

# Visualisasi tambahan
fig_age = px.histogram(df, x='Age', title='Distribusi Umur')
fig_age.show()

fig_food = px.bar(df, x='Name', y='Food Supply (Days)', title='Persediaan Makanan (Hari) Berdasarkan Nama')
fig_food.show()

fig_training = px.pie(df, names='Training Level', title='Distribusi Tingkat Pelatihan')
fig_training.show()

fig_supply = px.scatter_matrix(df, dimensions=['Food Supply (Days)', 'Water per Day (Liters)', 'First Aid Kits'],
                     title='Scatter Matrix untuk Data Supply')
fig_supply.show()

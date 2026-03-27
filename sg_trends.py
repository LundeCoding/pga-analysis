import pandas as pd
import plotly.express as px

player_name = input('Choose tour pro: ')

df = pd.read_csv('pga_data.csv')

df = df[df['sg_total'].notna()]

df_player = df[df['player'] == player_name]
df_player = df_player.sort_values('date')
df_player['sg_total_roll'] = df_player['sg_total'].rolling(window=8).mean()
df_player['sg_ott'] = df_player['sg_ott'].rolling(window=8).mean()
df_player['sg_putt'] = df_player['sg_putt'].rolling(window=8).mean()
df_player['sg_arg'] = df_player['sg_arg'].rolling(window=8).mean()
df_player['sg_app'] = df_player['sg_app'].rolling(window=8).mean()
df_player['sg_t2g'] = df_player['sg_t2g'].rolling(window=8).mean()

if df_player.empty:
    print('Player not found!')
    exit()

fig = px.line(df_player, x='date', y=['sg_total_roll', 'sg_ott', 'sg_putt', 'sg_arg', 'sg_app', 'sg_t2g'])
fig.update_layout(
    title= player_name + ' - Strokes Gained',
    xaxis_title='Date',
    yaxis_title='Strokes Gained'
)
fig.show()

print(df_player.shape)
print(df_player[['date', 'sg_total']])
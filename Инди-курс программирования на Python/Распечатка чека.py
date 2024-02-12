import random
video_games = ("PS4 Grand Theft Auto 5", "Gran Tourismo", "Fifa 23")
video_games_price = 29.99
console = ("Play Station 5", "Xbox 360")
console_price = 599.99
kase = [1, 2, 3, 4, 5, 6]
rekina_nr = 2327016
psc = 1
print("-" * 46)
print("-" * 46)
print(f" {'Veikals Euronics':^40} ")
print(f" {'Ceks':-^45} ")
print(f"Euronics Latvia SIA {'#':>25}")
print(f"{'#':>45}")
print(f"Rekina Nr.: {rekina_nr + 1} {'#':>25}")
print(f"Kase: {kase[1]} {'#':39}")
print(f"Pardevejs: M{random.randint(10, 99)} {'#':>30}")
print(f"{'#':>45}")
print(f"{video_games[0]} {psc:>6} gab. x {video_games_price}{'C':>3}")
print(f"{video_games[2]} {psc:>21} gab. x {video_games_price}{'C':>3}")
print(f"{console[0]} {psc:>14} gab. x {console_price}{'C':>2}")
print("-" * 46)
print(f"Kopsumma EUR {(video_games_price * 2) + (console_price):>32}")
print("-" * 46)
print("-" * 46)
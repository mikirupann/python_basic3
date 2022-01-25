def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    she = 0
    for total in range(0, 8):
        you = (weather_information[total]['temperature'])
        she = she + you
    print(she / 8)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    aka = (weather_information[3]['station'])
    ao = (weather_information[4]['station'])
    ki = (weather_information[5]['station'])
    print(f"'{aka},{ao},{ki}'")

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fuku_temperature = [a['temperature'] for a in weather_information if a['prefecture'] == '福岡県']
    print(sum(fuku_temperature) / 2)


if __name__ == '__main__':
    main()

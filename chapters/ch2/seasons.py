def whats_the_season(season):
    # season = input('Please enter a season: ')
    season = season.strip()
    print(season)
    if season.lower() == 'winter':
        return 'snow'
    elif season.lower() == 'spring':
        return 'flowers'
    elif season.lower() == 'summer':
        return 'beach'
    elif season.lower() == 'fall' or season.lower() == 'autumn':
        return 'leaves'
    else:
        return 'I don`t know that season'


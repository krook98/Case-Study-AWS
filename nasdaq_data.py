import nasdaqdatalink
import pandas as pd
import os

nasdaqdatalink.read_key("key")

countries = {
    'Vietnam': 'VNM',
    'Argentina': 'ARG',
    'Australia': 'AUS',
    'Brazil': 'BRA',
    'Britain': 'GBR',
    'Canada': 'CAN',
    'Chile': 'CHL',
    'China': 'CHN',
    'Colombia': 'COL',
    'Costa Rica': 'CRI',
    'Czech Republic': 'CZE',
    'Denmark': 'DNK',
    'Egypt': 'EGY',
    'Euro area': 'EUR',
    'Hong Kong': 'HKG',
    'Hungary': 'HUN',
    'India': 'IND',
    'Indonesia': 'IDN',
    'Israel': 'ISR',
    'Japan': 'JPN',
    'Lithuania': 'LTU',
    'Malaysia': 'MYS',
    'Mexico': 'MEX',
    'New Zealand': 'NZL',
    'Norway': 'NOR',
    'Pakistan': 'PAK',
    'Peru': 'PER',
    'Philippines': 'PHL',
    # 'Poland': 'POL',
    'Russia': 'RUS',
    'Saudi Arabia': 'SAU',
    'Singapore': 'SIN',
    'South Africa': 'ZAF',
    'South Korea': 'KOR',
    'Sri Lanka': 'LKA',
    'Sweden': 'SWE',
    'Switzerland': 'CHE',
    'Taiwan': 'ROC',
    'Thailand': 'THA',
    'Turkey': 'TUR',
    'UAE': 'UAE',
    'Ukraine': 'UKR',
    'United States': 'USA',
    'Uruguay': 'URY',
    'Venezuela': 'VEN',
    'Austria': 'AUT',
    'Belgium': 'BEL',
    'Estonia': 'EST',
    'Finland': 'FIN',
    'France': 'FRA',
    'Germany': 'DEU',
    'Greece': 'GRC',
    'Ireland': 'IRL',
    'Italy': 'ITA',
    'Netherlands': 'NLD',
    'Portugal': 'PRT',
    'Spain': 'ESP',
    'Latvia': 'LVA'
}

data = nasdaqdatalink.get('ECONOMIST/BIGMAC_POL')
data.insert(1, 'Country', 'POL', True)
for country in countries.values():
    imported = nasdaqdatalink.get('ECONOMIST/BIGMAC_' + country)
    imported.insert(1, 'Country', country, True)
    data = pd.concat([data, imported])
    imported.drop('Country', axis=1)
out = pd.DataFrame(data, columns=['Country', 'local_price', 'dollar_valuation'])
out.sort_values(by=['dollar_valuation'], ascending=False).to_csv("all_data.csv")
selected = out.loc['2021-07-31']
print(selected)
print(type(selected))
print(selected.sort_values(by=['dollar_valuation'], ascending=False).head())

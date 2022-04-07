import pandas as pd
import eurostat

def EUcountries():
    EU_dict = {'Code': ['AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'EL', 'HR', 'HU', 'IE',
                        'IT', 'LT', 'LU', 'LV', 'MT', 'NL', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK'],
               'Country': ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czechia', 'Germany', 'Denmark', 'Estonia',
                           'Spain',
                           'Finland', 'France', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Italy', 'Lithuania',
                           'Luxembourg',
                           'Latvia', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia',
                           'Slovakia'],
               'Accession_year': [1995, 1958, 2007, 2004, 2004, 1958, 1973, 2004, 1986, 1995, 1958, 1981, 2013, 2004,
                                  1973, 1958, 2004, 1958, 2004, 2004, 1958, 2004, 1986, 2007, 1995, 2004, 2004]
               }
    EU_df = pd.DataFrame(EU_dict)

    return EU_df






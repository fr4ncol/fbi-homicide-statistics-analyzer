import csv
import os

# Function to read mapping files and return a dictionary
def read_mapping_file(filename):
    mapping = {}
    with open(filename, 'r', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            mapping[row["code"]] = row["translation"]
    return mapping

# Read the state and location type mappings
state_mapping = read_mapping_file('mappings\\state_mapping.csv')
location_type_mapping = read_mapping_file('mappings\\location_type_mapping.csv')
situation_mapping = read_mapping_file('mappings\\situation_mapping.csv')
age_mapping = read_mapping_file("mappings\\age_mapping.csv")
sex_mapping = read_mapping_file("mappings\\sex_mapping.csv")
race_mapping = read_mapping_file("mappings\\race_mapping.csv")
ethnic_origin_mapping = read_mapping_file("mappings\\ethnic_origin_mapping.csv")
weapon_mapping = read_mapping_file("mappings\\weapon_mapping.csv")
circumstances_mapping = read_mapping_file("mappings\\circumstances_mapping.csv")
sub_circumstances_mapping = read_mapping_file("mappings\\sub_circumstances_mapping.csv")
relationship_mapping = read_mapping_file("mappings\\relationship_mapping.csv")
county_mapping = read_mapping_file("mappings\\county_codes_mapping.csv")

# Define the positions and their respective fields
fields = [
    ("numer_stanu", 2, 3),
    ("kod_agencji", 4, 10),
    ("typ_miejsca_zbrodni", 11, 12),
    ("rok", 14, 15),
    ("populacja", 16, 24),
    ("hrabstwo", 25, 27),
    ("nazwa_agencji", 32, 55),
    ("miesiac_przestepstwa", 62, 63),
    ("typ_zabojstwa", 71, 71),
    ("sytuacja", 75, 75),
    ("wiek_ofiary", 76, 77),
    ("plec_ofiary", 78, 78),
    ("rasa_ofiary", 79, 79),
    ("pochodzenie_etniczne_ofiary", 80, 80),
    ("wiek_sprawcy", 81, 82),
    ("plec_sprawcy", 83, 83),
    ("rasa_sprawcy", 84, 84),
    ("pochodzenie_etniczne_sprawcy", 85, 85),
    ("uzyta_bron", 86, 87),
    ("relacja_ofiary_wzledem_sprawcy", 88, 89),
    ("okolicznosc", 90, 91),
    ("podokolicznosc", 92, 92),
    ("ilosc_dodatkowych_ofiar", 93, 95),
    ("ilosc_dodatkowych_sprawcow", 96, 98),
]

# Function to parse each line based on the defined positions
def parse_line(line):
    data = {}
    for field, start, end in fields:
        value = line[start-1:end].strip()
        if field == "numer_stanu":
            value = state_mapping.get(value, value)  # Translate state number to name
        elif field == "typ_miejsca_zbrodni":
            value = location_type_mapping.get(value, value)  # Translate crime location type
        elif field == "sytuacja":
            value = situation_mapping.get(value, value)
        elif field == "wiek_ofiary" or field =="wiek_sprawcy":
            value = age_mapping.get(value, value)
        elif field == "rasa_sprawcy" or field == "rasa_ofiary":
            value = race_mapping.get(value, value)
        elif field == "plec_ofiary" or field == "plec_sprawcy":
            value = sex_mapping.get(value, value)
        elif field == "pochodzenie_etniczne_sprawcy" or field == "pochodzenie_etniczne_ofiary":
            value = ethnic_origin_mapping.get(value, value)
        elif field == "uzyta_bron":
            value = weapon_mapping.get(value, value)
        elif field == "okolicznosc":
            value = circumstances_mapping.get(value, value)
        elif field == "podokolicznosc":
            value = sub_circumstances_mapping.get(value, value)
        elif field == "relacja_ofiary_wzledem_sprawcy":
            value = relationship_mapping.get(value, value)
        elif field == "populacja" or field == "ilosc_dodatkowych_ofiar" or field == "ilosc_dodatkowych_sprawcow":
            try:
                value = int(value)
            except:
                value=""
        elif field == "typ_zabojstwa":
            if value == "A":
                value = "Murder and Nonnegligent Manslaughter"
            if value == "B":
                value = "Manslaughter by Negligence"
        elif field == "rok":
            try:
                if int(value) > 25:
                    value = int(value)+1900
                else:
                    value = int(value)+2000
            except:
                value=""
        elif field == "hrabstwo":
            try:
                value = int(value)
                value = str(value)
                value = county_mapping.get(value, value)
            except:
                value = ""
               
        data[field] = value
    return data

# Read the input file, parse the data, and write to a CSV file
output_filename = 'output_data.csv'
directory_path = 'resources'
files = os.listdir(directory_path)

with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=[field[0] for field in fields])
    writer.writeheader()
    for filename in files:
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as infile:
               for line in infile:
                    parsed_data = parse_line(line)
                    writer.writerow(parsed_data)

print(f"Data has been successfully written to {output_filename}")

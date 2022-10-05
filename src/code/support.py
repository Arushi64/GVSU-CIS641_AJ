from csv import reader

# since we are going to be importing multiple levels from csv files
# we are creating a function to import multiple csv files from different 
# paths this function will be called in level.py


def import_csv_layout(path):
    terrain_map = []
    # map is a variable that stores the csv we import
    with open(path) as map:
          #use reader method for csv file(stored in variable map)
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map
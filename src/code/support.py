from csv import reader

# since we are going to be importing multiple levels from csv files
# we are creating a function to import multiple csv files from different 
# paths this function will be called in level.py


def import_csv_layout(path):
    game_data = []
    # map is a variable that stores the csv we import
    with open(path) as game_data:
          #use reader method for csv file(stored in variable map)
        level = reader(game_data, delimiter = ',')
        for row in level:
            game_data.append(list(row))
        return game_data
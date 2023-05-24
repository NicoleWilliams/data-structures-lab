"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    data = open(filename)

    for line in data:
        lines = line.split("|")
        species1 = lines[1]
        species.add(species1)

    # TODO: replace this with your code

    return species


# all_species("villagers.csv")



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    data = open(filename)
    for line in data:
        lines = line.split("|")
        names = lines[0]
        villagers.append(names)
        

    # TODO: replace this with your code

    return sorted(villagers)

# get_villagers_by_species("villagers.csv")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    data = open(filename)
    hobbies = []

        # names = hobbies
    fitness = []
    fashion = []
    nature = []
    education = []
    music = []
    play = []

    for line in data:
        lines = line.split("|")
        name = lines[0]
        hobby = lines[3]

        if hobby == "Nature":
            nature.append(name)

        if hobby == "Fitness":
            fitness.append(name)

        if hobby == "Fashion":
            fashion.append(name)

        if hobby == "Education":
            education.append(name)

        if hobby == "Music":
            music.append(name)

        if hobby == "Play":
            play.append(name)


    names_by_hobby = [sorted(fitness), sorted(fashion), sorted(nature), sorted(education), sorted(music), sorted(play)]


    return names_by_hobby

# all_names_by_hobby("villagers.csv")


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        lines = line.split("|")
        lines = tuple(lines)
        all_data.append(lines)


    return all_data

# all_data("villagers.csv")

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    data = open(filename)

    for line in data:
        lines = line.split("|")
        motto = lines[4]
        name = lines[0]

        if villager_name == name:
            return motto

    return None

# find_motto("villagers.csv", "Nicole")  


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    villagers = set()

    data = open(filename)
    villager_name_personality = ""

    for line in data:
        lines = line.split("|")
        personality = lines[2]
        name = lines[0]

        if villager_name == name:
            villager_name_personality = personality
            break

    data = open(filename)

    if villager_name_personality:
        for line in data:
            lines = line.split("|")
            personality = lines[2]
            name = lines[0]
            if villager_name_personality == personality:
                villagers.add(name)
                
    return villagers 

# print(find_likeminded_villagers("villagers.csv", "Wendy"))


def count_villagers_with_name_starting_with(filename, letter):
    """returns a count of villagers whose name starts with a specific letter

    Arguments:
        - filename (str): the path to a data file"""
    
    data = open(filename)
    lst_of_names = []

    for line in data:
        lines = line.split("|")
        name = lines[0]

        if name[0] == letter:
            lst_of_names.append(name)
            # return name
        
    count = len(lst_of_names)
    return count

count_villagers_with_name_starting_with("villagers.csv", "A")
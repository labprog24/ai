def pour_water(juga, jugb, visited, path, max1, max2, fill):
    if jugb == fill:
        print("solution found: \n")
        print(path)
        print("\n")
        return True
    visited.add((juga, jugb))

    possibilities = [
        (max1, jugb), 
        (juga, max2), 
        (0, jugb),    
        (juga, 0),    
        (min(juga+jugb, max1), max(0, juga+jugb-max1)), 
        (max(0, juga+jugb-max2), min(juga+jugb, max2))  
    ]

    for possibility in possibilities:
        if possibility not in visited:
            if pour_water(possibility[0], possibility[1], visited, path+[possibility], max1, max2, fill):
                return True
    
    return False

visited_states = set()
result = pour_water(0, 0, visited_states, [], 4, 3, 2)

if not result:
    print("no result found\n")

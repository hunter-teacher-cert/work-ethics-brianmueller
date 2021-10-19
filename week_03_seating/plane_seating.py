# As a simpler alternative, any family that includes at least one child under the age of 5 (0-4) will all get economy_plus tickets and are thus able to choose their seats
# Implementation considerations: 
# Must include data that represents passengers' ages

import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists.

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold.
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win"
           and removes the number of economy_sold seats
    """
    avail = 0
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing.
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])


    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat


    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but
    just does the random assignment.

    We use this when we're ready to assign the economy seats after most
    of the economy plus seats are sold


    """
    rows = len(plane)
    cols = len(plane[0])

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
            print("seating " + name + " at row:" + str(r_row) + ", col: " + str(r_col))
            print(get_plane_string(plane))
            print("economy_sold: " + str(economy_sold))
            print(" ")
    return plane


def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold


def generate_family():
    """
    Generates a dictionary of up to 3 family members and their ages
    Example: {
        'f-1': 33,
        'f-2': 30,
        'f-3': 2
    }
    """
    max_family_size = 3
    family = {}
    for i in range(3):
        family['f-'+str(i+1)] = random.randrange(100) # max age: 99
    return family

def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """


    economy_sold={}
    total_seats = get_total_seats(plane)



    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 1:
        print("TOTAL SEATS: " + str(total_seats))
        print(" ")
        r = random.randrange(100)
        if r > 30:
            print("r=" + str(r) + ": purchase_economy_plus; economy_sold: " + str(economy_sold) + "; ep_" + str(ep_number))
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold)
        else:
            print("r=" + str(r) + ": purchase_economy_block; economy_sold: " + str(economy_sold) + "; u_" + str(u_number))
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1
        print(get_plane_string(plane))
        print(" ")


    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for name in economy_sold.keys():
        for i in range(economy_sold[name]):
            plane = seat_economy(plane,economy_sold,name)


    return plane



def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print(get_plane_string(plane))
if __name__=="__main__":
    main()

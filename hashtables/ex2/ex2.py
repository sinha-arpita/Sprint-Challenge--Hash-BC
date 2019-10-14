#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)

    #
    #Key : source
    #Value : Ticket to be used in that source
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket)

    #start from None, and reach till last detination
    src = "NONE"
    route = [None] * length
    i = 0;
    while True:
        ticket = hash_table_retrieve(hashtable, src)
        route[i] = ticket.destination
        i += 1

        if ticket.destination == "NONE":
            break

        src = ticket.destination

    print (route)
    return route

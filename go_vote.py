class GoVote():

    def __init__(self, votes):

        self.lower_case_votes = self.lower_case(votes) # fill in function below

        self.votes_dictionary = self.dict_empty_list(self.lower_case_votes) # fill in function below

        self.ballot = self.fill_votes(self.lower_case_votes, self.votes_dictionary) # fill in function below

        self.winner = self.tally(self.ballot) # fill in function below



    def lower_case(self, votes):

        '''Given a list of strings return a list with all lower case strings.

        Any non-string items should be ignored and not copied to the new list.

           

           votes - list of strings

            

           return list with strings all lowercase

        '''

		# insert code here
        votes = []
        for z in votes:
            if isinstance(z, str) and not z.isdigit():
                votes.append(z.lower())
        return votes

		# use isinstance(value, str) to check if an element is a string

		# somestring.isdigit() to check if a string, e.g., '100' is a number.

		



    def dict_empty_list(self, votes):

        '''Given list of strings create list entry in a dictionary.



           votes - list of strings (all lower case)

        

           return a dictionary with an empty list ([]) for each entry.

        '''

		# insert code here
        dict empty = dict()
        for z in votes:
            dict_empty[z] = []
        return dict_empty 


    def fill_votes(self, votes, votes_dictionary):

        '''Fill in the dictionary everytime you see the name in votes.

           

           votes - list of lower case strings

           votes_dictionary - dictionary with empty ([]) entries for each key



           return a dictionary where each time you see a key it is appended

           to the list, e.g., if you see 'anna' twice then the dictionary

           should have votes_dictionary['anna'] = ['anna', 'anna']

        '''

		# insert code here
        for z in votes:
            votes_dictionary[z].append[z]
        return votes_dictionary 



    def tally(self, ballot):

        '''Given the dictionary of how many times we see a user count the winner.



            ballot - dictionary with the number of times a name is in the list



            return a tuple (count, name) where count is the number of votes 

            the name was given, e.g., (2, 'anna')

        '''

        # inser code here
        maximumvotes = 0 
        winner = None 
        for a, b in ballot.items():
            if len(b) > maximumvotes:
                maximumvotes = len(b)
                winner = a
        return (maximumvotes, winner)



# write a decorator called debbuger that will output the current time the function was executed (using datetime library) and the name of the function executed using __name__ inside function (variable is defined by default by python).



def voting():



    votes = ['johny', 'Eli', 'Eli', 'Jane', 'Ally', 'Johny', 'john', 'Eli']



    voters = GoVote(votes)

	# output should be (3, 'eli')

    print(voters.winner)

    

if __name__ == '__main__':

    voting()

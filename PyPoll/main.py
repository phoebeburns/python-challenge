#Create python script to calculate
#   -The total number of votes cast
#   -A complete list of candidates who received votes
#   -The percentage of votes each candidate won
#   -The total number of votes each candidate won
#   -The winner of the election based on popular vote.
#
#   looking forward to doing this type of thing with pandas

# Modules
import os
import csv

#csvpath = os.path.join('.', 'resources','election_data.csv')
#txtpath = os.path.join('.', 'Analysis\\')

csvpath = 'c:\\users\\lunaclara\\python-challenge\\PyPoll\\resources\\election_data.csv'
txtpath = 'c:\\users\\lunaclara\\python-challenge\\PyPoll\\Analysis\\'


#Set numeric variables to 0
Totalvotes = 0

#Open CSV reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader) [1:]

    Totalvotes = 0
    Candidates = []
    Candidate_Vote = {}
    Candidate_Percentage = 0

    for row in csvreader:

        #count total votes
        Totalvotes = Totalvotes + 1

        #find candidates
        Candidate_Name = row[2]

        #determine if new candidate needs to be added to list
        if Candidate_Name not in Candidates:
            Candidates.append(Candidate_Name)

            #initialize new candidate's vote count
            Candidate_Vote[Candidate_Name] = 0

        #add vote    
        Candidate_Vote[Candidate_Name] = Candidate_Vote[Candidate_Name] + 1

    #Who won?
    maxkey = max(Candidate_Vote, key=Candidate_Vote.get)
    winner = ("Winner: " + maxkey)

    print("Election Results")
    print("-----------------------")
    for key, value in Candidate_Vote.items():
        print(key,": ","{:.0%}".format(value/Totalvotes)," (",value,")")
    print("-----------------------") 
    print("Winner: ",maxkey)
    print("-----------------------") 

    with open(txtpath + 'ElectionResults.txt','w') as f:
        f.write("Election Results")
        f.write('\n')
        f.write("-----------------------")
        f.write('\n')
        for key, value in Candidate_Vote.items():
            f.write(key)
            f.write(": ")
            f.write("{:.0%}".format(value/Totalvotes))
            f.write(" (")
            f.write(str(value))
            f.write(")")
            f.write("\n")
        f.write("-----------------------")
        f.write('\n')
        f.write(winner)
        f.write('\n')
        f.write("-----------------------")
        


        


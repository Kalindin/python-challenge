import csv
import os   

Polling_csv = os.path.join("PyPoll","Resources", "election_data.csv")

Results = os.path.join("PyPoll", "Analysis", "election_results.txt")
poll_data={}
total_votes = 0
candidate_options = []
candidate_votes = {}
with open(Polling_csv, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread)
    for row  in csvfile:
        total_votes += 1
       
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
          
            candidate_votes[candidate_name] = 0
       
        candidate_votes[candidate_name] += 1


with open(Results, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

       
        print(candidate_results)
        
        txt_file.write(candidate_results)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)



    













# for row in csvread:
#         total_votes += 1
#         if row[2] in poll_data.keys():
#             poll_data[row[2]] = poll_data[row[2]] + 1
#         else:
#             poll_data[row[2]] = 1 

# candidates = []  
# tot_num_votes = []

# for key, value in poll_data.items():
#     candidates.append(key)
#     tot_num_votes.append(value)

# with open(Results, 'w') as txt_file:
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes:{total_votes}\n"
#         f"-------------------------\n")
#     print(election_results, end="")
#     txt_file.write(election_results) 

#     for candidate_name in candidate_votes:
#         votes = candidate_votes[candidate_name]
#         vote_percentage = float(votes) / float(total_votes) * 100
#         candidate_results = (
#             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
#         print(candidate_results)
#         txt_file. Write(candidate_results)

# #     clean_data = list(zip(candidates, tot_num_votes, vote_percentage))

# #     winner_list = []
# #     for name in clean_data:
# #         if max(tot_num_votes) == name[1]:
# #             winner_list.append(name[0])
# #     winner = winner_list[0]

# #     winning_candidate_summary = (
# #     f"-------------------------\n"
# #     f"Winner: {winner}\n"
# #     f"-------------------------\n"
# #     )
# #     print(winning_candidate_summary)
# #     txt_file.write(winning_candidate_summary)



# # # print ("Election results :")
# # # print(total_votes) 
# # # print(tot_num_votes)  
# # # print(candidates)  
# # # print(votes_percent) 
# # # print(winner)

# # # PyPoll = open("output.txt","w+")
# # # PyPoll.write("Election Results")  
# # # PyPoll.write('\n' + "Total Votes: " + str(total_votes)) 
# # # PyPoll.write('\n' + str(candidates))
# # # PyPoll.write('\n' + str(votes_percent))
# # # PyPoll.write('\n' + str(tot_num_votes)) 
# # # PyPoll.write('\n' + "Winner: " + winner)
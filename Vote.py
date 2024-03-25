
parties= []

def update_voter_info(voter_id,Name,Voting_district ,has_voted):
 parties.append({"voter_id" :voter_id,
                  "Voting_district": Voting_district,
                  "has voted": has_voted})
 if has_voted in parties ==[]:
    has_voted="yes"
print("Vote update : ",parties)

#2.4 

parties =["ASC","ATM","AASD","ANC","AGANG SA",
          "ALJAMA","ATA","AZAPO","APS",
          "BRA","BLF","ZACP","CPM",
          "CSA","COPE","DA","DLC","ECOFORUM","EFF",
          "F4SD","FREE DEMS"
          ]
PatiesList=[memberC for memberC in parties if memberC<1000]
print (parties)

#2.5 Using list comprehension and the filter function, write a piece of code that filters out all

PartiesListN=[]
for MemberN in parties:
 if (MemberN<1000):
    PartiesListN.append(n)
print (PartiesListN)

#2.6
parties=lambda[registered_voters for registered_vote in parties if registered_vote=true)]
(lambda x, y: x + y)
(2, 3)

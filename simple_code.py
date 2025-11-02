"""
This script initializes a list of dictionaries, where each dictionary represents a member of team-alanin.
Each dictionary contains the following information about a team member:
- Name, Slack_Username, Country, Hobby, Affiliation, DNA seq.

The script then iterates through the list and prints each team member's dictionary to the console,
with a newline character separating each entry for better readability.
"""
team_alanin = [
    {
    "Name" : "Aworetan Olamide",
     "Slack_Username" : "Olamide_etan",
     "Country" : "Nigeria",
     "Hobby" : "Swimming",
     "Affiliation" : "Ekiti State University",
     "DNA seq" : "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTAT"
},
     {
    "Name" : "Faith Omondi",
     "Slack_Username" : "Faith",
     "Country" : "Kenya",
     "Hobby" : "Drawing",
     "Affiliation" : "University of Nairobi",
     "DNA seq" : "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGG ACCTGACCCAG"
},
     {
    "Name" : "Shreya Venugopalan Omesh Chendilkumar ",
     "Slack_Username" : "Shreya",
     "Country" : "India",
     "Hobby" : "Music",
     "Affiliation" : "Anna University",
     "DNA seq" : "AGTGCAGACGCGGCTCCTAGCGGATGGGTGCTATTGTGAGGCGGTTGTAGAAGGTATGAGGAGGCTGT"
},
     {
    "Name" : "Taiwo Bankole",
     "Slack_Username" : "Taiwo Bankole",
     "Country" : "Nigeria",
     "Hobby" : "Reading",
     "Affiliation" : "University of Maryland",
     "DNA seq" : "ACAGCCCACAAAATTCCACCTGCTCACAGGTTGGCTGGCTCGACCCAGGTGGTGTCCCCTGCTCTGAGCC"
},
     {
    "Name" : "Adeyeye Daniel",
     "Slack_Username" : "Adeyeye Daniel",
     "Country" : "Nigeria",
     "Hobby" : "Writing",
     "Affiliation" : "Mohammed VI Polytechnic University ",
     "DNA seq" : "ATGCGTACGTTAGCCTGACCGGATCGTTAAGGCTGATCGGCAATGCCGTTGATCCTGAGCTTGGACGATGCT"
},
     {
    "Name" : "Ofosaren Favour oghenevwerhie",
     "Slack_Username" : "Ofosaren Favour",
     "Country" : "Nigeria",
     "Hobby" : "Dancing",
     "Affiliation" : "Delta state university",
     "DNA seq" : "ATGCGTACCTGAACTGCTTAGGCTTACGGAATCGTAA"
},
     {
    "Name" : "Oyiyechukwu Elizabeth Chikelu ",
     "Slack_Username" : "Elizabeth Chikelu",
     "Country" : "Nigeria",
     "Hobby" : "Writing",
     "Affiliation" : "Enugu State University of Science and Technology, Nigeria",
     "DNA seq" : "AGCTCCCGGCCAAGCCAGCACCATGGCCAGATACCGATGCTGCCGCAGCAAAAGCAGGAGCAGATGCCGC"
},
     {
    "Name" : "Jana Zaki",
     "Slack_Username" : "Jana Zaki",
     "Country" : "UK",
     "Hobby" : "Drawing",
     "Affiliation" : "UCL",
     "DNA seq" : "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGATAT"
}

]

for members in team_alanin:
    print(members)
    print("\n")

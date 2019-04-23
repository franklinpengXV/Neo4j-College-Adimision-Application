from neo4jrestclient.client import GraphDatabase
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def deleteNodes(db):
    q = """MATCH (n) DETACH DELETE n"""
    result = db.query(q)

def createNodes(db):    
    try:
        Tk().withdraw()
        filename = askopenfilename()
        f = open(filename, "r")
        stringAddresses = f.read()                
        
    except:
                
        #most likely incorrect path/ no file selected
        print ("Error reading file. Please try again.")    
    
    listInfo = stringAddresses.split("\n")
    
    student = db.labels.create("Student")
    gre = db.labels.create("GRE_Score")
    toefl = db.labels.create("TOEFL_Score")
    uniRating = db.labels.create("University_Rating")
    sop = db.labels.create("SOP")
    lor = db.labels.create("LOR")
    cgpa = db.labels.create("CGPA")
    research = db.labels.create("Research")
    chance = db.labels.create("Chance_of_Admit")
    
    for i in range (5):
        u = db.nodes.create(rating = i + 1)
        uniRating.add(u)
    
        for j in listInfo:        
            listScores = j.split(",")
            schoolRating = listScores[3]
            if (int(i + 1) == int(schoolRating)):  
                print (listScores)
                
                s = db.nodes.create(name = listScores[0])
                student.add(s)
            
                g = db.nodes.create(score = listScores[1])
                gre.add(g)
                
                t = db.nodes.create(score = listScores[2])
                toefl.add(t)
                
                so = db.nodes.create(score = listScores[4])
                sop.add(so)
                
                l = db.nodes.create(score = listScores[5])
                lor.add(l)
                
                c = db.nodes.create(score = listScores[6])
                cgpa.add(c)
                
                r = db.nodes.create(score = listScores[7])
                research.add(r)
                
                ch = db.nodes.create(chance = listScores[8])
                chance.add(ch)
            
                ch.relationships.create("chance_of_admit",u)
                s.relationships.create("gre_score", g)
                s.relationships.create("toefl_score", t)
                s.relationships.create("sop_score", so)
                s.relationships.create("lor_score", l)
                s.relationships.create("cgpa_score", c)
                s.relationships.create("research", r)
                s.relationships.create("probability", ch)
        
    print("Done")
    return 

def main():
    correct = True
    
    while (correct):
        print("Please enter your neo4j user name (default is neo4j):")
        username = input()
        if (username == ""):
            username = "neo4j"
        
        print("Please enter you neo4j server password:")    
        password = input()    
        
        try:
            db = GraphDatabase("http://localhost:7474", username, password)
            correct = False
        except:
            print("Incorrect user name and/ or password. Please try again.\nIf it still fails, make sure server is online.")
    
    print("connection successful")
    
    print("Would you like to reset database (delete all nodes)? Yes/No")
    answer = input().upper()
    
    if (answer == "YES"):
        deleteNodes(db)
    
    print("Would you like to create a database? Yes/No")
    answer = input().upper()
    
    if (answer == "YES"):
        createNodes(db)

if __name__ == "__main__":
    main()
    

from TriviaFactModelsforTwitterBot import *

trivia = [

]

def TriviaFunction():
    db.session.query(TriviaFacts).delete()
    db.session.commit()
    
    for listentry in trivia:
        LoadedTrivia = TriviaFacts(listentry)
        db.session.add(LoadedTrivia)
        db.session.commit()
    
    print("All items have been loaded.")

#TriviaFunction()
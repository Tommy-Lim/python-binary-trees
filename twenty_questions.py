class QuestionNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class QuestionTree:
    def __init__(self):
        self.root = QuestionNode("hippo")

    def play_game(self):
        print("Welcome to 20 Questions.")
        self.root = self.play_game_helper(self.root)

    def play_game_helper(self, node):
        if node.left == None and node.right == None:
            print("You're thinking of:", node.data)
            response = input("y/n? ")
            if response == "y":
                print("I win!!")
                return node
            else:
                # call a function that will insert a new question node
                return self.add_answer(node)
        else:
            print(node.data)
            response = input("y/n? ")
            if response == "y":
                node.right = self.play_game_helper(node.right)
            elif response == "n":
                node.left = self.play_game_helper(node.left)
            else:
                # if someone put in bad in put just ask the question again.
                self.play_game_helper(node)
            return node

    # create a new node that adds a dis-ambiguiating question
    # and a new answer.
    def add_answer(self, old_node):
        your_thing = input("Enter the thing you were thinking of: ")
        question = input("Enter your disambiguating question: ")
        yes_or_no = input("Enter y/n for your thing: ")
        new_node = QuestionNode(question)
        new_thing = QuestionNode(your_thing)
        if yes_or_no == "y":
            new_node.right = new_thing
            new_node.left = old_node.data
        else:
            new_node.left = new_thing
            new_node.right = old_node.data
        return new_node
        # Create new node here.
        # return that node.

twenty_questions = QuestionTree()
twenty_questions.play_game()

keep_playing = True
while keep_playing:
    response = input("do you want to play again? ")
    if response == "y":
      twenty_questions.play_game()
    elif response == "n":
      print("Thanks for playing! Goodbye.")
      keep_playing = False
    else:
        print("I'm sorry I didn't understand you. enter y/n")

class ExtroversionQuiz:
    
    
    def __init__(self):
        self.valid = True
        self.score = 0
        self.output = ''
        self.prediction_statement = 'You are about to take a quiz on whether you are an introvert or an extrovert.\nBut first, lets see how well you know yourself.\nEnter 1 if you think you are an introvert, 2 if you think you are a extrovert, and 3 if you think you have qualities of both.'
        self.prediction_answers = ['1', '2', '3']
        self.prediction_output = ''
        self.compare_prediction = ''
        self.intro_statement = 'For each statement given, how well does this statement represent you?\nAnswer on a scale of 1-5 : 1 being very inaccurate to you, and 5 being very accurate to you.\n'
        self.statement_list = ['I never avoid contact with others. ',
                                'I find it very easy to make new friends. ',
                                'I am very good at cheering others up. ',
                                'I easily captivate people. ',
                                'I am a very talkative person. ',
                                'My overall experiences are exciting. ',
                                'If I am at a party I talk to many different people. ',
                                'I am good at handeling social situations. ',
                                'I am easy to get to know. ',
                                'I do not mind being the center of attention. ',
                                'I feel comfortable around new people. ',
                                'I have a lot to say when I am around others in a social setting. ',
                                'I am the life of the party. ',
                                'I warm up to others easily. ',
                                'I easily start new conversations. ']
        self.possible_answers = ['1', '2', '3', '4', '5']
        
    def run_extroversion_quiz(self):
        
        """ Prints out quiz statements for user. Changes input to an integer and adds the total score together. Catches if the
        user inputs an incorrect value and sets the variable self.valid to false.
        
        Parameters
        ----------
        none
        
        Returns
        -------
        self.valid : boolean
            If self.valid is false this means the user inputed an incorrect value. They are then prompted to rerun the code and 
            only input integer values between 1-5. If true, the quiz continues as normal.
            
       self.score : int
           The sum of all user inputs to the statement questions. Score is used to determined whether the user is an introvert,
           extrovert, or has qualities of both.
       
       """
        
        print(self.prediction_statement)
        self.user_prediction = input()
        
        if self.user_prediction in self.prediction_answers:
            print(self.intro_statement)
            
            for statement in self.statement_list:
                user_input = input(statement)
                print('')
                
                if user_input in self.possible_answers:
                    user_input = int(user_input)  # In order to add user inputs together, str must be changed to int
                    self.score = self.score + user_input
                    
                else: 
                    self.valid = False
                    return self.valid
                         
        return self.score 
    
    def score_analysis(self):
        
        """ Compares user score to fixed ranges to determine whether or not the user is more extroverted, introverted, or has
        qualities of both. Sets a value for self.compare_prediction depending on what the quiz results are. 
        
        Parameters
        ----------
        none
        
        Returns
        -------
        self.compare_prediction : str
            Assigns a value to the users quiz results to see if it matched the users prediction.
            
        self.output : str
            Attributes a string output to the users total quiz score indicating their quiz results. 
        
        self.valid : boolean 
            If self.valid is false this means the user inputed an incorrect value. They are then prompted to rerun the code and 
            only input integer values between 1-5. If true, the quiz continues as normal.
            
        """
        
        if type(self.score) == int and self.valid == True: #  extra checks to make sure inputs are correct
        
            if 15 <= self.score <= 35:
                self.output = ' are an introvert. '
                self.compare_prediction = '1'
        
            elif 36 <= self.score <= 55:
                self.output = ' have a mix of both introverted and extroverted qualities. '
                self.compare_prediction = '3'

            
            elif 56 <= self.score <= 75:
                self.output = ' are an extrovert. '
                self.compare_prediction = '2'
                
            return self.compare_prediction, self.output
        
        else:
            print('Oops, looks like you entered an invalid input. Please re-run the quiz and make sure you only enter integers between 1 and 5.')
            
            self.valid = False  # When self.valid = False the rest of the methods will not execute (or print anything).
            return self.valid

    def extroversion_prediction(self):
        
        """ Checks the users prediction vs. their actual quiz results, and attributes print statements to whether the user 
        correctly or incorrectly predicted their quiz results. 
        
        Parameters
        ----------
        none
        
        Returns
        -------
        self.valid : boolean
            If self.valid is false this means the user inputed an incorrect value. They are then prompted to rerun the code and 
            only input integer values between 1-5. If true, the quiz continues as normal.
            
        """
                  
        if self.user_prediction in self.prediction_answers:
                                    
            if self.user_prediction == self.compare_prediction:
                self.prediction_output = 'You guessed correctly!\nYour initial prediction matches your test results.'
            
            elif self.user_prediction != self.compare_prediction:
                self.prediction_output = 'Your initial prediction does not match your test results.'
                
        else: 
            print ('Oops, looks like you entered an invalid input. Please re-run and enter a 1, 2, or 3.')
            
            self.valid = False  # When self.valid = False the rest of the methods will not execute (or print anything).
            return self.valid 

    def quiz_results(self):
        
        #Makes sure self.valid = True and then prints out quiz results. This is the final print statement that the user sees. 
                
        if self.valid == True:
            print('Your score is ' + str(self.score) + ' meaning you' + self.output + self.prediction_output)

    
            

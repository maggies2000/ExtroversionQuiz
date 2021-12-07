from classes import ExtroversionQuiz

eq = ExtroversionQuiz()

def test_run_extroversion_quiz():
    assert callable(eq.run_extroversion_quiz)
    assert type(eq.score) == int
    
def test_score_analysis():
    assert callable(eq.score_analysis)
    assert type(eq.output) == str
    
def test_extroversion_prediction():
    assert callable(eq.extroversion_prediction)
    assert type(eq.prediction_output) == str

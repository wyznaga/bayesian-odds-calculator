# print welcome
print "*"*80
print "*"," "*5,"Welcome to the Bayesian Odds/Likelihood Updating Calculator v1.0"," "*5,"*"
print "*"*80
print

# print first prompt
prior_choie = ""
prior_odds_first = 0
prior_odds_second = 0
prior_percent_prev = 0.0
def get_prior_choice(iterative_prior=0.0):
    if (iterative_prior == 0.0):
        print "Please select whether you wish to enter:"
        print "(1) a prior odds ratio"
        print "(2) a prior percent prevalence: "
        prior_choice = raw_input()
        if prior_choice == "1":
            print "Enter prior odds ratio, first number: "
        elif prior_choice == "2":
            print "Enter percent prevalence, > 0. and < 1. : "
        else:
            print "Invalid input received. Please try again."
            get_prior_choice()
    else:
        print "Using previous posterior as prior; value: ",iterative_prior
get_prior_choice()

# deal with whatever case the user input

result = 0.0

def get_prior_odds():
    pass
def get_prior_percent_prev():
    pass
multi_odds_ratio = 0.0
def get_multi_odds_ratio():
    pass
compare_odds_first = 0
compare_odds_second = 0
def get_comparative_prev():
    pass
def display_results():
    pass
def get_new_iteration():
    pass


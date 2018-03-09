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
            prior_odds_first = int(raw_input())
            print "Enter prior odds ratio, second number: "
            prior_odds_second = int(raw_input())
            get_evidence_choice()
        elif prior_choice == "2":
            print "Enter percent prevalence, > 0. and < 1. : "
            prior_percent_prev = float(raw_input())
            get_evidence_choice()
        else:
            print "Invalid menu choice received. Please try again."
            get_prior_choice()
    else:
        print "Using previous posterior as prior; value: ",iterative_prior
get_prior_choice()

# deal with getting evidence to update on
result = 0.0
multi_odds_ratio = 0.0
compare_odds_first = 0
compare_odds_second = 0
def get_evidence_choice():
    print "Please select whether you wish to enter as evidence:"
    print "(1) "
    print "(2) "
    evidence_choice = raw_input()
    if evidence_choice == "1":
        print "Enter multiplicative likehood (odds) ratio, single float, > 0. :"
        multi_odds_ratio = float(raw_input())
    elif evidence_choice == "2":
        print "Enter prevalence of reporting among trait-postive population, first number: "
        compare_odds_first = int(raw_input())
        print "Enter prevalence of reporting among trait-positive population, second number: "
        compare_odds_second = int(raw_input())
    else:
        print "Invalid menu choice received. Please try again."
        get_evidence_choice()

# deal with displaying the result in multiple formats as described in README
def display_results():
    pass

# deal with the case in which the user wants to make the new prior = posterior
def get_new_iteration():
    pass


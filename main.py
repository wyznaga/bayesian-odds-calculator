from sys import *

if __name__ == "__main__":
    # initialize necessary global variables
    first_prior = 0.0
    first_run = True
    prior_choice = ""
    prior_odds_first = 0
    prior_odds_second = 0
    prior_percent_prev = 0.0
    multi_odds_ratio = 0.0
    compare_odds_first = 0
    compare_odds_second = 0
    posterior_odds_first = 0
    posterior_odds_second = 0
    posterior_likelihood = 0.0

    # print welcome
    print "*"*80
    print "*"," "*5,"Welcome to the Bayesian Odds/Likelihood Updating Calculator v1.0"," "*5,"*"
    print "*"*80
    print

    # deal with displaying the results in multiple formats as described in README
    def display_results():
        print "*"*80
        print "*"," "*34,"RESULT"," "*34,"*"
        print "*"*80
        print "Posterior likelihood: ",posterior_likelihood*100.0,"%"
        print "Posterior odds: ",posterior_likelihood*100.0,":",(100.0 - (posterior_likelihood*100.0))

    # deal with calculating results
    def calc_results():
        global multi_odds_ratio
        global prior_percent_prev
        global prior_odds_first
        global prior_odds_second
        global compare_odds_first
        global compare_odds_second
        global posterior_likelihood
        global first_prior
        # first determine what actual calculation is needed
        if (multi_odds_ratio > 0.0 and prior_percent_prev > 0.0):
            posterior_likelihood = ((prior_percent_prev * 100.0) * multi_odds_ratio)/(((prior_percent_prev * 100.0) * multi_odds_ratio) + (100.0 - (prior_percent_prev * 100.0)))
        elif (multi_odds_ratio > 0.0 and (prior_odds_first > 0 and prior_odds_second > 0)):
            posterior_likelihood = (float(prior_odds_first) * multi_odds_ratio)/(((float(prior_odds_first) * multi_odds_ratio)) + (float(prior_odds_second)))
        elif ((compare_odds_first > 0 and compare_odds_second > 0) and prior_percent_prev > 0.0):
            posterior_likelihood = ((prior_percent_prev * 100.0) * compare_odds_first)/(((prior_percent_prev * 100.0) * compare_odds_first) + ((100.0 - (prior_percent_prev * 100.0)) * compare_odds_second))
        elif ((compare_odds_first > 0 and compare_odds_second > 0) and (prior_odds_first > 0 and prior_odds_second > 0)):
            posterior_likelihood = (prior_odds_first * compare_odds_first)/((prior_odds_first * compare_odds_first) + (prior_odds_second * compare_odds_second))
        else:
            print "Unusable values were input for prior percent, prior odds, multiplicative ratio, or evidentiary odds."
            print "Returning to initial prior data collection..."
            get_prior_choice()

    # define function for dealing with getting evidence to update on since next function ...
        # ... already depends on it
    def get_evidence_choice():
        global multi_odds_ratio
        global compare_odds_first
        global compare_odds_second
        print "Please select whether you wish to enter as evidence:"
        print "(1) A multiplicative (single float) odds-altering ratio"
        print "(2) A new set of evidentiary comparative odds: "
        evidence_choice = raw_input()
        if evidence_choice == "1":
            print "Enter multiplicative likehood (odds) ratio, single float, > 0. :"
            multi_odds_ratio = float(raw_input())
            calc_results()
        elif evidence_choice == "2":
            print "Enter prevalence of reporting among trait-postive population, first number: "
            compare_odds_first = int(raw_input())
            print "Enter prevalence of reporting among trait-positive population, second number: "
            compare_odds_second = int(raw_input())
            calc_results()
        else:
            print "Invalid menu choice received. Please try again."
            get_evidence_choice()

    # print first prompt
    def get_prior_choice(iterative_prior=0.0):
        global prior_choice
        global prior_odds_first
        global prior_odds_second
        global first_run
        global first_prior
        global prior_percent_prev
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
                if first_run:
                    first_prior = float(prior_odds_first)/(float(prior_odds_first) + float(prior_odds_second))
                    first_run = False
                get_evidence_choice()
            elif prior_choice == "2":
                print "Enter percent prevalence, > 0. and < 1. : "
                prior_percent_prev = float(raw_input())
                if first_run:
                    first_prior = prior_percent_prev
                    first_run = False
                get_evidence_choice()
            else:
                print "Invalid menu choice received. Please try again."
                get_prior_choice()
        else:
            print "Using previous posterior as prior; value: ",iterative_prior
            prior_percent_prev = iterative_prior
            get_evidence_choice()

    while True:
        get_prior_choice()
        display_results()

        while True:
            print "Finally, please select whether you wish to: "
            print "(1) Calculate a new posterior, with the current posterior as the new prior"
            print "(2) Enter an entirely new prior and start over with a different calculation"
            print "(0) Exit"
            task_choice = raw_input()
            if task_choice == "1":
                get_prior_choice(iterative_prior = posterior_likelihood)
                break
            elif task_choice == "2":
                first_run = True
                get_prior_choice()
                break
            elif task_choice == "0":
                exit(0)
            else:
                print "Invalid menu choice received. Please try again."
                continue

#Specialisterne Academy - Uge 2 
# opgave - BlackJack

import numpy as np
import copy
import time



playing_cards_dict = { 
    #dictionary of a set of playing cards (52 cards) with names and values for BlackJack.
    #Key: A:Ace, J:Jack, Q:Queen, K:King, H:Hearts, S:Spades, C:Clubs, D:Diamonds.
    'AH' : np.array([1,11]) , '2H' : np.array([2]) , '3H' : np.array([3]) , 
    '4H' : np.array([4]) , '5H' : np.array([5]) , '6H' : np.array([6]) , '7H' : np.array([7]),
    '8H' : np.array([8]) , '9H' : np.array([9]) , '10H' : np.array([10]) , 
    'JH' : np.array([10]), 'QH' : np.array([10]), 'KH' : np.array([10]) , 
    'AS' : np.array([1,11]) , '2S' : np.array([2]) , '3S' : np.array([3]) , 
    '4S' : np.array([4]) , '5S' : np.array([5]) , '6S' : np.array([6]) , '7S' : np.array([7]),
    '8S' : np.array([8]) , '9S' : np.array([9]) , '10S' : np.array([10]) , 
    'JS' : np.array([10]), 'QS' : np.array([10]), 'KS' : np.array([10]) , 
    'AC' : np.array([1,11]) , '2C' : np.array([2]) , '3C' : np.array([3]) , 
    '4C' : np.array([4]) , '5C' : np.array([5]) , '6C' : np.array([6]) , '7C' : np.array([7]),
    '8C' : np.array([8]) , '9C' : np.array([9]) , '10C' : np.array([10]) , 
    'JC' : np.array([10]), 'QC' : np.array([10]), 'KC' : np.array([10]) , 
    'AD' : np.array([1,11]) , '2D' : np.array([2]) , '3D' : np.array([3]) , 
    '4D' : np.array([4]) , '5D' : np.array([5]) , '6D' : np.array([6]) , '7D' : np.array([7]),
    '8D' : np.array([8]) , '9D' : np.array([9]) , '10D' : np.array([10]) , 
    'JD' : np.array([10]), 'QD' : np.array([10]), 'KD' : np.array([10]) , 
    
    }
image_dict = { 
    #dictionary mapping cards to representative PNG files
    #Key: A:Ace, J:Jack, Q:Queen, K:King, H:Hearts, S:Spades, C:Clubs, D:Diamonds.
    'AH' : 'card_imgs/ace_of_hearts' , '2H' : 'card_imgs/2_of_hearts' , '3H' : 'card_imgs/3_of_hearts' , 
    '4H' : 'card_imgs/4_of_hearts' , '5H' : 'card_imgs/5_of_hearts' , '6H' : 'card_imgs/6_of_hearts' , '7H' : 'card_imgs/7_of_hearts',
    '8H' : 'card_imgs/8_of_hearts' , '9H' : 'card_imgs/9_of_hearts' , '10H' : 'card_imgs/10_of_hearts' , 
    'JH' : 'card_imgs/jack_of_hearts2', 'QH' : 'card_imgs/queen_of_hearts2', 'KH' : 'card_imgs/king_of_hearts2' , 
    'AS' : 'card_imgs/ace_of_spades' , '2S' : 'card_imgs/2_of_spades' , '3S' : 'card_imgs/3_of_spades' , 
    '4S' : 'card_imgs/4_of_spades' , '5S' : 'card_imgs/5_of_spades' , '6S' : 'card_imgs/6_of_spades' , '7S' : 'card_imgs/7_of_spades',
    '8S' : 'card_imgs/8_of_spades' , '9S' : 'card_imgs/9_of_spades' , '10S' : 'card_imgs/10_of_spades' , 
    'JS' : 'card_imgs/jack_of_spades2', 'QS' : 'card_imgs/queen_of_spades2', 'KS' : 'card_imgs/king_of_spades2' , 
    'AC' : 'card_imgs/ace_of_clubs' , '2C' : 'card_imgs/2_of_clubs' , '3C' : 'card_imgs/3_of_clubs' , 
    '4C' : 'card_imgs/4_of_clubs' , '5C' : 'card_imgs/5_of_clubs' , '6C' : 'card_imgs/6_of_clubs' , '7C' : 'card_imgs/7_of_clubs',
    '8C' : 'card_imgs/8_of_clubs' , '9C' : 'card_imgs/9_of_clubs' , '10C' : 'card_imgs/10_of_clubs' , 
    'JC' : 'card_imgs/jack_of_clubs2', 'QC' : 'card_imgs/queen_of_clubs2', 'KC' : 'card_imgs/king_of_clubs2' , 
    'AD' : 'card_imgs/ace_of_diamonds' , '2D' : 'card_imgs/2_of_diamonds' , '3D' : 'card_imgs/3_of_diamonds' , 
    '4D' : 'card_imgs/4_of_diamonds' , '5D' : 'card_imgs/5_of_diamonds' , '6D' : 'card_imgs/6_of_diamonds' , '7D' : 'card_imgs/7_of_diamonds',
    '8D' : 'card_imgs/8_of_diamonds' , '9D' : 'card_imgs/9_of_diamonds' , '10D' : 'card_imgs/10_of_diamonds' , 
    'JD' : 'card_imgs/jack_of_diamonds2', 'QD' : 'card_imgs/queen_of_diamonds2', 'KD' : 'card_imgs/king_of_diamonds2' , 
    
    }


def shuffle_cards(cards_dict):
    #Takes key values from the playing_cards_dict and returns them in random order
    SC_deck = list(cards_dict.keys())
    np.random.shuffle(SC_deck)
    return SC_deck




def deal_card(hand, deck):
    #Removes first card from deck and adds it to hand
    hand.append(deck[0])
    deck.pop(0)
    return hand, deck




def initialize_game(cards_dict):
    #Sets initial deck and hands by drawing 2 cards to both player and dealer
    init_player_hand = []
    init_dealer_hand = []
    init_deck = shuffle_cards(cards_dict)
    
    init_player_hand, init_deck = deal_card(init_player_hand, init_deck)
    
    init_dealer_hand, init_deck = deal_card(init_dealer_hand, init_deck)
    
    init_player_hand, init_deck = deal_card(init_player_hand, init_deck)
    
    init_dealer_hand, init_deck = deal_card(init_dealer_hand, init_deck)
    
    #print(init_deck)
    #print(init_player_hand)
    #print(init_dealer_hand)
    
    return init_player_hand, init_dealer_hand, init_deck




def compute_score(hand, cards_dict):
    # Given a blackjack hand, computes score, including ambiguous scores with Aces in hand

    CS_hand_values = []
    # Find card values from dictionary
    for i in range(len(hand)):
        CS_hand_values.append(cards_dict[hand[i]])
       
    #print(CS_hand_values)
    # adds up score of cards in hand, making sure to account for possibilities
    # offered by any aces present in hand
    CS_hand_sum = np.array([0])
    for i in range(len(hand)):
        if len(CS_hand_values[i]) == 1:
            CS_hand_sum += CS_hand_values[i]
        else:
            CS_temp1 = copy.deepcopy(CS_hand_sum) + CS_hand_values[i][0]
            CS_temp2 = copy.deepcopy(CS_hand_sum) + CS_hand_values[i][1]
            CS_hand_sum = CS_temp1
            CS_hand_sum = np.append(CS_hand_sum, CS_temp2)
    
    # Sorts potential scores in descending order
    CS_score=0
    CS_hand_sum = np.sort(CS_hand_sum)
    CS_hand_sum = CS_hand_sum[::-1]
    #print('Sorted possible scores: '+ str(CS_hand_sum))
    
    # Returns the highest potential score that doesn't violate the 21 score limit.
    # If no such score exists returns highest (only) score.
    for i in range(len(CS_hand_sum)):
        CS_score = CS_hand_sum[i]
        if CS_hand_sum[i] <=21:
            break
    #if CS_score >= 22:
    #    print(str(CS_score) + ', you lose')
    #else:
    #    print('Score: '+str(CS_score))    
    #print('Score: '+str(CS_score))
    return CS_score




def dealer_logic(player_hand, dealer_hand, deck):
    # Decision 'AI' for dealer; draws on 16 or below, stands on 17 or above.
    
    #Calculate scores and check if player went bust
    DL_player_score = compute_score(player_hand, playing_cards_dict)
    DL_dealer_score = compute_score(dealer_hand, playing_cards_dict)
    if DL_player_score >=22:
        print('House Wins\nYour Score: '+str(DL_player_score)+'\nDealer Score: '+str(DL_dealer_score))
        return
    
    # Dealer draws card if below 16, stops when at 17 or above.
    while DL_dealer_score <= DL_player_score or DL_dealer_score <= 16:
        
        if DL_dealer_score >= 17:
            break
        
        dealer_hand, deck = deal_card(dealer_hand, deck)
        print('Dealer drew '+str(dealer_hand[-1])+'\n')
        DL_dealer_score = compute_score(dealer_hand, playing_cards_dict)
        time.sleep(0.7)
    # Evaluate result; Win, lose or push.
    if DL_dealer_score <= DL_player_score-1 or DL_dealer_score >= 22:
        print('YOU WIN!!!\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    elif DL_dealer_score >= DL_player_score+1:
        print('House Wins\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    else:
        print('It´s a push!\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    return



def play_blackjack(cards_dict):
    # Initialize dictionary, deck and hands:
    PBJ_cards_dict = cards_dict
    PBJ_player_hand, PBJ_dealer_hand, PBJ_deck = initialize_game(PBJ_cards_dict)
    
    PBJ_player_score = compute_score(PBJ_player_hand, PBJ_cards_dict)
    PBJ_dealer_score = compute_score(PBJ_dealer_hand, PBJ_cards_dict)
    
    #Show player hand and open dealer card
    print('Your cards are '+str(PBJ_player_hand[0])+' and '+str(PBJ_player_hand[1]) + ' with a current score of '+str(PBJ_player_score)+'\n')
    print('Dealers open card is '+str(PBJ_dealer_hand[1])+'\n')
    
    
    while PBJ_player_score <= 22:
        
        PBJ_input = input('HIT/STAND\n\n')
        
        time.sleep(0.7)
        
        if PBJ_input == 'HIT':
            
            PBJ_player_hand, PBJ_deck = deal_card(PBJ_player_hand, PBJ_deck)
            
            PBJ_player_score = compute_score(PBJ_player_hand, PBJ_cards_dict)
            
            print('\n You drew '+str(PBJ_player_hand[-1])+'!\n')
            
            print('\n Your current score is '+str(PBJ_player_score)+'\n')
        elif PBJ_input == 'STAND':
            break
        
        else:
            print('\nERROR: invalid input\n')
        
    print('\nDealers hidden card is '+str(PBJ_dealer_hand[0])+'\n')
    
    time.sleep(0.7)
    
    dealer_logic(PBJ_player_hand, PBJ_dealer_hand, PBJ_deck)
    
    
    return

play_blackjack(playing_cards_dict)




#test_deck =shuffle_cards(playing_cards_dict)
#test_hand, test_deck = deal_card([], test_deck)
#print(test_hand)
#test_hand, test_deck = deal_card(test_hand, test_deck)
#print(test_hand)
#test_hand, test_deck = deal_card(test_hand, test_deck)
#print(test_hand)
#print(playing_cards_dict['2H'])

 

#print(len(['AH','AS','AD']))
#test_hand = ['AH','AS','AD']
#test_score = compute_score(test_hand, playing_cards_dict)

#test_deck =shuffle_cards(playing_cards_dict)
#test_hand = []
#print(list(playing_cards_dict.keys()))


#test_ph, test_dh, test_deck = initialize_game(playing_cards_dict)
#test_ph, test_deck = deal_card(test_ph, test_deck)
#dealer_logic(test_ph, test_dh, test_deck)
#print(test_deck)
#print(test_ph)
#print(test_dh)




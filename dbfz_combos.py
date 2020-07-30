''' This program is to help keyboard players who are playing dbfz
to use combos easily and use them with their keyboard controls'''

#(import pandas) use later to make output on a seperate .xlsx file or a .txt one
def sayhi(): # Just a regular function to grab the user's attention
	print("Welcome to: ")
	print()
	print("Dragon.Ball.FighterZ C-O-M-B-O GeNeRaToR ")
	print()

def get_controls(): #Gets the controls of the user
	Y_button = input('Please enter your (Y) button control: ')
	X_button = input('Please enter your (X) button control: ')
	A_button = input('Please enter your (A) button control: ')
	B_button = input('Please enter your (B) button control: ')
	RT_button = input('Please enter your (RT) button control: ')
	RB_button = input('Please enter your (RB) button control: ')
	LT_button = input('Please enter your (LT) button control: ')
	LB_button = input('Please enter your (LB) button control: ')
	xbox_controls_list = [Y_button, X_button, A_button, B_button, 
							RT_button, RB_button, LT_button, LB_button]
	print("Your keyboard controls are, ")
	print(xbox_controls_list)

	def generate_combos(): #Function to generate combos (I think it is clear 0_0)
		###general attacks and moves
		light_attack = ('Light Attack: ' + X_button) #Making the type of attacks in user keyboard controls
		medium_attack = ('Medium Attack: ' + Y_button)
		heavy_attack = ('Heavy Attack: ' + B_button)
		special_attack = ('Special Attack: ' + A_button)
		assist_1 = ('Assist 1: ' + LB_button)
		assist_2 = ('Assist 2: '+ LT_button)
		dragon_rush = ('Dragon Rush: ' + A_button + ' + ' + B_button)
		ki_charge = ('Ki Charge: ' + A_button + ' + ' + X_button)
		sparking_blast = ('Sparking Blast: ' + A_button + ' + ' + B_button + ' + ' + X_button + ' + ' + Y_button)
		super_dash = ('Super Dash: ' + X_button + ' + ' + Y_button)
		vanish = ('Vanish: ' + Y_button + ' + ' + B_button)
		#----GOKU----
		dragon_flash_fist = ('Special Attack (Dragon Flash Fist): ' + 'Down ' + ' + ' +  'Down right ' + ' + ' +
							 'right ' + ' + ' + X_button + ' or ' + Y_button + ' or ' + B_button)
		rapid_kick_rush = ('Special Attack (Rapid Kick Rush): ' + 'Down ' + ' + ' + 'Down left ' + ' + ' + 'Left ' + ' + ' +
						    X_button + ' or ' + Y_button + ' or ' + B_button)
		kamehameha = ('Special Attack (Kamehameha): ' + 'Down ' + ' + ' + 'Down right ' + ' + ' + 'right ' +  ' + ' + A_button)
		super_kamehameha = ('SUPER Special Attack (Super Kamehameha): ' + 'Down ' + ' + ' + 'Down right ' + ' + ' +  'right ' + ' + ' +
							RB_button)
		instant_tranmission_kamehameha = ('SUPER Special Attack (Instant Transmission Kamehameha): ' + 'Down ' + ' + ' + 'Down right' + ' + ' +
										  'right ' + ' + ' + RT_button)
		meteor_smash = ('SUPER Special Attack (Meteor Smash): ' + 'Down ' + ' + ' +  'Down left ' + ' + ' + 'left ' + ' + ' + RB_button + ' or ' + RT_button)
		#----TEEN GOHAN----
		aerial_kick = ('Special Attack (Aerial Kick): ' + 'Down ' + ' + ' + 'Down right ' + ' + ' + 'right ' +
					    X_button + ' or ' + Y_button + ' or ' + B_button)
		five_strike_combo = ('Special Attack (Five Strike Combo): ' + 'Down ' + ' + ' + 'Down right ' + ' + ' + 'right ' + 
							 X_button + ' or ' + Y_button + ' or ' + B_button)
		dragon_flight = ('Special Attack (Dragon Flight): ' + 'Down ' + ' + ' + 'Down left ' + ' + ' + 'left ' +
						 X_button + ' or ' + Y_button + ' or ' + B_button)
		no_motion_kamehameha = ('SUPER Special Attack (No Motion Kamehameha): ' + 'Down ' + ' + ' + 'Down right ' + ' + ' + 'right ' +
								RB_button + ' or ' + RT_button)
		Father_son_kamehameha = ('SUPER Special Attack (Father-son Kamehameha): ' + 'Down ' + ' + ' + 'Down left ' + ' + ' + 'left ' +
								RB_button + ' or ' + RT_button)
		Father_son_kamehameha_full_power = ('SUPER Special Attack (Father-son Kamehameha): ' + 'Down ' + ' + ' + 'Down left ' + ' + ' + 'left ' +
								RB_button + ' or ' + RT_button + ' Hold any button ' + ' (CONSUMES 2 GAUGES)')
		Goku_moves = [dragon_flash_fist,
		              rapid_kick_rush,
					  kamehameha,
					  super_kamehameha,
					  instant_tranmission_kamehameha,
					  meteor_smash]
		teen_gohan_moves = [aerial_kick,
							five_strike_combo,
							dragon_flight,
							no_motion_kamehameha,
							Father_son_kamehameha,
							Father_son_kamehameha_full_power]
		combos_generation = [light_attack,
							 medium_attack,         
							 heavy_attack,
							 special_attack,
							 assist_1,
							 assist_2,     #Making the attacks I previously made in a list in order to print them later 
							 dragon_rush,
							 ki_charge,
							 sparking_blast,
							 super_dash,
							 vanish
							]
		ask_to_proceed = input('Would you like to generate your combos (y/n): ')
		if ask_to_proceed == 'y':
			print('Here are your results! (YOU MAY COPY THEM) ')
			print()
			print(*combos_generation, sep='\n- ')				
		elif ask_to_proceed == 'n':
    			print('thanks for using Dragon.Ball.FighterZ C-O-M-B-O GeNeRaToR! ')
		#Character Choice
		choose_character = input('Would you like to see the moves of a specific character? (y/n)')
		characters_available = ['goku' , 'teen_gohan']
		if choose_character == 'y':
			print(characters_available)
			pick_character = input('pick one character from above: ')
			if pick_character == 'goku' or 'Goku' or 'GOKU':
    				print('Here are your results! (YOU MAY COPY THEM) ')
    				print(*Goku_moves , sep='\n- ')
			elif pick_character == 'teen_gohan' or 'Teen_Gohan' or 'TEEN_GOHAN':
    				print('Here are your results! (YOU MAY COPY THEM) ')
    				print(*teen_gohan_moves , sep='\n- ')
		
	generate_combos()

#After we get the controls of the user and make it in a list
#we create another list containing the actual combos in the game
#and assign the controls of the user to fit the combos and spit it out
sayhi()
get_controls()

def main():
    pass
if __name__ == '__main__':
    	main()

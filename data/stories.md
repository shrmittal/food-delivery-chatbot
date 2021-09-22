## complete path sep yes and email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

## location specified no email
* greet
    - utter_greet
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail

## complete path combined yes and email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
* emailConfirm{"emailConfirmation": "Yes", "to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

## complete path incorrect location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "italy"}

## complete path separate yes and email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "shenoy.tejaswini@gmail.com"}


## cuisine and location specified yes and email combined
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* emailConfirm{"emailConfirmation": "Yes", "to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

## location specified no results
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## location specified sep yes and email
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "pune"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## location specified separate yes and email
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "shenoy.tejaswini@gmail.com"}
    - slot{"to": "shenoy.tejaswini@gmail.com"}
    - action_send_mail
    - slot{"to": "shenoy.tejaswini@gmail.com"}


## complete path sep yes and email 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "noida"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "shenoy.tejaswini@gmail.com"}
    - slot{"to": "shenoy.tejaswini@gmail.com"}
    - action_send_mail
    - slot{"to": "shenoy.tejaswini@gmail.com"}

## location specified no email 2
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
    
## complete path no email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "agra"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail

## location specified combined yes and email
* greet
    - utter_greet
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "Ghaziabad"}
* emailConfirm{"emailConfirmation": "Yes", "to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

## location specified incorrect location
* greet
    - utter_greet
* restaurant_search{"location": "singapore"}
    - slot{"location": "singapore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "singapore"}

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "manali"}
    - slot{"location": "manali"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "manali"}
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
* goodbye
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
* emailConfirm{"emailConfirmation": "Yes", "to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "Jhansi"}
    - slot{"location": "Jhansi"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "Jhansi"}
* restaurant_search{"cuisine": "american", "location": "Goa"}
    - slot{"cuisine": "american"}
    - slot{"location": "Goa"}
    - utter_ask_price
* restaurant_search{"price": "Under 300"}
    - slot{"price": "Under 300"}
    - action_search_restaurants
    - slot{"location": "Goa"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
* greet
    - utter_greet

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_price
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

* greet
    - utter_greet
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - utter_ask_location
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
* restaurant_search{"price": "Between Rs. 300 to Rs. 700"}
    - slot{"price": "Between Rs. 300 to Rs. 700"}
    - utter_ask_location
* restaurant_search{"location": "hosur"}
    - slot{"location": "hosur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "AMERICAN"}
    - slot{"cuisine": "AMERICAN"}
    - action_search_restaurants
    - slot{"location": "hosur"}
* greet
    - utter_greet
* restaurant_search{"price": "Between300to700"}
    - slot{"price": "Between300to700"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "AMERICAN"}
    - slot{"cuisine": "AMERICAN"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneshwar"}
    - slot{"location": "Bhubaneshwar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "bhubaneshwar"}
* emailRecipient{"emailConfirmation": "Yes", "to": "shenoy.tejaswini@gmail.com"}
    - slot{"to": "shenoy.tejaswini@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "shenoy.tejaswini@gmail.com"}
* affirm
    - utter_goodbye

* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - utter_ask_location
* restaurant_search{"location": "Vizag"}
    - slot{"location": "Vizag"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "vizag"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "shenoy.tejaswini@gmail.com"}
    - slot{"to": "shenoy.tejaswini@gmail.com"}
    - action_send_mail
    - slot{"to": "shenoy.tejaswini@gmail.com"}

* restaurant_search{"location": "Vizag", "cuisine": "North Indian", "price": "Under300"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Vizag"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "vizag"}

* greet
    - utter_greet
* restaurant_search{"location": "chakan", "cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "chakan"}
    - utter_ask_price
* restaurant_search{"price": "Under300"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "chakan"}

* restaurant_search{"location": "Ooty", "price": "Between300to700"}
    - slot{"location": "Ooty"}
    - slot{"price": "Between300to700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "ooty"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail

* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Vadodara"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Vadodara"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "vadodara"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* affirm
    - utter_goodbye

* restaurant_search{"cuisine": "Italian", "location": "Lucknow"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Lucknow"}
    - utter_ask_price
* restaurant_search{"price": "Over700"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "lucknow"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

* restaurant_search{"location": "Jaipur", "price": "Over700"}
    - slot{"location": "Jaipur"}
    - slot{"price": "Over700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
* affirm
    - utter_goodbye

* restaurant_search{"price": "Over700", "location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - slot{"price": "Over700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
* restaurant_search{"location": "Mangalore", "price": "Between300to700"}
    - slot{"location": "Mangalore"}
    - slot{"price": "Between300to700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "mangalore"}
* emailRecipient{"emailConfirmation": "Yes", "to": "shenoy_lata@yahoo.co.in"}
    - slot{"to": "shenoy_lata@yahoo.co.in"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "shenoy_lata@yahoo.co.in"}

* restaurant_search{"location": "NOIDA", "price": "Under300"}
    - slot{"location": "NOIDA"}
    - slot{"price": "Under300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "noida"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail

* restaurant_search{"price": "Between300to700", "location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - slot{"price": "Between300to700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "jamshedpur"}

* restaurant_search{"price": "Over700", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Over700"}
    - utter_ask_location
* restaurant_search{"location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* affirm
    - utter_goodbye
* restaurant_search{"cuisine": "chinese", "price": "Over700"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Over700"}
    - utter_ask_location
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_search_restaurants
    - slot{"location": "varanasi"}
* affirm
    - utter_goodbye
* restaurant_search{"cuisine": "Mexican", "price": "Under 300"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Under 300"}
    - utter_ask_location
* restaurant_search{"location": "KANNUR"}
    - slot{"location": "KANNUR"}
    - action_search_restaurants
    - slot{"location": "kannur"}
* affirm
    - utter_goodbye
* restaurant_search{"price": "Between300to700", "cuisine": "NORTH INDIAN"}
    - slot{"cuisine": "NORTH INDIAN"}
    - slot{"price": "Between300to700"}
    - utter_ask_location
* restaurant_search{"location": "Ooty"}
    - slot{"location": "Ooty"}
    - action_search_restaurants
    - slot{"location": "ooty"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"price": "Between300to700", "cuisine": "SOUTH INDIAN"}
    - slot{"cuisine": "SOUTH INDIAN"}
    - slot{"price": "Between300to700"}
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_search_restaurants
    - slot{"location": "mysore"}
* emailConfirm{"emailConfirmation": "Yes", "to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}

* restaurant_search{"price": "Over700", "cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* affirm
    - utter_goodbye

* restaurant_search{"cuisine": "NORTH INDIAN", "location": "FARIDABAD", "price": "UPTO RS 300"}
    - slot{"cuisine": "NORTH INDIAN"}
    - slot{"location": "FARIDABAD"}
    - slot{"price": "UPTO RS 300"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
* emailConfirm{"emailConfirmation": "Yes"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
* emailRecipient{"to": "tejaswinishreyadsc23@gmail.com"}
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
    - action_send_mail
    - slot{"to": "tejaswinishreyadsc23@gmail.com"}
* affirm
    - utter_goodbye
* restaurant_search{"cuisine": "Italian", "location": "Pune", "price": "Over700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Pune"}
    - slot{"price": "Over700"}
    - action_search_restaurants
    - slot{"location": "pune"}
* emailRecipient{"emailConfirmation": "Yes", "to": "SHENOY.TEJASWINI@GMAIL.COM"}
    - slot{"to": "SHENOY.TEJASWINI@GMAIL.COM"}
    - slot{"emailConfirmation": "Yes"}
    - action_send_mail
    - slot{"to": "SHENOY.TEJASWINI@GMAIL.COM"}
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "JODHPUR", "price": "Under300"}
    - slot{"location": "JODHPUR"}
    - slot{"price": "Under300"}
    - action_search_restaurants
    - slot{"location": "jodhpur"}
* affirm
    - utter_goodbye

* restaurant_search{"location": "New Delhi", "cuisine": "north indian", "price": "under300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "New Delhi"}
    - slot{"price": "under300"}
    - action_search_restaurants
    - slot{"location": "new delhi"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail
* restaurant_search{"location": "faridabad", "price": "under300", "cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "faridabad"}
    - slot{"price": "under300"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
* emailConfirm{"emailConfirmation": "No"}
    - slot{"emailConfirmation": "No"}
    - action_send_mail

class CreditCard:
    
    def __init__(self,card_number):
        self.card_number = card_number
        self.card_length = self.card_length_meth()
        self.card_type = self.card_type_meth()
        self.valid = self.valid()

    def card_length_meth(self):
        card_length = len(self.card_number)
        if card_length == 15 or card_length == 16:
            self.card_length = True
        else:
            self.card_length = False
        return self.card_length
    
    def card_type_meth(self):
        if self.card_length:
            if self.card_number[0:2] in ["51","52","53","54","55"]:
                self.card_type = "Master"
            elif self.card_number[0] == "4":
                self.card_type = "Visa"
            elif self.card_number[0:2] == "37" or self.card.type == "34":
                self.card_type = "Amex"
            elif self.card_number[0:5] == "6011":
                self.card_type = "Dscover"
        else:
            self.card_type = False
        return self.card_type
    
    def valid(self):
        doubled_list = []
        result_list = []
        for i in self.card_number[-2::-2]:
            doubled_list.append(int(i)*2)
            
        for i in doubled_list:
#             print(i)
            if i > 9:
                i = i - 9
                result_list.append(i)
            else:
                result_list.append(i)
        
        for i in self.card_number[-1::-2]:
            result_list.append(int(i))
            
#         alt_list = [int(i) for i in self.card_number[-1::-2]]

        total = sum(result_list)%10
#         total = (sum(result_list)+sum(alt_list))%10
#         print(total)
        if total == 0:
            self.valid = True
        else:
            self.valid = False
        return self.valid

cc = CreditCard('5515460934365316')
cc.card_length
cc.card_type
cc.valid
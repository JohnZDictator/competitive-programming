class Solution:
    def numberToWords(self, num: int) -> str:
        Ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        Tens_dig = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
                    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        Tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 
                6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        Hundred = 'Hundred'
        Thousand = 'Thousand'
        Million = 'Million'
        Billion = 'Billion'
        
        def tenths(num):
            if num == 9:
                return Billion
            elif num == 6:
                return Million
            elif num == 3:
                return Thousand
        
        def numToWord(num_arr, idx, output, isDig):
            if idx < 0:
                return output

            dig = tenths(idx)
            if num_arr[idx] == 0:
                if dig and isDig:
                    isDig = False
                    output += " " + dig
                return numToWord(num_arr, idx-1, output, isDig)
            
            if (idx + 1) % 3 == 2:
                if output:
                        output += " "
                if num_arr[idx] in Tens:
                    isDig = True
                    output += Tens[num_arr[idx]]
                    if dig:
                        isDig = False
                        output += " " + dig
                    return numToWord(num_arr, idx - 1, output, isDig)                    
                else:
                    output += Tens_dig[num_arr[idx] * 10 + num_arr[idx - 1]]
                    isDig = True
                    dig = tenths(idx-1)
                    if dig:
                        isDig = False
                        output += " " + dig
                    return numToWord(num_arr, idx - 2, output, isDig)
            elif (idx + 1) % 3 == 1:
                if output:
                    output += " "
                output += Ones[num_arr[idx]]
                isDig = True
                if dig:
                    isDig = False
                    output += " " + dig
                return numToWord(num_arr, idx - 1, output, isDig)
            elif (idx + 1) % 3 == 0:
                if output:
                    output += " "
                output += Ones[num_arr[idx]] + " " + Hundred
                isDig = True
                if dig:
                    isDig = False
                    output += " " + dig
                return numToWord(num_arr, idx - 1, output, isDig)
            
        
        if num == 0:
            return "Zero"
        
        num_arr = []
        while num > 0:
            num_arr.append(num % 10)
            num = num // 10
        
        return numToWord(num_arr, len(num_arr) - 1, '', False)
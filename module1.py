import os
import json

class App:
    def __init__(self):
        self.running = True
        self.parameters = {
            "position_code": '',
            "num_late_absences": 0,
            "num_of_days": 0,
            "days_ot": 0,
            "hours_ot": 0
        }
        with open('data.json', 'r') as file:
            self.positions = json.load(file)
    
    def show_data(self, values):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Payroll System")
        print("-"*10)
        print(f"Position Code: {values['pos_code']}")
        print(f"Position: {values['position']}")
        print(f"Basic pay: {values['basic pay']}")
        print(f"Rate per day: {values['rate per day']}")
        print(f"Amount of Days: {values['amount of days']}")
        print(f"Amount of Late & Absences: {values['amount of late']}")
        print(f"Amount of Overtime: {values['amount ot']}")
        print(f"Tax: {values['tax']}")
        print(f"Gross Pay: {values['gross pay']}")
        print(f"Net Pay: {values['net pay']}")

    def show_entry(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Payroll System")
        print("-"*10)
        print("\nEnter Parameters")
        position_code = input("Position Code> ")
        num_late_absences = input("Number of Lates & Absences> ")
        num_of_days = input("Number of Days> ")
        days_ot = input("Days of Overtime> ")
        hours_ot = input("Hours of Overtime> ")

        self.parameters['position_code'] = position_code.capitalize()
        self.parameters['num_late_absences'] = int(num_late_absences)
        self.parameters['num_of_days'] = int(num_of_days)
        self.parameters['days_ot'] = int(days_ot)
        self.parameters['hours_ot'] = int(hours_ot)

        values = self.compute()
        self.show_data(values)
        
        choice = input('\nTry Again? [Y/N]: ')

        if choice.lower() == 'y':
            self.show_entry()
        elif choice.lower() == 'n':
            self.running = False
        else:
            print("<error> Invalid input press [Enter] to continue")
            input()

    def compute(self):
        for position in self.positions:
            if self.parameters["position_code"] == position["pos_code"]:
                rate_per_day = (position['basic_pay'] / 2) / 10
                amount_num_of_days = rate_per_day * self.parameters['num_of_days']
                amount_num_of_late = rate_per_day * self.parameters['num_late_absences']
                amount_ot = (rate_per_day / 8) * self.parameters['hours_ot']
                gross_pay = amount_num_of_days + amount_ot
                tax = gross_pay * position['tax']
                net_pay = (gross_pay - (tax + position['philhealth'] + position['sss'] + position['pagibig'] + amount_num_of_late))
                
                return {
                    'pos_code': position['pos_code'],
                    'position': position['position'],
                    'basic pay': position['basic_pay'],
                    'rate per day': rate_per_day,
                    'amount of days': amount_num_of_days,
                    'amount of late': amount_num_of_late,
                    'amount ot': amount_ot,
                    'gross pay': gross_pay,
                    'tax': tax,
                    'net pay': net_pay
                }
    
    def show_menu(self):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Payroll System")
            print("-"*10)
            print("A. Compute Net Salary\nB. Exit")
            choice = input("\nEnter choice> ")
        
            if choice.lower() == 'a':
                self.show_entry()
            elif choice.lower() == 'b':
                self.running = False
            else:
                print("<error> Invalid input press [Enter] to continue")
                input()
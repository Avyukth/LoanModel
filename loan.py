from datetime import datetime, timedelta
from db import Database


class Loan:
    def __init__(self, email, interest_rate, repayment_terms, loan_amount):
        self.email = email

        self.interest_rate = interest_rate

        self.repayment_terms = repayment_terms

        self.loan_amount = loan_amount

    #Calculate Total Interest
    def get_total_interest(self):
        return (self.loan_amount*self.interest_rate)/100

    #Generate Loan Interest
    def gen_loan(self):
        loan = {}

        total_interest = (self.loan_amount*self.interest_rate *
                          self.repayment_terms)/(100)

        loan["interest"] = total_interest/self.repayment_terms

        loan["principal"] = self.loan_amount/self.repayment_terms

        return loan

    #Save Loan info to the database
    def save_loan(self):

        db = self.get_db_connection()

        db.create_loan_databases()

        loan = self.gen_loan()

        self.save_loan_info(db)

        for terms in range(self.repayment_terms):
            self.save_loan_details(terms, loan, db)

        db.commit()

        db.close()

    #Save Loan details to the database
    def save_loan_info(self, db):
        total_interest = self.get_total_interest()

        total_outstanding = self.loan_amount+self.get_total_interest()

        db.execute(f"INSERT INTO LOAN (EMAIL,LOAN_AMOUNT,INTEREST_RATE,REPAYMENT_TERMS) \
      VALUES ('{self.email}',{self.loan_amount},{self.interest_rate}, {self.repayment_terms} )")

    #calculate repayment information
    def calculate_payment_time(self, terms):

        # current date and time
        now = datetime.now()

        next_payment_dew = now+timedelta(days=terms*30)

        return next_payment_dew

    #Save Loan details to the database
    def save_loan_details(self, terms, loan, connection):
        next_payment_dew = self.calculate_payment_time(terms)

        total_Amount = loan["principal"]+loan["interest"]

        connection.execute(f"INSERT INTO LOAN_DETAILS (TERM_NO,EMAIL,PRINCIPAL,INTEREST,TOTAL_AMOUNT,PAYMENT_DUE_DATE) \
      VALUES ({terms+1},'{self.email}',{loan['principal']},{loan['interest']},{total_Amount},'{next_payment_dew}' )")

    #process repayment info from the database
    def repayment(self, email, repayment_amount):
        db = self.get_db_connection()

        db.execute(
            f"SELECT ID, TERM_NO,EMAIL,TOTAL_AMOUNT,PAYMENT_DUE_DATE,LOAN_STATUS,PAYMENT_TIME  FROM LOAN_DETAILS WHERE EMAIL ='{email}' AND LOAN_STATUS = 0")

        list_of_dew_payments = db.cursor.fetchall()

        if len(list_of_dew_payments) > 0:
            record = list_of_dew_payments[0]

        if len(list_of_dew_payments) > 0 and repayment_amount >= record[3]:

            repayment_amount -= record[3]

            self.save_repayment(record, db)
        else:
            pass

        db.commit()

        db.close()

    #Save repayment to the database
    def save_repayment(self, record, db):
        now = datetime.now()

        db.execute(
            f"UPDATE LOAN_DETAILS SET LOAN_STATUS=1 ,PAYMENT_TIME = '{now}' WHERE ID ={record[0]}")

    #Show loan details from the database
    def show_installment(self, email):
        db = self.get_db_connection()

        db.execute(
            f"SELECT ID, TERM_NO,EMAIL,PRINCIPAL,INTEREST,TOTAL_AMOUNT,PAYMENT_DUE_DATE,LOAN_STATUS,PAYMENT_TIME FROM LOAN_DETAILS WHERE EMAIL ='{email}' ")

        list_of_installment = db.cursor.fetchall()

        result=[f"| Term   | Principal | Interest | Total     | Date         | Status   |"]

        result.append(f"________________________________________________________________________")

        if len(list_of_installment) > 0:

            for record in list_of_installment:
                if record[7]:
                    status="Paid    "
                else:
                    status="Not-Paid"
                result.append(f"| {record[1]}      | {record[3]}     | {record[4]}    | {record[5]}     | {record[6].split()[0]}   | {status} |")

        db.close()

        return "\n".join(result)

    #retreive database connection
    def get_db_connection(self):

        db = Database()

        return db


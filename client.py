import grpc

import loan_pb2
import loan_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = loan_pb2_grpc.LoanStub(channel)

email = 'test@example.com'

# client sending loan details to the server


def save_loan():

    loan = loan_pb2.loan_data(
        email=email, interest_rate=10.0, repayment_terms=2, loan_amount=1000)

    stub.save_loan(loan)

# client sending  and retriving data about different installment from the server


def show_installment():
    installment = loan_pb2.installement_data(email=email)

    instalment_data = stub.show_installment(installment)

    print(instalment_data.installement_message)

# client sending repayment details to the server


def repayment():
    repayment = loan_pb2.repayment_data(email=email, repayment_amount=600)

    stub.repayment(repayment)


def main():
    save_loan()

    show_installment()

    repayment()

    show_installment()


if __name__ == '__main__':
    main()

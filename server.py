from concurrent import futures
import grpc
import time
import loan_pb2
import loan_pb2_grpc

from loan import Loan


class LoanServer(loan_pb2_grpc.LoanServicer):
    """
    docstring
    """

    def __init__(self):
        self.loan = None

    def save_loan(self, request, context):
        email = request.email

        interest_rate = request.interest_rate

        repayment_terms = request.repayment_terms

        loan_amount = request.loan_amount

        self.loan = Loan(email, interest_rate, repayment_terms, loan_amount)

        self.loan.save_loan()

        response = loan_pb2.empty()

        return response

    def show_installment(self, request, context):
        email = request.email

        response = loan_pb2.installement_response()

        response.installement_message = self.loan.show_installment(email)

        return response

    def repayment(self, request, context):
        email = request.email

        repayment_amount = request.repayment_amount

        self.loan.repayment(email, repayment_amount)

        response = loan_pb2.empty()

        return response


def serve():
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    loan_pb2_grpc.add_LoanServicer_to_server(LoanServer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

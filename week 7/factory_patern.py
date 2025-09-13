from abc import ABC, abstractmethod

#Abstratc base class
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

  #Concrete implementations
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} via PayPal."

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} via Stripe."

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} via Credit Card."

#Factory class
class PaymentProcessorFactory:
    _processors = {
        "paypal": PayPalProcessor,
        "stripe": StripeProcessor,
        "creditcard": CreditCardProcessor
    }

    @classmethod
    def create_processor(cls, processor_method):
        processor_class = cls._processors.get(processor_method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment processor: {processor_method}")
        return processor_class()

# Clean client code
def checkout(payment_method, amount):
    processor = PaymentProcessorFactory.create_processor(payment_method)
    return processor.process_payment(amount)

# Example usage
print(checkout("paypal", 100))
print(checkout("stripe", 50))
print(checkout("creditcard", 75))
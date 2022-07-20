from celery import task
from django.core.mail import send_mail
from .models import Order


# @task
def order_created(order_id, payment_done):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    if(payment_done):
        message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order at Choco-Stop. ' \
              f'Your order ID is {order.id}. ' \
                  f'Payment done successfully.'
    else:
        message = f'Dear {order.first_name},\n\n' \
                  f'You have successfully placed an order at Choco-Stop. ' \
                  f'Your order ID is {order.id}. ' \
                  f'Please pay by cash on delivery.'
    mail_sent = send_mail(subject,
                          message,
                          'chocolateshop111@gmail.com',
                          [order.email])
    # print(subject,message,order.email)
    return mail_sent

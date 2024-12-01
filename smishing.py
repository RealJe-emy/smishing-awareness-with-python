from faker import Faker
import random

fake = Faker()

def generate_smishing_message():
    templates = [
        "Your bank account has been compromised. Please visit {link} to verify.",
        "Congratulations! You've won a prize. Claim now at {link}",
        "Urgent: Your account will be locked in 24 hours. Verify here: {link}"
    ]

    link = fake.url()
    message = random.choice(templates).format(link=link)
    return message

print(generate_smishing_message())

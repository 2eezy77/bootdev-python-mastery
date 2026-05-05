def welcome_tenant(email, name="there"):
    welcome = f"Hello {name}, welcome to your new home. We are excited to have you! The email: {email} will be the one used to provide updated information associated with your account."
    return welcome 

tenant1 = welcome_tenant("isaacmontero@gmail.com", "Isaac")
print(tenant1)

user =  ['admin', 'guillaume', 'zuzana', 'monique', 'raymond']

log_name =input("What is your logging? :")

if log_name in user:
    if log_name == 'admin':
        print("Hello admin, would like to see a status report ?")

    else:
        print(f"Hello {log_name}, thans for looging again")

else:
    print("Unknow user.")

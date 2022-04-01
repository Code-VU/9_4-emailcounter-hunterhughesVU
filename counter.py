def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    max_value = 0
    topSender = ""

    senders = dict()

    for line in handle:
        line = line.strip()
        if line.startswith("From") and not line.startswith("From:"):
               sentBy = line.split()[1]
               if sentBy not in senders:
                 senders[sentBy] = 1
               else:
                 senders[sentBy] += 1

    for name, num_sent in senders.items():
        if  num_sent > max_value:
            max_value = num_sent
            topSender = str(name)
    
    print(topSender, max_value)


        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()

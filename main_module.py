from codeexplore import emailProcess, printMsg

def main():
    emails = ["diep@codeexplore.cpm", "youtube@codeexplore.dev","diep@gmail.com"]
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printMsg(email_username,email_domain)

if __name__ == "__main__":
    main()